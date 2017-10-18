from django.test import TestCasefrom django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required(login_url='/notes/login.html')
def secure(request):
    user = request.user
    return render(request, base.html)



#tests.py
class SimpleTest(TestCase):
    def setUp(self):
        user = User.objects.create_user('temporary','temporary','temporary', 'temporary@gmail.com', 'temporary')

    def test_secure_page(self):
        self.client.login(username='temporary', password='temporary')
        response = self.client.get('/users', follow=True)')

