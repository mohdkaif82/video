How to use Movepy on Ubuntu/linux
sudo apt install imagemagick
convert --version
sudo apt install graphicsmagick-imagemagick-compat
sudo apt install imagemagick-6.q16
sudo apt install imagemagick-6.q16hdri
cd /etc/
sudo chmod 777 -R ImageMagick-6/
cat /etc/ImageMagick-6/policy.xml | sed 's/none/read,write/g'> /etc/ImageMagick-6/policy.xml




______________________________________________________________________________________________________________________

How to install hindi font in ubuntu/linux
sudo apt-get install language-pack-gnome-hi
sudo apt-get install fonts-lohit-deva
gsettings set org.gnome.desktop.interface font-name 'Lohit Devanagari 11'
