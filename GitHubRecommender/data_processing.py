import re
import base64

def clean_and_transform(data):
    """
    Cleans and transforms repository data.
    
    This function takes a list of repository data dictionaries and performs the following transformations:
    - Ensures the 'stars' attribute is correctly extracted as an integer.
    - Simplifies the 'name' attribute by removing special characters and converting it to lowercase.
    - Converts the 'url' attribute to a short version containing only the 'user/repo' part.
    - Categorizes repositories based on their number of stars into 'Highly Popular', 'Popular', or 'Moderately Popular'.
    - Handles missing or 'Unknown' values for the 'updated_at' attribute.
    
    :param data: A list of repository data dictionaries.
    :type data: list of dict
    
    :return: The transformed repository data.
    :rtype: list of dict
    """
    for item in data:
        # Ensure the number of stars is correctly extracted
        item['stars'] = int(item.get('stargazers_count', 0))

        # Simplify repository name (removing special characters and making lowercase)
        item['name'] = re.sub(r'\W+', '', item['name']).lower()

        # Convert URL to a short version (just the user/repo part)
        item['url'] = item['url'].split('.com/')[1]

        # Categorize repositories based on stars
        if item['stars'] > 10000:
            item['category'] = 'Highly Popular'
        elif 5000 <= item['stars'] <= 10000:
            item['category'] = 'Popular'
        else:
            item['category'] = 'Moderately Popular'

        # Handling of update times
        item['updated_at'] = item.get('updated_at', 'Unknown')

    return data

import re

def evaluate_learning_friendliness(readme_data):
    """
    Evaluates the learning friendliness of a repository based on its README.
    
    This function calculates a learning score for a GitHub repository based on its README content. The higher the
    learning score, the more beginner-friendly the repository is considered.
    
    :param readme_data: The content of the README file.
    :type readme_data: str
    
    :return: The learning score for the repository.
    :rtype: int
    """
    learning_score = 0

    # Score based on README content length
    readme_length = len(readme_data)
    if readme_length >= 900:
        learning_score += readme_length // 10  # For every 100 characters, gain 10 points

    # Score based on the number of requirements in README
    num_requirements = readme_data.lower().count('requirement')
    if num_requirements <= 3:
        learning_score += 100
    elif 3 < num_requirements <= 6:
        learning_score += 50
    elif 6 < num_requirements <= 10:
        learning_score += 10
    else:
        learning_score -= 10

    # Score for 'No limits' phrase in README
    if 'no limits' in readme_data.lower():
        learning_score += 100

    # Score based on the number of question marks
    num_questions = readme_data.count('?')
    learning_score += (10 * num_questions)

    # Deduction for each WARNING found
    num_warnings = readme_data.upper().count('WARNING')
    learning_score -= (10 * num_warnings)
    
    # Checking for beginner-friendly sections
    beginner_sections = ["getting started", "quick start", "tutorial", "examples"]
    for section in beginner_sections:
        if re.search(section, readme_data, re.IGNORECASE):
            learning_score += 100  # Score for each section found

    # Checking for community support and communication
    community_keywords = ["forum", "faq", "discussion", "chat", "discord", "slack", "gitter"]
    for keyword in community_keywords:
        if re.search(keyword, readme_data, re.IGNORECASE):
            learning_score += 50  # Score for each keyword found

    # Checking for video tutorials or demos
    if re.search(r'\bvideo\b|\bdemo\b', readme_data, re.IGNORECASE):
        learning_score += 100

    # Checking for API documentation links
    if re.search(r'\bapi\b.*\bdocumentation\b|\bdocumentation\b.*\bapi\b', readme_data, re.IGNORECASE):
        learning_score += 100

    # Checking for common errors and solutions section
    if re.search(r'\bcommon errors\b|\bfaq\b|\btroubleshooting\b', readme_data, re.IGNORECASE):
        learning_score += 100

    return learning_score

def process_repositories(repositories):
    """
    Processes the list of repositories to extract necessary information.
    
    This function takes a list of GitHub repository data dictionaries and extracts essential information from each
    repository, including 'full_name', 'name', 'description', 'language', 'stars', 'updated_at', and 'url'. The extracted
    data is returned as a list of dictionaries.
    
    :param repositories: A list of GitHub repository data dictionaries.
    :type repositories: list of dict
    
    :return: A list of dictionaries containing processed repository information.
    :rtype: list of dict
    """
    processed_repos = []
    for repo in repositories:
        repo_full_name = repo['full_name']
        repo_data = {
            'full_name': repo_full_name,
            'name': repo['name'],
            'description': repo.get('description', 'No description available'),
            'language': repo.get('language', 'Unknown'),
            'stars': repo.get('stargazers_count', 0),
            'updated_at': repo.get('updated_at', 'Unknown'),
            'url': repo.get('html_url', '')
        }
        processed_repos.append(repo_data)
    return processed_repos

def decode_readme_content(readme_data):
    """
    Decodes the README content from base64 to string.
    
    This function decodes the README content, which is expected to be in base64 encoding, to a UTF-8 encoded string.
    
    :param readme_data: The README content as a dictionary with 'content' and 'encoding' attributes.
    :type readme_data: dict
    
    :return: The decoded README content as a string, or an error message if decoding fails.
    :rtype: str
    """
    try:
        if isinstance(readme_data, dict) and 'content' in readme_data and 'encoding' in readme_data:
            if readme_data['encoding'] == 'base64':
                return base64.b64decode(readme_data['content']).decode('utf-8')
            else:
                return "Unexpected encoding format."
        else:
            return "README content not available or not in expected format."
    except Exception as e:
        print(f"Error decoding README content: {e}")
        return "Error in decoding README."




