from django.db import models

class Question(models.Model):
	Email = models.CharField("Email", max_length = 100)
	Text = models.TextField("Вопрос")

	def __str__(self):
		return self.Email

	class Meta:
		verbose_name = 'Вопрос'
		verbose_name_plural = 'Вопросы'