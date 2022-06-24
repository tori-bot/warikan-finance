
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
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)   
    profile_picture=models.ImageField(upload_to='profile_pictures/',default='default.jpg',null=True) 
    bio=models.TextField()
    gender=models.CharField(max_length=30,choices=CATEGORIES,default='non-binary',null=True,blank=True)
    date_of_birth=models.DateField(null=True, blank=True)
    country=models.CharField(max_length=50,null=True,blank=True)
    city=models.CharField(max_length=50,null=True,blank=True)

    
    
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

    def create_account(self):
            self.save()

    def delete_account(self):
        self.delete()

    def update_account(self,name,category,amount,description,user):
        self.name=name
        self.category=category
        self.amount=amount
        self.description=description
        self.user=user
        self.save()

    def update_account(self,name,category,amount,description,user):
        self.user=user
        self.name=name
        self.category=category
        self.amount=amount
        self.description=description
        self.save()

    def __str__(self):
        return self.name

CATEGORIES=(
    ('weekly', 'weekly'),
    ('2 weeks', '2 weeks'),
    ('monthly', 'monthly'),
    ('quarterly', 'quarterly'),
    ('6 months', '6 months'),
    ('annually', 'annually'),
)


class Bill(models.Model):
    category=models.CharField(max_length=30,choices=CATEGORIES,default='monthly',null=True)
    name=models.CharField(max_length=100,null=True)
    amount=models.IntegerField()
    description=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    due_date=models.DateTimeField(null=True)

    def create_bill(self):
            self.save()

    def delete_bill(self):
        self.delete()

    def update_bill(self,name,category,amount,description,user,due_date):
        self.name=name
        self.category=category
        self.amount=amount
        self.description=description
        self.user=user
        self.due_date=due_date
        self.save()

    def __str__(self):
        return self.name