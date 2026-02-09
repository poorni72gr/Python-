'''orders=[[101,1500,"success"],[102,800,"success"],[103,2500,"failed"],[104,3000,"success"]]
valid_orders=[o[0] for o in orders if o[1]>1000 and o[2]=="success"]
print(valid_orders)'''

'''servers=[["srv1",85,"running"],["srv2",60,"running"],["srv3",90,"stopped"]]
alert=[s[0] for s in servers if s[1]>80 and s[2]=="running"]
print(alert)'''

transactions=[[1,60000,"usa"],[2,12000,"india"],[3,90000,"uk"]]
alert=[t[0] for t in transactions if t[1]>5000 and t[2]== "india"]
print(alert)
      
        
