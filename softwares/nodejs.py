import os
import click


def clean_cache():
    try:
        click.secho(
            "Cleaning cache before installation 🗑", fg="bright_yellow", bold=True
        )
        os.system("sudo npm cache clean -f")
        click.secho("Successfully cleared the cache 🗑", fg="bright_green", bold=True)
    except:
        click.secho(
            "Cache clearing failed ❌",
            fg="red",
            bold=True,
        )


def install_n():
    try:
        click.secho(
            "Installing node version manager 'n' 🚧", fg="bright_yellow", bold=True
        )
        os.system("sudo npm install -g n")
        click.secho(
            "Successfully installed node version manager 'n' ✅",
            fg="bright_green",
            bold=True,
        )
    except:
        click.secho(
            "Failed to install node version manager 'n' ❌",
            fg="red",
            bold=True,
        )


def install_latest_npm():
    try:
        click.secho("Installing latest npm version 🚧", fg="bright_yellow", bold=True)
        os.system("sudo npm install -g npm")
        click.secho(
            "Successfully installed latest version of npm ✅",
            fg="bright_green",
            bold=True,
        )
    except:
        click.secho(
            "Failed to install latest version of npm ❌",
            fg="red",
            bold=True,
        )


def change_node_version_greetings():
    click.secho(
        "To change the node version type 'sudo n' ✅",
        fg="bright_green",
        bold=True,
        blink=True,
    )


def install_stable_nodejs():
    clean_cache()
    install_n()
    try:
        click.secho("Installing LTS version of NodeJS 🚧", fg="bright_yellow", bold=True)
        os.system("sudo n stable")
        click.secho(
            "Successfully installed LTS version of NodeJS ✅",
            fg="bright_green",
            bold=True,
        )
        change_node_version_greetings()
    except:
        click.secho(
            "Failed to install LTS version of NodeJS ❌",
            fg="red",
            bold=True,
        )
    install_latest_npm()


def install_latest_nodejs():
    clean_cache()
    install_n()
    try:
        click.secho(
            "Installing latest version of NodeJS 🚧", fg="bright_yellow", bold=True
        )
        os.system("sudo n latest")
        click.secho(
            "Successfully installed latest version of NodeJS ✅",
            fg="bright_green",
            bold=True,
        )
        change_node_version_greetings()
    except:
        click.secho(
            "Failed to install latest version of NodeJS ❌",
            fg="red",
            bold=True,
        )
    install_latest_npm()


def npm():
    try:
        click.secho("Installing npm  🚧", fg="bright_yellow", bold=True)
        os.system("sudo apt-get install npm")
        click.secho(
            "Successfully installed npm ✅",
            fg="bright_green",
            bold=True,
        )
    except:
        click.secho(
            "Failed to install npm ❌",
            fg="red",
            bold=True,
        )


def install():
    try:
        click.secho(
            "Installing Node js stable version 🚧", fg="bright_yellow", bold=True
        )
        os.system("sudo apt-get install nodejs")
        click.secho(
            "Successfully installed nodejs ✅",
            fg="bright_green",
            bold=True,
        )
        # install npm
        npm()
    except:
        click.secho(
            "Failed to install nodejs ❌",
            fg="red",
            bold=True,
        )
