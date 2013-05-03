from Validation import val_qry
from final import prcs

def Query(Que):
	retval,mess= val_qry(Que)
	if  retval == 0:
		return mess
	else:
		return prcs(Que)





def Start(Que):
	RetMess = "Content-type:text/html\r\n\r\n"+"<html>\n<head>\n<title>Python 3</title>\n</head>\n<body>\n<br/><br/>\n<h2>Query Entered :: "+Que+"</h2>"
	Results = Query(Que)

	
	import types

	if type(Results) == types.ListType:
		if len(Results) != 0:
			RetMess = RetMess +  '\n<br/><br/>	\n<table>\n<caption>Results</caption>'
			
			for i in Results:
				RetMess = RetMess + '<p>'+str(i)+'</p>'
			
			
			RetMess= RetMess + '\n</table>'
		else:
			RetMess= RetMess + '<p style="color:red">Empty Results</p>'
	else:
		RetMess = RetMess + '\n<p style="color:red">Error In Query Entered</p><br/>'
		RetMess = RetMess + '\n<p>Error:'+ Results+'</p><br/>'
	
	RetMess= RetMess + '\n<br/><br/>\n<a href="http://localhost/Main.html"><input type="button" value="Try Another Query"/></a>\n</body>\n</html>'

	return RetMess