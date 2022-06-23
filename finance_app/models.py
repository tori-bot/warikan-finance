from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Profile(models.Model):
    CATEGORIES=(
        ('non-binary','non-binary'),
    ('male', 'male'),
    ('female', 'female'),
    )
    user=models.OneToOneField(User,primary_key=True,on_delete=models.CASCADE)   
    profile_picture=models.ImageField(upload_to='profile_pictures/',default='default.jpg',null=True) 
    bio=models.TextField()
    gender=models.CharField(max_length=30,choices=CATEGORIES,default='non-binary',null=True,blank=True)
    country=models.CharField(max_length=50,null=True,blank=True)
    date_of_birth=models.DateField(null=True, blank=True)
    
    
    @receiver(post_save, sender=User) 
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)


    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()

    def delete_profile(self):
        self.delete()

    def update_profile(self,user,profile_picture,bio):
        self.user=user
        self.profile_picture=profile_picture
        self.bio=bio
        self.save()

    @classmethod
    def get_profile_by_id(cls,id):
        profile = Profile.objects.filter(user__id = id).first()
        return profile

    @classmethod
    def search_profile(cls,search_term):
        profile=cls.objects.filter(user__username__icontains=search_term).all()
        return profile

    def __str__(self):
        return self.user

CATEGORIES=(
    ('cash', 'cash'),
    ('bank account', 'bank account'),
    ('mpesa', 'mpesa'),
)
class Account(models.Model):
    name = models.CharField(max_length=100)
    category=models.CharField(max_length=30,choices=CATEGORIES,default='cash',null=True)
    amount=models.IntegerField(null=True)
    description = models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)


    def delete_account(self):
        self.delete()

    def update_account(self,name,category,amount,description,user):
        self.user=user
        self.name=name
        self.category=category
        self.amount=amount
        self.description=description
        self.save()