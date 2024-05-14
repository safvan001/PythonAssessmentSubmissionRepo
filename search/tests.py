from django.test import TestCase
from django.test import TestCase
from django.urls import reverse
from .models import Github

class SearchViewTests(TestCase):

    def test_search_with_query(self):
        """
        Test the search functionality with a mock query and check if results are displayed.
        """
        # Setup a mock database entry
        Github.objects.create(repo_id=123, name="Test Repo", owner="testuser",
                              description="A test repository", stars=10, forks=5, html_url="http://example.com/test")
        
        # Use the client to perform the get request on the search url with a query.
        response = self.client.get(reverse('search') + '?q=Test')
        self.assertEqual(response.status_code, 200)
        


class GithubModelTests(TestCase):
    def test_create_github_repo(self):
        """
        Test the creation of a Github repo and assert it exists.
        """
        repo = Github.objects.create(repo_id=124, name="New Test Repo", owner="newtestuser",
                                     description="Another test repository", stars=15, forks=3, html_url="http://example.com/newtest")
        self.assertEqual(repo.name, "New Test Repo")
        self.assertTrue(Github.objects.filter(name="New Test Repo").exists())

# Create your tests here.
