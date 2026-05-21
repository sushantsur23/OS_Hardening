# 1. Create project structure
echo "📂 Setting up project structure..."

mkdir -p modules
touch modules/__init__.py
touch modules/firewall.py
touch modules/ssh_hardening.py
touch modules/sysctl_hardening.py
touch modules/fail2ban.py
touch modules/auditing.py

mkdir -p inventory
touch inventory/hosts.yaml

mkdir -p reports
touch reports/compliance_report.json

mkdir -p policies
touch .env

mkdir -p logs
mkdir -p backups


touch harden.py

touch .env

# 4. Create requirements.txt if not exists & add libraries
if [ ! -f "requirements.txt" ]; then
    echo "📄 Creating requirements.txt..."
    cat <<EOL > requirements.txt
paramiko
pyyaml
rich
concurrent-log-handler
EOL
    echo "✅ requirements.txt created with default libraries."
else
    echo "📄 requirements.txt already exists, skipping creation."
fi

set -e  # Exit if any command fails

echo "🚀 Initializing OS Hardening project with Conda..."
conda create --prefix ./venv python=3.12 -y

# 1. Create Conda environment in local folder (./venv)
if [ ! -d "venv" ]; then
    echo "📦 Creating Conda environment in ./venv ..."
    conda create --prefix ./venv python=3.12 -y
else
    echo "✅ Conda environment already exists in ./venv"
fi

echo "🚀 Creating setup.py file with the Project information as needed..."
touch setup.py

# Create setup.py
echo "📝 Creating setup.py..."
cat > setup.py <<EOL
from setuptools import setup, find_packages

setup(
    name="Linux_Hardening_Workflow",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "paramiko",
        "pyyaml",
        "rich",
        "concurrent-log-handler"
            ],

    author="Sushant Sur",
    description="Linux Hardening Automation Workflow",
    python_requires=">=3.12",
)
EOL

echo "✅ Setup complete and ready to run! 

echo "✅ Project structure is ready."

echo "⚙️  Installing project in editable mode..."
pip install -e .

#Run the file using the command as ./init.sh in gitbash terminal