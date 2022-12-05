import os
os.chdir(r'C:\Users\eilyn\Downloads')
import pandas as pd
import numpy as np
df = pd.read_excel("siembra.xlsx")

//EJERCICIO 1: MOSTRAR LOS PRIMEROS 10 PRODUCTOS DE LOS DATOS
df[["PRODUCTO"]].head(10)


//EJERCICIO 2: MOSTRAR LOS 5 PRODUCTOS MÁS PRODUCIDOS EN 2019
df.loc[108:169]
df['TOTAL']=df.iloc[108:170, 1:13].sum(axis=1)
df[df.AÑO==2019]
df.nlargest(5,['TOTAL'])


//EJERCICIO 3: PRODUCTOS DEL 2018 QUE TIENEN UN INCREMENTO EN ENERO, FEBRERO Y MARZO.
//EXPORTAR ESTOS DATOS A UN EXCEL Y LLAMARLO ''INCREMENTO T1 2018''

df18=df.iloc[45:108] //creación de variable
df18["RESTA1"]=(df18["FEBRERO"]-df18["ENERO"])/df18["ENERO"] //PORCENTAJE DE GANANCIA DE ENERO A FEBRERO
df18["RESTA2"]=(df18["MARZO"]-df18["FEBRERO"])/df18["FEBRERO"] //PORCENTAJE DE GANANCIA DE FEBRERO A MARZO

df18.loc[(df18['RESTA1']>0)&(df18['RESTA2']>0),'RESULTADO']='True' //Primera condición
df18.loc[(df18['RESTA1']<0)|(df18['RESTA2']<0),'RESULTADO']='False' //Segunda condición

aumento=df18[df18.RESULTADO=='True'] //OBTENCIÓN DE GANANCIAS
aumento=aumento.iloc[:,0:4] //GUARDANDO SOLO LOS MESES DE ENERO A MARZO

aumento.to_excel('INCREMENTO T1 2018.xlsx',sheet_name='Sheet1',index=False) //EXPORTANDO A EXCEL


//EJERCICIO 4: CANTIDAD DE PRODUCTOS DIFERENTES QUE SE PRODUCEN
df['PRODUCTO'].nunique()


//EJERCICIO 5: TOTAL PRODUCIDO POR PRODUCTO EN 2019. EXPORTAR EL RESULTADO A EXCEL
df['TOTAL']=df.iloc[108:170, 1:13].sum(axis=1)
df[df.AÑO==2019]

df19=df[df.AÑO==2019]
df19=df19.iloc[:,14] //almacenando la columna TOTAL
df19.to_excel('TOTAL PRODUCIDO AÑO 2019.xlsx',sheet_name='Sheet1',index=False)
