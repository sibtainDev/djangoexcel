from email.policy import default

from django.db import models
from django.utils import timezone

import datetime


class FormAList(models.Model):
    b_f = models.TextField(null=True, blank=True, default="")
    a_f = models.TextField(null=True, blank=True, default="")
    c_f = models.TextField(null=True, blank=True, default="")
    d_f = models.TextField(null=True, blank=True, default="")
    e_f = models.TextField(null=True, blank=True, default="")
    f_f = models.TextField(null=True, blank=True, default="")
    g_f = models.TextField(null=True, blank=True, default="")
    h_f = models.TextField(null=True, blank=True, default="")
    i_f = models.TextField(null=True, blank=True, default="")
    j_f = models.TextField(null=True, blank=True, default="")
    k_f = models.TextField(null=True, blank=True, default="")
    l_f = models.TextField(null=True, blank=True, default="")
    m_f = models.TextField(null=True, blank=True, default="")
    n_f = models.TextField(null=True, blank=True, default="")
    o_f = models.TextField(null=True, blank=True, default="")
    p_f = models.TextField(null=True, blank=True, default="")
    q_f = models.TextField(null=True, blank=True, default="")
    r_f = models.TextField(null=True, blank=True, default="")
    s_f = models.TextField(null=True, blank=True, default="")
    date_time = models.DateTimeField(null=True, blank=True, verbose_name='更新時間', default=timezone.now)

    class Meta:
        db_table = 'form_alist'


class FormBList(models.Model):
    a_f = models.TextField(null=True, blank=True, default="")
    b_f = models.TextField(null=True, blank=True, default="")
    c_f = models.TextField(null=True, blank=True, default="")
    d_f = models.TextField(null=True, blank=True, default="")
    e_f = models.TextField(null=True, blank=True, default="")
    f_f = models.TextField(null=True, blank=True, default="")
    g_f = models.TextField(null=True, blank=True, default="")
    h_f = models.TextField(null=True, blank=True, default="")
    i_f = models.TextField(null=True, blank=True, default="")
    j_f = models.TextField(null=True, blank=True, default="")
    k_f = models.TextField(null=True, blank=True, default="")
    l_f = models.TextField(null=True, blank=True, default="")
    m_f = models.TextField(null=True, blank=True, default="")
    n_f = models.TextField(null=True, blank=True, default="")
    o_f = models.TextField(null=True, blank=True, default="")
    p_f = models.TextField(null=True, blank=True, default="")
    q_f = models.TextField(null=True, blank=True, default="")
    r_f = models.TextField(null=True, blank=True, default="")
    s_f = models.TextField(null=True, blank=True, default="")
    date_time = models.DateTimeField(null=True, blank=True, verbose_name='更新時間', default=timezone.now)

    class Meta:
        db_table = 'form_blist'


class FormFields(models.Model):
    name = models.CharField(max_length=50, verbose_name='原名稱', default="")
    new_name = models.TextField(verbose_name='欄位名稱', null=True, default="")
    hide = models.CharField(max_length=5, null=True, verbose_name='隱藏欄位', default="")
    create_date = models.DateTimeField(verbose_name='建立日期', default=datetime.datetime.now())

    class Meta:
        db_table = 'form_fields'
