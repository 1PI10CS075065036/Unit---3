import urllib2
import copy
import thread
import datetime
from Miner import Get_Data
Base_URL='http://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=XXXXX&type=10-Q&dateb=2013&owner=exclude&count=100'
count =0
def Get_Urls(data):
    url=[]
    year=[]
    try:
        copydata=copy.deepcopy(data)
        comp_index= copydata.index("companyName")
        copydata=copydata[comp_index:]
        copydata=copydata[copydata.index(">")+1:copydata.index("<")]
        for i in range(4): 
            index1= data.index("documentsbutton")
            data = data[index1:]
            index2= data.index("href")
            data = data[index2:]
            finindex = data.index('"')
            url.append('http://www.sec.gov'+data[finindex+1:data.index('"',finindex+1)])
            data=data[data.index("<td>"):]
            data=data[data.index("<td>"):]
            year.append(int(data[4:data.index("-")]))
        return url,copydata,year
    except:
        return [],"",[]

def Get_Archive_From_Url(url,Rep):
    Rep=Rep.lower()
    finurl=[]
    try:
        for u in url:
            usock = urllib2.urlopen(u)
            data = usock.read()
            usock.close()
            copydata=data
            data=data.lower()
            index1=data.index(Rep)
            copydata = copydata[:index1]
            index2=copydata.rfind(');">')
            copydata=copydata[:index2]
            repindex=copydata[-1]     
            copydata=copydata[copydata.index(''+repindex+'] ='):]
            copydata=copydata[copydata.index('"')+1:]
            copydata=copydata[:copydata.index(';')-1]
            copydata="http://www.sec.gov"+copydata
            finurl.append(copydata);
    finally:
        return finurl


def Start_Crawler(Field):
    global count
    for tick in     open('Ticker_Sym.txt'):
        tick.strip()
        temp=Base_URL
        temp=temp.replace('XXXXX',tick)
        temp=temp.replace('\n', '')
        temp=temp+'\n'#Generate The Required URLS to be Crawled
     #   print temp
        usock = urllib2.urlopen(temp)
        data = usock.read()
        usock.close()
        tick=tick.strip()
        url,c_name,year= Get_Urls(data)
        count=count+1
        finurl = Get_Archive_From_Url(url, Field)
        print year
        if len(finurl) == 4:
            Get_Data(year,[c_name,tick],finurl)
    #        print 'thread started'
            #thread.start_new_thread(Thread_Print,(year,[c_name,tick],finurl))

def Thread_Print(a,mess,count):
    try:
        print a,mess,count
    except Exception,e:
        print "Exception",e

if __name__ == '__main__':
   # a = datetime.datetime.now().replace(microsecond=0)
    Start_Crawler('CONSOLIDATED STATEMENTS OF OPERATIONS')
    #b = datetime.datetime.now().replace(microsecond=0)
    #print(b-a)
