from absbox.local.china import SPV 

test01 = SPV(
    "Loan Level "
    ,{"封包日":"2021-03-31","起息日":"2021-06-15","首次兑付日":"2021-07-26"
      ,"法定到期日":"2060-12-01","收款频率":"月末","付款频率":["每月",26]}
    ,{'清单':[["贷款"
        ,{"放款金额":120,"放款利率":["固定",0.045],"初始期限":30
          ,"频率":"每月","类型":"先息后本","放款日":"2021-02-01"}
          ,{"当前余额":120000
          ,"当前利率":0.05
          ,"剩余期限":5
          ,"状态":"正常"}]]}
    ,(("账户01",{"余额":0}),)
    ,(("A1",{"当前余额":100
             ,"当前利率":0.07
             ,"初始余额":100
             ,"初始利率":0.07
             ,"起息日":"2020-01-03"
             ,"利率":{"固定":0.08}
             ,"债券类型":{"过手摊还":None}})
      ,("B",{"当前余额":20
             ,"当前利率":0.0
             ,"初始余额":100
             ,"初始利率":0.07
             ,"起息日":"2020-01-03"
             ,"利率":{"固定":0.00}
             ,"债券类型":{"权益":None}
             }))
    ,(("信托费用",{"类型":{"固定费用":10}}),)
    ,{"未违约":[
         ["支付费用",["账户01"],['信托费用']]
         ,["支付利息","账户01",["A1"]]
         ,["支付本金","账户01",["A1"]]
         ,["支付本金","账户01",["B"]]
         ,["支付收益","账户01","B"]
     ]}
    ,(["利息回款","账户01"]
      ,["本金回款","账户01"]
      ,["早偿回款","账户01"]
      ,["回收回款","账户01"])
    ,None
    ,None
    ,None
)
