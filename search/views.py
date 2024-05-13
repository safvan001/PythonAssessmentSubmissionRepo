from django.shortcuts import render
from search.models import Github
from django.core.paginator import Paginator
import requests
from requests.exceptions import RequestException
def home(request):
    return render(request,'home.html')



def search_repositories(request):
    context = {}
    query = request.GET.get('q')

    if query:
        url = f"https://api.github.com/search/repositories?q={query}&per_page=100"
        
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()['items']
                paginator = Paginator(data, 10)  # Show 10 repositories per page.
                page_number = request.GET.get('page')
                page_obj = paginator.get_page(page_number)
                context['page_obj'] = page_obj

                # Saving to database should happen outside of pagination handling.
                for repo_data in data:
                    Github.objects.update_or_create(
                        repo_id=repo_data['id'],
                        name=repo_data['name'],
                        owner= repo_data['owner']['login'],
                        description=repo_data.get('description', ''),
                        stars=repo_data['stargazers_count'],
                        forks=repo_data['forks'],
                        html_url=repo_data['html_url'],
                    )
            else:
                context['error'] = "Error fetching data from GitHub."
        except RequestException as e:
            context['error'] = f"Failed to retrieve data: {str(e)}"

    return render(request, 'search.html', context)

# Create your views here.
