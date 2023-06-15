from .models import ReviewsBlocks
from .models import FormModal
from django.forms import ModelForm, TextInput, Textarea, EmailInput


class ReviewsBlockForm(ModelForm):
    class Meta:
        model = ReviewsBlocks
        fields = ["nameuser", "reviews"]
        widgets = {
            "nameuser" : TextInput(attrs={
                'class' : 'form__input',
                'placeholder' : 'Как Вас зовут?'
            }),
            "reviews": Textarea(attrs={
                'class': 'textarea__otziv',
                'placeholder': 'Оставьте здесь свой отзыв',
                'cols' : '30',
                'rows' : '10',
                'maxlength' : '230'
            }),
        }


class FormModalForm(ModelForm):
    class Meta:
        model = FormModal
        fields = ['customer', 'phone', 'email']
        widgets = {
            'customer' : TextInput(attrs={
            'type' : 'text',
            'class' : 'form__input',
            'id' : 'name',
            'name' : 'name',
            'data-reg' : '^[а-яА-ЯёЁa-zA-Z]+ [а-яА-ЯёЁa-zA-Z]+ ?[а-яА-ЯёЁa-zA-Z]+$',
            'placeholder' : 'Иван Иванович'
            }),
            'phone': TextInput(attrs={
                'id': 'phone',
                'name': 'phone',
                'data-reg': '\8\ [0-9]{3}\ [0-9]{3}\ [0-9]{2}\ [0-9]{2}',
                'class': 'form__input',
                'placeholder': '8 ХХХ ХХХ ХХ ХХ'
            }),
            'email': EmailInput(attrs={
                'type': 'email',
                'id': 'email',
                'name': 'email',
                'data-reg': '[-\w.]+@([A-z0-9][-A-z0-9]+\.)+[A-z]{2,4}$',
                'class': 'form__input',
                'placeholder': 'help@yandex.ru'
            })
        }