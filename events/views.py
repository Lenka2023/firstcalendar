from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
   rem='10'
   context = {
   'page_header': 'Contacts_form',
   }
   return render(request, 'events/contacts_form.html', context)

   
  #if request.method=='POST':
      # rem_data=request.POST   
       #st=request.POST.get('st')
      # et=request.POST.get('et')
       #rem=request.POST.get('rem') 
         #if et=st+10:
            # rem=''  

	
