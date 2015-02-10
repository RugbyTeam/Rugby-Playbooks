# Spawn VM's to test ansible configuration

Vagrant.configure "2" do |config|  
    
    config.vm.define "MongoDB" do |db|
        db.vm.box = "ubuntu/trusty64"
        db.vm.provision "ansible" do |ansible|
            ansible.playbook = "site.yml"
            ansible.sudo = true
            ansible.groups = {
               "db" => ["mongo"]
            }
            ansible.extra_vars = {
                db_type: "mongo"
            }
        end
    end
    
    config.vm.define "UCRCareer" do |app|
        app.vm.box = "ubuntu/trusty64"
        app.vm.provision "ansible" do |ansible|
            ansible.playbook = "site.yml"
            ansible.sudo = true
            ansible.groups = {
               "app" => ["node"]
            }
            ansible.extra_vars = {
                app_type: "node"
            }
        end
    end
    
end