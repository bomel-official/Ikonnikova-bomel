from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField

class Regulation(models.Model):
	Title = models.CharField("Заголовок", max_length = 50)
	Preview = ThumbnailerImageField("Изображение", default='students.jpg', resize_source = dict(quality=95, size=(370, 370), sharpen=True))
	Text = models.TextField("Текст")
	Pub_date = models.DateField("Дата публикации")
	File = models.FileField("Файл", upload_to='uploads/', default = None, blank = True)	

	def __str__(self):
		return self.Title

	class Meta:
		verbose_name = 'Нормативный документ'
		verbose_name_plural = 'Нормативные документы'