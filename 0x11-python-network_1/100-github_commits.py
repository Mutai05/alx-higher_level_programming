#!/usr/bin/python3
"""Lists the 10 most recent commits on a given GitHub repository.
Usage: ./100-github_commits.py <repository name> <repository owner>
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <repository name> <repository owner>".format(sys.argv[0]))
        sys.exit(1)

    url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[2], sys.argv[1])

    try:
        r = requests.get(url)

        # Check if the request was successful (status code 200)
        r.raise_for_status()

        commits = r.json()

        for i in range(min(10, len(commits))):
            commit = commits[i]
            sha = commit.get("sha")
            author_name = commit.get("commit", {}).get("author", {}).get("name", "Unknown")
            print("{}: {}".format(sha, author_name))

    except requests.RequestException as e:
        print("Error: {}".format(e))
    except ValueError:
        print("Error: Unable to parse JSON response.")
    except IndexError:
        print("Error: Insufficient number of commits.")
