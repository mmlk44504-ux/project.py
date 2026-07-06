import typer
import json
import os

app = typer.Typer()

FILE_NAME = "movies.json"


def load_movies():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_movies(movies):
    with open(FILE_NAME, "w") as file:
        json.dump(movies, file)


@app.command()
def add_movie(title: str):
    movies = load_movies()
    movies.append(title)
    save_movies(movies)
    typer.echo(f"Added: {title}")


@app.command()
def show_movies():
    movies = load_movies()

    if not movies:
        typer.echo("No movies found.")
        return

    typer.echo("\nMovies List:")
    for i, movie in enumerate(movies, start=1):
        typer.echo(f"{i}. {movie}")


if __name__ == "__main__":
    app()
