from time import sleep

# =-=-=-=-=-= FUNCÕES DE INTERFACE =-=-=-=-=-=

# Inicia o sistema.


def iniciarsistema():
    arq = 'Dados dos clientes.txt'

    if not arquivoexiste(arq):
        criararquivo(arq)

    while True:
        resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
        if resposta == 1:
            lerarquivo(arq)
        elif resposta == 2:
            cabecalho('NOVO CADASTRO')
            nome = input('Nome: ')
            idade = leiaint('Idade: ')
            cadastrar(arq, nome, idade)
        elif resposta == 3:
            cabecalho('Programa encerrado. Até logo!')
            break
        else:
            print(f'{Cor.vermelho}Opção invalida. Tente novamente.{Cor.base}')
        sleep(2)

# Cria um cabeçalho com texto personalizado.


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

# Uma verificação para aceitar apenas numeros inteiros em um imput do usuário.


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'{Cor.vermelho()}ERRO: Por favor digite um número inteiro válido.{Cor.base()}')
            continue
        except KeyboardInterrupt:
            print(f'{Cor.vermelho()}Usuário preferiu não digitar um número.{Cor.base()}')
            return 0
        else:
            return n

# Cria uma linha com tamanho personalizável.


def linha(tam=42):
    return '-' * tam


# Exibe um menu com opções para o usuário.


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{Cor.amarelo()}{c}{Cor.base()} - {Cor.azulescuro()}{item}{Cor.base()}')
        c += 1
    print(linha())
    opc = leiaint(f'{Cor.verde()}Sua Opção: {Cor.base()}')
    return opc

# Uma forma mais simples de editar as cores dos textos (Cor.cor_que_deseja).


class Cor:
    def __init__(self):
        pass

    def base(self=0):
        return '\033[m'

    def vermelho(self=0):
        return '\033[31m'

    def verde(self=0):
        return '\033[32m'

    def amarelo(self=0):
        return '\033[33m'

    def azulescuro(self=0):
        return '\033[34m'

    def roxo(self=0):
        return '\033[35m'

    def azulclaro(self=0):
        return '\033[36m'

    def cinza(self=0):
        return '\033[37m'

    def branco(self=0):
        return '\033[97m'


# =-=-=-=-=-= FUNÇÕES PARA ARQUIVOS =-=-=-=-=-=

# Verifica se o arquivo em questão já existe.


def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

# Cria um arquivo para registrar os cadastros.


def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print(f'{Cor.vermelho()}ERRO ao criar arquivo.{Cor.base()}')
    else:
        print(f'{Cor.azulclaro()}Arquivo {nome} criado.{Cor.base()}')

# Lê o arquivo e mostra as informações dos usuários já cadastrados.


def lerarquivo(nome):
    a = 0
    try:
        a = open(nome, 'rt')
    except:
        print(f'{Cor.vermelho()}Erro ao ler arquivo.{Cor.base()}')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for pessoa in a:
            dado = pessoa.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


# Cadastra um novo usuario.


def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('ERRO na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro ao escrever no arquivo.')
        else:
            print(f'Novo registro de {nome} criado!')
            a.close()
