from django.db import models

# passing this variable to choice parameter of mood
# in diary model
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
    mood = models.IntegerField(choices=MOOD)

    class Meta:
        ordering = ('date', )

    def __str__(self):
        return self.title


# class DiaryImage(models.Model):
#     diary = models.ForeignKey(Diary,
#                               related_name='images',
#                               on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='images/', blank=True, null=True)
