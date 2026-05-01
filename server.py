import subprocess
import sys

def main():
    # أول سكربت
    subprocess.run([sys.executable, "DATA.py"])

    # تاني سكربت
    subprocess.run([sys.executable, "api.py"])

    # ثالث سكربت
    # subprocess.run([sys.executable, "AB.py"])

if __name__ == "__main__":
    main()