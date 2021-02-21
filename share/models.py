from django.db import models

class Image(models.Model):         ##画像を扱うためのもの
    picture = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Friend(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=200)
    gender = models.BooleanField()
    age = models.IntegerField(default=0)
    birthday = models.DateField()
     
    def __str__(self):
        return '<Friend:id=' + str(self.id) + ', ' + \
            self.name + '(' + str(self.age) + ')>'


class Post(models.Model):
    content = models.TextField(max_length=400)

    def __str__(self):
        return str(self.content) 
