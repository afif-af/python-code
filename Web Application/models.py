from django.db import models

class Topic(models.Model):
    text = models.ChatField(max_length=200)
    data_added_models.DataTimeField(auto_now_add=True)

    def __str__(self):
        return self.text