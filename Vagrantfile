$script = <<SCRIPT
yum clean all
yum install epel-release -y
yum install ansible python-flask python-jinja2 mongodb mongodb-server pymongo git -y
yum update -y
chkconfig mongod on
service mongod start
git clone https://github.com/peltzaj/hucat.git hucat
chown -R vagrant.vagrant /home/vagrant/hucat
echo "localhost ansible_connection=local" >> /etc/ansible/hosts
ansible-playbook /home/vagrant/hucat/flaskapp.yml
SCRIPT

Vagrant.configure("2") do |config|
  config.vm.define 'flask' do |cs|
    cs.vm.box = "harvardcatalyst/centos-6-core"
    cs.vm.network "forwarded_port", guest: 8080, host: 8080
    cs.vm.synced_folder ".", "/vagrant", disabled: true
    cs.vm.provision "shell", inline: $script
  end
end
