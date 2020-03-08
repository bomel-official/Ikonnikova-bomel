from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField

class Development(models.Model):
	Title = models.CharField("Заголовок", max_length = 50)
	Category = models.ForeignKey("DevelopmentCategory", on_delete = models.CASCADE, default = None, blank = True)
	Preview = ThumbnailerImageField("Изображение", default='students.jpg', resize_source = dict(quality=95, size=(370, 370), sharpen=True))
	Text = models.TextField("Текст")
	Pub_date = models.DateField("Дата публикации")

	def __str__(self):
		return self.Title

	class Meta:
		verbose_name = 'Разработка'
		verbose_name_plural = 'Разработки'

class DevelopmentCategory(models.Model):
	Title = models.CharField("Название категории", max_length = 50)

	def __str__(self):
		return self.Title

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'



class File(models.Model):	
	Title = models.CharField("Название (Можно не указывать)", max_length = 50, default = None, blank = True)
	file = models.FileField("Файл", upload_to='uploads/', default = None, blank = True)	
	Development = models.ForeignKey("Development", on_delete = models.CASCADE, default = None, blank = True)

	def __str__(self):
		return self.Title

	class Meta:
		verbose_name = 'Файл'
		verbose_name_plural = 'Файлы'

	def save(self, *args, **kwargs):
		self.Title = self.file.name
		super(File, self).save(*args, **kwargs)