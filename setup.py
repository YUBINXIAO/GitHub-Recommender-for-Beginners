from setuptools import setup, find_packages

setup(
    name='GitHubRecommender',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests', 'numpy', 'scikit-learn', 'pandas', 'beautifulsoup4',
    ],
    author='Yubin Xiao',
    author_email='Yubin.Xiao@columbia.edu',
    description='A GitHub Repository Recommender System',
    keywords='github api recommender system',
    url='https://github.com/YUBINXIAO/GitHub-Recommender-for-Beginners',
)
