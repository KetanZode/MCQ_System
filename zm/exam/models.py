from django.db import models

# Create your models here.
class que(models.Model):
    qno = models.IntegerField()
    que = models.TextField()
    ans = models.CharField(max_length = 100)
    op1 = models.CharField(max_length = 100)
    op2 = models.CharField(max_length = 100,null=True)
    op3 = models.CharField(max_length = 100)
    op4 = models.CharField(max_length = 100)
    def __str__(self):
        return self.ans 