def install(*apps):
    print(type(apps))
    for app in apps:
        print(f'{app}')
    cmd = '\"C:\\Program Files\\Oracle\\VirtualBox\\VBoxManage.exe\" list vms'
    # cmd = popen(cmd).read()
    # cmd_lista = cmd.split('\"')
    # if host_vm in cmd_lista:
    #     # print(f'Host virtual {host_vm} existe!')
    #     return True
    # else:
    #     print(f'Host virtual {host_vm} não existe!')
    #     return False

'''
Referencias
https://www.edivaldobrito.com.br/instalar-google-chrome-no-ubuntu/
'''
install(
    'sudo sh -c \'echo \"deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main\" >> /etc/apt/sources.list.d/google.list\'', 
    'wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -',
    'sudo apt-get update',
    'sudo apt-get install google-chrome-stable'
    )

install(
    'wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | sudo apt-key add -',
    'wget -q https://www.virtualbox.org/download/oracle_vbox.asc -O- | sudo apt-key add -',
    'sudo add-apt-repository "deb http://download.virtualbox.org/virtualbox/debian bionic contrib"',
    'sudo apt update',
    'sudo apt install virtualbox-6.0'
    )