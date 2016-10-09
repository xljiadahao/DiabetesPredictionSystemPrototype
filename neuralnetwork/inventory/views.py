from django.shortcuts import render

# Create your views here.
from django.template import Template
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
 
from myproject.inventory.models import Customer
 
def customers(request):
    list = Customer.objects.all
    t = get_template('customers.html')
    html = t.render(Context({'customers':list}))
    return HttpResponse(html)
 
def customer(request, custid):
    try:
        c = Customer.objects.get(cid=custid)
        t = get_template('customer.html')
        html = t.render(Context({'customer':c}))
        return HttpResponse(html)
    except Exception as e:
        t = Template("""<html><body>
                     Customer {{ c }} not found
                     </body></html>""")
        html = t.render(Context({'c':custid }))
        return HttpResponse(html)
