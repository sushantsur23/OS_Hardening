def backup_configs(ssh):

    commands = [

        "mkdir -p /tmp/hardening_backups",

        "cp /etc/ssh/sshd_config /tmp/hardening_backups/",

        "cp /etc/sysctl.conf /tmp/hardening_backups/"
    ]

    for cmd in commands:
        ssh.exec_command(cmd)

    print("[+] Backup completed")