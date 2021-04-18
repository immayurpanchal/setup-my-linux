import os
import click


def install():
    try:
        click.clear()
        click.secho("Installing VSCode 🧰", fg="yellow")
        os.system(
            "wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg"
        )
        os.system(
            "sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/"
        )
        os.system(
            """sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/trusted.gpg.d/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'"""
        )
        os.system("rm - f packages.microsoft.gpg")
        os.system("sudo apt install apt-transport-https")
        os.system("sudo apt update")
        os.system("sudo apt install code")
        click.secho(
            "Successfully installed VSCode ✅",
            fg="bright_green",
            bold=True,
        )
    except KeyboardInterrupt:
        click.secho("Pressed Ctrl+C, Aborting the script 🔥", fg="red")
    except:
        print("Failed to install VSCode ❌, Existing the system", bold=True, blink=True)
