from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.CharField(max_length=2000)
    image = models.ImageField(upload_to='images/blog')

    def summary(self):
        return self.body[:100]

    def pub_date_short(self):
        return self.pub_date.strftime('%B %e, %Y')

    def __str__(self):
        return self.title
