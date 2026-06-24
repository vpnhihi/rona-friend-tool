import typer
from src.ui.cli import cli_app
from src.ui.web.app import run_web

app = typer.Typer()

@app.command()
def web() -> None:
    """Chạy giao diện web giống zalo-manager"""
    run_web()

@app.command()
def cli() -> None:
    """Chạy CLI"""
    cli_app()

if __name__ == "__main__":
    app()
