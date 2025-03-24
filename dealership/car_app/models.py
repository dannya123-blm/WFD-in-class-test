from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state_province = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)

class Car(models.Model):
    serial_number = models.CharField(max_length=50)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=30)
    year = models.IntegerField()
    car_for_sale = models.BooleanField(default=True)

class Salesperson(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class SalesInvoice(models.Model):
    invoice_number = models.CharField(max_length=50)
    date = models.DateField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    salesperson = models.ForeignKey(Salesperson, on_delete=models.CASCADE)

class Mechanic(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class Service(models.Model):
    service_name = models.CharField(max_length=100)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)

class ServiceTicket(models.Model):
    service_ticket_number = models.CharField(max_length=50)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_received = models.DateField()
    comments = models.TextField()
    date_returned_to_customer = models.DateField()

class ServiceMechanic(models.Model):
    service_ticket = models.ForeignKey(ServiceTicket, on_delete=models.CASCADE)
    mechanic = models.ForeignKey(Mechanic, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    hours = models.DecimalField(max_digits=5, decimal_places=2)
    comment = models.TextField()
    rate = models.DecimalField(max_digits=10, decimal_places=2)

class Part(models.Model):
    part_number = models.CharField(max_length=50)
    description = models.TextField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    retail_price = models.DecimalField(max_digits=10, decimal_places=2)

class PartsUsed(models.Model):
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    service_ticket = models.ForeignKey(ServiceTicket, on_delete=models.CASCADE)
    number_used = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

