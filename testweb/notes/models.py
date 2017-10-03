from django.db import models


class note(models.Model):
    title = models.CharField(max_length=150)
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.title + ", " + self.content


class mention(models.Model):
    mention_name = models.CharField(max_length=150)
    note_in = models.ForeignKey(note, on_delete=models.CASCADE)
   # is_favorite = models.BooleanField(default=False)

    # if the cat is deleted, the human is unimportant
    # so delete it also
    def __str__(self):
        return str(self.mention_name) + " is owned by a cat."
        # cat_overlord returns an adorable_kitten object
