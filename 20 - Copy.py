print("Номер 20")

def g(s1,s2,move):
    if (s1+s2) >=72 or move >3 or s1<0 or s2<0:            #Условие для победы
        return ((( move==3) and ((s1+s2)%2==0)) or ((move==2) and ((s1+s2)%2!=0))) and s1>=0 and s2>=0  #Надо поменять номера ходов, чтобы был 2 ход Байдена или 1 ход Путина
    if move%2==0:                           #Ходы Байдена
        move+=1
        return any([g(s1*2,s2,move), g(s1,s2*2,move)]) #Раз теперь мы смотрим победу Байдена, то он ходит через any
    else:                                   #Ходы Владимира Владимировича Путина
        move+=1
        return all([g(s1*2,s2,move), g(s1,s2*2,move), g(s1+7,s2-5,move),g(s1-5,s2+7,move)]) #а Владимир Владимирович через all
for s in range(2,51):
    if g(s,21,0):
        print(s)
