from django.db import models

class Sport(models.Model):
    naziv = models.CharField(max_length=100)

    def __str__(self):
        return self.naziv
    

class Tim(models.Model):
    naziv = models.CharField(max_length=100)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)

    def __str__(self):
        return self.naziv


class Natjecanje(models.Model):
    naziv = models.CharField(max_length=100)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    tim = models.ManyToManyField(Tim)

    def __str__(self):
        return self.naziv 


class RezultatUtakmice(models.Model):
    natjecanje = models.ForeignKey(Natjecanje, on_delete=models.CASCADE)
    domacin = models.ForeignKey(Tim, related_name='domacin_utakmice', on_delete=models.CASCADE)
    gost = models.ForeignKey(Tim, related_name='gost_utakmice', on_delete=models.CASCADE)
    rezultat_domacin = models.IntegerField(default=0)
    rezultat_gost = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.domacin} vs {self.gost} - {self.rezultat_domacin} : {self.rezultat_gost}"