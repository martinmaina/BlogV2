from app import app
import unittest

class TestWega(unittest.TestCase):

    #Ensure flask was geare up sawa sawa
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    #Ensure that the login page loads visawa
    def test_loginPageLoadsWell(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'Username', b'Password' in response.data)

    #ensure index loads coreectly 
    def test_indexPageLoadsDatabaseContent(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertTrue(b'Title', b'Post' in response.data)

    #ensure flash message posp up
    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login', data=dict(username='user', password='pass'), follow_redirects=True)
        self.assertIn(b'You are logged in',  response.data)

     #ensure after incorrect credentials the error message pops up
    def test_incorrect_login(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login', data=dict(username='mama', password='pass'), follow_redirects=True)
        self.assertIn(b'Invalid credentials',  response.data)
    
    #Ensure logout works successfully
    def test_logout(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login', data=dict(username='user', password='pass'), follow_redirects=True)
            
        response = tester.get('/logout', follow_redirects=True)
        self.assertIn(b'You have been logged out',  response.data) 

    #Ensure login works well
    def test_login(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(username='user', password='pass', follow_redirects=True))
        response = tester.get('/', follow_redirects=True)
        self.assertIn(b'You are logged in', response.data)


    #Ensure the main page requires login(user='anonymous', passwd='', acct='')
    def test_login_required(self):
        tester = app.test_client(self)
        response = tester.get('/', follow_redirects=True)
        self.assertTrue(b'You need to login first' in response.data)

    #Ensure after logout, there is login option
    def test_login_after_logout(self):
        tester = app.test_client(self)
        response = tester.get('/logout', follow_redirects=True)
        self.assertTrue(b'Click here to login', 'You have been logged out' in response.data)

         
if __name__ == "__main__":
    unittest.main()
        
