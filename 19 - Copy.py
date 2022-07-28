print("Номер 19")

def g(s1,s2,move): 
    if (s1+s2) >=72 or move >2 or s1<0 or s2<0:           
        return (((move==2) and ((s1+s2)%2==0)) or ((move==1) and ((s1+s2)%2!=0))) and s1>=0 and s2>=0 #Условие для победы (на своем 1 ходу Путин должен победить или прямо перед этим Байден должен проиграть)
    if move%2==0:                           
        move+=1
        return all([g(s1*2,s2,move), g(s1,s2*2,move)]) 
    else:                                   
        move+=1
        return any([g(s1*2,s2,move), g(s1,s2*2,move), g(s1+7,s2-5,move),g(s1-5,s2+7,move)]) 

for s in range(2,51):
    if g(s,21,0):
        print(s)
