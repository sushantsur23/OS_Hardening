def configure_auditd(ssh):

    commands = [

        # Install auditd
        "apt-get install auditd -y",

        # Enable auditd
        "systemctl enable auditd",

        # Start auditd
        "systemctl start auditd",

        # Add audit rules
        "echo '-w /etc/passwd -p wa -k passwd_changes' >> /etc/audit/rules.d/audit.rules",

        # Restart service
        "service auditd restart"
    ]

    for cmd in commands:
        ssh.exec_command(cmd)

    print("[+] Auditd configured")