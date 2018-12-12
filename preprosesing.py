#!/usr/bin/python

# import MySQLdb
import pymysql as mdb
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

dbConnection = mdb.Connect(host="localhost", user="root", passwd="27011996malang", db="batik_data_2")
cursor = dbConnection.cursor()
cursor2 = dbConnection.cursor()

factoryStemmer = StemmerFactory()
stemmer = factoryStemmer.create_stemmer()

simbol =['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
         '!', '@', '#', '$', '%', '%', '^', '&', '*', '(',
         ')', '_', '-', '+', '=', '[', ']', '\\', '{', '}',
         '|', ':', ';', '"', '\'', ',', '.', '/', '<', '>',
         '?', '`', '~', '\n']

singkatan = ['yg', 'yng', 'dg', 'tdk', 'dr', 'jl', 'rsi', 'ojk', 'klm', 'rp', 'mui', 'uu', 'ri', 'hub', 'rb', 'pcs', 'batikmadura', 'batiktulismadura', 'dalamnegeri', 'slalu', 
'kerenpakelokal', 'sd', 'sbg', 'radarmadura', 'hrs', 'dgn', 'brbg', 'brbagai', 'spti', 'kainbatik', 'bekerjasama', 'harpelnas', 'gratisongkir', 'ongkir', 'belashtml', 
'bloggerperempuan', 'rb ', 'pesonabusananusantara', 'berkainbatikmadura']

kepanjangan = ['yang', 'yang', 'dengan', 'tidak', 'doktor', 'jalan', 'rumah sakit islam', 'ojek', 'kapal layar motor', 'rupiah', 'majelis ulamak indonesia', 'undang-undang', 
'republik indonesia', 'hubung', 'ribu', 'picis', 'batik madura', 'batik tulis madura', 'dalam negeri', 'selalu', 'keren pake lokal', 'sampai dengan', 'sebagai', 
'radar madura', 'harus', 'dengan', 'berbagai', 'berbagai', 'seperti', 'kain batik', 'bekerja sama', 'hari pelanggan nasional', 'gratis ongkir', 'ongkos kirim',
'belas', 'blogger perempuan', 'ribu', 'pesona busana nusantara', 'berkain batik madura']

