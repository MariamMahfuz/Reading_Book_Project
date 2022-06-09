from django.db import models

# Create your models here.
class User_list(models.Model):
    name=models.CharField(max_length=60)
    address=models.CharField(max_length=300)
    message=models.CharField(max_length=500)
    photo=models.ImageField(upload_to='photo',null=False,blank=False)
    def __str__(self):
        return str(self.name)

class Writer(models.Model):
    user=models.ForeignKey(User_list,on_delete=models.CASCADE,null=True,blank=True)
    writer_name=models.CharField(max_length=30)
    book_title=models.CharField(max_length=70)
    def __str__(self):
        return str(self.user)
