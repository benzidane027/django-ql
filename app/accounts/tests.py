from rest_framework.test import RequestsClient, APITestCase, APIClient
from rest_framework import status
import datetime,time,json


def progress(_func=None):
    def wrapper(*args, **kwargs):
        print(f"\nstart ===> {_func.__name__.replace('_',' ').capitalize()}")
        start_time=datetime.datetime.now().timestamp()
        _func(*args, **kwargs)
        end_time=datetime.datetime.now().timestamp()
        print(f"checked : ok {(end_time-start_time):.4f} ms \n")

    return wrapper

class AccountTests(APITestCase):

    client = APIClient()
     
    #########################################################
    #################### sing up testing ####################
    #########################################################

    @progress
    def test_sing_up_without_field(self):
        
        response = self.client.post('/accounts/users/')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    @progress        
    def test_sing_up_with_field(self):
        data = {
            "email":"test@test.dz",
            "password":"test",
            "first_name":"test",
            "last_name":"test"
        }
        response = self.client.post('/accounts/users/',data,format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    @progress
    def test_sing_up_unique_email(self):
        data = {
            "email":"test@test.dz",
            "password":"test",
            "first_name":"test",
            "last_name":"test"
        }
        self.client.post('/accounts/users/',data,format='json')
        response = self.client.post('/accounts/users/',data,format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(json.loads(response.content), {"email":["profile with this email address already exists."]})

    #########################################################
    #################### sing up testing ####################
    #########################################################

    @progress
    def test_login_without_field(self):
        data_sing_up = {}
        response = self.client.post('/accounts/token/login/',data_sing_up,format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @progress   
    def test_login_with_wrong_credentials(self):
        data_sing_up = {
            "email":"no_one@no_one.no_one",
            "password":"no_one"
            }
        response = self.client.post('/accounts/token/login/',data_sing_up,format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @progress
    def test_login_with_field(self):
        data = {
            "email":"test@test.dz",
            "password":"test",
            "first_name":"test",
            "last_name":"test"
        }
        self.client.post('/accounts/users/',data,format='json')
        response = self.client.post('/accounts/token/login/',data,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual("auth_token" in json.loads(response.content), True)



