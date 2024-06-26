# Python
import subprocess

def fix_jinja2_import_error():
    try:
        import jinja2
        print(f"Jinja2 version: {jinja2.__version__}")
    except ImportError:
        print("Jinja2 is not installed. Installing...")
        subprocess.check_call(["pip", "install", "jinja2"])
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Uninstalling Jinja2...")
        subprocess.check_call(["pip", "uninstall", "-y", "jinja2"])
        print("Reinstalling Jinja2...")
        subprocess.check_call(["pip", "install", "jinja2"])

fix_jinja2_import_error()