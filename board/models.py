# -*- coding: utf-8 -*-
from django.db import models

class Test1(models.Model):
    deathcnt = models.IntegerField(db_column='deathCnt', blank=True, null=True)  # Field name made lowercase.
    defcnt = models.IntegerField(db_column='defCnt', blank=True, null=True)  # Field name made lowercase.
    gubun = models.TextField(blank=True, null=True)
    gubuncn = models.TextField(db_column='gubunCn', blank=True, null=True)  # Field name made lowercase.
    gubunen = models.TextField(db_column='gubunEn', blank=True, null=True)  # Field name made lowercase.
    incdec = models.IntegerField(db_column='incDec', blank=True, null=True)  # Field name made lowercase.
    isolclearcnt = models.IntegerField(db_column='isolClearCnt', blank=True, null=True)  # Field name made lowercase.
    isolingcnt = models.IntegerField(db_column='isolIngCnt', blank=True, null=True)  # Field name made lowercase.
    localocccnt = models.IntegerField(db_column='localOccCnt', blank=True, null=True)  # Field name made lowercase.
    overflowcnt = models.IntegerField(db_column='overFlowCnt', blank=True, null=True)  # Field name made lowercase.
    qurrate = models.TextField(db_column='qurRate', blank=True, null=True)  # Field name made lowercase.
    stdday = models.TextField(db_column='stdDay', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.gubun