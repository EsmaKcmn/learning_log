from django.db import models

# Create your models here. # modelinizi burda oluşturun
class Topic(models.Model):
    """A topic the user is learning about"""
    text= models.CharField(max_length=200)  #text adında bir Charfield tanımlıyoruz ve bu veri tabanında bir sütun oluşturur
     # max karakter uzunluğu 200
    # def added adında bir DateTimeField tanımlıyoruz
    date_added = models.DateTimeField(auto_now_add=True)
    #modelin string temsilini yazalım
    def __str__(self):
        return self.text


# Topic (konular) altında belirli bir girdi girebilmek için Enttry isimli moddel oluşturalım
class Entry(models.Model):
    """Something specific learned about a topic"""
    #ForeignKey field'ı 'çoktan bire2 ilişkiyi temsil eder ve Her Entry bir topic ile ilişkilidir.
    #on_delete eğer ilgili Topic silinirse herşey silinir.
    topic=models.ForeignKey(Topic, on_delete=models.CASCADE)
    text=models.TextField()
    date_added = models.DateTimeField(auto_now_add=True) # Entry nin oluşturulduğu zaman

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return f"{self.text[:50]}..."

