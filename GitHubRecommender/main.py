import argparse
import pandas as pd
import sqlite3
import data_acquisition as da
import data_processing as dp
import recommender_system as rs



def fetch_and_store_news():
    """
    Fetches the latest Python news and stores it in a database.

    This function fetches the latest Python news from planetpython.org, stores it in a DataFrame, and returns the DataFrame.

    :return: A DataFrame containing the latest Python news.
    :rtype: pandas.DataFrame
    """
    python_news = da.fetch_latest_python_news()
    
    news_df = pd.DataFrame(python_news)
    return news_df


def main():
    # Fetch and store the latest Python news
    news_df = da.fetch_and_store_news()
    print("\nFetching the latest Python news...\n")
    print(news_df.to_string(index=False))

    # Argument parsing for language and stars
    parser = argparse.ArgumentParser(description='GitHub Repository Recommender System')
    parser.add_argument('-l', '--language', default='python', type=str, help='Programming language for repositories')
    parser.add_argument('-s', '--stars', default=1000, type=int, help='Minimum number of stars for repositories')
    args = parser.parse_args()

    print("GitHub Repository Recommender System")
    print(f"Fetching {args.language} repositories with at least {args.stars} stars from GitHub...")

    # Fetch repositories and process them
    repositories = da.fetch_repositories(args.language, args.stars)
    
    # Sort repositories based on weighted score
    sorted_repos = sorted(repositories, key=lambda x: x['weighted_score'], reverse=True)

    print("\nList of Repositories:")
    for idx, repo in enumerate(sorted_repos):
        print(f"{idx}: {repo['name']} - Stars: {repo['stargazers_count']}, Learning Score: {repo.get('learning_score', 0)}, Weighted Score: {repo['weighted_score']}")

    try:
        repo_id = int(input("\nEnter the ID (number) of a repository to get recommendations: "))
        if repo_id < 0 or repo_id >= len(sorted_repos):
            raise ValueError("Invalid ID")
    except ValueError as e:
        print(str(e))
        return

    use_additional_features = input("Do you want to use additional features for recommendations? (yes/no): ").lower() == 'yes'

    print(f"\nRecommendations based on: {sorted_repos[repo_id]['name']}")
    recommended_repos = rs.content_based_recommendation(sorted_repos, repo_id, use_additional_features)

    print("\nRecommended Repositories:")
    for repo in recommended_repos:
        print(f"{repo['name']} - {repo['description']}")

if __name__ == '__main__':
    main()
