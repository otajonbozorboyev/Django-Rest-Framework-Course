from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.name



class Level(models.Model):
    name = models.CharField(max_length=100)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Unit(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name='units')
    name = models.CharField(max_length=100)
    audio_image = models.ImageField(upload_to='images/')
    audio_name = models.CharField(max_length=100)
    audio_description = models.TextField()
    audio = models.FileField(upload_to='audio/')
    score = models.PositiveSmallIntegerField()
    coin = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name



class Vocabulary(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='vocabularies')
    word = models.CharField(max_length=100)
    translation = models.CharField(max_length=100)
    translation_flag = models.ImageField(upload_to='images/')
    description = models.TextField()
    example = models.TextField()

    def __str__(self):
        return self.word



class Phrase(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='phrases')
    word = models.CharField(max_length=100)
    translation = models.CharField(max_length=100)
    translation_flag = models.ImageField(upload_to='images/')
    description = models.TextField()
    example = models.TextField()

    def __str__(self):
        return self.word



class PodcastBanner(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    time = models.CharField(max_length=100)
    coin = models.SmallIntegerField()

    def __str__(self):
        return self.title



class VideoBanner(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    time = models.CharField(max_length=100)
    coin = models.SmallIntegerField()

    def __str__(self):
        return self.title



class BookBanner(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    pages = models.CharField(max_length=100)
    coin = models.SmallIntegerField()

    def __str__(self):
        return self.title



class Podcast(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    audio = models.FileField(upload_to='audio/')

    def __str__(self):
        return self.title



class Video(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='images/')
    video = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.title



class Book(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='books')
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    pdf = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.title
