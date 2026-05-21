def configure_firewall(ssh):

    commands = [

        # Install UFW
        "apt-get install ufw -y",

        # Allow SSH
        "ufw allow 22/tcp",

        # Allow HTTP/HTTPS
        "ufw allow 80/tcp",
        "ufw allow 443/tcp",

        # Enable firewall
        "ufw --force enable"
    ]

    for cmd in commands:
        ssh.exec_command(cmd)

    print("[+] Firewall configured")