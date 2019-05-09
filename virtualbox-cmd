import os
import sys 
from argparse import ArgumentParser

parser = ArgumentParser(prog='virtualbox-cmd cli',
                        description='VirtualBox commandline - programa para manipular hosts virtuais',
                        fromfile_prefix_chars='@')
parser.add_argument('-l', '--liga', type=str, 
                    action='append', help='Liga host no VirtualBox') #default=0)
parser.add_argument('-d', '--desliga', type=str, 
                    action='append', help='Desliga host no VirtualBox') #default=0)
parser.add_argument('-v', '--verbose', action='count',
                    help='Entenda o que estamos fazendo', default=0)
args = parser.parse_args()
# print(args)

def verbose(func):
    def _inner(liga, desliga):
        if args.verbose == 1:
            print(f'Estamos operando com {liga, desliga}')
        if args.verbose == 2:
            print(f'{func.__name__}({liga, desliga})')
        if args.verbose >= 10:
            print('Vá se danar com tanta verbosidade')
            exit()
        return func(liga, desliga)
    return _inner

@verbose
def host_existe(host_vm):
    cmd = '\"C:\\Program Files\\Oracle\\VirtualBox\\VBoxManage.exe\" list vms'
    cmd = os.popen(cmd).read() 
    cmd_lista = cmd.split('\"')
    if host_vm in cmd_lista:
        return True
    else:
        print(f'Host virtual {host_vm} não existe!')
        return False

@verbose
def host_is_ativo(host_vm):
    cmd = '\"C:\\Program Files\\Oracle\\VirtualBox\\VBoxManage.exe\" list runningvms'
    cmd = os.popen(cmd).read() 
    cmd_lista = cmd.split('\"')
    if host_vm in cmd_lista:
        print(f'Host virtual {host_vm} está ligado!!')
        return True
    elif host_existe(host_vm):
        print(f'Host {host_vm} está desligado')
        return False
    else:
        # Host nao existe 
        return False

@verbose
def lista_host_ativos():
    cmd = '\"C:\\Program Files\\Oracle\\VirtualBox\\VBoxManage.exe\" list runningvms'
    cmd = os.popen(cmd).read()
    print('\nLista de Hosts Virtuais Ativos:')
    print(cmd)

@verbose
def liga_host(*hosts_vms):
    for host_vm in hosts_vms:
        if host_existe(host_vm):
            if not host_is_ativo(host_vm):
                cmd = '\"C:\\Program Files\\Oracle\\VirtualBox\\VBoxManage.exe\" startvm ' + host_vm +' --type headless'
                myCmd = os.popen(cmd).read() 
                print(f'Host virtual {host_vm} está sendo ligado...')

@verbose
def desliga_host(*host_vms):
    for host_vm in host_vms:
        if host_existe(host_vm) and host_is_ativo(host_vm):
            print (f'\nHost virtual {host_vm} está sendo preparado para o desligamento...!!')
            cmd = '\"C:\\Program Files\\Oracle\\VirtualBox\\VBoxManage.exe\" controlvm ' + host_vm +' poweroff'
            myCmd = os.popen(cmd).read() 
            print(f'Host virtual {host_vm} foi desligado com sucesso!')

if __name__ == '__main__':
    operações = {'liga': 'liga',
                'desliga': 'desliga', 
                }
    # print(operações[args.operação](args.x, args.y))
