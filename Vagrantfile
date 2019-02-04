# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"


Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

###  yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
# yum install python-pip
# pip install ansible
# yum install sshpass

    # node 1-6 is masters/nodes
    # Node 7,8 and 9 are gluster nodes hence the drives
    N = 9
    (1..N).each do |machine_id|
        #config.
        config.vm.define "node#{machine_id}" do |node|
            dataDisk = "./disk#{machine_id}.vdi"

            node.vm.provider "virtualbox" do |v|
                if machine_id >= 7 and machine_id <= 9 #machine_id >= 7 or machine_id == 8 or machine_id == 9
                    if not File.exists?(dataDisk)
                        v.customize ['createhd', '--filename', dataDisk, '--size', 10 * 1024]
                    end
    
                    v.customize ['storageattach', :id, '--storagectl', 'SATA Controller', '--port', 1, '--device', 0, '--type', 'hdd', '--medium', dataDisk]
                end
      


                v.memory = 2048
                v.cpus = 2
            
            end
            node.vm.box = "bento/ubuntu-16.04" #"bento/centos-7.4" #"bento/ubuntu-16.04"
            node.vm.hostname = "node#{machine_id}"
            node.vm.network "private_network", ip: "192.168.79.#{20+machine_id}"
            node.ssh.insert_key = false
            node.vm.provision "file", source: "~/.ssh/id_rsa.pub", destination: "/home/vagrant/.ssh/id_rsa.pub"
            node.vm.provision "shell", inline: "cat ~vagrant/.ssh/id_rsa.pub >> ~vagrant/.ssh/authorized_keys"
            
            end
    end
end
