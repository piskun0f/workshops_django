from django.db import models
from django.utils import timezone

class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()

class Post(models.Model):
    photo = models.TextField()
    created_date = models.DateField(default=timezone.now)
    updated_date = AutoDateTimeField(default=timezone.now)
class Service(models.Model):
    name = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    termination_date = models.DateField(blank=True, null=True)
    created_date = models.DateField(default=timezone.now)
    updated_date = AutoDateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Workshop(models.Model):
    title = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    close_date = models.DateField(blank=True, null=True)
    created_date = models.DateField(default=timezone.now)
    updated_date = AutoDateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Client(models.Model):
    first_name = models.CharField(max_length=40)
    second_name = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)
    email = models.CharField(max_length=30)
    created_date = models.DateField(default=timezone.now)
    updated_date = AutoDateTimeField(default=timezone.now)

    def __str__(self):
        return self.first_name + " " + self.second_name
class Order(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=40)
    final_sum = models.DecimalField(max_digits=5, decimal_places=2)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)
    close_date = models.DateField(blank=True, null=True)
    created_date = models.DateField(default=timezone.now)
    updated_date = AutoDateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Employee(models.Model):
    first_name = models.CharField(max_length=40)
    second_name = models.CharField(max_length=40)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)
    created_date = models.DateField(default=timezone.now)
    updated_date = AutoDateTimeField(default=timezone.now)

    def __str__(self):
        return self.first_name + " " + self.second_name

class Services_order(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    created_date = models.DateField(default=timezone.now)
    updated_date = AutoDateTimeField(default=timezone.now)

    def __str__(self):
        return self.order.title + ": " + self.service.name
