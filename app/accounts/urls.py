from django.contrib import admin
from django.urls import path,include
from .views import UserList

urlpatterns = [
    #path('',views.index),
    path('test/', UserList.as_view(), name='user-list')

]

# /users/    " POST => singUp "
# /users/me/
# /users/confirm/
# /users/resend_activation/
# /users/set_password/
# /users/reset_password/
# /users/reset_password_confirm/
# /users/set_username/
# /users/reset_username/
# /users/reset_username_confirm/
# /token/login/ (Token Based Authentication)
# /token/logout/ (Token Based Authentication)

            #### not used ####
# /jwt/create/ (JSON Web Token Authentication)
# /jwt/refresh/ (JSON Web Token Authentication)
# /jwt/verify/ (JSON Web Token Authentication)