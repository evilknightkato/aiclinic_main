from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    is_staff_member = models.BooleanField(default=False,verbose_name="Персонал",help_text="Отметьте, если пользователь является сотрудником")
    phone = models.CharField(max_length=20,blank=True,verbose_name="Телефон")

#class CustomUser(AbstractUser):
#    is_staff_member = models.BooleanField(default=False)
#    phone = models.CharField(max_length=20, blank=True)
#    class Meta:
#        verbose_name = 'Пользователь'
#        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f"{self.username} ({'Персонал' if self.is_staff_member else 'Клиент'})"