import os
import sys
import click


def brave():
    try:
        click.clear()
        click.secho("Installing Brave...", fg="yellow")
        os.system("sudo apt install apt-transport-https curl")
        os.system(
            "sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg"
        )
        os.system(
            'echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main"|sudo tee /etc/apt/sources.list.d/brave-browser-release.list'
        )
        os.system("sudo apt update")
        os.system("sudo apt install brave-browser")
        click.secho(
            "Successfully installed Brave ✅", fg="bright_green", bold=True, blink=True
        )
    except:
        click.secho("Failed to install Brave ❌", fg="red", bold=True, blink=True)
        sys.exit(1)


def firefox():
    try:
        click.clear()
        click.secho("Installing firefox 🦊 ...", fg="yellow")
        os.system("sudo apt install firefox")
        click.secho(
            "Successfully installed Firefox ✅", fg="bright_green", bold=True, blink=True
        )
    except:
        click.secho("Failed to install Firefox ❌", fg="red", bold=True, blink=True)
        sys.exit(1)
