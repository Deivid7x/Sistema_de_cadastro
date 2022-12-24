from time import sleep

# =-=-=-=-=-= FUNCÕES DE INTERFACE =-=-=-=-=-=

# Inicia o sistema.


def iniciarsistema():
    arq = 'Dados dos clientes.txt'

    if not arquivoexiste(arq):
        criararquivo(arq)

    while True:
        resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Atualizar dados de usuário', 'Apagar usuário cadastrado', 'Sair do sistema'])
        if resposta == 1:
            lerarquivo(arq)

        elif resposta == 2:
            cabecalho('NOVO CADASTRO')
            nome = str(input('Nome: ')).strip().lower()
            cadastrar(arq, nome)

        elif resposta == 3:
            cabecalho('ATUALIZAR DADOS')
            nome = str(input(f'{Cor.azulescuro()}Nome:{Cor.base()} ')).strip().lower()
            atualizar_dados(arq, nome)

        elif resposta == 4:
            cabecalho('APAGAR USUÁRIO')
            nome = str(input(f'{Cor.azulescuro()}Nome:{Cor.base()} ')).strip().lower()
            apagar_usuario(arq, nome)

        elif resposta == 5:
            cabecalho(f'{Cor.vermelho()}Programa encerrado. Até logo!{Cor.base()}')
            break

        else:
            print(f'{Cor.vermelho()}Opção inválida. Tente novamente.{Cor.base()}')
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
        identificacao = 'Nome', 'Nascimento'
        print(f'{Cor.roxo()}{identificacao[0]:<30}{identificacao[1]:>3}{Cor.base()}')
        for pessoa in a:
            dado = pessoa.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0].title():<30}{dado[1]:>3}')
    finally:
        a.close()


# Cadastra um novo usuário.


def cadastrar(arq, nome='Desconhecido'):
    try:
        with open(arq, 'a') as arquivo:
            dia = leiaint(f'{Cor.verde()}Dia de nascimento:{Cor.base()} ')
            mes = leiaint(f'{Cor.verde()}Mês de nascimento:{Cor.base()} ')
            ano = leiaint(f'{Cor.verde()}Ano de nascimento:{Cor.base()} ')
            if dia < 10:
                dia = f'0{dia}'
            if mes < 10:
                mes = f'0{mes}'
            data_nascimento = f'{dia}/{mes}/{ano}'
            arquivo.write(f'{nome};{data_nascimento}\n')
    except Exception as e:
        print(f'{Cor.vermelho()}Erro ao cadastrar pessoa: {e}{Cor.base()}')
    else:
        print(f'{Cor.verde()}Novo registro de {nome.title()} adicionado!{Cor.base()}')
        arquivo.close()


# Deleta o usuário cadastrado.

def apagar_usuario(arquivo, nome):
    with open(arquivo, 'r') as arq:
        dados = arq.readlines()
    
    encontrado = False
    with open(arquivo, 'w') as arq:
        for dado in dados:
            if dado.split(';')[0] != nome:
                arq.write(dado)
            else:
                encontrado = True

    if not encontrado:
        print(f'{Cor.vermelho()}Usuário não encontrado{Cor.base()}')
    else:
        print(f'{Cor.verde()}Usuário {Cor.vermelho()}{nome.title()}{Cor.verde()} deletado com sucesso!{Cor.base()}')


# Atualiza os dados do usuário

def atualizar_dados(arq, nome):
    try:
        with open(arq, 'r') as arquivo:
            linhas = arquivo.readlines()
    except Exception as e:
        print(f'{Cor.vermelho()}Erro ao ler arquivo: {e}{Cor.base()}')
    else:
        encontrado = False
        with open(arq, 'w') as arquivo:
            for linha in linhas:
                dado = linha.split(';')
                if dado[0] == nome:
                    encontrado = True
                    dia = leiaint(f'{Cor.azulescuro()}Dia de nascimento:{Cor.base()} ')
                    mes = leiaint(f'{Cor.azulescuro()}Mês de nascimento:{Cor.base()} ')
                    ano = leiaint(f'{Cor.azulescuro()}Ano de nascimento:{Cor.base()} ')
                    if dia < 10:
                        dia = f'0{dia}'
                    if mes < 10:
                        mes = f'0{mes}'
                    data_nascimento = f'{dia}/{mes}/{ano}'
                    arquivo.write(f'{nome};{data_nascimento}\n')
                else:
                    arquivo.write(linha)
        if not encontrado:
            print(f'{Cor.vermelho()}Registro não encontrado.{Cor.base()}')
        else:
            print(f'{Cor.verde()}Registro de {nome.title()} atualizado com sucesso!{Cor.base()}')
        arquivo.close()

