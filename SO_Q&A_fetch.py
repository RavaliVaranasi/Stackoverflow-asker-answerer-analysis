#!/usr/bin/env python
# coding: utf-8

# In[4]:


from stackapi import StackAPI, StackAPIError

SITE = StackAPI('stackoverflow',key='Qw9QT*o*6*NoY1ZHKGsVNg((')#passing key to avoid throttling
SITE.max_pages=3   #number of pages to fetch data
SITE.page_size=100 #number of posts per page
questions = SITE.fetch('questions', sort='activity',tagged='.net')#Fetching Questions from .net sorted by votes


# In[94]:


print(len(questions['items'])) #checking for number of questions fetched


# In[6]:


#Block to collect all the question Id's of the data
qid = []
for i in (questions['items']):
    qid.append(i['question_id'])
print(len(qid))


# In[7]:


#Fetching all the answers for the respective questions
answer = []
for q in qid:
    ans = SITE.fetch('questions/{0}/answers/'.format(q))
    answer.append(ans)
print(len(answer))
# print((answer[1]))


# In[137]:


def header(output):
    output.append('Tags');
    output.append('Asker Reputation')
    output.append('Asker Id')
    output.append('Profile Image')
    output.append('Asker Name')
    output.append('Link to Asker')
    output.append('Is Answered')
    output.append('View Count')
    output.append('Answer Count')
    output.append('Score')
    output.append('last_activity_date')
    output.append('creation_date')
    output.append('Question Id')
    output.append('link')
    output.append('Title')
    output.append('Answerer reputation')
    output.append('Answerer Id')
    output.append('Answerer user_type')
    output.append('Answerer accept rate')
    output.append('Answerer profile_image')
    output.append('Answerer Name')
    output.append('Answerer link')
    output.append('Is Accepted')
    output.append('Answerer score')
    output.append('last_activity_date')
    output.append('last_edit_date')
    output.append('creation_date')
    output.append('Answer_id')
    output.append('Question_id')
    return(output)


# In[138]:


def extract():
    for i in range(len(questions['items'])):
        for j in range(len(answer[i]['items'])):
            qown = questions['items'][i]['owner']
            aown = answer[i]['items'][j]['owner']
            if qown['user_type'] == 'does_not_exist' or aown['user_type'] == 'does_not_exist':
                continue
            else:    
                out = []
                out.append(questions['items'][i]['tags'])
                out.append(qown['reputation'])
                out.append(qown['user_id'])
                out.append(qown['user_type'])
                out.append(qown['profile_image'])
                out.append(qown['display_name'])
                out.append(qown['link'])
                out.append(questions['items'][i]['is_answered'])
                out.append(questions['items'][i]['view_count'])
                out.append(questions['items'][i]['score'])
                out.append(questions['items'][i]['last_activity_date'])
                out.append(questions['items'][i]['creation_date'])
                out.append(questions['items'][i]['question_id'])
                out.append(questions['items'][i]['link'])
                out.append(questions['items'][i]['title'])

                out.append(aown['reputation'])
                out.append(aown['user_id'])
                out.append(aown['user_type'])
                if 'accept_rate' not in aown:
                    out.append('N/A')
                else:
                    out.append(aown['accept_rate'])
                out.append(aown['profile_image'])
                out.append(aown['display_name'])
                out.append(aown['link'])
                out.append(answer[i]['items'][j]['is_accepted'])
                out.append(answer[i]['items'][j]['score'])
                out.append(answer[i]['items'][j]['last_activity_date'])
                if 'last_edit_date' not in answer[i]['items'][j]:
                    out.append('N/A')
                else:
                    out.append(answer[i]['items'][j]['last_edit_date'])
                out.append(answer[i]['items'][j]['creation_date'])
                out.append(answer[i]['items'][j]['answer_id'])
                out.append(answer[i]['items'][j]['question_id'])
                tsvout.writerow(out)

import csv
#opening the file which we want to write the data
with open('C:/Users/Ravali/Desktop/allposts.tsv', 'w',encoding='utf-8') as tsvout:
    output = []
    head = header(output);
    tsvout = csv.writer(tsvout, delimiter = '\t')
    tsvout.writerow(head)
    extract()
print('File generated succesfully')


# In[141]:


def output(result):
    with open('C:/Users/Ravali/Desktop/trail3.tsv', 'w',encoding='utf-8') as tsvout:
        out2 = []
        out2.append('Asker Id')
        out2.append('Answerer Id')
        if result == 'meta_data':
            out2.append('Post')
        tsvout = csv.writer(tsvout, delimiter = '\t')
        tsvout.writerow(out2)

        for i in range(len(questions['items'])):
            for j in range(len(answer[i]['items'])):
                qown = questions['items'][i]['owner']
                aown = answer[i]['items'][j]['owner']
                if qown['user_type'] == 'does_not_exist' or aown['user_type'] == 'does_not_exist':
                    continue
                else:    
                    out2 = []
                    out2.append(qown['user_id'])
                    out2.append(aown['user_id'])
                    if result == 'meta_data':
                        out2.append(questions['items'][i]['link'])
                    tsvout.writerow(out2)

    print('File generated succesfully')

output('ask_ans')
output('meta_data')

