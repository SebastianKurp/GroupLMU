from django.db import models
from django.core.urlresolvers import reverse


class note(models.Model):
    title = models.CharField(max_length=150)
    content = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('notes:detail', kwargs={'pk': self.pk})
        #kwargs is keyword argument

    def __str__(self):
        return self.title + ", " + self.content


class mention(models.Model):
    mention_name = models.CharField(max_length=150)
    note_in = models.ForeignKey(note, on_delete=models.CASCADE)
   # is_favorite = models.BooleanField(default=False)

    # if the not is deleted, the mention is unimportant
    # so delete it also
    def __str__(self):
        return str(self.mention_name)
        # note_in returns an note object
