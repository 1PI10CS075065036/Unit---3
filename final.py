import pymongo
import types
import datetime
import sys
from Validation import val_qry
from bson.objectid import ObjectId
sting=""

def read(z) : #reads all the data from list and returns a list of with proper structured data
	a={}
	n=4
	i=0
	k=0
	counter=0
	Company_Name,Ticker_Symbol=fdetails(z)
	while i<n :
		k=i+1
		Eps,Revenue,SandM_Expenses,RandD_Expenses,Tax,Service_Expenses,Total_Expenses,Operating_Margin,Operating_Margin_Percentage,RandD_Expense_ratio,Growth_Rate,Year,counter=details(z,counter)
		if k==1 :
			a["q1"]={"Eps":Eps,"Revenue":Revenue,"S&M_Expenses":SandM_Expenses,"R&D_Expenses":RandD_Expenses,"Tax":Tax,"Service_Expenses":Service_Expenses,"Total_Expenses":Total_Expenses,"Operating_Margin":Operating_Margin,"Operating_Margin_Percentage":Operating_Margin_Percentage,"R&D_Expense_ratio":RandD_Expense_ratio,"Growth_Rate":Growth_Rate,"Year":Year}
		elif k==2 :
			a["q2"]={"Eps":Eps,"Revenue":Revenue,"S&M_Expenses":SandM_Expenses,"R&D_Expenses":RandD_Expenses,"Tax":Tax,"Service_Expenses":Service_Expenses,"Total_Expenses":Total_Expenses,"Operating_Margin":Operating_Margin,"Operating_Margin_Percentage":Operating_Margin_Percentage,"R&D_Expense_ratio":RandD_Expense_ratio,"Growth_Rate":Growth_Rate,"Year":Year}
		elif k==3 :
			a["q3"]={"Eps":Eps,"Revenue":Revenue,"S&M_Expenses":SandM_Expenses,"R&D_Expenses":RandD_Expenses,"Tax":Tax,"Service_Expenses":Service_Expenses,"Total_Expenses":Total_Expenses,"Operating_Margin":Operating_Margin,"Operating_Margin_Percentage":Operating_Margin_Percentage,"R&D_Expense_ratio":RandD_Expense_ratio,"Growth_Rate":Growth_Rate,"Year":Year}
		elif k==4 :
			a["q4"]={"Eps":Eps,"Revenue":Revenue,"S&M_Expenses":SandM_Expenses,"R&D_Expenses":RandD_Expenses,"Tax":Tax,"Service_Expenses":Service_Expenses,"Total_Expenses":Total_Expenses,"Operating_Margin":Operating_Margin,"Operating_Margin_Percentage":Operating_Margin_Percentage,"R&D_Expense_ratio":RandD_Expense_ratio,"Growth_Rate":Growth_Rate,"Year":Year}
		k=0
		i=i+1
	#print a
	return Company_Name,Ticker_Symbol,a

def fdetails(z): #obtain cname,tsym
	return z[0],z[1]

	
def details(z,counter):#from the crawled data list extract the data in a orderly manner

	Eps=z[2][counter][0]
	
	Revenue=z[2][counter][1]
	  
	SandM_Expenses=z[2][counter][2]
	 
	RandD_Expenses=z[2][counter][3]
	 
	Tax=z[2][counter][4]
	
	Service_Expenses=z[2][counter][5]
	
	Total_Expenses=z[2][counter][6]
	
	Operating_Margin=z[2][counter][7]
	
	Operating_Margin_Percentage=z[2][counter][8]
	
	RandD_Expense_ratio=z[2][counter][9]
	
	Growth_Rate=z[2][counter][10]
	
	Year=z[2][counter][11]


	counter=counter+1
	return Eps,Revenue,SandM_Expenses,RandD_Expenses,Tax,Service_Expenses,Total_Expenses,Operating_Margin,Operating_Margin_Percentage,RandD_Expenses,Growth_Rate,Year,counter

def con():#make connections
	from pymongo import MongoClient
	client=MongoClient("localhost",27017)
	db = client['test_database']
	collection = db['test_collection']
	return db,collection

