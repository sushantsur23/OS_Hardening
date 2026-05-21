def secure_packages(ssh):

    commands = [

        # Update packages
        "apt-get update -y",

        # Upgrade packages
        "apt-get upgrade -y",

        # Remove insecure services
        "apt-get remove telnet -y",

        # Remove FTP server
        "apt-get remove vsftpd -y"
    ]

    for cmd in commands:
        ssh.exec_command(cmd)

    print("[+] Package security completed")