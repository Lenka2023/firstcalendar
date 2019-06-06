from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
   rem_data=''
   if request.method=='POST':
       rem_data=request.POST   
  # rem=request.POST.get('rem')   
    return HttpResponse("""<html> 
   <body>       
      <form action = "http://localhost:8000/events" method = "post"> 
         <p>Enter Start_time:</p> 
         <p><input type = "text" name = "st" /></p> 
		 <p>Enter End_time:</p> 
         <p><input type = "text" name = "et" /></p> 
		 <p>Enter remember:</p> 
		  <p><input type = "text" name = "rem" /></p>
         <p><input type = "submit" value = "submit" /></p> 
      </form>  
      {{rem_data}}     
   </body> 
</html>""")
	
