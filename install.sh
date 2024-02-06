# Install dependencies
echo "Installing dependencies"
pip3 install openai redis

dpkg-deb --root-owner-group --build ../AI-Terminal-Tool
sudo dpkg -i ../AI-Terminal-Tool.deb
