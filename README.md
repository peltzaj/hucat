# hucat
Interview Submission of How Not To Code

#
# Issues - Jane's Checksum doesn't match what was provided "ed4ce371ae41c41a39a71bc5275eae02"
#
[vagrant@localhost ~]$ echo -n "2|Jane Doe|2015-05-13T14:36:00.451765" | md5sum 
9596b7614de851e0dd48419e9413f40e  -

#
# Usage initially
#
The "Vagrantfile" will create an instance and install basic applications as needed. It will create 
 a /var/flask directory and then pull from git. it will have ansible run itself locally to place the 
 flaskapp.py and the daemon script. it will then seed the mongodb.

#
# Repeated usage
#
Since this is a one-off with not a large deployment, the ansible hosts file was used, just run the playbook
 and it will stop the service, update the flaskapp, reseed the mongodb if the collection is gone, and start the service

     $ ansible-playbook -i "localhost," -c local /home/vagrant/flaskapp.yml

->in /etc/ansible/hosts
localhost ansible_connection=local


#
# testing
#
curl "http://localhost:18080/?uid=1&date=2015-06-25"

curl -H "Content-Type: application/json" -X POST -d '[{"uid": "1","name": "John Doe","date": "2015-05-12T14:36:00.451765","md5checksum": "f6903e9838720c98ed4098d842264d7c"}]' http://localhost:18080/
curl -H "Content-Type: application/json" -X POST -d '[{"uid": "1","name": "John Doe","date": "2015-05-12T14:36:00.451765","md5checksum": "f6903e9838720c98ed4098d842264d7c"},{"uid": "2","name": "Jane Doe","date": "2015-05-13T14:36:00.451765","md5checksum": "9596b7614de851e0dd48419e9413f40e"}]' http://localhost:18080/
curl -H "Content-Type: application/json" -X POST -d '[{"uid": "3","name": "Anthony Peltz","date": "2016-06-25T14:36:00.451765","md5checksum": "cf1d28a96777f65cbcd447b126db92ad"}]' http://localhost:18080/