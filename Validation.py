import sys 
sting=""

def val_qry(a):#validation begins from here
    
    global sting
    b,pf,pw=chk_basic(a)
    
    m=a.split()
    n=len(m)
    c=appnd(m,0,pf)
    d=0

    if b!=0 :
        d=chk_sel(c)
    if d!=0 :
        e=chk_from(m,pf)
        if e!=0:
            f=appnd(m,pw,n)
            
            g,conf=numand(f)
            if conf > 0 :
                if g > 0 :
                    h=chck_where(f,g)
                    return h , sting
                else :
                    h=chk_args2(f)
                    return h , sting
                    
            else :
                return 0 , sting
            
        else :
            return 0 , sting
    else :
        return 0 , sting
    return e , 's'

def numand(a):
    global sting
    n=len(a)
    x=0
    b=0
    z=0
    pos=[]
    
    while x < n :
        if a[x].lower()=='and' :
            b=b+1
            pos.append(x)
        x=x+1
    
    if b > 0 :
        
        while z < b :
            
            if a[pos[z]] != 'AND' :
                
                sting=sting+' and not in caps '
                return 0,0
            
            z=z+1
        return b,1
    else :
        
        return b,1
            
def chck_where(a,b):  
    global sting          
    x=0
    z=0
    # print a
    while z < b+1 :
        
        c=appnd(a,x-1,x+3)
        h=chk_args2(c)
        if h == 0 :
            sting=sting+' error in arguments of where '
            return 0
        x=x+4
        z=z+1
    return 1
        
        
def chk_args2(a):
    global sting
    n=len(a)
    x=0
    ret=0
    
    if (a[x] == 'Company_Name' or a[x] == 'Ticker_Symbol' or a[x] == 'Operating_Margin_Percentage' or a[x] == 'Year' or a[x] == 'Tax' or a[x] == 'Revenue' or a[x] == 'SandM_Expenses' or a[x] == 'Service_Expenses' or a[x] == 'RandD_Expenses' or a[x] == 'Quarter' or a[x] == 'Eps' or a[x] == 'Total_Expenses' or a[x] == 'Operating_Margin' or a[x] == 'Ratio' or a[x] == 'Growth_Rate') and (a[x+1]=='>' or a[x+1]=='>=' or a[x+1]=='<' or a[x+1]=='<=' or a[x+1]=='=' or a[x+1]=='!=') and a[x+2].isalnum() :
        ret=1
    else :
        sting=sting+' wrong argument2 '
        return 0
            
    return ret
   
def appnd(a,b,c):#custom append function list name, start index ,stop index
    global sting
    x=b+1
    d=[]
    while x < c :
        d.append(a[x])
        x=x+1
    return d

def chk_basic(a):#check slect * from * where *
    global sting
    c=a.split()
    d=len(c)
    #print c
    e,pf,pw=chk_pos1(c,d)
    #print e
    if e==1 :
        return 1,pf,pw
        
    else :
        sting=sting+' syntax u entered is error '
        return 0,0,0
            
def chk_pos1(c,d):#make sure select > from > where is order followed   
    global sting
    str1='SELECT'
    str2='FROM'
    str3='WHERE'
    x=0
    pf=0
    pw=0
    while x < d :
        if c[x].lower()==str2.lower() :
            pf=x
        if c[x].lower()==str3.lower() :
            pw=x
        x=x+1
    if pf == 0 :
        sting=sting+" no from present "
        return 0,0,0
    if pw == 0 :
        sting=sting+" no where present "
        return 0,0,0
    if pw < pf :
        sting=sting+' wrong format for is after where '
        return 0,0,0
    if pf == 0 or pf < 2 :
        sting=sting+' no argument for select or select is not present '
        return 0,0,0
    if (pf+2) != pw :
        #print pf
        #print pw
        sting=sting+' no argument for from '
        return 0,0,0
    if c[0] != str1 :
        sting=sting+' select not in capitals '
        return 0,0,0
    
    
    if c[pf] != str2 :
            sting=sting+' for not in capitals '
            return 0,0,0
    
    if c[pw] != str3 :
            sting=sting+' where not in capitals '
            return 0,0,0
    return 1,pf,pw#exit
          
