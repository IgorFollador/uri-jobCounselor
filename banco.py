import mysql.connector
from mysql.connector import errorcode

print("Conectando...")
try:
      conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='admin'
      )
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Existe algo errado no nome de usuário ou senha')
      else:
            print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `jobCounselor`;")

cursor.execute("CREATE DATABASE `jobCounselor`;")

cursor.execute("USE `jobCounselor`;")

# criando tabelas
TABLES = {}
TABLES['Sentence'] = ('''
      CREATE TABLE `Sentence` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `grade` DECIMAL(4,2) NOT NULL,
      `sentence` varchar(600) NOT NULL,
      `date` DATETIME NOT NULL,
      PRIMARY KEY (`id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

for tabela_nome in TABLES:
      tabela_sql = TABLES[tabela_nome]
      try:
            print('Criando tabela {}:'.format(tabela_nome), end=' ')
            cursor.execute(tabela_sql)
      except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                  print('Já existe')
            else:
                  print(err.msg)
      else:
            print('OK')


# commitando se não nada tem efeito
conn.commit()

cursor.close()
conn.close()