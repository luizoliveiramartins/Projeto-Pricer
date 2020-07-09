import pyodbc
import os
caminho = ('c:/arquivo')
 
if not os.path.exists(caminho):
    os.makedirs(caminho)

lista1=[]
lista2=[]
lista3=[]
lista4=[]
lista5=[]
lista6=[]

cod1='0001'
cod2='7 0'
cod3='23 0'
cod4='121 0'
normal='NORMAL'
cod5='200 0'
otugui='OTUGUI'
a='|'

connection = pyodbc.connect('DRIVER={SQL Server};server=localhost\shopcontrol9;database=S9_Real;uid=sa;pwd=Senha123')
sql=connection.cursor()
sql.execute('SELECT P.CODIGO,P.NOME,PR.PRECO FROM PROD_SERV AS P INNER JOIN PROD_SERV_PRECOS AS PR ON(P.ORDEM=PR.ORDEM_PROD_SERV) INNER JOIN GRUPOS AS G ON(G.ORDEM=P.ORDEM_GRUPO)WHERE PR.ORDEM_TABELA_PRECO=1 AND DATEPART(DD,PR.DATA_ALTERACAO)=DATEPART(DD,GETDATE()) AND DATEPART(MM,PR.DATA_ALTERACAO)=DATEPART(MM,GETDATE())')
data=sql.fetchall()


for i in data:
    zero='{:0>8}'.format(i[0])
    pre=str(i[2]).replace('.','')
    resultado=cod1,zero,cod2,a+str(i[1])+a,cod3,a+pre[:len(pre)-2]+a,cod4,a+str(normal)+a,cod5,a+str(otugui)+a
    troca=resultado[9].replace("|OTUGUI|","|OTUGUI|,")
    resu=resultado[0],resultado[1],resultado[2],resultado[3],resultado[4],resultado[5],resultado[6],resultado[7],resultado[8],troca
    lista1.append(resu)

for i in lista1:
    troca1=str(i).replace("(","")
    lista2.append(troca1)

for i in lista2:
    troca2=str(i).replace(")","")
    lista3.append(troca2)

for i in lista3:
    troca3=str(i).replace("'","")
    lista4.append(troca3)

for i in lista4:
    troca4=str(i).replace(",","")
    lista5.append(troca4)

for i in lista5:
    troca5=str(i).replace("|OTUGUI|","|OTUGUI|,")
    lista6.append(troca5)
del lista1
del lista2
del lista3
del lista4
del lista5

arquivo_novo=open('c:/arquivo/PRICER.i1','w')

for i in lista6:
    arquivo_novo.write(str(i))
    arquivo_novo.write('\n')
arquivo_novo.close()
