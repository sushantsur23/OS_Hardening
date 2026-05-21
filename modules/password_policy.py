def enforce_password_policy(ssh):

    commands = [

        # Install PAM module
        "apt-get install libpam-pwquality -y",

        # Set password minimum length
        "sed -i 's/^# minlen =.*/minlen = 12/' /etc/security/pwquality.conf",

        # Password expiry
        "sed -i 's/^PASS_MAX_DAYS.*/PASS_MAX_DAYS 90/' /etc/login.defs",

        # Password warning age
        "sed -i 's/^PASS_WARN_AGE.*/PASS_WARN_AGE 7/' /etc/login.defs"
    ]

    for cmd in commands:
        ssh.exec_command(cmd)

    print("[+] Password policy enforced")