from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
   context = {
   'page_header': 'Contacts_form',
   }
   return render(request, 'default_app/contacts_form.html',context)
   #rem='10'
  #if request.method=='POST':
      # rem_data=request.POST   
       #st=request.POST.get('st')
      # et=request.POST.get('et')
       #rem=request.POST.get('rem') 
         #if et=st+10:
            # rem=''  

	
