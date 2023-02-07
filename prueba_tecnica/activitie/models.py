from django.db import models
from user.models import UserModel

# Create your models here.
class ActivityModel(models.Model):

    activity = models.CharField(max_length = 255, unique = True)
    type = models.CharField(max_length = 255)
    participants = models.IntegerField()
    price = models.FloatField()
    link = models.CharField(max_length = 500, null = True)
    key = models.IntegerField()
    accessibility = models.FloatField()
    use_it = models.BooleanField(default = True)
    done = models.BooleanField(default = False)
    user_id = models.ForeignKey(UserModel, on_delete = models.CASCADE)

    def __str__(self): #
        return self.activity
    
    class Meta:
        db_table = 'activity'