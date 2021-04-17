import softwares.vscode as vscode


def main():
    print('Welcome 😎 to Setup my Linux 💻 (Ubuntu 20.04)')
    res = input('Do you want to install VSCode? [yn]').lower()

    if res == 'y':
        vscode.install()


if __name__ == '__main__':
    main()
