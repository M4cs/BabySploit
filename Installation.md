# Installation

Run:

```
sudo apt-get update
sudo apt-get install exploitdb netcat nmap php7.0 -y
wget http://owl.phy.queensu.ca/~phil/exiftool/Image-ExifTool-11.17.tar.gz
gzip -dc Image-ExifTool-11.17.tar.gz
cd Image-ExifTool-11.17
perl MakeFile.PL
make test
sudo make install
cd ..
sudo rm -rf Image-ExifTool-11.17
pip3 install -m requirements.txt --user
```
 
 This is all you need to run BabySploit