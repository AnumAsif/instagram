from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Image, Comments
from django.db import models
# Create your tests here.
class ProfileTestCase(TestCase):

    def setUp(self):
        self.u1 = User.objects.create(username='user1')
        self.anum = Profile.objects.create(user=self.u1)

    def tearDown(self):
        self.anum.delete()
        self.u1.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.anum, Profile))

    def test_save_profile(self):
        self.anum.save_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)>0)

    def test_search_profile(self):
        self.anum.save_profile()
        profile= Profile.search_profile(self.anum)
        self.assertTrue(len(profile)>0)

class ImageTestCase(TestCase):

    def setUp(self):
        self.u1 = User.objects.create(username='user1')
        self.image=Image.objects.create(image_name="lantern",image_caption="dasdasdasd", profile=self.u1)        

    def tearDown(self):
        self.image.delete()
        self.u1.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def test_save_image(self):
        self.image.save_image()
        images=Image.objects.all()
        self.assertTrue(len(images)>0)
     
    def test_get_all_images(self):
        self.image.save_image()
        images= Image.get_all_images()
        self.assertTrue(len(images)>0)
    
    def test_get_profile_image(self):
        self.image.save_image()
        image=Image.get_profile_images(self.u1.id)
        self.assertTrue(len(image)>0)
        
class CommentsTestCase(TestCase):
       
    def setUp(self):   
        self.u1 = User.objects.create(username='user1')
        self.image=Image.objects.create(image_name="lantern",image_caption="dasdasdasd", profile=self.u1)        
        self.comment=Comments.objects.create(comment="sdadas", image=self.image, user=self.u1)

    def tearDown(self):
        self.comment.delete()    
        self.image.delete()
        self.u1.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.comment, Comments))
     
    def test_save_comment(self):
        self.comment.save_comment()
        comments=Comments.objects.all()
        self.assertTrue(len(comments)>0)

    def test_get_comments_by_images(self):
        self.image.save_image()
        self.comment.save_comment()
        comments=Comments.get_comments_by_images(self.image.id)
        self.assertTrue(len(comments)>0)