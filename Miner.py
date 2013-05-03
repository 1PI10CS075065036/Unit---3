import thread
import urllib2
import re
import random
import time
from final import insert

def Clean_Data(robj):
    elem=[]
    i=0
    ele=robj.group(2)
    ele=ele.strip()
    ele=ele.strip("$")
    ele=ele.strip()
    ele=ele.strip("(")
    ele=ele.strip(")")
    elem=list(ele)
    while i < len(elem):
        if elem[i]!=",":
            pass
        else:
            elem.pop(i)
        i=i+1
    ele=''.join(elem)
    return float(ele)

def tax():
    return random.randint(25,35)

def Check_Empty(z):
    flag=0
    for i in z:
        if i!=0:
#            print z
            pass
        else:
#            print z
            flag=1
            break
    if flag==0:
#        print z
        return z
    else:
#        print "aha",z
        return 0

def Calculations(y):
    #print y
    z=y[2]+y[3]+y[4]
    y.append(z)
    z=y[0]-y[5]
    y.append(z)
    z=(float(y[6])/y[0])*100
    y.append(z)
    z=(float(y[3])/y[0])
    y.append(z)
    z=(float(y[6])/y[0])
    y.append(z)
    return y

def Mine_Data(year,data):
    z=[]
    print"h0"
    pattern = r'<td (.*?)><a (.*?)>(.*?)basic(.*?)</a></td>(.*?)</tr>'
    robj = re.search(pattern, str(data),re.DOTALL|re.I)
    if robj:
        b=str(robj.group(5))
        pattern_1= r'<td (.*?)>(.*?)<span></span></td>'
        robj1 = re.search(pattern_1, b, re.DOTALL|re.I)
        a = Clean_Data(robj1)
        z.append(a)
    else:
        return z.append(0)
    print"h1"
    pattern = r'<td (.*?)><a (.*?)>(total net revenue|total revenues|revenues|net revenues|revenue|total revenue)</a></td>(.*?)</tr>'
    robj = re.search(pattern, str(data), re.DOTALL|re.I)
    if robj:
        a = str(robj.group(4))
        pattern_1= r'<td (.*?)>(.*?)<span></span></td>'
        robj1 = re.search(pattern_1, a, re.DOTALL|re.I)
        a = Clean_Data(robj1)
        z.append(a)
    else:
        return z.append(0)
    print"h2"
    pattern = r'<td (.*?)><a (.*?)>(selling and marketing|sales and marketing)</a></td>(.*?)</tr>'
    robj = re.search(pattern, str(data),re.DOTALL|re.I)
    if robj:
        b=str(robj.group(4))
        pattern_1= r'<td (.*?)>(.*?)<span></span></td>'
        robj1 = re.search(pattern_1, b, re.DOTALL|re.I)
        a=Clean_Data(robj1)
        z.append(a)
    else:
        return z.append(0)
    print"h3"
    pattern = r'<td (.*?)><a (.*?)>(research and development|product development)</a></td>(.*?)</tr>'
    robj = re.search(pattern, str(data),re.DOTALL|re.I)
    if robj:
        b=str(robj.group(4))
        pattern_1= r'<td (.*?)>(.*?)<span></span></td>'
        robj1 = re.search(pattern_1, b, re.DOTALL|re.I)
        a=Clean_Data(robj1)
        z.append(a)
    else:
        return z.append(0)
    print"h4"
    a=tax()
    z.append(a)
    pattern = r'<td (.*?)><a (.*?)>(services|general and administrative)</a></td>(.*?)</tr>'
    robj = re.search(pattern, str(data),re.DOTALL|re.I)
    if robj:
        b=str(robj.group(4))
        pattern_1= r'<td (.*?)>(.*?)<span></span></td>'
        robj1 = re.search(pattern_1, b, re.DOTALL|re.I)
        a=Clean_Data(robj1)
        z.append(a)
    else:
        return z.append(0)
    return z

def Get_Data(y,details,url_list):
    send_set=[]
    temp=[]
    year=y
    det=details
    print details
    for i in details:
        i=i.strip()
        i=i.replace(" ","_")
        send_set.append(i)
    
    for i in url_list:
        print i
        usock = urllib2.urlopen(i)
        data = usock.read()
        usock.close()
        try:
            a=Mine_Data(year,data)
        except Exception,e:
            print e
        y= Check_Empty(a)
        #print year
        if y!=0:
            y=Calculations(y)
            for i in range(1):
                y.append(year[i])
            year.pop(0)
            temp.append(y)
    send_set.append(temp)
    insert(send_set)
    

if __name__ == "__main__":
    pass
