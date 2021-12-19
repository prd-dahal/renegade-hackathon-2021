from django.db import models


# Create your models here.
class Questions(models.Model):
    question_text = models.CharField(max_length = 500)
    val = models.FloatField(null = True, blank = True)
    yes = models.ForeignKey('self', on_delete = models.CASCADE, null= True, blank = True, related_name= "yes_option")
    no = models.ForeignKey('self', on_delete = models.CASCADE,null= True, blank = True, related_name="no_option")
    
    def save(self, *args, **kwargs):
        if not self.yes:
            self.yes = None
        super(Questions, self).save(*args, **kwargs)

    def __str__(self):
        return self.question_text
