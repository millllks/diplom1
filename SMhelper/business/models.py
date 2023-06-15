from django.db import models

class CompanyPages(models.Model):
    contentCompany = models.TextField('Блок')

    def __str__(self):
        return self.contentCompany



    class Meta:
        verbose_name = 'Блоки страницы о компании'
        verbose_name_plural = 'Блок о компании'


class ReviewsBlocks(models.Model):
    nameuser = models.CharField('Имя', max_length=20)
    reviews = models.TextField('Отзыв', max_length=230)

    def __str__(self):
        return self.reviews

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class ModalForm(models.Model):
    customer = models.CharField('Имя клиента', max_length=30)
    phone = models.TextField('Телефон', max_length=30)
    email = models.EmailField('Email')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class FormModal(models.Model):
    customer = models.CharField('Имя клиента', max_length=30)
    phone = models.CharField('Телефон', max_length=30)
    email = models.EmailField('Email')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class Contacts(models.Model):
    address = models.CharField('Адрес', max_length=80)
    hours = models.CharField('Режим работы', max_length=40)
    phone = models.CharField('Телефон', max_length=25)
    email = models.EmailField('Email')

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контактные данные'

class ServicesList(models.Model):
    title = models.CharField('Название услуги', max_length=90)
    serv_item1 = models.CharField('Описание услуги', max_length=120)
    serv_item2 = models.CharField('Описание услуги', max_length=120)
    serv_item3 = models.CharField('Описание услуги', max_length=120)
    serv_item4 = models.CharField('Описание услуги', max_length=120)
    serv_item5 = models.CharField('Описание услуги', max_length=120)
    serv_item6 = models.CharField('Описание услуги', max_length=120)
    serv_item7 = models.CharField('Описание услуги', max_length=120)
    serv_item8 = models.CharField('Описание услуги', max_length=120)
    serv_item9 = models.CharField('Описание услуги', max_length=120)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Список услуг'