def chk_sel(a):#check contents of select
    global sting
    n=len(a)
    x=n
    if a[0].upper()=='TOP' :
        return chk_top(a,x)
    elif a[0].upper()=='MAX' :
        return chk_max(a,x)
    elif a[0].upper()=='MIN' :
        return chk_min(a,x)
    else :
        return chk_args(a)
 
def chk_args(a):#checks arguments given
    global sting
    n=len(a)
    x=0
    ret=0
    
    
    if a[0] != '*' :
        while x < n :
            if (a[x] == 'Company_Name' or a[x] == 'Operating_Margin_Percentage' or a[x] == 'Eps'or a[x] == 'Ticker_Symbol' or a[x] == 'Year' or a[x] == 'Tax' or a[x] == 'Revenue' or a[x] == 'SandM_Expenses' or a[x] == 'Service_Expenses' or a[x] == 'RandD_Expenses' or a[x] == 'Quarter' or a[x] == 'Total_Expenses' or a[x] == 'Operating_Margin' or a[x] == 'Ratio' or a[x] == 'Growth_Rate' and a[x+1]==','):
                ret=1
            else :
                sting=sting+' wrong argument '
                return 0
            x=x+2
    else :
        ret=1
    return ret 
           

def chk_top(a,n):#check conetnts of top
    global sting
    x=n
    if a[0]== 'TOP' :
        if a[1] == '(' and (a[2]=='Company_Name' or a[2]=='TOTAL_EXPENSES' or a[2]=='OPERATING_MARGIN' or a[2]=='OPERATING_MARGIN_PERCENTAGE' or a[2]=='RATIO' or a[2]=='GROWTH_RATE' or a[2]=='Revenue' ) and a[3]==',' :
            b=a[4]
            if b.isdigit() :
                if a[5]==')' :
                    return 1
                else :
                    sting=sting+' mistake in closing ) '
                    return 0
            else :
                sting=sting+' wrong type '
                return 0
        else :
            sting=sting+' error in initial part '
            return 0   
    else :
        sting=sting+' top not in caps '
        return 0
        
def chk_max(a,n):#check contents of max
    global sting
    x=n
    if a[0]== 'MAX' :
        if a[1] == '(' and (a[2]=='Company_Name' or a[2]=='TOTAL_EXPENSES' or a[2]=='OPERATING_MARGIN' or a[2]=='OPERATING_MARGIN_PERCENTAGE' or a[2]=='RATIO' or a[2]=='GROWTH_RATE' or a[2]=='RandD_Ratio' ) and a[3]==',' :
            b=a[4]
            if b.isdigit() :
                if a[5]==')' :
                    return 1
                else :
                    sting=sting+' mistake in closing ) '
                    return 0
            else :
                sting=sting+' wrong type '
                return 0
        else :
            sting=sting+' error in initial part '
            return 0   
    else :
        sting=sting+' MAX not in caps '
        return 0
    
def chk_min(a,n):#check contents of min
    global sting
    x=n
    if a[0]== 'MIN' :
        if a[1] == '(' and (a[2]=='Company_Name' or a[2]=='TOTAL_EXPENSES' or a[2]=='OPERATING_MARGIN' or a[2]=='OPERATING_MARGIN_PERCENTAGE' or a[2]=='RATIO' or a[2]=='GROWTH_RATE') and a[3]==',' :
            b=a[4]
            if b.isdigit() :
                if a[5]==')' :
                    return 1
                else :
                    sting=sting+' mistake in closing ) '
                    return 0
            else :
                sting=sting+' wrong type '
                return 0
        else :
            sting=sting+' error in initial part '
            return 0   
    else :
        sting=sting+' MIN not in caps '
        return 0
 
def chk_from(a,pf) :#check from value
    global sting
    #print a[pf+1]
    if a[pf+1] != 'DB' :
        sting=sting+' wrong database '
        return 0
    else :
        return 1
 


if __name__ == "__main__":		
	print "enter query"
	a=raw_input()
	b=val_qry(a)#begin validation
	if b==1:
		print 'success'
		#return ''
	else:
		print sting