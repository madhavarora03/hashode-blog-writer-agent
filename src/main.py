from rich.console import Console

from publish import publish_article

console = Console()

if __name__ == "__main__":
    user_input = console.input(
        "What is [i]your[/i] [bold red]name[/]? :smiley: ")
    title = f"Hello from {user_input}"
    content = f"""
    This is a test article written by {user_input} using the
    Hashnode Blog Writer Agent.
    """
    published_post = publish_article(title, content, tags=["test", "api"])
    if published_post:
        console.print(
            f"Published post URL: [bold blue]{published_post['url']}[/]")
    else:
        console.print("[bold red]Failed to publish the article.[/]")
