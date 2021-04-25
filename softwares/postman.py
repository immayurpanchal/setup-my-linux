import os
import click


def install():
    try:
        click.secho("Installing Postman 🚧", fg="bright_yellow", bold=True)
        os.system("sudo snap install postman")
        click.secho("Successfully installed Postman ✅", fg="bright_green", bold=True)
    except:
        click.secho("Failed to install Postman ❌", fg="red", bold=True, blink=True)
