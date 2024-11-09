from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, unique=True, blank=False, null=False)
    senha = models.CharField(max_length=255, blank=False, null=False)
    profile = models.ImageField(
        upload_to='images/',
        default='images/profile_default.svg',
        blank=True
    )
    logged_in = models.BooleanField(default=False)

    def __str__(self):
        return self.nome


class Tweet(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, related_name='tweets', on_delete=models.CASCADE)
    post = models.TextField(blank=False, null=False)
    image = models.URLField(blank=True)
    data_postagem = models.DateField(auto_now_add=True)
    hora_postagem = models.TimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.image:
            self.image = self.owner.profile.url if self.owner.profile else ''
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Tweet by {self.owner.nome}'
