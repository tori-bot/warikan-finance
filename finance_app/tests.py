from django.test import TestCase
from .models import Profile,Bill,Account
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTest(TestCase):
    def setUp(self):
        self.test = User(username = 'test',email = 'tess@gmail.com')
        self.test = Profile(user = self.test,user_id = 1,bio = 'my hood', email='tess@gmail.com',profile_pic = 'image.jpg',location='Nairobi', NeighbourHood='Nairobi')

    def test_instance(self):
        self.assertTrue(isinstance(self.test,Profile))

    def test_save_profile(self):
        self.save_profile()
        all_profiles = Profile.objects.all()
        self.assertTrue(len(all_profiles),0)

    def test_delete_profile(self):
        self.test.delete_profile()
        all_profiles = Profile.objects.all()
        self.assertEqual(len(all_profiles),0)

class AccountTestCase(TestCase):
    def setUp(self):
        self.new= Account(name ='Nairobi Hospital',category = 'cash',amount = '100000',description = 'I like your my ethic',user = 'test')

    def test_save_neighbourhood(self):
        self.save_account()
        accounts = Account.objects.all()
        self.assertEqual(len(Account),1)

    def test_delete_account(self):
        self.image.save_account()
        self.image.delete_account()
        account_list = Account.objects.all()
        self.assertTrue(len(Account)==0)


class BillTestCase(TestCase):
    def setUp(self):
        self.new= Bill(category='monthly',name ='Nairobi Hospital',amount = '100000',description = 'I like your my ethic',user = 'test',due_date='21-2-2023')

    def test_save_bill(self):
        self.save_bill()
        bills = Bill.objects.all()
        self.assertEqual(len(Bill),1)

    def test_delete_bill(self):
        self.image.save_bill()
        self.image.delete_bill()
        bill_list = Bill.objects.all()
        self.assertTrue(len(Bill)==0)