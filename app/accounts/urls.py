from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenBlacklistView

urlpatterns = [
    path('/', include('djoser.urls')),
    path('/', include('djoser.urls.jwt')),
    path('/logout/', TokenBlacklistView.as_view(), name='token_blacklist'),
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

            #### used ####
# /jwt/create/ (JSON Web Token Authentication)
# /jwt/refresh/ (JSON Web Token Authentication)
# /jwt/verify/ (JSON Web Token Authentication)