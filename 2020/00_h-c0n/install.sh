# Update repositories and install required dependencies
sudo apt update
sudo apt -y install git build-essential

# Clone and install radare2
git clone --depth=1 https://github.com/radareorg/radare2
./radare2/sys/install.sh

# Install required dependencies for r2frida
sudo apt -y install libzip-dev nodejs npm curl pkg-config

# Init radare2 package manager and install plugins
r2pm init
r2pm -ci r2frida
r2pm -ci r2dec

# Download Cutter and give exec perm
wget https://github.com/radareorg/cutter/releases/download/v1.10.0/Cutter-v1.10.0-x64.Linux.AppImage
chmod +x ./Cutter-v1.10.0-x64.Linux.AppImage
