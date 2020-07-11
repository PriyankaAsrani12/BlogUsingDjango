from django.db import models

# Create your models here.
class Contact(models.Model):
    serialNo=models.AutoField(primary_key=True)
    name=models.CharField(max_length=500)
    phone=models.CharField(max_length=20)
    email=models.CharField(max_length=200)
    subject=models.CharField(max_length=500)
    message=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message from '+self.name
