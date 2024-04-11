from django.urls import path
from graphene_django.views import GraphQLView


urlpatterns = [
    #path('',views.index),
    path('graph/', GraphQLView.as_view(graphiql=True))

]