def insert(z):#the function for inserting data into a collection and into the db

	db,collection=con()
	
	#d=raw_input("enter number of companies\n")
	e=1
	q=0
	while q != 1 :
		q1={}
		Company_Name,Ticker_Symbol,q1=read(z)
		post={}
		post = {"Company_Name": Company_Name , "Ticker_Symbol": Ticker_Symbol , "Quarter":q1}
		posts = db.posts
		post_id=posts.insert(post)
		post_id
		i=0
		while i<4 :
			stri="Quarter.q"
			test=''
			test=stri+str(i+1)
			Company_Name,Eps,Revenue,SandM_Expenses,RandD_Expenses,Tax,Service_Expenses,Total_Expenses,Operating_Margin,Operating_Margin_Percentage,RandD_Expense_ratio,Growth_Rate,Year=details(z,i)
			a=Company_Name
			posts.update({'Company_Name':a},{"$set":{test:{'Eps':Eps,'Revenue':Revenue,'S&M_Expenses':SandM_Expenses,'R&D_Expenses':RandD_Expenses,'Tax':Tax,'Year':Year}},})
			i=i+1	
		q=q+1

def wbsp(a,n):#removes sp chars and spaces
	i=0
	c=[]
	
	while i < n :
		
		if a[i]!=' ' and a[i] != ',' and a[i] != '(' and a[i] != ')' :
			c.append(a[i])
		i=i+1
	d=["*"]
	c.append(d[0])
	return c

def nums(c):#number of select aruments
	n=len(c)
	i=1
	j=0
	#print c[0]
	while i+1<n :
		if c[i]!='FROM' :
			#print c[i]
			j=j+1
		else :
			break
		i=i+1
	#print j
	return j

def posw(w,n):#position of where
	i=0
	while i<n:

		if w[i]=="WHERE":
			break
		i=i+1
	return i

def numa(c):#number of ands
	n=len(c)
	
	j=0
	x=posw(c,n)
	i=x
	while i+1<n :
		if c[i]=='AND' :
			j=j+1
		if c[i]=='*':
			break
		i=i+1
	return j

def arwq(c,noa):#number of where arguments
	x=-2
	i=0
	
	if c[x]!='DB':
		while c[x]!='DB':

			if c[x]!= '=' and c[x]!= '!=' and c[x]!= '>' and c[x]!= '<' :
				
				i=i+1
			x=x-1
		if noa==0:
			
			i=i-1
		else :
			i=i-1-noa

	#print i
	return i/2
	
	

#DHIREN>PY BEGINS HERE !


def convert(x):#conversion from string to int and vice versa
	try:
		return int(x)
	except:
		return x																																																																																																																											





def get(a,nos,noa):#get the select and where dictionaries for querying mongodb
	#print a
	where={}
	select={}

	select=get_sel(a,nos)
	#print select
	where=get_where(a,noa)
	#print where
	return select , where 

def get_sel(a,nos):#get select dict
	s={}
	i=1
	n=len(a)
	i=0
	#print a
	while i < n :
		#print a[i]
		if a[i]=='WHERE' :
			break
		i=i+1
	j=0
	#print i
	#print a[6]
	c=i
	q=chkq(a,n,c)
	#print q
	i=1

	while i <= nos :
		l=chks(a[i])
		#print l
		if l==1 :
			b=a[i]
			s[b]=1
			i=i+1
		elif l==0:
			if q==1:
				g=getsq(a)
				k="Quarter."
				b=a[i]
				j=k+g+'.'+b
				s[j]=1
				i=i+1
			elif q==0 :
				k="Quarter.q1."
				b=a[i]
				j=k+b
				s[j]=1
				i=i+1
	s['_id']=0
	
	return s

def getsq(a) :#getting quarter
	n=len(a)
	i=0
	while i<n:
		if a[i]=='Quarter':
			break
		i=i+1
	return a[i+2] 

def chks(a):#a check for slect if the arguments are either cname or tsym
	b=0
	if a == 'Company_Name' or a == 'Ticker_Symbol' :
		return 1
	else :
		return b

def chkq(a,n,k):#check if quarter speciifed for query
	i=k
	while i< n :
		if a[i]=='Quarter' :
			return 1
		i=i+1
	return 0

def get_q(a,n):#get the number of quarter
	i=0
	while i<n:
		if a[i]=='Quarter' :
			return a[i+2]
		i=i+1

