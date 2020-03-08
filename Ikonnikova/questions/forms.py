from django import forms
from .models import Question

class QuestionForm(forms.Form):
	Email = forms.EmailField()
	Text = forms.CharField(widget = forms.Textarea)

	Email.widget.attrs.update({
		'class': 'email',
		'placeholder': 'Ваш email'
	})

	Text.widget.attrs.update({
		'class': 'text',
		'placeholder': 'Вопрос'
	})

	def save(self):
		new_question = Question.objects.create(
			Email = self.data['Email'], 
			Text = self.data['Text']
		)
		return new_question