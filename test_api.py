import os
import unittest
from dotenv import load_dotenv
from github import Auth, Github

load_dotenv()
unittest.TestLoader.sortTestMethodsUsing = None

api_token = os.environ.get('token')
username = os.environ.get('username')
r_name = os.environ.get('repo')

class GithubTestCase(unittest.TestCase):
    def setUp(self):
        auth = Auth.Token(api_token)
        g = Github(auth=auth)
        self.user = g.get_user()
        self.addCleanup(g.close)

    def test_1_create_repo(self):
        try:
            self.user.create_repo(r_name)
            print('Repo created successfully')
        except:
            self.fail('Repo not created')
    def test_2_check_repo(self):
        if r_name in [r.name for r in self.user.get_repos()]:
            print('Repo checked')
        else:
            self.fail('Repo not found')

    def test_3_delete_repo(self):
        try:
            self.user.get_repo(r_name).delete()
            print('Repo deleted')
        except:
            self.fail('Repo not deleted')

if __name__ == '__main__':
    unittest.main()
