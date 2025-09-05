from rich.console import Console

console = Console()

if __name__ == "__main__":
    user_input = console.input(
        "What is [i]your[/i] [bold red]name[/]? :smiley:")
    console.print(f"Hello, {user_input}!")
