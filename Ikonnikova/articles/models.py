from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField


class Article(models.Model):
	Title = models.CharField("Заголовок", max_length = 50)
	Category = models.ForeignKey("ArticleCategory", on_delete = models.CASCADE, default = None, blank = True)
	Preview = ThumbnailerImageField("Изображение", default='students.jpg', resize_source = dict(quality=95, size=(770, 770), sharpen=True))
	Text = models.TextField("Текст")
	Pub_date = models.DateField("Дата публикации")

	def __str__(self):
		return self.Title

	class Meta:
		verbose_name = 'Статья'
		verbose_name_plural = 'Статьи'

class ArticleCategory(models.Model):
	Title = models.CharField("Название категории", max_length = 20)

	def __str__(self):
		return self.Title

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'



class File(models.Model):	
	Title = models.CharField("Название (Можно не указывать)", max_length = 50, default = None, blank = True)
	file = models.FileField("Файл", upload_to='uploads/', default = None, blank = True)	
	Article = models.ForeignKey("Article", on_delete = models.CASCADE, default = None, blank = True)

	def __str__(self):
		return self.Title

	class Meta:
		verbose_name = 'Файл'
		verbose_name_plural = 'Файлы'

	def save(self, *args, **kwargs):
		self.Title = self.file.name
		super(File, self).save(*args, **kwargs)


class Award(models.Model):
	Year = models.IntegerField("Год")
	Image = ThumbnailerImageField("Изображение", resize_source = dict(quality=95, size=(500, 750), sharpen=True))

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Грамота'
		verbose_name_plural = 'Грамоты'
