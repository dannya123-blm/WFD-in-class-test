from django.contrib import admin
from .models import Customer, Car, Salesperson, SalesInvoice, Mechanic, Service, ServiceTicket, ServiceMechanic, Part, PartsUsed

# Register your models here.
admin.site.register(Customer)
admin.site.register(Car)
admin.site.register(Salesperson)
admin.site.register(SalesInvoice)
admin.site.register(Mechanic)
admin.site.register(Service)
admin.site.register(ServiceTicket)
admin.site.register(ServiceMechanic)
admin.site.register(Part)
admin.site.register(PartsUsed)
