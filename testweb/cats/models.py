from django.db import models


class adorable_kitten(models.Model):
    breed = models.CharField(max_length=150)
    height = models.FloatField(max_length=100)
    cat_name = models.CharField(max_length=200)
    cat_pic = models.CharField(max_length=500)

    def __str__(self):
        return self.breed + ", " + self.cat_name + " is " + str(self.height) + " tall"


class human(models.Model):
    human_name = models.CharField(max_length=150)
    height = models.FloatField(max_length=100)
    cat_overlord = models.ForeignKey(adorable_kitten, on_delete=models.CASCADE)

    # if the cat is deleted, the human is unimportant
    # so delete it also
    def __str__(self):
        return str(self.human_name) + " is owned by a cat."
        # cat_overlord returns an adorable_kitten object
