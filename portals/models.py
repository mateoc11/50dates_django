from django.db import models


class users(models.Model): 
   userid = models.PositiveIntegerField(primary_key=True)
   person_1 = models.CharField(max_length=50,null=False) 
   person_2 = models.CharField(max_length=50,null=False) 
   user_password = models.CharField(max_length=50,null=False) 

   def __str__(self): 
      return self.userid
   
   class Meta:
    db_table = 'users'