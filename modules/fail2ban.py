def install_fail2ban(ssh):

    commands = [

        # Install fail2ban
        "apt-get install fail2ban -y",

        # Enable service
        "systemctl enable fail2ban",

        # Start service
        "systemctl start fail2ban"
    ]

    for cmd in commands:
        ssh.exec_command(cmd)

    print("[+] Fail2Ban enabled")