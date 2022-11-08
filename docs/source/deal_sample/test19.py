test01 = 信贷ABS(
     "基于分段违约率的信用事件"
     ,{"封包日":"2021-03-01","起息日":"2021-05-01","首次兑付日":"2021-06-26"
      ,"法定到期日":"2060-12-01","收款频率":"月末","付款频率":["每月",26]}     
     ,{'发行':{'资产池规模':120.00},
       '清单':[["按揭贷款"
         ,{"放款金额":120,"放款利率":["固定",0.0485],"初始期限":30
           ,"频率":"每月","类型":"等额本金","放款日":"2020-06-01"}
           ,{"当前余额":120
           ,"当前利率":0.08
           ,"剩余期限":10
           ,"状态":"正常"}]],
      }
     ,(("账户01",{"余额":0}),)
     ,(("A1",{"当前余额":100
              ,"当前利率":0.07
              ,"初始余额":100
              ,"初始利率":0.07
              ,"起息日":"2020-01-03"
              ,"利率":{"固定":0.08}
              ,"债券类型":{"过手摊还":None}
              })
       ,("B",{"当前余额":40
              ,"当前利率":0.08
              ,"初始余额":100
              ,"初始利率":0.07
              ,"起息日":"2020-01-03"
              ,"利率":{"固定":0.08}
              ,"债券类型":{"过手摊还":None}
              }))
     ,tuple()
     ,{("兑付日","摊销"):[
          ["支付利息","账户01",["A1"]]
          ,["支付利息","账户01",["B"]]
          ,["支付本金","账户01",["A1"]]
          ,["支付本金","账户01",["B"]]
       ]
       ,("兑付日","加速清偿"):[
          ["支付利息","账户01",["A1"]]
          ,["支付剩余本金","账户01",["A1"]]]      
      ,"回款后":[]
      ,"清仓回购":[]}
     ,(["利息回款","账户01"]
       ,["本金回款","账户01"]
       ,["早偿回款","账户01"]
       ,["回收回款","账户01"])
     ,None
     ,None
     ,None
     ,{"分配前":[
                [[("资产池累积违约率",),
                  ">",
                  [["2021-06-30",0.02],["2021-08-31",0.022]]
                 ]
                 ,("新状态","加速清偿")]]}
 )

myAssump = [{"CDR":0.06}]

localAPI = API("http://localhost:8081")
#remoteAPI = API("https://absbox.org/api/latest")
#remoteAPI = API("https://deal-bench.xyz/api")
r = localAPI.run(test01,assumptions=myAssump,read=True)