#NB!
sudo password is vagrant

# Run this
vagrant up

with kubespray do the following

## Create cluster
ansible-playbook --user=vagrant -b --become-user=root -i inventory/vagrant/hosts.ini ./cluster.yml --ask-sudo-pass   


## Create gluster setup and enable pvc
ansible-playbook --user=vagrant -b --become-user=root -i inventory/vagrant/hosts.ini contrib/network-storage/glusterfs/glusterfs.yml --ask-sudo-pass


