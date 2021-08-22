from django.urls import path
from cv.views import index, about, cv, skills, work, work_form

app_name = 'personal'

urlpatterns =[
    path('', index, name ='index'),
    path('about/', about, name ='about'),
    path('skills/', skills, name ='skills'),
    path('work/', work, name ='work'),
    path('cv/', cv, name ='cv'),
    path('work_form/', work_form, name ='work_form'),
]