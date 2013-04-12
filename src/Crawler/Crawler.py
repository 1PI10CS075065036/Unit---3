'''
Created on 30-Mar-2013

@author: Sai Gopal
'''

import urllib2
import thread
import datetime
Base_URL='http://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=XXXXX&type=10-Q&dateb=2013&owner=exclude&count=100'
count =0
def Get_Urls(data):
    url=[]
    try:
        for i in range(4): 
            index1= data.index("documentsbutton")
            data = data[index1:]
            index2= data.index("href")
            data = data[index2:]
            finindex = data.index('"')
            
            url.append('http://www.sec.gov'+data[finindex+1:data.index('"',finindex+1)])
        return url
    except:
        return []

def Get_Archive_From_Url(url,Rep):
    Rep=Rep.lower()
    finurl=[]
    try:
        for u in url:
            usock = urllib2.urlopen(u)
            data = usock.read()
            usock.close()
            data=data.lower()
            index1=data.index(Rep)
            data = data[:index1]
            index2=data.rfind(');">')
            data=data[:index2]
            repindex=data[-1]
            data=data[data.index(''+repindex+'] ='):]
            data=data[data.index('"'):]
            data=data[:data.index(';')]
            finurl.append(data);
    finally:
        return finurl


def Start_Crawler(Field):
    global count
    for tick in open('Ticker_Sym'):
        tick.strip()
        temp=Base_URL
        temp=temp.replace('XXXXX',tick)
        temp=temp.replace('\n', '')
        temp=temp+'\n'#Generate The Required URLS to be Crawled
        usock = urllib2.urlopen(temp)
        data = usock.read()
        usock.close()   
        url= Get_Urls(data)
        count=count+1
        thread.start_new_thread(Thread_Print,(tick,Get_Archive_From_Url(url, Field),count))
        return

def Thread_Print(tick,mess,count):
    print tick,mess,count

if __name__ == '__main__':
   # a = datetime.datetime.now().replace(microsecond=0)
    Start_Crawler('CONSOLIDATED STATEMENTS OF INCOME')
    #b = datetime.datetime.now().replace(microsecond=0)
    #print(b-a)