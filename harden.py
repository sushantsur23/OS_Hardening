import paramiko
import yaml
import logging
from concurrent.futures import ThreadPoolExecutor
from rich.console import Console
from rich.table import Table

console = Console()

logging.basicConfig(
    filename='logs/hardening.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

HARDENING_COMMANDS = [

    # Update packages
    "apt-get update -y && apt-get upgrade -y",

    # Disable root SSH login
    "sed -i 's/^#PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config",

    # Disable password authentication
    "sed -i 's/^#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config",

    # Restart SSH
    "systemctl restart sshd",

    # Install fail2ban
    "apt-get install fail2ban -y",

    # Enable firewall
    "ufw allow OpenSSH",
    "ufw --force enable",

    # Kernel hardening
    "echo 'net.ipv4.ip_forward=0' >> /etc/sysctl.conf",
    "echo 'net.ipv4.conf.all.send_redirects=0' >> /etc/sysctl.conf",
    "sysctl -p",

    # Password policy
    "apt-get install libpam-pwquality -y",

    # Auditd
    "apt-get install auditd -y",
    "systemctl enable auditd",
    "systemctl start auditd",

    # Disable unused filesystem modules
    "echo 'install cramfs /bin/true' >> /etc/modprobe.d/hardening.conf",

    # Permissions
    "chmod 600 /etc/shadow",
    "chmod 644 /etc/passwd"
]

def load_inventory():
    with open("inventory/hosts.yaml") as f:
        return yaml.safe_load(f)

def execute_commands(ssh, host):
    for cmd in HARDENING_COMMANDS:
        stdin, stdout, stderr = ssh.exec_command(cmd)

        out = stdout.read().decode()
        err = stderr.read().decode()

        logging.info(f"{host}: CMD: {cmd}")
        logging.info(f"{host}: OUT: {out}")

        if err:
            logging.error(f"{host}: ERR: {err}")

def connect_and_harden(server):
    host = server['host']
    username = server['username']
    key_path = server['key']

    try:
        console.print(f"[yellow]Connecting to {host}[/yellow]")

        key = paramiko.RSAKey.from_private_key_file(key_path)

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(
            hostname=host,
            username=username,
            pkey=key,
            timeout=10
        )

        console.print(f"[green]Connected to {host}[/green]")

        execute_commands(ssh, host)

        ssh.close()

        return (host, "SUCCESS")

    except Exception as e:
        logging.error(f"{host}: {str(e)}")
        return (host, f"FAILED: {str(e)}")

def main():

    inventory = load_inventory()

    results = []

    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [
            executor.submit(connect_and_harden, server)
            for server in inventory['servers']
        ]

        for future in futures:
            results.append(future.result())

    table = Table(title="Hardening Results")

    table.add_column("Host")
    table.add_column("Status")

    for host, status in results:
        table.add_row(host, status)

    console.print(table)

if __name__ == "__main__":
    main()