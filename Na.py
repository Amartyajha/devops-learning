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

All that's left is writing the script. Given you are a star scripter, write a script to help Amir.
The script should maintain the topics in kafka based on the list. What that means is
1) If a topic is added to the list, it should be added in Kafka as well.
2) If a topic is deleted from the list, it should be deleted from Kafka as well.
3) If any of the factors are modified like retention_ms, it should be reflected in Kafka.
Note:
1) You can assume that script is run once after every file change from some kind of ci/cd
system.
2) You have to install kafka locally for testing.

"""
# VCS any change in this should call the commands


# Start time 11:30

# if a topic added, and it has all the values like partition count etc  --> create it

# GET THE GIT diff
# 

from calendar import c
import pwd
import subprocess
import os
import git

os.chdir('/Users/amartyajha/Learning/Python/devops-learning')
last2commits=subprocess.run('git rev-list HEAD -n 2 topics.csv',capture_output=True, shell=True, text=True, check=True)
data=last2commits.stdout.split('\n')
diff_commits=subprocess.run(['git', 'diff', data[0], data[1]],capture_output=True,text=True)
diff=(diff_commits.stdout.split('\n'))
modifiedArray=[]
for i in diff:
    if((i.startswith('+') and not i.startswith('+++')) or (i.startswith('-') and not i.startswith('---'))):
        modifiedArray.append(i)
print(modifiedArray)
#applyModifications(modifiedArray)


"""p1=subprocess.run('''
for i in $data 
do 
    echo $i
    git diff $i $i | grep "^+" | grep -v "^+++"
done
''',capture_output=True, shell=True, text=True, check=True)

print(p1.stdout)"""




import os
import git


"""def getModifications():
    repo = git.Repo('.')
    listofChanges=(repo.git.diff('HEAD~1').split('\n'))
    modifiedArray=[]
    for i in listofChanges:
        if((i.startswith('+') and not i.startswith('+++')) or (i.startswith('-') and not i.startswith('---'))):
            modifiedArray.append(i)
    #print(modifiedArray)
    applyModifications(modifiedArray)

def applyModifications(modifiedArray):
    topicName=[]
    for i in modifiedArray:
        print(i)
        if(i.startswith('-')):
            topicName.append(i[1:].split(',')[0])
        else:
            topicName.append(i.split('+')[1].split(',')[0])

        #print(i.split('-'))
        # check if a new topic is created or is it modified
        #topicName.append(i.split('-').split('+')[1].split(',')[0])
    #print(topicName)


getModifications()"""

