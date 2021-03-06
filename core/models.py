from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.
VISIBILITY_CHOICES = (
(0, 'Public'),
(1, 'Anonymous'),
)

candidate_options = (
(0, ''),
(1, 'Jeb Bush'),
(2, 'Ben Carson'),
(3, 'Hillary Clinton'),
(4, 'Ted Cruz'),
(5, 'Lawrence Lessig'),
(6, 'Martin OMalley'),
(7, 'Marco Rubio'),
(8, 'Bernie Sanders'),
(9, 'Donald Trump'),
(10, 'Guido Lang'),
)

class Question(models.Model):
  title = models.IntegerField(choices=candidate_options, default=0)
  name = models.CharField(max_length=300)
  email = models.EmailField(max_length=254, blank=False, null= True, unique= False)
  review = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(User)
  visibility = models.IntegerField(choices=VISIBILITY_CHOICES, default=0)

  def __unicode__(self):
    return self.name

  def get_absolute_url(self):
    return reverse("question_detail", args=[self.id])

class Answer(models.Model):
    question = models.ForeignKey(Question)
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    opinion = models.TextField()
    visibility = models.IntegerField(choices=VISIBILITY_CHOICES, default=0)

    def __unicode__(self):
        return self.opinion

class Vote(models.Model):
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question, blank=True, null=True)
    answer = models.ForeignKey(Answer, blank=True, null=True)

    def __unicode__(self):
        return "%s upvoted" % (self.user.username)