from django.db import models


class Users(models.Model): 
   userid = models.AutoField(primary_key=True)
   person_1 = models.CharField(max_length=50,null=False) 
   person_2 = models.CharField(max_length=50,null=False) 
   user_password = models.CharField(max_length=50,null=False) 

   def __str__(self): 
      return self.userid
   
   class Meta:
    db_table = 'users'

class Photos(models.Model): 
   image_id = models.AutoField(primary_key=True)
   title = models.CharField(max_length=100,null=True) 
   imagepath = models.CharField(max_length=50,null=True,default="'images/love.png'") 
   userid = models.ForeignKey(Users,on_delete=models.CASCADE,db_column='userid')

   def __str__(self): 
      return self.image_id
   
   class Meta:
    db_table = 'images_DB'