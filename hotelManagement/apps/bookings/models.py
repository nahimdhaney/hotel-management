from django.db import models

class Client(models.Model):
    """Client model
    nit: NIT or CI
    Comercial Name: (name like client is known)
    invoice Name: (razon social)
    """
    nit = models.TextField(max_length=20)
    comercial_name = models.TextField(max_length=200)
    invoice_name = models.TextField(max_length=200)
    email = models.FileField(null=True)
    create=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    def __str__(self):
        # import pdb; pdb.set_trace()
        return '%s %s %s' % (self.nit," - ",self.comercial_name)




class Room(models.Model):
    """Room model
    number: just the number of the room 
    price: this is the price model
    """
    number = models.TextField(max_length=20)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    create=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)


    def __str__(self):
        return '%s %s %s' % (self.number,"-",self.price)





class Booking(models.Model):
    """
    The main Model (or trunk) which determines 
    the Booking itself
    work directly with BookingRoom in order that one Booking could
    contains 1 or more rooms
    
    """
    client = models.ForeignKey(
        Client, on_delete=models.PROTECT)  # you cant delete the client if it has Bookings 
    status = models.IntegerField(default=1,null=True)
    create = models.DateTimeField(auto_now_add=True)  # creation date
    modified = models.DateTimeField(auto_now=True)  # modification date

class Invoice(models.Model):
    """Invoice model
    which represents an local invoice,

    """
    booking = models.ForeignKey(
        Booking, on_delete=models.PROTECT,null=True)  # you cant delete the booking if it has Bookings 
    nit = models.TextField(max_length=25)
    name = models.TextField(max_length=100)
    number = models.IntegerField()
    status = models.IntegerField()
    auth_number = models.TextField(max_length=25)
    code_control = models.TextField(max_length=25)
    discount = models.DecimalField(max_digits=5,decimal_places=2)
    total = models.DecimalField(max_digits=8,decimal_places=2)
    date = models.DateField()
    create = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s %s' % (self.number,"-",self.name)

class BookingRoom(models.Model):
    """
    this model represents N x N 
    Booking vs Rooms
    """
    room = models.ForeignKey(
        Room, on_delete=models.PROTECT)  # you cant delete a booked room if it has Bookings 
    booking = models.ForeignKey(
        Booking, on_delete=models.PROTECT)  # you cant delete the booking if it has Bookings 
    status = models.IntegerField(default=1) # could has their own status
    inicial_date = models.DateField()  
    final_date = models.DateField()  
    create = models.DateTimeField(auto_now_add=True)  # creation date
    modified = models.DateTimeField(auto_now=True)  # modification date


class Payment(models.Model):
    """
    this model represent a payment
    from the client
    """
    booking = models.ForeignKey(
        Booking, on_delete=models.PROTECT)  # you cant delete a payment if it has Bookings asociated 
    status = models.IntegerField(default=1) # could has their own status 
    method = models.IntegerField(default=1) #1 cash| 2 Credit Card | 3 Debit Card 
    amount = models.DecimalField(max_digits=8,decimal_places=2)
    date = models.DateField() #payment day
    create = models.DateTimeField(auto_now_add=True)  # creation date
    modified = models.DateTimeField(auto_now=True)  # modification date

    