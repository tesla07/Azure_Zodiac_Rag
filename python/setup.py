#!/usr/bin/env python3
"""
Setup script for Linda Goodman's Zodiac Guide
This script helps set up the virtual environment and install dependencies.
"""

import os
import sys
import subprocess
import platform

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"   Error: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8 or higher is required")
        print(f"   Current version: {version.major}.{version.minor}.{version.micro}")
        return False
    print(f"✅ Python version {version.major}.{version.minor}.{version.micro} is compatible")
    return True

def setup_virtual_environment():
    """Set up virtual environment"""
    venv_name = "labenv"
    
    # Check if virtual environment already exists
    if os.path.exists(venv_name):
        print(f"⚠️  Virtual environment '{venv_name}' already exists")
        response = input("   Do you want to recreate it? (y/N): ").strip().lower()
        if response == 'y':
            print(f"🗑️  Removing existing virtual environment...")
            if platform.system() == "Windows":
                run_command(f"rmdir /s /q {venv_name}", "Removing existing virtual environment")
            else:
                run_command(f"rm -rf {venv_name}", "Removing existing virtual environment")
        else:
            print("   Using existing virtual environment")
            return True
    
    # Create virtual environment
    if not run_command(f"python -m venv {venv_name}", "Creating virtual environment"):
        return False
    
    return True

def install_dependencies():
    """Install Python dependencies"""
    venv_name = "labenv"
    
    # Determine activation script based on platform
    if platform.system() == "Windows":
        activate_script = f"{venv_name}\\Scripts\\activate"
        pip_path = f"{venv_name}\\Scripts\\pip"
    else:
        activate_script = f"{venv_name}/bin/activate"
        pip_path = f"{venv_name}/bin/pip"
    
    # Install dependencies
    if not run_command(f"{pip_path} install -r requirements.txt", "Installing dependencies"):
        return False
    
    return True

def create_env_file():
    """Create .env file from template if it doesn't exist"""
    if os.path.exists(".env"):
        print("⚠️  .env file already exists")
        return True
    
    if os.path.exists("env_template.txt"):
        try:
            with open("env_template.txt", "r") as template:
                with open(".env", "w") as env_file:
                    env_file.write(template.read())
            print("✅ Created .env file from template")
            print("📝 Please edit .env file with your Azure service details")
            return True
        except Exception as e:
            print(f"❌ Failed to create .env file: {e}")
            return False
    else:
        print("❌ env_template.txt not found")
        return False

def main():
    """Main setup function"""
    print("♈ Linda Goodman's Zodiac Guide Setup")
    print("=" * 40)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Set up virtual environment
    if not setup_virtual_environment():
        print("❌ Failed to set up virtual environment")
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        print("❌ Failed to install dependencies")
        sys.exit(1)
    
    # Create .env file
    if not create_env_file():
        print("❌ Failed to create .env file")
        sys.exit(1)
    
    print("\n🎉 Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Edit the .env file with your Azure service details")
    print("2. Activate the virtual environment:")
    if platform.system() == "Windows":
        print("   .\\labenv\\Scripts\\activate")
    else:
        print("   source labenv/bin/activate")
    print("3. Run the zodiac guide:")
    print("   python rag-app.py")
    print("\n📖 See README.md for detailed setup instructions")

if __name__ == "__main__":
    main() 