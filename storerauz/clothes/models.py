from django.db import models
from django.contrib.auth.models import User
from PIL import Image

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from smtplib import SMTPException
from django.contrib.auth import get_user_model


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Clothes(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='clothes_images/',default='clothes_images/default.jpg', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    author: User = models.ForeignKey(User,
                                     on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # We have to save the form first before getting the image path
        img = Image.open(self.image.path)
        if img.height > 600 or img.width > 600:
            output_size = (600, 600)
            img.thumbnail(output_size)
            img.save(self.image.path)
    


    


@receiver(post_save, sender=Clothes)
def print_info_of_book(sender, instance, created, **kwargs):
    if created:
        print("--------------------------------------------------")
        print(f' instance named: {instance.name} was created')
        print("--------------------------------------------------")


        try:
            send_mail(
                f'Product instance named: {instance.name} was created',
                'In your project Storerauz new product was added',
                settings.EMAIL_HOST_USER,
                ['mmansurjonov62@gmail.com'],
                fail_silently=False,
            )
        except SMTPException as error:
            print("--------------------------------------------")
            print("Error while sending email: ", error)
            print("--------------------------------------------")
