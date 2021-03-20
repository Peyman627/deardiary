from django.db import models

MOOD = (
    (0, 'brilliant'),
    (1, 'good'),
    (2, 'meh'),
    (3, 'bad'),
    (4, 'awful'),
)


class Diary(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    mood = models.CharField(max_length=1, choices=MOOD)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title
