sudo apt-get update -y

wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -

sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'

sudo apt update

sudo apt install jenkins -y


sudo apt-get update -y


sudo systemctl daemon-reload

sudo systemctl start jenkins

sudo systemctl enable nginx

sudo systemctl enable jenkins

sudo systemctl status jenkins