stopword = ['yang', 'untuk', 'pada', 'ke', 'para', 'namun', 'menurut', 'antara', 'dia', 'dua', 'apa',
            'ia', 'seperti', 'jika', 'jika', 'sehingga', 'kembali', 'dan', 'tidak', 'ini', 'karena',
            'kepada', 'oleh', 'saat', 'harus', 'sementara', 'setelah', 'belum', 'kami', 'sekitar', 'aja',
            'bagi', 'serta', 'di', 'dari', 'setelah', 'telah', 'sebagai', 'masih', 'hal', 'ketika', 'adalah', 'lalu',
            'itu', 'dalam', 'bisa', 'bahwa', 'atau', 'hanya', 'kita', 'dengan', 'akan', 'juga', 'ke', 'luh',
            'ada', 'mereka', 'sudah', 'saya', 'terhadap', 'secara', 'agar', 'lain', 'anda', 'lama',
            'begitu', 'mengapa', 'kenapa', 'yaitu', 'yakni', 'daripada', 'itulah', 'lagi', 'maka', 'makanya',
            'tentang', 'demi', 'dimana', 'kemana', 'pula', 'sambil', 'sebelum', 'sesudah', 'supaya',
            'guna', 'kah', 'pun', 'sampai', 'sedangkan', 'selagi', 'sementara', 'tetapi', 'apakah', 'tak',
            'kecuali', 'sebab', 'selain', 'seolah', 'seraya', 'seterusnya', 'tanpa', 'agak', 'boleh', 'sesudah',
            'dapat', 'dsb', 'dst', 'dll', 'dahulu', 'dulunya', 'anu', 'demikian', 'tapi', 'ingin', 'lalu',
            'juga', 'nggak', 'mari', 'nanti', 'melainkan', 'oh', 'ok', 'seharusnya', 'sebetulnya', 'kemudian',
            'setiap', 'setidaknya', 'sesuatu', 'pasti', 'saja', 'toh', 'ya', 'walau', 'tolong', 'si', 'redy', 'disimpen',
            'tentu', 'amat', 'apalagi', 'bagaimanapun', 'sama', 'dengan', 'sedikit', 'banyak', 'banget', 
            'tribunnewscom', 'tribunjatimcom', 'tribunkaltimcom', 'tribunkaltimco', 'tribunwowcom', 'tribunnewsco',
            'tribunnewsmdash', 'tribunnews', 'kata', 'tak', 'beberapa', 'tribun', 'sangat', 'hanya', 'mau', 'httpstcoocfbxra', 'httpindonesianbatikidpesona',
            'httpindonesianbatikidsejarah', 'httpdlvritqkqvw', 'indonesianculture', ' httpsmediamaduracomini', 'maduraculture', 'beautymadura', 'beautyindonesia',
            'httpdlvritqjwn', 'httpdlvritqjlx', 'httpkrafiecommeru', 'httpdestyycomwbwyh', 'httpdlvritqhdvj', 'httpsgooglcjxuw',
            'httpsgoogljttya', 'httpsgooglczkg', 'httpdlvritqfmmjf', 'httpiftttbkxaqn', 'httpsshopeecoidbatikraddina', 'httpswwwfacebookcomsenjangebu',
            'httpdlvritqcnmxm', 'httpdlvritq', 'httpwwwmerdekacomperistiwablusukan', 'httpwwwrosediananetsemua', 'httpsgooglnkyvj', 'httpsgoogltqnsj',
            'httpdlvritqcclnm', 'httpsgooglrjgusw', 'httpsgooglmhz', 'httpdlvritqpbj', 'httpdlvritqpb', 'httpdestyycomwiimw', 'httpdlvritqcb', 'httpdlvritqcfq', 'httpdlvritqcf',
            'httpdlvritqcf', 'httpdlvritqc', 'httpdestyycomwinjij', 'httpstabinaconetbatik', 'httpdlvritqzd', 'httpdlvritqzcx', 'httpdlvritqzcl',
            'httpstabinaconetbatik', 'httpsolshopananabilawordpresscombatik', 'httpsgooglonknea', 'httpbitlyizqiji', 'httpiftttjynjve', 'httpiftttawrhbp',
            'httpswwwtokopediacomtabinabatikkain', 'httpskualitaspalingbaguswajualbatikmadurabangwordpresscomjual', 'httpdlvritqcqq', 'httpdlvritqcqs',
            'httpdlvritqcqh', 'httpdlvritqcq', 'httpswwwgooglecoidsearchsafestrictbiwbiheiaufwaqembsvasxblydwqkainbatikmaduraoqkainbatikmaduragslpsy', 'abjikjljiikjikljpsy',
            'abiksbshjwsgnpsicrflfqrlharllag', 'tbmlclrldimmvedahukewiurxsvhxahvepkhykaeyqvsistaarldoctbslrfmemesiaelflfuirlfihdsimvmddd', 'mfffmiiftbslrfmemesiaelflfui',
            'httpsgooglrhy', 'httpsgooglzlkimc', 'httpsshopeecoidbatikumiromlah', 'httpshopeecoidshop', 'httpstabinaconetproductkain', 'httpswwwtokopediacomtabinabatiketalaserb',
            'httpbisnissurabayacommiracle', 'httpswwwbukalapakcompfashion', 'httpwwwpustakalewicommodberitaid', 'httpkabarsurabayacompeduli', 'httpharianbhirawacommiracle',
            'httpsshopeecoidkainbatikpekalongan', 'httpdlvritpsqq', 'httpbitlyxbab', 'httpmatamaduranewscombertepatan', 'httpswwwswarmappcomcfxiheiba', 'httpdlvritqckqrp',
            'trkidfdcalpwsshcopofrcbsrcdshop', 'productpagedobdqdcatiddpod', 'httpswwwtokopediacomtabinabatiketalasebatik', 'httpsgooglqjci', 'httpswwwbukalapakcompfashion',
            'httpswwwinstagramcompbysxcvchbju', 'httpswwwinstagramcompbysxinhvdl', 'httpswwwinstagramcompbysxnomnlac', 'httpswwwinstagramcompbysxtnhyh', 'httpskompasidbacaekonomibatik',
            'httpswwwinstagramcompbysxbmhcx', 'httpokzmecyui', 'httpswwwinstagramcompbysxhqnwfl', 'httpsgooglfaepui', 'httpsranselmungilblogspotcoidberburu', 'mfffmiiftbslrfmemesiaelflfui',
            'httpswwwgoodnewsfromindonesiaideksotis', 'httpswwwtokopediacomtabinabatiketalasebahan', 'httpsgooglwqmrvc', 'httpbitlyvfdlgo', 'httpdlvritphtnf', 'httpiftttbkxaqn', 'httpsgooglzfqd',
            'httpbitlywlfze', 'httpbitlyxutxzi', 'httpbitlyxuawqy', 'httpbitlyioqmvs', 'httpsinfokampusnewsbatik', 'httpwwwlazadacoidcek', 'htmlfffdampbscdetpofferidaffiliateidaffiliatenameserverforceonecom',
            'httpsgooglfdzkqz', 'httpstabinaconetmotif', 'httpswwwgoodnewsfromindonesiaideksotis', 'httpswwwinstagramcompbxzwnglietaken', 'httpsgooglprnf', 'httpsshopeecoidalmiraolshop', ' httpsgooglcjxuw',
            'httppojokpitucombacaphpiduruttopktgjatimkeyrbkekonomi', 'httpdlvritnwpgt', 'httptabinacobatik', 'madurablogspotcoid', 'httpsmediamaduracomini', 'httpdlvritqhflcb', 'httptabinaconet', 'httpwwwtabinaconet',
            'maduratrkidfdcalpwsshcopofrcbsrcdshop','madurautmsourcedlvritutmmediumtwitter', 'httpswwwtokopediacomtabinabatikbatik', 'murahtrkidfdcalpwsshcopofrcbsrcdshop', 'httpswwwtokopediacomtabinabatiketalasekain',
            'httpsgooglnbhdb', 'rbtrkidfdcalpwsshcopofrcbsrcdshop', 'httpswwwinstagramcomtaqiyyabatik', 'httpstabinaconetsolo', 'trkidfcalpwsshcopofrcbsrcshop'
            'productpageobqcatidpo', 'httpbitlyskiwuf', 'httparemamediacombatik',' httpdlvrit dvj', 'mfffmiiftbslrfmemesiaelflfui', 'httpdlvritps']

