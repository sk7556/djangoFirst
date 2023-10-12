mkdir accounts
cd accounts
python -m venv venv

# 가상환경속으로 들어가기
.\venv\Scripts\activate # window
.\venv\Script\activate.bat # window
source ./venv/bin/activate # mac, linux

pip install django
django-admin startproject tutorialdjango .
python manage.py migrate

# settings.py에서 접속할 수 있는 사람 설정
ALLOWED_HOSTS = ['*'] # 28번째 줄에 접속할 수 있는 사람을 모든 사람으로 변경


python manage.py startapp accounts


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
]

###################################
# tutorialdjango > urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts', include('accounts.urls')),
]

###################################
# accounts > urls.py 
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
]

###################################
# accounts > views.py 
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views.generic import CreateView

# def signup(request):
#     pass

signup = CreateView.as_view(
    form_class = UserCreationForm,
    template_name = 'accounts/form.html',
    success_url = settings.LOGIN_URL,
)

# def login(request):
#     pass

login = LoginView.as_view(
    template_name = 'accounts/form.html',
)

# def logout(request):
#     pass

logout = LogoutView.as_view(
    next_page = settings.LOGOUT_URL,
)

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

###################################
# settings.py 맨 마지막
LOGIN_URL = '/accounts/hellologin/'
LOGOUT_URL = '/accounts/hellologout/'

###################################
# accounts > templates > accounts > form.html
# accounts > templates > accounts > profile.html

###################################
# accounts > templates > accounts > form.html
<form action="" method="post" enctype="multipart/form-data">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
    </table>
    <input type="submit">
</form>

###################################
# accounts > templates > accounts > profile.html
<h1>wellcome</h1>
<p>{{ user }} 프로필 페이지입니다.</p>

###################################

python manage.py createsuperuser

leehojun
leehojun@gmail.com
이호준123!@