def get_where(a,noa):#get the where dictionary for query
	w={}
	n=len(a)
	i=0
	#print a
	while i < n :
		#print a[i]
		if a[i]=='WHERE' :
			break
		i=i+1
	j=0
	#print i
	#print a[6]
	c=i
	q=chkq(a,n,c)
	if q != 0 :
		x=get_q(a,n)
		noa=noa-1
	#print x
	b=['=']
	#print noa+1
	while j < noa+1 :
		
		#print a[i+2]
		#print i
		if a[i+2] == '=' :
			if q == 1 :
				st='Quarter.'+x+'.'
				re=st+a[i+1]
				x=convert(a[i+3])
				if type(x) == types.StringType :
					re=a[i+1]
				w[re]=x
			else :
				st='Quarter.q1.'
				re=st+a[i+1]
				x=convert(a[i+3])
				if type(x) == types.StringType :
					re=a[i+1]
				w[re]=x
			
		else :
			if a[i+2] == '<' :
				if q == 1 :
					#print 'hello'
					st='Quarter.'+x+'.'
					

					f={}
					f['$lt']=convert(a[i+3])
					#print f
					
					re=st+a[i+1]
					w[re]=f
				else :
					f={}
					f['$lt']=convert(a[i+3])
					#print f
					st='Quarter.q1.'
					re=st+a[i+1]
					w[re]=f
					
			elif a[i+2] == '>' :
				if q == 1 :
					
					st='Quarter.'+x+'.'
					
					f={}
					f['$lt']=convert(a[i+3])
					#print f
					
					re=st+a[i+1]
					w[re]=f
				else :
					f={}
					f['$gt']=convert(a[i+3])
					st='Quarter.q1.'
					re=st+a[i+1]
					w[re]=f
			elif a[i+2] == '>=' :
				if q == 1 :
					st='Quarter.'+x+'.'
					f={}
					f['$lt']=convert(a[i+3])
					#print f
					
					re=st+a[i+1]
					w[re]=f
				else :
					f={}
					f['$gte']=convert(a[i+3])
					st='Quarter.q1.'
					re=st+a[i+1]
					w[re]=f
			elif a[i+2] == '<=' :
				if q == 1 :
					st='Quarter.'+x+'.'
					f={}
					f['$lt']=convert(a[i+3])
					#print f
					
					re=st+a[i+1]
					w[re]=f
				else :
					f={}
					f['$lte']=convert(a[i+3])
					st='Quarter.q1.'
					re=st+a[i+1]
					w[re]=f
			elif a[i+2] == '!=' :
				if q == 1 :
					st='Quarter.'+x+'.'
					f={}
					f['$lt']=convert(a[i+3])
					#print f
					
					re=st+a[i+1]
					w[re]=f
				else :
					f={}
					f['$ne']=convert(a[i+3])
					st='Quarter.q1.'
					re=st+a[i+1]
					w[re]=f
		i=i+4
		j=j+1
	return w






#ENDS HERE












def prcs(a):#processing query
	db,collection=con()
	posts = db.posts
	m=a.split()
        n=len(m)
        
        v=wbsp(m,n)
        
        nos=nums(v)
        
        noa=numa(v)
        
        arw=arwq(v,noa)
        
        #print nos,noa,arw
        if v[1]=='*' and noa==0 and arw==0 :#select 8
			cursor= posts.find()
			return getres(cursor)
	elif v[1]=='*' and noa==0 and arw==1 :
			#c="Quarter.q1.Year"
			#print "hello"
			#cursor=posts.find({c:1123})
			#print cursor
			#print "here"
			v.pop(-1)
			select,where=get(v,nos,noa)
			cursor=posts.find(where)
			return getres(cursor)
	elif nos==2 and noa==0 and arw==1:
			#c="Quarter.q2.Revenue"
			#cursor=posts.find({c:6},{"Company_Name":1,"tysym":1,"_id": 0})
			#print cursor
			v.pop(-1)
			select,where=get(v,nos,noa)
			cursor=posts.find(where,select)
			return getres(cursor)
	elif nos ==1 and noa==2 and arw==3:
			#c=""
			#print "at 1,2,3"
			
			#v.pop(-1)
			#print v
			v.pop(-1)
			select,where=get(v,nos,noa)
			#print where , select
			cursor=posts.find(where,select)
			#cursor=posts.find({"Quarter.q1.Tax":94,"Quarter.q1.Revenue": { '$gt' : 50 },"Quarter.q1.Eps":64},{"_id":0,"Company_Name":1})
			return getres(cursor)
	elif nos ==1 and noa==0 and arw==1:
			#c=""
			#print "at 1,2,3"
			
			#v.pop(-1)
			#print v
			v.pop(-1)
			select,where=get(v,nos,noa)
			#print where , select
			cursor=posts.find(where,select)
			#cursor=posts.find({"Quarter.q1.Tax":94,"Quarter.q1.Revenue": { '$gt' : 50 },"Quarter.q1.Eps":64},{"_id":0,"Company_Name":1})
			return getres(cursor)

	elif v[1] == 'TOP' :
			#tprint v
			x=convert(v[9])
			cursor=posts.find({"Quarter.q1.Year":{'$gt':x}}).sort("Revenue",1).limit(1)
			#print cursor
			return getres(cursor)
	elif v[1] == 'MAX' :
			x=convert(v[9])
			cursor=posts.find({"Quarter.q1.Year":{'$gt':x}}).sort("R&D_Expenses",1).limit(1)
			return getres(cursor)						
						
						#print db.posts.find_one()
			
			
