
# Background

Initially, my aim was to develop a GitHub repository recommender. However, my Teaching Assistant pointed out that the concept was quite broad and commonplace. This feedback led me to deep research and observation, where I identified a significant gap: there are no GitHub recommenders specifically tailored for beginners.

It's a common belief that repositories with a higher number of stars are generally better. However, for beginners, a high-star but complex repository might not be as beneficial. It’s akin to giving a high school textbook to a primary school student - the content, though high quality, is not appropriate for their level. Primary students have materials that are best suited for their learning stage.

Addressing this, my recommender system doesn't solely focus on the number of stars. Instead, it employs a series of data techniques to calculate a ‘Learning Score’ for each repository. This score, along with the stars, is used to compute a weighted score, with 35% weightage for stars and 65% for the Learning Score. Repositories are then ranked based on this weighted score. A higher score indicates not only quality but also a greater friendliness towards beginners. This ranking is among repositories with at least 1,000 stars, ensuring a baseline quality.

**Addressing this, my recommender system doesn't solely focus on the number of stars. Instead, it employs a series of data techniques to calculate a ‘Learning Score’ for each repository. This score, along with the stars, is used to compute a weighted score, with 35% weightage for stars and 65% for the Learning Score. Repositories are then ranked based on this weighted score. A higher score indicates not only quality but also a greater friendliness towards beginners. This ranking is among repositories with at least 1,000 stars, ensuring a baseline quality.**
   
   **Another innovative aspect of my project is a front-end feature that captures the latest news from Python-related news websites (Fetches the latest Python news from planetpython.org). This functionality ensures that, along with the repository recommendations, beginners are also kept abreast of the latest happenings in the Python world. It’s a way to provide learners with real-time insights into what's trending and new in their field of interest.**


The system is in continuous evolution, requiring regular refinement and updates to accurately calculate Learning Scores and weighted scores. It’s a long-term commitment, and I am fully prepared for this enduring journey to create a more scientifically sound and beginner-friendly GitHub repository recommender.


# GitHub Recommender for Beginners

Welcome to my GitHub Recommender for Beginners project! This tool is designed to assist newcomers in discovering GitHub repositories that are both popular and beginner-friendly.

## Overview

Originally conceived as a general GitHub Recommender, I realized the need for a more tailored approach for beginners. While GitHub is abundant with high-star repositories, they can be overwhelming and complex for newcomers. My mission is to provide a platform that ranks repositories from a beginner's perspective, focusing on learning-friendliness, thorough documentation, active community support, beginner-oriented content, and personalized recommendations.

## Key Features

- **Learning-Friendly Scoring:** I use a unique scoring system to evaluate repositories on their beginner-friendliness.
- **Comprehensive Documentation:** I prioritize repositories with beginner-oriented documentation.
- **Active Community Support:** I identify repositories with active discussions and community engagement.
- **Beginner-Friendly Content:** I look for repositories offering tutorials, guides, or resources for newcomers.
- **Personalized Recommendations:** I provide recommendations based on coding interests and level.

This tool is here to help both programming novices and those seeking beginner-friendly open-source projects. Join me in making GitHub more accessible to newcomers.

### The Challenge

My initial goal was to create a tool for suggesting repositories based on various factors. However, the real challenge was catering to beginners, who are just starting their coding journey or exploring new technologies.

### Bridging the Gap

For newcomers, GitHub can be like a labyrinth. This tool aims to match beginners with repositories they can genuinely understand and learn from, curating a list tailored to specific learning needs.

### How It Works

I employ a learning-friendly scoring system, considering factors like comprehensive documentation and the presence of beginner-friendly content, to recommend accessible repositories.

## Installation Instructions

### Prerequisites

- Python 3.6 or higher
- Installed pip package manager

### Installation Steps

1. **Create a Virtual Environment** (Optional)

   ```bash
   python -m venv myenv

This isolates project dependencies in a virtual environment named "myenv".

 1. Activate the Virtual Environment (Optional)
 
 On Windows:

  ```bash
  myenv\Scripts\activate
  ```

 On macOS and Linux:

  ```bash
  source myenv/bin/activate
  ```
  2. Install the Package

  Use pip to install the package from the Python Package Index (PyPI):

  pip install GitHubRecommender


  Alternatively, if you are installing from source code hosted on GitHub:

  pip install git+https://github.com/QMSS-G5072-2023/GitHub_Recommender_Beginners.git


  3. Verify the Installation

  Open a Python interpreter and try importing the package to verify the installation:

  ```python
  import github_recommender_for_beginners
  ```

## Uninstallation

If you decide to uninstall the package, you can use the following command:
```bash
pip uninstall GitHubRecommender
```

## Updating
To update the package to the latest version, use the following command:
```bash
pip install --upgrade GitHubRecommender
```




This format, using the first-person perspective, is ready for markdown-supported platforms.

