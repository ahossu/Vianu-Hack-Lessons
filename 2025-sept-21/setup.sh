#!/bin/bash

# chmod +x setup.sh
# su -
# ./setup.sh

set -e
echo "=================================================="
echo "Installing Command-Line Tools for WSL"
echo "=================================================="

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

if [[ $EUID -ne 0 ]]; then
   print_error "This script must be run as root (use sudo)"
   exit 1
fi

apt update -y
apt upgrade -y

apt install -y curl wget gcc gdb python3 python3-pip python3-dev build-essential make git vim nano

apt install -y tcpdump netcat-openbsd nmap net-tools

apt install -y binwalk exiftool file xxd tree less grep

apt install -y strace ltrace objdump readelf nm ldd unzip p7zip-full jq zip

pip3 install --break-system-packages requests pwntools pycryptodome Pillow numpy 2>/dev/null || {
    print_warning "Some Python packages failed to install. Try installing manually if needed."
}

chmod +s /usr/bin/tcpdump || print_warning "Could not set tcpdump permissions (normal in WSL)"

echo ""
echo "=================================================="
print_status "Installation completed successfully!"
echo "=================================================="
