from django.db import models

# Create your models here.
class Poll(models.Model):
    # 投票主題文字，至多 200 字
    subject = models.CharField(max_length=200, verbose_name='主題')
    # 投票建立日期，在建立時若未指定，則自動填入建立時的時間
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + ")" + self.subject

class Option(models.Model):
    poll_id = models.IntegerField()
    title = models.CharField(max_length=200)
    count = models.IntegerField(default=0)
    def __str__(self):
        return str(self.poll_id) + ": " + self.title
