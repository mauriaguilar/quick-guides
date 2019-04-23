# KERNEL: COMPILE AND INSTALL

# Search stable kernel in:
www.kernel.org

# Download
wget -c https://cdn.kernel.org/pub/linux/kernel/v5.x/linux-5.0.8.tar.xz

# Show installed kernels:
uname -r

# The kernel are in /usr/src
ls /usr/src

# Show size. I need 100Mb in /boot and 5Gb en / to compile
du -hsc carpeta/

# Extract
tar xvf linux-5.0.8.tar.xz

# Move zipped folder
mkdir /var/kernel
mv linux-5.0.8 /var/kernel

# Show hardware info
lshw | less
dmidecode | less
lspci
lscpu
vmstat

# Delete previous configurations
make mrproper

# Open graphic tools to select the setting of my hardware
make menuconfig
# save config as .config file

# Compile the kernel
make

# Optional: Install modeles.
make modules_install

# Install:
make install

# Verify files created:
# initrd.img-*
# System-map-*
# vmlinuz-*
# config-*
# * version ej. 3.16.0
ls /boot/

# If initrd.img-* not exists, create it with:
mkinitramsfs -o /boot/ initrd.img-*

# Update grub menu:
update-grub

# Verify actual kernel version:
uname -r

# Reboot and select the new kernel
reboot

# Check errors
dmesg | grep -i error
dmesg | grep -i warning

# Verify kernels
ls /boot/
dpkg --get-selections | grep linux-image

# Uninstall previous kernel version
# ** arch
apt remove --purge linux-image-*-**

# Update grub
update-grub
