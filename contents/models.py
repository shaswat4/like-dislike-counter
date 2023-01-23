from django.db import models


class Post(models.Model):
    post_text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')
    like_votes = models.IntegerField(default=0)
    dislike_votes = models.IntegerField(default=0)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.post_text

#obselete models
class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    #choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    
class Dislike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    #choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    