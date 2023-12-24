from absbox.local.china import SPV

gy = SPV(
    "工元乐居2021年第七期"
    ,{"封包日":"2021-03-01","起息日":"2021-10-15","首次兑付日":"2021-11-26"
     ,"法定到期日":"2060-12-01","收款频率":"月末","付款频率":["每月",26]}      
    ,{"清单":[["按揭贷款"
        ,{"放款金额":9961626400,"放款利率":["固定",0.0485],"初始期限":218
          ,"频率":"每月","类型":"等额本息","放款日":"2020-06-01"}
          ,{"当前余额":7596981800
          ,"当前利率":0.0495
          ,"剩余期限":165
          ,"状态":"正常"}]
      ,["按揭贷款"
        ,{"放款金额":330_977.45*10000,"放款利率":["固定",0.0485],"初始期限":218
          ,"频率":"每月","类型":"等额本金","放款日":"2020-06-01"}
          ,{"当前余额":239_790.20*10000
          ,"当前利率":0.0495
          ,"剩余期限":165
          ,"状态":"正常"}]]}
    ,(("本金分账户",{"余额":0})
      ,("收入分账户",{"余额":0}))
    ,(("A1",{"当前余额":3_650_000_000
                             ,"当前利率":0.03
                             ,"初始余额":3_650_000_000
                             ,"初始利率":0.03
                             ,"起息日":"2020-01-03"
                             ,"利率":{"浮动":[0.0131,"LPR5Y",-0.0169,["每年",3,1]]}
                             ,"债券类型":{"过手摊还":None}
                            })
      ,("A2",{"当前余额":5_444_000_000
                             ,"当前利率":0.03
                             ,"初始余额":5_444_000_000
                             ,"初始利率":0.03
                             ,"起息日":"2020-01-03"
                             ,"利率":{"浮动":[0.0209,"LPR5Y",-0.0091,["每年",3,1]]}
                             ,"债券类型":{"过手摊还":None}
                            })
      ,("次级",{"当前余额":900_883_783.62
                             ,"当前利率":0.0
                             ,"初始余额":2_123_875_534.53
                             ,"初始利率":0.00
                             ,"起息日":"2020-01-03"
                             ,"利率":{"期间收益":0.02}
                             ,"债券类型":{"权益":None}
                            }))
    ,(("增值税",{"类型":{"差额费用":[("*"
                                   ,("资产池累计",None,"利息"),0.0326)
                                   ,("费用支付总额",None,"增值税")]}})
      ,("服务商费用",{"类型":{"年化费率":[("资产池余额",),0.02]}})
      ,("执行费用", {"类型":{"周期费用":["月初",599]}}))
    ,{"未违约":[
         ["支付费用","收入分账户",["执行费用"]]
         ,["支付费用","收入分账户",["服务商费用"],{"应计费用百分比":0.1}]
         ,["计提支付利息","收入分账户",["A1","A2"]]
         ,["支付费用","收入分账户",["服务商费用"]]
         ,["支付收益","收入分账户","次级"]
         ,["账户转移","收入分账户","本金分账户"]
         ,["支付本金","本金分账户",["A1"]]
         ,["支付本金","本金分账户",["A2"]]
         ,["支付本金","本金分账户",["次级"]]
         ,["支付收益","本金分账户","次级"]]
     ,"回款后":[["计提费用","增值税"]]}
    ,(["利息回款","收入分账户"]
      ,["本金回款","本金分账户"]
      ,["早偿回款","本金分账户"]
      ,["回收回款","本金分账户"])
    ,None
    ,None
    ,None 
    ,None
    ,("设计","摊销")
)
