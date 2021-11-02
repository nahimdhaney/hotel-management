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
