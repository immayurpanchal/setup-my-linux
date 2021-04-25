import os
import click
import subprocess


def configure():
    os.system("mkdir -p ~/.config/fusuma")
    os.system("cp ./mac_gestures.yml ~/.config/fusuma/config.yml")


def install():
    try:
        click.secho("Installing Mac Gestures 🚧", fg="bright_yellow", bold=True)
        click.secho("Adding user to input group 🚧", fg="bright_yellow", bold=True)
        os.system("sudo gpasswd -a $USER input")
        click.secho("Installing libinput-tools 🚧", fg="bright_yellow", bold=True)
        os.system("sudo apt-get install libinput-tools")
        click.secho("Installing ruby 🚧", fg="bright_yellow", bold=True)
        os.system("sudo apt-get install ruby")
        click.secho("Installing ruby gem 🚧", fg="bright_yellow", bold=True)
        os.system("sudo apt-get install rubygems")
        click.secho("Installing fusuma 🚧", fg="bright_yellow", bold=True)
        os.system("sudo gem install fusuma")
        click.secho("Installing xdotool 🚧", fg="bright_yellow", bold=True)
        os.system("sudo apt-get install xdotool")
        click.secho("enabling touch events 🚧", fg="bright_yellow", bold=True)
        os.system(
            "gsettings set org.gnome.desktop.peripherals.touchpad send-events enabled"
        )
        click.secho("Updating fusuma 🚧", fg="bright_yellow", bold=True)
        os.system("sudo gem update fusuma")
        # copy config file
        configure()
        # auto start gesture on login
        # os.system("which fusuma")
        # os.system("gnome-session-properties")
        click.secho(
            "Successfully installed Mac Gestures ✅",
            fg="bright_green",
            bold=True,
        )
        # adding newgrp will restart the terminal
        os.system("newgrp input")
    except:
        click.secho(
            "Failed to install Mac Gestures ❌",
            fg="red",
            bold=True,
        )
