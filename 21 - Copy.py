print("Номер 21")

def g(s1,s2,move):
    if (s1+s2) >=72 or move >4 or s1<0 or s2<0:            #Условие для победы
        return (((move==4 or move==2) and ((s1+s2)%2==0))) and s1>=0 and s2>=0  #Путин должен победить именно на своем ходе
    if move%2==0:                           #Ходы Байдена
        move+=1
        return all([g(s1*2,s2,move), g(s1,s2*2,move)])
    else:                                   #Ходы Владимира Владимировича Путина
        move+=1
        return any([g(s1*2,s2,move), g(s1,s2*2,move), g(s1+7,s2-5,move),g(s1-5,s2+7,move)])
for s in range(2,51):
    if g(s,21,0):
        print(s)


print("-----------------------")
print("Способ отсеить варианты, когда у Путина есть выигрышная стратегия, которая позволит ему гарантированно выиграть первым ходом.")
def g(s1,s2,move):
    if (s1+s2) >=72 or move >2 or s1<0 or s2<0:            #Условие для победы
        return (((move==2) and ((s1+s2)%2==0))) and s1>=0 and s2>=0
    if move%2==0:                           #Ходы Байдена
        move+=1
        return all([g(s1*2,s2,move), g(s1,s2*2,move)])
    else:                                   #Ходы Владимира Владимировича Путина
        move+=1
        return any([g(s1*2,s2,move), g(s1,s2*2,move), g(s1+7,s2-5,move),g(s1-5,s2+7,move)])
for s in range(2,51):
    if g(s,21,0):
        print(s)
