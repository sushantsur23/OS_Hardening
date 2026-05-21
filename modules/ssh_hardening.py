def harden_ssh(ssh):

    commands = [

        # Backup SSH configuration
        "cp /etc/ssh/sshd_config /tmp/sshd_config.bak",

        # Disable root login
        "sed -i 's/^#PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config",

        # Disable password authentication
        "sed -i 's/^#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config",

        # Set idle timeout
        "echo 'ClientAliveInterval 300' >> /etc/ssh/sshd_config",

        # Restart SSH service
        "systemctl restart sshd"
    ]

    for cmd in commands:
        ssh.exec_command(cmd)

    print("[+] SSH hardening completed")