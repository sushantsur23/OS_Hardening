def detect_os(ssh):

    stdin, stdout, stderr = ssh.exec_command(
        "cat /etc/os-release"
    )

    output = stdout.read().decode()

    if "Ubuntu" in output:
        return "ubuntu"

    elif "CentOS" in output:
        return "centos"

    elif "Rocky" in output:
        return "rocky"

    return "unknown"