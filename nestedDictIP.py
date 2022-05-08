"""{
    'amartya': {'len': '8', 'did': 'True'},
    'saini': {'len': '2', 'did': 'True'},
    'sameer': {'len': 3, 'did': False}
}
"""


"""
46.72.177.4 - - [12/Dec/2015:18:31:08 +0100] "GET /administrator/ HTTP/1.1" 200 4263 "-" "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0" "-"
46.72.177.5 - - [12/Dec/2015:18:31:08 +0100] "POST /administrator/index.php HTTP/1.1" 203 4494 "http://almhuette-raith.at/administrator/" "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0" "-"
46.72.177.4 - - [14/Dec/2015:16:39:27 +0100] "GET /administrator/ HTTP/1.1" 400 4263 "-" "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0" "-"
46.72.177.5 - - [14/Dec/2015:16:39:28 +0100] "POST /administrator/index.php HTTP/1.1" 503 4494 "http://almhuette-raith.at/administrator/" "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0" "-"
46.72.177.8 - - [15/Dec/2015:18:16:52 +0100] "GET /administrator/ HTTP/1.1" 300 4263 "-" "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0" "-"
46.72.177.9 - - [15/Dec/2015:18:16:52 +0100] "POST /administrator/index.php HTTP/1.1" 310 4494 "http://almhuette-raith.at/administrator/" "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0" "-"
46.72.177.47 - - [17/Dec/2015:19:43:47 +0100] "GET /administrator/ HTTP/1.1" 200 4263 "-" "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0" "-"
46.72.177.43 - - [17/Dec/2015:19:43:47 +0100] "POST /administrator/index.php HTTP/1.1" 204 4494 "http://almhuette-raith.at/administrator/" "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0" "-"
"""

# Give a list of top I/P adreess with 2xx, 3xx, 5xx count 

"""{
    "46.72.177.4":{
        "2xx": 10,
        "3xx": 12,
        "4xx": 17,
        "5xx": 2
    },
    "46.72.177.4":{
        "2xx": 1,
        "3xx": 12,
        "4xx": 15,
        "5xx": 12
    }
}"""



from cmath import log


def getListofIPaddress():
    dict={}
    with open('devops-learning/ip_address.log', 'r') as f:
        lines=f.readlines()
        for line in lines: 
            logArr=line.split(' ')
            statusCode=int(logArr[8])
            if (logArr[0] not in dict):
                dict[logArr[0]]={}
                if(statusCode>=200 and statusCode<300):
                    dict[logArr[0]]['2xx']=1
                elif(statusCode>=300 and statusCode<400):
                    dict[logArr[0]]['3xx']=1
                elif(statusCode>=400 and statusCode<500):
                    dict[logArr[0]]['4xx']=1
                else:
                    dict[logArr[0]]['5xx']=1
            else:
                if(statusCode>=200 and statusCode<300):
                    getValue('2xx',dict[logArr[0]])
                elif(statusCode>=300 and statusCode<400):
                    getValue('3xx',dict[logArr[0]])
                elif(statusCode>=400 and statusCode<500):
                    getValue('4xx',dict[logArr[0]])
                else:
                    getValue('5xx',dict[logArr[0]])
    print(dict)

def getValue(statusCode, dict):
    if(statusCode in dict):
        dict[statusCode]+=1
    else:
        dict[statusCode]={}
        dict[statusCode]=1
    

getListofIPaddress()