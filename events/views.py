from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("""<html> 
   <body>       
      <form action = "http://localhost:8000/events" method = "post"> 
         <p>Enter time:</p> 
         <p><input type = "text" name = "t" /></p> 
		 <p>Enter time:</p> 
         <p><input type = "text" name = "t" /></p> 
		 <p>Enter remember:</p> 
		  <p><input type = "text" name = "rem" /></p>
         <p><input type = "submit" value = "submit" /></p> 
      </form>       
   </body> 
</html>""")
	
