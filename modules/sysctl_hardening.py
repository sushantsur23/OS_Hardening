def apply_sysctl_hardening(ssh):

    commands = [

        # Disable IP forwarding
        "echo 'net.ipv4.ip_forward = 0' >> /etc/sysctl.conf",

        # Disable ICMP redirects
        "echo 'net.ipv4.conf.all.send_redirects = 0' >> /etc/sysctl.conf",

        # Enable SYN cookies
        "echo 'net.ipv4.tcp_syncookies = 1' >> /etc/sysctl.conf",

        # Reload sysctl
        "sysctl -p"
    ]

    for cmd in commands:
        ssh.exec_command(cmd)

    print("[+] Kernel hardening completed")