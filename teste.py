from os import popen

cmd_vboxmanage = '\"C:\\Program Files\\Oracle\\VirtualBox\\VBoxManage.exe\"'

def host_is_ativo(host_vm):
    """
    Verifica se a maquina virtual está ativa.

    args:
    host_vms - Nome da máquina virtual
    """
    cmd = cmd_vboxmanage + ' list runningvms'
    cmd = popen(cmd).read()
    cmd_lista = cmd.split('\"')
    if host_vm in cmd_lista:
        print(f'Host virtual {host_vm} está ligado!!')
        return True
    elif host_existe(host_vm):
        print(f'Host {host_vm} está desligado')
        return False
    else:
        print('Host nao existe')
        return False



def lista_host_ativos():
    """Lista máquinas virtuais ativas."""
    cmd =  cmd_vboxmanage + ' list runningvms'
    cmd = popen(cmd).read()
    print('Lista de Hosts Virtuais Ativos:')
    return cmd



def host_existe(host_vm):
    """
    Verifica se a maquina virtual existe.

    args:
    host_vms - Nome da máquina virtual
    """
    cmd = f'{cmd_vboxmanage} list vms'
    cmd = popen(cmd).read()
    cmd_lista = cmd.split('\"')
    if host_vm in cmd_lista:
        print(f'Host virtual {host_vm} existe!')
        return True
    else:
        print(f'Host virtual {host_vm} não existe!')
        return False


def liga_host(*hosts_vms):
    """
    Liga a maquina virtual.

    args:
    host_vms - Nome da máquina virtual
    """
    for host_vm in hosts_vms:
        if host_existe(host_vm):
            if not host_is_ativo(host_vm):
                cmd = cmd_vboxmanage + ' startvm ' + host_vm + ' --type headless'
                print(cmd)
                popen(cmd).read()
                print(f'Host virtual {host_vm} está sendo ligado...')
                # return f'Host virtual {host_vm} está sendo ligado...'

def lista_host_ativos():
    """Lista máquinas virtuais ativas."""
    cmd =  cmd_vboxmanage +' list runningvms'
    cmd = popen(cmd).read()
    print('Lista de Hosts Virtuais Ativos:')
    return cmd

def host_is_ativo(host_vm):
    """
    Verifica se a maquina virtual está ativa.

    args:
    host_vms - Nome da máquina virtual
    """
    cmd = cmd_vboxmanage + ' list runningvms'
    cmd = popen(cmd).read()
    cmd_lista = cmd.split('\"')
    if host_vm in cmd_lista:
        print(f'Host virtual {host_vm} está ligado!!')
        return True
    elif host_existe(host_vm):
        print(f'Host {host_vm} está desligado')
        return False
    else:
        print('Host nao existe')
        return False


host_is_ativo('eclipse820')
host_existe('eclipse820')
if host_existe('eclipse820') and host_is_ativo('eclipse820'):
    print('ok')
# liga_host('eclipse820')
# cmd_vboxmanage = '\"C:\\Program Files\\Oracle\\VirtualBox\\VBoxManage.exe\"'
# lista_host_ativos()
# host_existe('eclipse820')