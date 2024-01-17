import requests
import base64
import pandas as pd
import sqlite3
from bs4 import BeautifulSoup
from data_processing import evaluate_learning_friendliness

def fetch_readme(repo_full_name):
    """
    This function fetches the README file of a GitHub repository.

    :param repo_full_name: The full name of the repository in the format 'owner/repo'.
    :type repo_full_name: str

    :return: The content of the README file as a UTF-8 encoded string.
             If the README is not found or if there is an error in the request, an empty string is returned.
    :rtype: str
    """
    # Construct the URL for fetching the README
    readme_url = f"https://api.github.com/repos/{repo_full_name}/readme"

    # Set the headers for the GitHub API request
    headers = {
        'Authorization': 'token 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',
        'Accept': 'application/vnd.github.v3+json'
    }

    # Send a GET request to fetch the README
    response = requests.get(readme_url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Retrieve the JSON data from the response
        readme_data = response.json()

        # Decode the base64-encoded content of the README and convert it to a UTF-8 encoded string
        content = base64.b64decode(readme_data['content']).decode('utf-8')

        # Return the content of the README
        return content
    else:
        # If the request was not successful, return an empty string
        return ""

        
        
def fetch_repositories(language, min_stars):
    """
    This function fetches GitHub repositories based on a specified programming language and a minimum number of stars.
    It also calculates the learning score and weighted score for each repository.

    :param language: The programming language to filter repositories by.
    :type language: str
    :param min_stars: The minimum number of stars a repository must have to be included in the results.
    :type min_stars: int

    :return: A list of dictionaries, where each dictionary represents a GitHub repository.
             Each dictionary includes information such as the repository name, stargazers count, learning score,
             star score, and weighted score.
    :rtype: list of dict
    """
    # Construct the URL for fetching repositories based on language and stars
    url = f'https://api.github.com/search/repositories?q=language:{language}&sort=stars&min_stars={min_stars}'

    # Set the headers for the GitHub API request
    headers = {'Accept': 'application/vnd.github.v3+json'}

    # Send a GET request to fetch the repositories
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code != 200:
        raise Exception(f"API request failed with status code: {response.status_code}")

    # Parse the JSON response and extract the list of repositories
    repos = response.json()['items']

    # Sort the repositories based on stargazers count in descending order
    repos = sorted(repos, key=lambda x: x['stargazers_count'], reverse=True)

    # Iterate through each repository
    for repo in repos:
        # Fetch the README content for the repository
        readme_content = fetch_readme(repo['full_name'])

        # Calculate the learning score for the repository based on the README content
        learning_score = evaluate_learning_friendliness(readme_content)

        # Calculate the star score for the repository (35% of stargazers_count)
        star_score = repo['stargazers_count'] * 0.35

        # Assign the learning score and star score to the repository dictionary
        repo['learning_score'] = learning_score
        repo['star_score'] = star_score

    # Calculate the weighted score for each repository based on star score and learning score
    for repo in repos:
        repo['weighted_score'] = repo['star_score'] + (repo['learning_score'] * 0.65)

    # Sort the repositories based on weighted score in descending order
    repos = sorted(repos, key=lambda x: x['weighted_score'], reverse=True)

    # Round the weighted score to two decimal places
    for repo in repos:
        repo['weighted_score'] = round(repo['weighted_score'], 2)

    # Return the list of repositories with calculated scores
    return repos



# Example usage
language = 'python'
min_stars = 1000
repositories = fetch_repositories(language, min_stars)
#print(repositories)

def fetch_default_branch(repo_full_name):
    """
    This function fetches the default branch of a given GitHub repository.

    :param repo_full_name: The full name of the repository in the format 'owner/repo'.
    :type repo_full_name: str

    :return: The name of the default branch of the repository.
             If the default branch cannot be determined or if there is an error in the request, 'main' is returned.
    :rtype: str
    """
    # Construct the URL for fetching the repository data
    branch_url = f"https://api.github.com/repos/{repo_full_name}"

    # Set the headers for the GitHub API request, including authorization
    headers = {
        'Authorization': 'token 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',
        'Accept': 'application/vnd.github.v3+json'
    }

    # Send a GET request to fetch the repository data
    response = requests.get(branch_url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Retrieve the JSON data from the response
        repo_data = response.json()

        # Extract the name of the default branch from the repository data
        default_branch_name = repo_data.get('default_branch', 'main')

        # Return the name of the default branch
        return default_branch_name
    else:
        # If the request was not successful, print an error message and return 'main'
        print(f"Failed to fetch default branch for {repo_full_name}: {response.status_code}, {response.text}")
        return 'main'
          
def fetch_issues(repo_full_name):
    """
    This function fetches issues from a given GitHub repository.

    :param repo_full_name: The full name of the repository in the format 'owner/repo'.
    :type repo_full_name: str

    :return: A list of dictionaries, where each dictionary represents an issue in the repository.
             If there are no issues or if there is an error in the request, None is returned.
    :rtype: list of dict or None
    """
    # Construct the URL for fetching issues from the repository
    issues_url = f"https://api.github.com/repos/{repo_full_name}/issues"

    # Set the headers for the GitHub API request, including authorization
    headers = {
        'Authorization': 'token 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',
        'Accept': 'application/vnd.github.v3+json'
    }

    # Send a GET request to fetch the issues
    response = requests.get(issues_url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response and extract the list of issues
        issues_data = response.json()

        # Return the list of issues
        return issues_data
    else:
        # If the request was not successful, return None
        return None



def fetch_latest_python_news():
    """
    This function fetches the latest Python news from the website 'planetpython.org' and organizes it into a Pandas DataFrame.

    :return: A Pandas DataFrame containing the latest Python news.
             The DataFrame includes columns for the date, title, link, and description of each news article.
             If no news articles are found or if there is an error in the request, an empty DataFrame is returned.
    :rtype: pandas.DataFrame
    """
    # Define the URL of the website to fetch Python news from
    url = "https://planetpython.org/"

    # Send a GET request to the website and parse the HTML content
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Initialize a list to store the news data
    news_data = []

    # Find all date headers (h2) on the webpage
    date_headers = soup.find_all('h2')

    # Iterate through the first three date headers (limiting to the most recent news)
    for date_header in date_headers[:3]:
        date = date_header.get_text().strip()  # Get the date as a string

        # Find all siblings of the date_header until the next date header (h2) is found
        for sibling in date_header.find_next_siblings():
            if sibling.name == 'h2':
                break  # Next date header found, exit the loop

            if sibling.name == 'h3':
                title = sibling.get_text().strip()  # Get the title of the news article

                # Find the link associated with the title, or indicate 'No link available'
                link = sibling.find('a')['href'] if sibling.find('a') else 'No link available'

                # Look for the description of the news article in the next h4 tag, or indicate 'No description available'
                description_tag = sibling.find_next_sibling('h4')
                description = description_tag.get_text().strip() if description_tag else 'No description available'

                # Create a dictionary representing the news article and append it to the news_data list
                news_data.append({
                    'date': date,
                    'title': title,
                    'link': link,
                    'description': description
                })

    # Create a Pandas DataFrame from the collected news data and return it
    news_df = pd.DataFrame(news_data)
    return news_df

# Example usage
news_df = fetch_latest_python_news()
print(news_df)

def store_news_to_db(df):
    """
    This function stores news data from a Pandas DataFrame into a SQLite database.

    :param df: A Pandas DataFrame containing news data to be stored.
    :type df: pandas.DataFrame

    The function checks if the DataFrame is empty. If the DataFrame is empty, it prints a message indicating
    that there is no news data to store in the database and exits. If the DataFrame is not empty, it connects
    to a SQLite database named 'python_news.db' and stores the DataFrame as a table named 'news'. If the table
    'news' already exists in the database, it replaces the existing table with the new data. The function then
    closes the database connection and prints a success message if the data storage is successful. If there is
    an error during the data storage process, the function prints an error message.

    :return: None
    """
    if df.empty:
        print("No news data to store in the database.")
        return

    print("Storing the following DataFrame in the database:")
    print(df)

    try:
        # Connect to the SQLite database (or create a new one if it doesn't exist)
        conn = sqlite3.connect('python_news.db')

        # Store the DataFrame as a SQL table named 'news' (replace it if it already exists)
        df.to_sql('news', conn, if_exists='replace', index=False)

        # Close the database connection
        conn.close()

        print("News data stored successfully.")
    except Exception as e:
        print(f"An error occurred while storing news data: {e}")

    
def fetch_and_store_news():
    """
    This function fetches the latest Python news from the website 'planetpython.org', stores it in a SQLite database,
    and returns the news data as a Pandas DataFrame.

    :return: A Pandas DataFrame containing the latest Python news.
             The DataFrame includes columns for the date, title, link, and description of each news article.
             If no news articles are found or if there is an error in the request, an empty DataFrame is returned.
    :rtype: pandas.DataFrame
    """
    # Fetch the latest Python news and store it in a SQLite database
    df = fetch_latest_python_news()
    store_news_to_db(df)

    # Return the fetched news data as a Pandas DataFrame
    return df

def debug_fetch_readme_and_issues(repositories):
    """
    This function is used for debugging and demonstration purposes. It fetches README data and issues data for the first
    5 repositories in the given list and prints the results.

    :param repositories: A list of repository dictionaries.
    :type repositories: list of dict

    The function iterates through the first 5 repositories in the list (for demonstration purposes), fetches the README
    data and issues data for each repository, and prints the repository full name, a portion of the README content (if
    available), and whether issues data is present or not.

    :return: None
    """
    for repo in repositories[:5]:  # Limiting to the first 5 repositories for demo
        repo_full_name = repo['full_name']
        print(f"Repository full name: {repo_full_name}")
        
        # Fetch the README data for the repository
        readme_data = fetch_readme(repo_full_name)
        
        # Fetch the issues data for the repository
        issues_data = fetch_issues(repo_full_name)
        
        print(f"README: {readme_data[:500] if readme_data else 'None'}")
        print(f"Issues: {issues_data is not None}")


if __name__ == '__main__':
    language = 'python'
    min_stars = 1000
    repositories = fetch_repositories(language, min_stars)
    debug_fetch_readme_and_issues(repositories)

    # Fetch and store Python news
    python_news = fetch_latest_python_news()
    store_news_to_db(python_news)