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