kata_salah = ['bangkal', 'cur', 'krampung', 'suryacoid', 'tribunnewscom', 'bperempuan', 'rb']
kata_benar = ['bangkalan', 'curi', 'kampung', '', '', 'perempuan', 'ribu']

try:
    sql = "SELECT * FROM `batik_data`"
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

        content = content.replace('luh', ' ')
        content = content.replace('qq', ' ')
        content = content.replace('qs', ' ')
        content = content.replace('qh', ' ')
        content = content.replace('pake', ' ')
        content = content.replace('httpdlvrit dvj', ' ')
        content = content.replace('httpdlvritqkqvw', ' ')
        content = content.replace('httpdlvritqjwn', ' ')
        content = content.replace('httpdlvritqjlx', ' ')
        content = content.replace('httpkrafiecommeru', ' ')
        content = content.replace('httpdestyycomwbwyh', ' ')
        content = content.replace('httpdlvritqhflcb', ' ')
        content = content.replace('httpdlvritqhdvj', ' ')
        content = content.replace('httpsgoogljttya', ' ')
        content = content.replace('httpsgooglczkg', ' ')
        content = content.replace('httpdlvritqfmmjf', ' ')
        content = content.replace('httpsshopeecoidbatikraddina', ' ')
        content = content.replace('httpswwwfacebookcomsenjangebu', ' ')
        content = content.replace('httpdlvritqcnmxm', ' ')
        content = content.replace('httpsgooglnkyvj', ' ')
        content = content.replace('httpsgoogltqnsj', ' ')
        content = content.replace('httpdlvritqcclnm', ' ')
        content = content.replace('httpsgooglrjgusw', ' ')
        content = content.replace('httpsgooglmhz', ' ')
        content = content.replace('httpdlvritqpbj', ' ')
        content = content.replace('httpdlvritqpb', ' ')
        content = content.replace('httpdestyycomwiimw', ' ')
        content = content.replace('httpdlvritqcb', ' ')
        content = content.replace('httpdlvritqcfq', ' ')
        content = content.replace('httpdlvritqc', ' ')
        content = content.replace('httpdestyycomwinjij', ' ')
        content = content.replace('httpdlvritqzd', ' ')
        content = content.replace('httpdlvritqzcx', ' ')
        content = content.replace('httpdlvritqzcl', ' ')
        content = content.replace('httpsgooglonknea', ' ')
        content = content.replace('httpbitlyizqiji', ' ')
        content = content.replace('httpiftttjynjve', ' ')
        content = content.replace('httpiftttawrhbp', ' ')
        content = content.replace('httpskualitaspalingbaguswajualbatikmadurabangwordpresscomjual', ' ')
        content = content.replace('httpdlvritqcqq', ' ')
        content = content.replace('httpdlvritqcqs', ' ')
        content = content.replace('httpdlvritqcqh', ' ')
        content = content.replace('httpdlvritqcq', ' ')
        content = content.replace('httpsshopeecoidkainbatikpekalongan', ' ')
        content = content.replace('httpdlvritpsqq', ' ')
        content = content.replace('httpbitlyxbab', ' ')
        content = content.replace('httpswwwswarmappcomcfxiheiba', ' ')
        content = content.replace('httpswwwtokopediacomtabinabatikbatik', ' ')
        content = content.replace('httpsgooglqjci', ' ')
        content = content.replace('httpsgooglcjxuw', ' ')
        content = content.replace('httpiftttbkxaqn', ' ')
        content = content.replace('httpswwwinstagramcompbysxcvchbju', ' ')
        content = content.replace('httpswwwinstagramcompbysxinhvdl', ' ')
        content = content.replace('httpswwwinstagramcompbysxnomnlac', ' ')
        content = content.replace('httpswwwinstagramcompbysxtnhyh', ' ')
        content = content.replace('httpswwwinstagramcompbysxbmhcx', ' ')
        content = content.replace('httpokzmecyui', ' ')
        content = content.replace('httpswwwinstagramcompbysxhqnwfl', ' ')
        content = content.replace('httpsgooglfaepui', ' ')
        content = content.replace('httpwwwpustakalewicommodberitaid', ' ')
        content = content.replace('productpagedobdqdcatiddpod', ' ')
        content = content.replace('httpsshopeecoidbatikumiromlah', ' ')
        content = content.replace('httpsgooglwqmrvc', ' ')
        content = content.replace('httpbitlyvfdlgo', ' ')
        content = content.replace('httpdlvritphtnf', ' ')
        content = content.replace('httpbitlywlfze', ' ')
        content = content.replace('httpbitlyxutxzi', ' ')
        content = content.replace('httpbitlyxuawqy', ' ')
        content = content.replace('httpbitlyioqmvs', ' ')
        content = content.replace('htmlfffdampbscdetpofferidaffiliateidaffiliatenameserverforceonecom', ' ')
        content = content.replace('httptabinaconet', ' ')
        content = content.replace('httpsgooglprnf', ' ')
        content = content.replace('httpsshopeecoidalmiraolshop', ' ')
        content = content.replace('httppojokpitucombacaphpiduruttopktgjatimkeyrbkekonomi', ' ')
        content = content.replace('httpdlvritnwpgt', ' ')
        content = content.replace('httpbitlyskiwuf', ' ')
        content = content.replace('httpsgooglfdzkqz', ' ')
        content = content.replace('httpswwwinstagramcomtaqiyyabatik', ' ')
        content = content.replace('httpwwwtabinaconet', ' ')
        content = content.replace('httpsgooglzlkimc', ' ')
        content = content.replace('httpshopeecoidshop', ' ')
        content = content.replace('httpsgooglrhy', ' ')
        content = content.replace('httpsgooglnbhdb', ' ')

        content = content.replace('x8f', ' ')
        content = content.replace('x89', ' ')
        content = content.replace('x8c', ' ')
        content = content.replace('x9b', ' ')
        content = content.replace('x9d', ' ')
        content = content.replace('x90', ' ')
        content = content.replace('x8d', ' ')
        content = content.replace('x99', ' ')
        content = content.replace('x97', ' ')
        content = content.replace('x93', ' ')
        content = content.replace('x9f', ' ')
        content = content.replace('x98', ' ')
        content = content.replace('x8a', ' ')
        content = content.replace('xa0', ' ')
        content = content.replace('xad', ' ')
        content = content.replace('x80', ' ')
        content = content.replace('x83', ' ')
        content = content.replace('  ', ' ')
        print(content)
        
        #insert hasil preproses
        try:
            sql2 = "UPDATE `batik_data` SET `hasil_stemming` = \"%s\" WHERE `ids` = \"%s\"" % \
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
