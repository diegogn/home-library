from django.db import models

# Create your models here.

class Tag(models.Model):
    '''
    Tag´s class
    '''
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=7)
    
    class Meta:
        '''
        Meta
        '''
        ordering = ('name',)
    
    def __str__(self):
        return self.name


class Author(models.Model):
    '''
    Author´s class
    '''
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    
    class Meta:
        '''
        Meta
        '''
        ordering = ('name',)
    
    def __str__(self):
        return self.name +" "+ self.surname


class Work(models.Model):
    '''
    Work´s class
    '''
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    tags = models.ManyToManyField(Tag, related_name='works')
    authors = models.ManyToManyField(Author, related_name='works')
    
    class Meta:
        '''
        Meta
        '''
        ordering = ('title',)
        
    def __str__(self):
        return self.title