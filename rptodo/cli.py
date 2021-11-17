import typer
from typing import Optional
from rptodo import __app_name__, __version__

app = typer.Typer()


def __version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")


@app.callback()
def main(
        version: Optional[bool] = typer.Option(
            None,
            "--version",
            "-v",
            help="Shows the application version and exits",
            callback=__version_callback,
            is_eager=True)
) -> None:
    return
