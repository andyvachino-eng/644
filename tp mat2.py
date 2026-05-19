import matplotlib.pyplot as plt
#PUNTO 5
x = [0,5,10,15,20,25,30,35,40,45,50] #DEFINO EL DOMINIO DE LA FUNCION
a = [0] * len(x)
b = [0] * len(x) #CREO LOS VECTORES DEL TAMÑAO DEL DOMINIO
c = [0] * len(x)
for i in range(len(x)): #RELLENA LOS VECTORES CON LOS PUNTOS DEL GRAFICO
    a[i]=40*x[i] +200
    b[i]=70*x[i]+50
    c[i]=-2*x[i]**2+80*x[i]+100
#punto 6 graficar
plt.plot(x,a,label="A(X)")
plt.plot(x,b,label="B(X)")
plt.plot(x,c,label="C(X)")
plt.legend()
#PUNTO 7 MOSTRAR VALORES
print("Los resultados de la funcion A son:", a)
print("Los resultados de la funcion B son:", b)
print("Los resultados de la funcion C son:", c)
#8 CALCULAR LA CONVENIENCIA DE LOS PLANES CONVERGENTES
for i in range (len(x)):
    if ((a[i]<=b[i]) and (a[i]<=c[i])):
        print("para ", x[i], "HS el plan A es el ideal")
    elif ((b[i]<=a[i]) and (b[i]<=c[i])):
        print("para ", x[i], "HS el plan B es el ideal")
    else :
        print("para ", x[i], "HS el plan C es el ideal (PARA EL CLIENTE, NO LA EMPRESA)")
plt.show() #MUESTRA LA GRAFICA DE LA FUNCION
