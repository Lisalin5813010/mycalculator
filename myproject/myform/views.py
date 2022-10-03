from django.shortcuts import render
from django.template import loader
from django.views.generic import TemplateView
# Create your views here.
from .models import CostForm
from django.http import HttpResponse
from myform.forms import BalanceForm


'''def index(request):
    template = loader.get_template('myform/index.html')
    #return render(request, template)
    return HttpResponse(template.render({},request))
    #return HttpResponse("Hello, world. You're at the myform index.")'''

class IndexPage(TemplateView):
    template_name = 'myform/mymodal.html'
    def get(self, request, *args, **kwargs):
        
        form = BalanceForm()

        return render(request,self.template_name, {'form':form})

 
'''def post(self,request):
        form = BalanceForm(request.POST)
       
        if form.is_valid():
            balance = form.cleaned_data['balance']
            if 'add' in request.POST:
                result =  balance
            #elif 'cost' in request.POST:
                
                #tasks = Cost.objects.filter(username__username=request.COOKIES.get('title'))#.order_by('priority')
                #form2 = CostForm(request.POST)
                #if form2.is_valid():
                #form2 = Cost(request.POST or None)
                    #args = {'form': form2}
                    #return render(request, self.template_name,args)

            form = BalanceForm()
        else:
            form = BalanceForm()
            
        args = {'form': form , 'result': result}
        return render(request, self.template_name, args )'''