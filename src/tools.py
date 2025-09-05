import json
import os

import requests
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_tavily import TavilySearch
from langgraph.types import interrupt

# Env vars
load_dotenv()

HASHNODE_API_ENDPOINT = os.getenv(
    "HASHNODE_API_ENDPOINT", "https://gql.hashnode.com")
HASHNODE_API_KEY = os.getenv("HASHNODE_API_KEY")
HASHNODE_PUBLICATION_ID = os.getenv("HASHNODE_PUBLICATION_ID")


# TOOLS
@tool
def publish_article(title, content_markdown, tags=None):
    """
    Publishes an article to Hashnode.
    """
    headers = {
        "Content-Type": "application/json",
        "Authorization": HASHNODE_API_KEY,
    }

    # GraphQL mutation for publishing an article
    query = """
    mutation PublishPost($input: PublishPostInput!) {
      publishPost(input: $input) {
        post {
          id
          title
          url
        }
      }
    }
    """

    variables = {
        "input": {
            "publicationId": HASHNODE_PUBLICATION_ID,
            "title": title,
            "contentMarkdown": content_markdown,
            "tags": [{"name": tag, "slug": tag.lower()}
                     for tag in tags] if tags else [],
        }
    }

    payload = {
        "query": query,
        "variables": variables,
    }

    try:
        response = requests.post(
            HASHNODE_API_ENDPOINT, headers=headers, data=json.dumps(payload))
        response.raise_for_status()  # Raise an exception for bad status codes

        response_data = response.json()
        if "errors" in response_data:
            print(f"Error publishing article: {response_data['errors']}")
            return None
        else:
            post_info = response_data["data"]["publishPost"]["post"]
            print("Article published successfully!")
            print(f"Title: {post_info['title']}")
            print(f"URL: {post_info['url']}")
            return post_info
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


@tool
def human_assistance(query: str) -> str:
    """Request assistance from a human."""
    human_response = interrupt(
        {"query": query})  # This saves the state in DB and kills the graph
    return human_response["data"]


search_tool = TavilySearch(max_results=5, topic="general")

# List of all tools
tools = [publish_article, human_assistance, search_tool]
