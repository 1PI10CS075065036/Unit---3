'''
Created on 30-Mar-2013

@author: Sai Gopal
'''

import urllib2
import thread
Base_URL='http://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=XXXXX&type=10-Q&dateb=2013&owner=exclude&count=100'

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
    finurl=[]
    try:
        for u in url:
            usock = urllib2.urlopen(u)
            data = usock.read()
            usock.close()
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
        thread.start_new_thread(Thread_Print,(tick,Get_Archive_From_Url(url, Field)))

def Thread_Print(tick,mess):
    print tick,mess

if __name__ == '__main__':
    Start_Crawler('CONSOLIDATED STATEMENTS OF INCOME')