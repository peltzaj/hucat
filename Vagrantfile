$script = <<SCRIPT
yum clean all
yum install epel-release -y
yum install ansible python-flask python-jinja2 mongodb mongodb-server pymongo git -y
chkconfig mongod on
service mongod start
mkdir /var/flask
chmod -R 755 /var/flask
git clone https://github.com/peltzaj/hucat.git hucat
chown -r vagrant.vagrant hucat
ansible all -i "localhost," -c local /home/vagrant/flaskapp.yaml
SCRIPT

Vagrant.configure("2") do |config|
  config.vm.box = "harvardcatalyst/centos-6-core"
  config.vm.network "forwarded_port", guest: 8080, host: 8080
  config.vm.synced_folder ".", "/vagrant", disabled: true
  config.vm.provision "shell", inline: $script
end
