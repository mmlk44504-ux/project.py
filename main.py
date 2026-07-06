import typer

app = typer.Typer()

movies = []

@app.command()
def add_movie(title: str):
    """
    Add a movie to the list.
    """
    movies.append(title)
    typer.echo(f"Added: {title}")

@app.command()
def show_movies():
    """
    Show all movies.
    """
    if not movies:
        typer.echo("No movies found.")
        return

    typer.echo("\nMovies List:")
    for i, movie in enumerate(movies, start=1):
        typer.echo(f"{i}. {movie}")

if __name__ == "__main__":
    app()