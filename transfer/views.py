from django.shortcuts import render
from django.utils import timezone
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from .models import Transfer
from django.contrib.auth.models import User
from django.contrib.auth import login



# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})

def lk(request):
    me = request.user
    test = Transfer.objects.filter(author=me)
    #test = Transfer.objects.filter(author=me)
    return render(request, 'blog/lk.html', {'me': me})

class RegisterFormView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/lk/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "blog/register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)
