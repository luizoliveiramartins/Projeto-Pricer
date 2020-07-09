import os
import pyodbc
caminho = ('c:/arquivo')
 
if not os.path.exists(caminho):
    os.makedirs(caminho)

connection = pyodbc.connect('DRIVER={SQL Server};server=localhost\shopcontrol9;database=S9_Real;uid=sa;pwd=Senha123')
sql=connection.cursor()
sql.execute('SELECT P.CODIGO,P.NOME,PR.PRECO FROM PROD_SERV AS P INNER JOIN PROD_SERV_PRECOS AS PR ON(P.ORDEM=PR.ORDEM_PROD_SERV) WHERE PR.ORDEM_TABELA_PRECO=1 AND DATEPART(DD,PR.DATA_ALTERACAO)=DATEPART(DD,GETDATE()) AND DATEPART(MM,PR.DATA_ALTERACAO)=DATEPART(MM,GETDATE())')

arquivo=open('c:/arquivo/pricer.txt','w')
for i in sql:
    zero='{:0>8}'.format(i[0])
    preco=str(i[2]).replace('.','')
    resultado='0001'+' ',zero,' ''7 0'' ','|'+str(i[1])+'|',' ''23 0'' ','|'+preco[:len(preco)-2]+'|',' ''121 0'' ','|'+'NORMAL'+'|',' ''200 0'' ','|'+'OTUGUI'+'|'
    troca=str(resultado).replace("'","")
    troca1=str(troca).replace("(","")
    troca2=str(troca1).replace(")","")
    troca3=str(troca2).replace(",","")
    troca4=str(troca3).replace("|OTUGUI|","|OTUGUI|,")
    arquivo.write(str(troca4))
    arquivo.write('\n')
print('Arquivo Gerado com Sucesso em C:/arquivo/pricer.txt')
arquivo.close()
sql.close()
