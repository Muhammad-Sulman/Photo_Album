from django.db import models

# Create your models here.
# one to many relationship (one category can have many photos)
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False ) # blanks indicates that in form field cannot be left blank and in database value cannot be null

    def __str__(self):
        return self.name
    
class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True) # sets value to null on delete
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.description