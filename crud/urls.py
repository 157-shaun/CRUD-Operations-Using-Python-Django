from django.urls import path
from crud import views

urlpatterns = [
    path("",views.home,name='home'),
    path("create/",views.create),
    path("update-list/", views.update_list, name="update_list"),
    path("update/<int:student_id>/", views.update, name="update"),
    path("delete/",views.delete_page,name="delete_page"),
    path("delete/<int:student_id>",views.delete,name="delete"),
    path("display/",views.display,name="display"),
]