def getres(cursor):#get results from object list returned from processed query
	#print "hey"
	#return 'test'
	retlist = []
	for i in cursor:
		#print "hello"
		retlist.append(i)   # result_object is a dict that holds JSON object
		#result_object['_id']
	#print len(retlist)
	return retlist
def query():#entering query

	db,collection=con()
	posts = db.posts
	#print posts.find_one()
	#print "enter query \n"
	a=raw_input()
	#b=val_qry(a)#try this first :
	b=1
	
	if b==1 :
		print prcs(a)
	else:
		exit(0)

	
	'''
	inp=raw_input("the query please: \n")
	if(len(inp)>0):
		print posts.find_one(inp)#run it
	else:
		print posts.find_one()#run it
		#run it
	'''	

def initlist():#test initialisation list used for debugging purposes
	return ['werty','wer',[['1','1','1','1','1','1','1','1','1','1','1','1'],['2','2','2','2','2','2','2','2','2','2','2','2'],['3','3','3','3','3','3','3','3','3','3','3','3'],['4','4','4','4','4','4','4','4','4','4','4','4']]]

def update():#performing updates ....not needed
	db,collection=con()
	posts = db.posts
                
	#posts.update({'Company_Name':'werty'},{"$set":{"Quarter.q1":{'Eps':64,'Revenue':65,'S&M_Expenses':34,'R&D_Expenses':48,'Tax':94,"Service_Expenses":45,"Total_Expenses":49,"Operating_Margin":53,"Operating_Margin_Percentage":57,"R&D_Expense_ratio":61,"Growth_Rate":65,'Year':1134}}})
	#posts.update({'Company_Name':'werty'},{"$set":{"Quarter.q2":{'Eps':56,'Revenue':66,'S&M_Expenses':13,'R&D_Expenses':84,'Tax':93,"Service_Expenses":46,"Total_Expenses":50,"Operating_Margin":54,"Operating_Margin_Percentage":58,"R&D_Expense_ratio":62,"Growth_Rate":66,'Year':11}}})
	#posts.update({'Company_Name':'werty'},{"$set":{"Quarter.q3":{'Eps':74,'Revenue':67,'S&M_Expenses':44,'R&D_Expenses':78,'Tax':92,"Service_Expenses":47,"Total_Expenses":51,"Operating_Margin":55,"Operating_Margin_Percentage":59,"R&D_Expense_ratio":63,"Growth_Rate":67,'Year':34}}})
	#posts.update({'Company_Name':'werty'},{"$set":{"Quarter.q4":{'Eps':57,'Revenue':74,'S&M_Expenses':54,'R&D_Expenses':75,'Tax':91,"Service_Expenses":48,"Total_Expenses":52,"Operating_Margin":56,"Operating_Margin_Percentage":60,"R&D_Expense_ratio":64,"Growth_Rate":68,'Year':134}}})
	print posts.find_one()
	
if __name__ == '__main__':#main
	z=initlist()
	while(1):
		a=raw_input("1.to input 2.to query 3.to update\n")
		b=int(a)
		if b==1 :
			insert(z)
		elif b==2 :
			query()
		elif b==3 :
			update()



#more importantly all the read is happening manually not by some list or anything so this is far from complete...
