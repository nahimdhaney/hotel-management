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
        return '%s %s %s' % (self.number," - ",self.price)