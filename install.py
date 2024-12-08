import os
import subprocess
import sys

def install_requirements():
    """Install dependencies from requirements.txt."""
    print("Memeriksa dan menginstal dependensi...")
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("Semua dependensi berhasil diinstal.")
    except subprocess.CalledProcessError as e:
        print(f"Terjadi kesalahan saat menginstal dependensi: {e}")
        sys.exit(1)

def main():
    # Cek apakah file requirements.txt ada
    if not os.path.exists('requirements.txt'):
        print("File requirements.txt tidak ditemukan!")
        sys.exit(1)
    
    # Instal dependensi
    install_requirements()

if __name__ == '__main__':
    main()