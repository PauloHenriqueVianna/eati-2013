# -*- coding: utf-8 -*-
from django.db import models

class Equipes(models.Model):
	equipe = models.CharField(u'Equipe',max_length=128,blank=False,null=False)
	integrante01 = models.CharField(u'Integrante 01',max_length=128,blank=False,null=False)
	emailintegrante01 = models.CharField(u'E-mail Integrante 01',max_length=128,blank=False,null=False)
	integrante02 = models.CharField(u'Integrante 02',max_length=128,blank=False,null=False)
	emailintegrante02 = models.CharField(u'E-mail Integrante 02',max_length=128,blank=False,null=False)
	integrante03 = models.CharField(u'Integrante 03',max_length=128,blank=False,null=False)
	emailintegrante03 = models.CharField(u'E-mail Integrante 03',max_length=128,blank=False,null=False)
	integrante04 = models.CharField(u'Integrante 04',max_length=128,blank=True,null=True)
	emailintegrante04 = models.CharField(u'E-mail Integrante 04',max_length=128,blank=True,null=True)
	dataInscricao = models.DateField(u'Data de Inscrição',blank=True,null=True,auto_now=True)

	class Meta:
		verbose_name = u'Equipe'
		verbose_name_plural = u'Equipes'
