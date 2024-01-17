from setuptools import setup, find_packages

setup(
    name='GitHubRecommender',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests', 'numpy', 'scikit-learn', 'argparse',
        
    ],
    author='Yubin Xiao',
    author_email='Yubin.Xiao@columbia.edu',
    description='A GitHub Repository Recommender System',
    keywords='github api recommender system',
    url='https://github.com/QMSS-G5072-2023/XIAO_YUBIN/tree/9901d0adc43d6f24dd8c7884202320107f9d9f94/Final%20Project',
)
