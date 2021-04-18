import os
import click


def stacer():
    try:
        click.clear()
        click.secho("Installing Stacer", fg="yellow")
        os.system("sudo apt install stacer")
        click.secho(
            "Successfully installed Stacer ✅", fg="bright_green", bold=True, blink=True
        )
    except:
        click.secho("Failed to install stacer ❌", fg="red", bold=True, blink=True)


def copyq():
    try:
        click.clear()
        os.system("sudo add-apt-repository ppa:hluk/copyq")
        os.system("sudo apt update")
        os.system("sudo apt install copyq")
        click.secho(
            "Successfully installed CopyQ ✅", fg="bright_green", bold=True, blink=True
        )
    except:
        click.secho("Failed to install CopyQ ❌", fg="red", bold=True, blink=True)


def vlc():
    try:
        click.clear()
        os.system("sudo snap install vlc")
        click.secho(
            "Successfully installed VLC ✅", fg="bright_green", bold=True, blink=True
        )
    except:
        click.secho("Failed to install VLC ❌", fg="red", bold=True, blink=True)


def qbittorrent():
    try:
        click.clear()
        os.system("sudo add-apt-repository ppa:qbittorrent-team/qbittorrent-stable")
        os.system("sudo apt install qbittorrent")
        click.secho(
            "Successfully installed qBitTorrent ✅",
            fg="bright_green",
            bold=True,
            
        )
    except:
        click.secho("Failed to install qBitTorrent ❌", fg="red", bold=True, blink=True)


def gnome_tweak_tool():
    try:
        click.clear()
        os.system("sudo apt-add-repository universe")
        os.system("sudo apt install gnome-tweak-tool")
        click.secho(
            "Successfully installed Gnome Tweak Tool ✅",
            fg="bright_green",
            bold=True,
            
        )
    except:
        click.secho(
            "Failed to install Gnome Tweak Tool ❌", fg="red", bold=True, blink=True
        )
