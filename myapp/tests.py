from django.test import TestCase
from .models import Image, Profile

# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):
        self.image = Image(image_name='image1', image_caption='image1 caption', image='image1 image', image_likes=0, image_comments='image1 comments')

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def test_save_method(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)


    def test_delete_method(self):
        self.image.save_image()
        self.image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)






    