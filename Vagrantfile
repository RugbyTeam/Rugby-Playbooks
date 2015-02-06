# Spawn VM's to test ansible configuration

Vagrant.configure "2" do |config|

    # MongoDB VM
    config.vm.define "MongoDB" do |db|
        db.vm.box = "ubuntu/trusty64"
        db.vm.provision "ansible" do |ansible|
            ansible.playbook = "site.yml"
            ansible.sudo = true
            ansible.groups = {
                "db" => ["MongoDB"]
            }
            ansible.extra_vars = {
                db_type: "MongoDB"
            }
        end
    end

end
