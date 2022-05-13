"""
At a newly founded startup, one of the developers Amir has introduced Kafka and because of
his adventure every developer has to start using it in their microservice.
Kafka, though it solves hundreds of problems for developers but it brings ten more. One of the
tedious problems is maintenance of topics.
To solve this problem, Amir introduced a csv file containing list of topics in below format:

TOPICS,PARTITIONS,REPLICATION_FACTOR,RETENTION_TIME_MS,MESSAGE_BYTES
dev-eod-enach-for-dpd-accounts,2,3,10800000,5242880
qa-eod-enach-for-dpd-accounts,2,3,10800000,5242880
dev-campaigns-association-updated_two,2,3,10800000,5242880
credit_underwriting.public.batch_text_messages,12,3,10800000,5242880

All that’s left is writing the script. Given you are a star scripter, write a script to help Amir.
The script should maintain the topics in kafka based on the list. What that means is
1) If a topic is added to the list, it should be added in Kafka as well.
2) If a topic is deleted from the list, it should be deleted from Kafka as well.
3) If any of the factors are modified like retention_ms, it should be reflected in Kafka.
Note:
1) You can assume that script is run once after every file change from some kind of ci/cd
system.
2) You have to install kafka locally for testing.

"""


# CSV 

# file -> last commited version 
# changes 
# ++ 
# -- 
# [+dev-eod-enach-for-dpd-accounts,2,3,10800000,5242880, -qa-eod-enach-for-dpd-accounts,2,3,10800000,5242880, +qa-eod-enach-for-dpd-accounts,2,5,10800000,5242880]
# docker compoase file

import os
import subprocess

def getModifications():
    os.chdir('/Users/amartyajha/Learning/Python/devops-learning/Interview')

    # get the last two revision for the same file
    last2commits=subprocess.run('git rev-list HEAD -n 2 topics.csv',capture_output=True, shell=True, text=True, check=True)
    data=last2commits.stdout.split('\n')
    diff_commits=subprocess.run(['git', 'diff', data[1], data[0]],capture_output=True,text=True)
    diff=(diff_commits.stdout.split('\n'))
    modifiedArray=[]
    for i in diff:
        if((i.startswith('+') and not i.startswith('+++')) or (i.startswith('-') and not i.startswith('---'))):
            modifiedArray.append(i)
    print(modifiedArray)
    applyModifications(modifiedArray)

def applyModifications(modifiedArray):
    topicName={}
    for i in modifiedArray:
        if(i[1:].split(',')[0] in topicName):
            topicName[i[1:].split(',')[0]]+=1
        else:
            topicName[i[1:].split(',')[0]]=1
    print(topicName)
    
    """for i in topicName:
        if(topicName[i]>1):
            getTopicValues(i,modifiedArray)
            #subprocess.run(['kafka-topics','--bootstrap-server','localhost:9092','--alter','--topic',i,'--partitions',topicValues[1], '--replication-factor', topicValues[2]],capture_output=True, text=True, check=True)
        else:
            for j in modifiedArray:
                if(j.startswith("+"+i)):
                    topicValues=j.split(',')
                    print(topicValues)
                    #subprocess.run(['kafka-topics','--bootstrap-server','localhost:9092','--create','--topic',i,'--partitions',topicValues[1], '--replication-factor', topicValues[2]],capture_output=True, text=True, check=True)
                elif(j.startswith("-"+i)):
                    topicValues=j.split(',')
                    print(topicValues)
                    #subprocess.run(['kafka-topics','--bootstrap-server','localhost:9092','--delete','--topic',i,'--partitions',topicValues[1], '--replication-factor', topicValues[2]],capture_output=True, text=True, check=True)"""

def getTopicValues(i,modifiedArray):
    for j in modifiedArray:
        if(j.startswith("+"+i)):
            topicValues=j.split(',')
            print(topicValues)


getModifications()