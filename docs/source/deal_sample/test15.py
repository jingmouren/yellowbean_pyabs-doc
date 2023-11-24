from absbox.local.china import SPV
# 合格投资 暂时不参与分配 
test01 = SPV(
    "速利银丰中国 2021 年第一期个人汽车抵押贷款支持证券信托"
    ,{"归集日":["2022-09-30","2022-10-31"],"兑付日":["2022-10-26","2022-11-26"]
     ,"法定到期日":"2060-12-01","收款频率":"月末","付款频率":["每月",26]}
    ,{'归集表':[ ["2022-09-30",4784936786,528909185.2,21282112.96]
                ,["2022-10-31",4304247306,480689479.9,18307777.31]
                ,["2022-11-30",3850419452,453827854.6,16502702.18]
                ,["2022-12-31",3421607632,428811820.1,14778431.28]
                ,["2023-01-31",3013633943,407973688.6,13149122.92]
                ,["2023-02-28",2647016507,366617436,11605251.78]
                ,["2023-03-31",2286770183,360246324.2,10235285.46]
                ,["2023-04-30",1954800819,331969363.6,8884510.74]
                ,["2023-05-31",1655566418,299234401.5,7637610.86]
                ,["2023-06-30",1393137673,262428744.6,6507730.19]
                ,["2023-07-31",1169116006,224021666.9,5509034.69]
                ,["2023-08-31",980306104,188809902.3,4653045.26]
                ,["2023-09-30",824222559.1,156083544.9,3925579.64]
                ,["2023-10-31",686655031.1,137567528,3316188.66]
                ,["2023-11-30",565956744.6,120698286.5,2770883.69]
                ,["2023-12-31",460002546,105954198.6,2289704.73]
                ,["2024-01-31",362450149.3,97552396.74,1866080.6]
                ,["2024-02-29",285011170.4,77438978.89,1475630.61]
                ,["2024-03-31",214157901.8,70853268.62,1166109.85]
                ,["2024-04-30",156686922.8,57470979,882526.69]
                ,["2024-05-31",111572058.4,45114864.34,651349.9]
                ,["2024-06-30",76450517.84,35121540.6,469113.96]
                ,["2024-07-31",49698861.84,26751656,325848.02]
                ,["2024-08-31",28896808.19,20802053.65,215172.23]
                ,["2024-09-30",13614661.42,15282146.77,127369.68]
                ,["2024-10-31",4857897.29,8756764.13,60661.17]
                ,["2024-11-30",1399804.87,3458092.42,21215.87]
                ,["2024-12-31",496096.76,903708.11,5916.37]
                ,["2025-01-31",94830.28,401266.48,2102.58]
                ,["2025-02-28",58960.9,35869.38,447.78]
                ,["2025-03-31",38119.22,20841.68,277.46]
                ,["2025-04-30",17178,20941.22,177.92]
                ,["2025-05-31",2537.35,14640.65,77.47]
                ,["2025-06-30",0,2537.35,8.41]]
      ,'发行':{'资产池规模':9_179_540_189.72},
     }
    ,(("一般准备金账户",{"余额":89_922_387.64
                      ,"类型":{"较低":[
                                 {"分段":
                                   [[("债券余额","A","次级"),">",0]
                                    ,{"目标储备金额":{"公式":("自定义","资产池调整后余额"),"系数":0.01}}
                                    ,{"固定储备金额":0}]}
                                ,{"目标储备金额":[("债券余额",),1.0]}]}
                      ,"计息":{"周期":"季度末","利率":0.04,"最近结息日":"2022-09-30"}})
      ,("经营账户",{"余额":0.0})
      ,("混合准备金账户",{"余额":0.0})
      ,("持续购买准备金账户",{"余额":0.0})
      ,("费用账户",{"余额":0.0})
     )
    ,(("A",{"当前余额":3_649_536_000.00
             ,"当前利率":0.0348
             ,"初始余额":7_920_000_000
             ,"初始利率":0.0348
             ,"起息日":"2022-10-26"
             ,"利率":{"固定":0.0348}
             ,"债券类型":{"过手摊还":None}})
      ,("次级",{"当前余额":416_842_105.26
             ,"当前利率":0.0
             ,"初始余额":416_842_105.26
             ,"初始利率":0.07
             ,"起息日":"2022-10-26"
             ,"利率":{"固定":0.00}
             ,"债券类型":{"权益":None}
             }))
    ,(("增值税",{"类型":{"百分比费率":["资产池当期","利息",0.0326]}})
      ,("代理支付费用利息",{"类型": {"百分比费率":["已付利息合计","A",0.0002]}})
      ,("代理支付费用本金",{"类型": {"百分比费率":["已付本金合计","A",0.0002]}})
      ,("贷款服务费用",{"类型": {"年化费率":[("资产池余额",),0.005]},"计算日":"2022-09-29"})
     )
    ,{"未违约":[
        ["流动性支持","发起人","账户","一般准备金账户",{"公式":("储备账户缺口","一般准备金账户")}] 
        ,["账户转移","费用账户","经营账户"]
        ,["支付费用","经营账户",['增值税']]
        ,["支付费用","经营账户",['贷款服务费用']]
         ,["计提支付利息","经营账户",["A"]]
         ,["计提费用","代理支付费用利息"]
         ,["支付费用","经营账户",['代理支付费用利息']]
         ,["账户转移","经营账户","一般准备金账户",{"储备":"缺口"}]
         ,["支付本金","经营账户",["A"]
           ,{"公式":("Min"
                      ,("债券余额","A")
                      ,("差额"
                        ,("债券余额","A","次级")
                        ,("Max"
                          ,("差额",("自定义","资产池调整后余额"),("自定义","目标超额担保金额"))
                          ,("常数",0.0))))}]
         ,["计提费用","代理支付费用本金"]
         ,["支付费用","经营账户",['代理支付费用本金']]    
         ,["计提支付利息","经营账户",["次级"]]
         ,["条件执行"
           ,[("债券余额","A"),"=",0]
           ,["支付本金","经营账户",["次级"]]]
         ,["流动性支持报酬","经营账户","发起人"]
         ]
     ,"回款后":[["计提费用","增值税","贷款服务费用"]]
     }
    ,(["利息回款","经营账户"]
      ,["本金回款","经营账户"]
      ,["早偿回款","经营账户"]
      ,["回收回款","经营账户"])
    ,{"发起人":{"类型":"无限制"}}
    ,None
    ,None
    ,None
    ,"摊销"
    ,{"收益补充超额担保金额":
      {"余额曲线":[["2022-10-01",63322258.41]
                  ,["2022-11-01",50234030.96]
                  ,["2022-12-01",38881437.99]
                  ,["2023-01-01",29197182.73]
                  ,["2023-02-01",21089455.64]
                  ,["2023-03-01",14475798.7]
                  ,["2023-04-01",9227206.729]
                  ,["2023-05-01",5329504.123]
                  ,["2023-06-01",2671007.271]
                  ,["2023-07-01",1063561.6]
                  ,["2023-08-01",262786.9647]
                  ,["2023-09-01",0]]}
     ,"资产池调整后余额":{"公式":("差额",("资产池余额",),("自定义","收益补充超额担保金额"))}
     ,"目标超额担保金额":{"常量":655_396_658.24} 
     }
)
