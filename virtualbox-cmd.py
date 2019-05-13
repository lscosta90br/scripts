"""Programa para interagir com o VirtualBox."""

from os import popen
from argparse import ArgumentParser

parser = ArgumentParser(prog='virtualbox-cmd cli',
                        description='VirtualBox commandline - programa para manipular hosts virtuais',  # NOQA
                        fromfile_prefix_chars='@')

parser.add_argument('operacao', choices=['liga', 'desliga', 'lista', 'lista_todos', 'ativo', 'existe'],
                    help='''
                    liga: Liga a(s) VM passada no parâmetro;
                    desliga: Desliga a(s) VM passada no parâmetro;
                    lista: Lista as VMs ativas;
                    lista_todos: Lista as VMs ligadas;
                    ativo: Verifica quais VMs estão ativas
                    existe: Verifica se VM existe;
                    ''')

parser.add_argument('--host', action='store', 
                    help='VM a ser manipulada no VirtualBox')

parser.add_argument('-v', '--verbose', action='count',
                    help='Entenda o que estamos fazendo', default=0)

args = parser.parse_args()


def verbose(func):
    """Decorador para verificar a verbosidade (-v)."""
    def _inner(*verb):
        if args.verbose == 1:
            print(f'Estamos operando com {args.operacao} {args.host}')
        if args.verbose == 2:
            print(f'{func.__name__}({args.host})')
        if args.verbose >= 10:
            print('Vá se danar com tanta verbosidade')
            exit()
        return func(*verb)
    return _inner

# windows
cmd_vboxmanage = '\"C:\\Program Files\\Oracle\\VirtualBox\\VBoxManage.exe\"'

#linux
# cmd_vboxmanage = '/usr/bin/vboxmanage'


@verbose
def host_existe(host_vm):
    """
    Verifica se a maquina virtual existe.

    args:
    host_vms - Nome da máquina virtual
    """
    cmd = cmd_vboxmanage + ' list vms'
    cmd = popen(cmd).read()
    cmd_lista = cmd.split('\"')
    if host_vm in cmd_lista:
        # print(f'Host virtual {host_vm} existe!')
        return True
    else:
        print(f'Host virtual {host_vm} não existe!')
        return False


@verbose
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


@verbose
def lista_host_ativos():
    """Lista máquinas virtuais ativas."""
    cmd =  cmd_vboxmanage +' list runningvms'
    cmd = popen(cmd).read()
    print('Lista de Hosts Virtuais Ativos:')
    return cmd

@verbose
def lista_todos_host():
    """Lista máquinas virtuais ativas."""
    cmd =  cmd_vboxmanage +' list vms'
    cmd = popen(cmd).read()
    print('Lista de todos os Hosts Virtuais:')
    return cmd


@verbose
def liga_host(*hosts_vms):
    """
    Liga a maquina virtual.

    args:
    host_vms - Nome da máquina virtual
    """
    # print(type(hosts_vms))
    # host
    for host_vm in hosts_vms:
        if host_existe(host_vm):
            if not host_is_ativo(host_vm):
                cmd = cmd_vboxmanage + 'startvm' + host_vm + ' --type headless'
                popen(cmd).read()
                print(f'Host virtual {host_vm} está sendo ligado...')
                # return f'Host virtual {host_vm} está sendo ligado...'


@verbose
def desliga_host(*host_vms):
    """
    Desliga a maquina virtual.

    args:
    host_vms - Nome da máquina virtual
    """
    print(type(host_vms))
    print(host_vms)
    for host_vm in host_vms:
        if host_existe(host_vm) and host_is_ativo(host_vm):
            print(f'Host virtual {host_vm} está sendo preparado para o desligamento...!!')
            cmd = cmd_vboxmanage + ' controlvm ' + host_vm + ' poweroff'
            print(f'desliga: {cmd}')
            popen(cmd).read()
            print(f'Host virtual {host_vm} foi desligado com sucesso!')
            # return f'Host virtual {host_vm} foi desligado com sucesso!'


if __name__ == '__main__':
    if args.operacao == 'liga':
        liga_host(args.host)

    if args.operacao == 'desliga':
        desliga_host(args.host)

    if args.operacao == 'lista' and args.host is None:
        lista_host_ativos()

    if args.operacao == 'ativo':
        host_is_ativo(args.host)

    if args.operacao == 'existe':
        host_existe(args.host)

    if args.operacao == 'lista_todos':
        host_existe(args.host)
