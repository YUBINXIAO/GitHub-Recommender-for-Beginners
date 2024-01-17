import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def preprocess_text(text):
    # Convert to lowercase, remove punctuation, etc.
    # Check if text is not None
    return text.lower() if text else ''

def calculate_similarity(vectorizer, repo_matrix, base_vector):
    similarity_scores = cosine_similarity(base_vector, repo_matrix)
    return similarity_scores[0]

def content_based_recommendation(repositories, base_repo_id, use_additional_features=False, top_n=5):
    # Preprocess descriptions
    descriptions = [preprocess_text(repo.get('description', '')) for repo in repositories]
    base_description = preprocess_text(repositories[base_repo_id].get('description', ''))

    # Vectorize descriptions
    description_vectorizer = TfidfVectorizer()
    description_matrix = description_vectorizer.fit_transform(descriptions)
    base_description_vector = description_vectorizer.transform([base_description])

    # Prepare the final matrix for similarity calculation
    final_matrix = description_matrix
    base_vector = base_description_vector

    if use_additional_features:
        # Combine additional features (language and stars)
        additional_features = [f"{repo.get('language', '')} {repo.get('stars', 0)}" for repo in repositories]
        additional_vectorizer = TfidfVectorizer()
        additional_matrix = additional_vectorizer.fit_transform(additional_features)

        # Concatenate description matrix with additional feature matrix
        final_matrix = np.hstack((description_matrix.toarray(), additional_matrix.toarray()))
        base_vector = np.hstack((base_description_vector.toarray(), additional_vectorizer.transform([f"{repositories[base_repo_id].get('language', '')} {repositories[base_repo_id].get('stars', 0)}"]).toarray()))

    # Calculate similarity scores
    scores = calculate_similarity(description_vectorizer, final_matrix, base_vector)

    # Get top N similar repositories, excluding the base repository itself
    top_indices = np.argsort(scores)[::-1][1:top_n+1]
    return [repositories[i] for i in top_indices]



