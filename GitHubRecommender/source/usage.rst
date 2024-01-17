.. _usage:

=================
Usage Guide
=================

This guide provides instructions on how to use the **GitHub Recommender for Beginners** package to discover GitHub repositories based on your preferences.

Installation
------------

Before using the package, make sure you have installed it as described in the [Installation Instructions](installation.rst).

Getting Started
----------------

To get started, you'll need to import the package in your Python code:

.. code-block:: python

   from github_recommender_for_beginners import GitHubRecommender

Creating a Recommender
------------------------

To create a recommender instance, use the following code:

.. code-block:: python

   recommender = GitHubRecommender()

Setting Preferences
---------------------

You can set your preferences for repository recommendations using the following methods:

- `set_language(language)`: Set the preferred programming language.
- `set_min_stars(min_stars)`: Set the minimum number of stars for recommended repositories.

For example:

.. code-block:: python

   recommender.set_language('python')
   recommender.set_min_stars(1000)

Fetching Recommendations
-------------------------

Once you have set your preferences, you can fetch repository recommendations using the `get_recommendations()` method:

.. code-block:: python

   recommendations = recommender.get_recommendations()

The `get_recommendations()` method returns a list of recommended repositories based on your preferences.

Displaying Recommendations
---------------------------

You can display the recommended repositories in a user-friendly format. For example:

.. code-block:: python

   for repo in recommendations:
       print(f"Repository Name: {repo['name']}")
       print(f"Description: {repo['description']}")
       print(f"Stars: {repo['stars']}")
       print(f"URL: {repo['url']}")
       print("\n")

That's it! You can now use the **GitHub Recommender for Beginners** package to discover GitHub repositories that match your preferences.

For more advanced usage and additional features, refer to the package documentation and available methods.

If you encounter any issues or have questions, please refer to the [Troubleshooting Guide](troubleshooting.rst) or [contact me](#contact) for assistance.
