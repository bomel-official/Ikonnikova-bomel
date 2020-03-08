from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField

class Contact(models.Model):
	Title = models.CharField("Название контакта", max_length = 50)
	Category = models.ForeignKey("ContactCategory", on_delete = models.CASCADE, default = None, blank = True)
	Value = models.CharField("Значение контакта", max_length = 50)

	def __str__(self):
		return self.Title

	class Meta:
		verbose_name = 'Контакт'
		verbose_name_plural = 'Контакты'

class ContactCategory(models.Model):
	Title = models.CharField("Название категории контакта", max_length = 50)

	def __str__(self):
		return self.Title

	class Meta:
		verbose_name = 'Категория контакта'
		verbose_name_plural = 'Категории контакта'

class Text(models.Model):
	Title = models.CharField("Название", max_length = 50)
	Text = models.TextField("Текст")

	def __str__(self):
		return self.Title

	class Meta:
		verbose_name = 'Контент'
		verbose_name_plural = 'Контент'

class Image(models.Model):
	Title = models.CharField("Название", max_length = 50)
	Image = ThumbnailerImageField("Изображение", resize_source = dict(quality=95, size=(770, 770), sharpen=True))

	def __str__(self):
		return self.Title

	class Meta:
		verbose_name = 'Изображение'
		verbose_name_plural = 'Изображения'