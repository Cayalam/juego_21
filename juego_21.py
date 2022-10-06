print("////JUEGO//DE//LA//21///")
# processing
import random

jugador= random.randint(1, 12)
contri_pc=random.randint(1, 12)
sum1=0
sum2 =0
i=1


while  i<=2:
    sum1= (sum1 + jugador)
    sum2= (sum2 + contri_pc)
    i=i+1
print("jugador",sum1) 
print("contri_pc",sum2)   
print("¿Quieres continuar?")
f=int(input("1. para seguir jugando o 2. para parar el juego: ")) 
if f==1:
    while sum1<=21 and f!=2:
        l=random.randint(1, 12)
        sum1=(sum1+l) 
        print("jugador",sum1)
        if sum1>21:
            print("Te arriesgaste en vano, perdiste")
            break
        print("¿Quieres continuar?")
        f=int(input("1. para seguir jugando o 2. para continuar  contrincante: ")) 
        if sum1>21:
            print("Te arriesgaste en vano perdiste") 
        elif f==2:
            while sum2<=sum1 and sum2< 21:
                r=random.randint(1, 12)
                sum2= (sum2+r)
                print("contri_pc",sum2)
            if sum2>sum1 and sum2<21:
                print("Gana el contrincante por ",sum2-sum1, "puntos")
            elif sum2==sum1:
                print("Acaba de ocurrir un empate")
            elif sum2 >21:
                print("el contrincante perdió , ganaste ")
                   
elif f==2:

    while sum2<=sum1 and sum2< 21:

        r=random.randint(1, 12)
        sum2= (sum2+r)
        print("contri_pc",sum2)
    if sum2>sum1 and sum2<21:
        print("Gana el contrincante por ",sum2-sum1, "puntos")
    elif sum2==sum1:
        print("Acaba de ocurrir un empate")
    elif sum2 >21:
        print("el contrincante perdió ganaste ")
else:
    print("FIN DEL JUEGO ")


    


    

