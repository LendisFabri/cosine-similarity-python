# import MySQLdb
import pymysql as mdb
from math import log

dbConnection = mdb.Connect(host="localhost", user="root", passwd="27011996malang", db="batik_data_2")
cursor = dbConnection.cursor()
cursor2 = dbConnection.cursor()
# cursor.execute("SELECT VERSION()")

try:
    sql = "SELECT * FROM `batik_data`"
    cursor.execute(sql)
    row = cursor.fetchone()   

    totalFrekuensiKata = {};
    totalDokumen = 0
    tf = {};
    
    while row is not None:
        potong_content = str(row[2]).split(' ')
        totalKataPerDokumen = {}
        for fr in potong_content:
            if totalKataPerDokumen.has_key(fr) == False:
                totalKataPerDokumen[fr] = 0
            totalKataPerDokumen[fr] = potong_content.count(fr)

        for tkp in totalKataPerDokumen:
            if totalFrekuensiKata.has_key(tkp) == False:
                totalFrekuensiKata[tkp] = 0
            totalFrekuensiKata[tkp] = totalFrekuensiKata[tkp] + totalKataPerDokumen[tkp]

        totalDokumen = totalDokumen + 1
        row = cursor.fetchone()

    cursor.execute(sql)
    row = cursor.fetchone()
    while row is not None:
        potong_content = str(row[2]).split(' ')
        for fr in totalFrekuensiKata:
            if potong_content.count(fr) > 0:
                if(tf.has_key(fr) == False):
                    tf[fr] = 0
                tf[fr] = tf[fr] + 1

        row = cursor.fetchone()

    idfPerKata = {}   
    for tkp in totalFrekuensiKata:
        if idfPerKata.has_key(tkp) == False:
            idfPerKata[tkp] = 0
        a = float(float(totalDokumen)/float(tf[tkp]))
        idfPerKata[tkp] = float(log(a))

    cursor.execute(sql)
    row = cursor.fetchone()
    while row is not None:
        potong_content = str(row[2]).split(' ')
        totalKataPerDokumen = {}
        for fr in potong_content:
            if totalKataPerDokumen.has_key(fr) == False:
                totalKataPerDokumen[fr] = 0
            totalKataPerDokumen[fr] = potong_content.count(fr)
        
        for kata in totalKataPerDokumen:
            try:
                if kata != '' and kata != ' ':
                    sql2 = "INSERT INTO `tf_idf`(`ID_CONTENT_WEB`, `TREM`, `TF`, `DF`, `IDF`, `WDT`) VALUES (\"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\")" % \
                       (int(row[0]), kata, totalKataPerDokumen[kata], tf[kata], idfPerKata[kata], (float(totalKataPerDokumen[kata])*float(idfPerKata[kata])))
                    cursor2.execute(sql2)
                    dbConnection.commit()
            except Exception as e:
                print(e)
                dbConnection.rollback()
        #92 dokumen
        row = cursor.fetchone()
    
except Exception as e:
    print(e)
    dbConnection.rollback()
