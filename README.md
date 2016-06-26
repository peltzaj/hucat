# hucat
Anthony Peltz Submission - ~6 hours while camping total.

#
# Complication 
#
In testing, Jane's checksum didn't match what was provided "ed4ce371ae41c41a39a71bc5275eae02"

  $ echo -n "2|Jane Doe|2015-05-13T14:36:00.451765" | md5sum 
  9596b7614de851e0dd48419e9413f40e  -

#
# Usage initially
#
The "Vagrantfile" will create an instance and install basic applications as needed. It will pull 
from git. It will have ansible run itself locally to place the flaskapp.py, a daemon script and 
will seed the mongodb database, if it is empty. Finally, ansible will start the service.

#
# Repeated usage
#
Since this is a one-off with not a large deployment, the ansible hosts file was configured only for localhost. Just run the playbook
and perform a git pull, stop the service, update the flaskapp, reseed the mongodb if the collection is gone, and start the service.

  $ ansible-playbook /home/vagrant/hucat/flaskapp.yml

#
# Testing
#
In testing the application, I tested multiple GET strings generally of the form below, and received json responses with "count".

  $ curl "http://localhost:8080/?uid=1&date=2015-06-25"

And multiple json POST commands (below), and received json responses that told me if the data was successfully added or not.

  $ curl -H "Content-Type: application/json" -X POST -d '[{"uid": "1","name": "John Doe","date": "2015-05-12T14:36:00.451765","md5checksum": "f6903e9838720c98ed4098d842264d7c"}]' http://localhost:8080/

  $ curl -H "Content-Type: application/json" -X POST -d '[{"uid": "1","name": "John Doe","date": "2015-05-12T14:36:00.451765","md5checksum": "f6903e9838720c98ed4098d842264d7c"},{"uid": "2","name": "Jane Doe","date": "2015-05-13T14:36:00.451765","md5checksum": "9596b7614de851e0dd48419e9413f40e"}]' http://localhost:8080/

  $ curl -H "Content-Type: application/json" -X POST -d '[{"uid": "3","name": "Anthony Peltz","date": "2016-06-25T14:36:00.451765","md5checksum": "cf1d28a96777f65cbcd447b126db92ad"}]' http://localhost:8080/

#
# Future Work
#
1. Better error handling all around parsing for the flask application
2. More stable deployment mechanism that can tell the difference between revisions, why replace if you do not have to.
3. Optimize for remote deployments - 
     - Modification to the NAT (local deployer style for the VM)
     - Have the daemon NOT run as 'root'
     - Configure code to use a centralized mongodb, instead of local instance

