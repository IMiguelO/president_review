from django.db import models
from django.contrib.auth.models import User

# Create your models here.

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

  def __unicode__(self):
    return self.name

