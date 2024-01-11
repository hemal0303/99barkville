from django.db import models
from PIL import Image
from django_resized import ResizedImageField
from django.core.files import File
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile


class Breed(models.Model):
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    temperament = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Dog(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, null=False, blank=False)
    color = models.CharField(max_length=50)
    image1 = models.ImageField(upload_to="dog_images/", default="default_pic.png")
    image2 = models.ImageField(upload_to="dog_images/", null=True, blank=True)
    image3 = models.ImageField(upload_to="dog_images/", null=True, blank=True)
    rescue_story = models.TextField(default="")
    behavior = models.JSONField(null=True)
    up_for_adoption = models.BooleanField(default=False)
    vaccinated = models.BooleanField(default=False)
    sterilized = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="blog_images/", default="default_pic.png")
    full_image = models.ImageField(upload_to="blog_images/", default="default_pic.png")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.image:
            # Save the original image to the `full_image` field
            self.full_image.save(self.image.name, self.image, save=False)

            # Open the image
            img = Image.open(self.image)

            # Define the desired width and height
            fixed_size = (350, 218)

            # Resize the image
            img.thumbnail(fixed_size)

            # Create a BytesIO object to hold the resized image data
            output_io = BytesIO()

            # Save the resized image to the BytesIO object
            img = img.convert("RGB")
            img.save(output_io, format="JPEG")

            # Create a new InMemoryUploadedFile with the resized image data
            resized_image = InMemoryUploadedFile(
                output_io,
                "ImageField",
                f"{self.image.name.split('.')[0]}_resized.jpg",
                "image/jpeg",
                output_io.tell(),
                None,
            )

            # Assign the resized image to the `image` field
            self.image = resized_image

        super().save(*args, **kwargs)
