from contextlib import suppress
from django.db import models

class CustomManager(models.Manager):

    def get_queryset(self):
        #return super().get_queryset().order_by('-cprice')
        return super().get_queryset().order_by('cprice')
        

    def sortfeeshightolowdev(self):
        return super().order_by('-cprice').filter(ccat="Developement")

    
    def sortfeeslowtohighdev(self):
        return super().order_by('cprice').filter(ccat="Developement")


    def sortfeeshightolowds(self):
        return super().order_by('-cprice').filter(ccat="Data Science")


    def sortfeeslowtohighds(self):
        return super().order_by('cprice').filter(ccat="Data Science")



        