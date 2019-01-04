#!/usr/bin/python

# import MySQLdb
import pymysql as mdb
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

dbConnection = mdb.Connect(host="", user="", passwd="", db="")
cursor = dbConnection.cursor()
cursor2 = dbConnection.cursor()

factoryStemmer = StemmerFactory()
stemmer = factoryStemmer.create_stemmer()

simbol =['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
         '!', '@', '#', '$', '%', '%', '^', '&', '*', '(',
         ')', '_', '-', '+', '=', '[', ']', '\\', '{', '}',
         '|', ':', ';', '"', '\'', ',', '.', '/', '<', '>',
         '?', '`', '~', '\n']

singkatan = [''] #berisi kata yang disingkat

kepanjangan = [''] #berisi kepanjangan kata dalam variabel singkatan 

stopword = ['']

kata_salah = [''] # berisi kata yang rancu atau salah 
kata_benar = [''] # berisi kata pembenaran untuk kata dalam variabel kata_salah

try:
    sql = "SELECT * FROM ``"
    cursor.execute(sql)
    row = cursor.fetchone()

    while row is not None:
        content = str(row[2]).lower()

        #Habus angka dan simbol
        for i in simbol:
            if(i == '\n' or i == '-'):
                content = content.replace(i, ' ')
            else:
                content = content.replace(i, '')

        content2 = str(content).split(' ')

        #pembenaran kata tipo dan singkatan
        for i in range(0, len(content2)):
            for j in range(0, len(singkatan)):
                if content2[i] == singkatan[j]:
                    content2[i] = kepanjangan[j]
                    break

        #penggabungan konten
        content = ''
        for i in content2:
            content = content +' '+i

        #hapus stopword
        content2 = str(content).split(' ')
        for i in range(0, len(content2)):
            for j in range(0, len(stopword)):
                if content2[i] == stopword[j] or len(content2[i]) == 1:
                    content2[i] = ''
                    break
                
        #proses stemming
        content3 = str(content2)
        content = stemmer.stem(content3)

        #pembenaran kata setelah stemming
        content4 = str(content).split(' ')
        
        for i in range(0, len(content4)):
            for j in range(0, len(kata_salah)):
                if content4[i] == kata_salah[j]:
                    content4[i] = kata_benar[j]
                    break 

        #penggabungan konten
        content = ''
        for i in content4:
            content = content +' '+i

        content = content.replace('kata salah', ' ') # kata salah, ganti dengan spasi
        # print(content)
        
        #insert hasil preproses
        try:
            sql2 = "UPDATE `` SET `` = \"%s\" WHERE `` = \"%s\"" % \
                   (content, int(row[0]))
            cursor2.execute(sql2)
            dbConnection.commit()
        except Exception as e:
            print(Exception.message)
            dbConnection.rollback()

        row = cursor.fetchone()
    
except Exception as e:
    print(e.message)
    dbConnection.rollback()
