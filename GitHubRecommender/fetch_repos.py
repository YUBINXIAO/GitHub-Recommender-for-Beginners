
import os
import requests

def fetch_github_repositories(language='python', sort_by='stars', max_repos=100):
    # GitHub API endpoint for searching repositories
    url = f'https://api.github.com/search/repositories?q=language:{language}&sort={sort_by}&per_page=100'

    # Authorization is sent only when GITHUB_TOKEN is set, same rule as github_headers().
    headers = {}
    token = os.environ.get('GITHUB_TOKEN')
    if token:
        headers['Authorization'] = f'token {token}'

    repositories = []
    page = 1

    while len(repositories) < max_repos:
        response = requests.get(f'{url}&page={page}', headers=headers)

        if response.status_code == 200:
            repo_data = response.json()
            repositories.extend(repo_data.get('items', []))
        else:
            print("Failed to retrieve data:", response.status_code, response.json().get('message'))
            break

        if len(repositories) >= repo_data['total_count']:
            break

        page += 1

    return repositories[:max_repos]

# Example Usage
if __name__ == '__main__':
    fetched_repositories = fetch_github_repositories()
    for repo in fetched_repositories:
        print(repo['name'], repo['stargazers_count'])
