import subprocess
import sys
import shutil

def is_ollama_installed():
    return shutil.which("ollama") is not None

def install_ollama():
    print("Ollama not found. Installing via Homebrew...")
    try:
        # Ensure Homebrew is installed
        if shutil.which("brew") is None:
            print("Homebrew is not installed. Please install Homebrew first.")
            sys.exit(1)
        # Update Homebrew and install Ollama via cask
        subprocess.run(["brew", "update"], check=True)
        subprocess.run(["brew", "install", "--cask", "ollama"], check=True)
    except Exception as e:
        print(f"Failed to install Ollama: {e}")
        sys.exit(1)

def pull_gemma3_4b():
    print("Pulling gemma3:4b model...")
    try:
        subprocess.run(["ollama", "pull", "gemma3:4b"], check=True)
    except Exception as e:
        print(f"Failed to pull gemma3:4b model: {e}")
        sys.exit(1)

def start_ollama():
    print("Starting Ollama service...")
    try:
        subprocess.run(["ollama", "serve"], check=True)
    except Exception as e:
        print(f"Failed to start Ollama service: {e}")
        sys.exit(1)

if not is_ollama_installed():
    install_ollama()
else:
    print("Ollama is already installed.")

pull_gemma3_4b()
print("Starting Ollama...")
start_ollama()
print("Ollama is running with gemma3:4b model.")