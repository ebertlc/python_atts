class aluno():
    #criar arquivo txt de alnunos
    def __init__(self, matricula, nome, curso):
        self.matricula = matricula
        self.nome = nome
        self.curso = curso
        self.arquivo = open('alunos.txt', 'a')
        self.arquivo.write(f'{self.matricula};{self.nome};{self.curso}\n')
        self.arquivo.close()

    #inserir aluno no arquivo txt
    def inserir_aluno(self, matricula, nome, curso):
        self.arquivo = open('alunos.txt', 'a')
        self.arquivo.write(f'; {matricula};{nome};{curso}\n')
        self.arquivo.close()

    #remover aluno do arquivo txt
    def remover_aluno(self, matricula):
        self.arquivo = open('alunos.txt', 'r')
        self.linhas = self.arquivo.readlines()
        self.arquivo.close()
        self.arquivo = open('alunos.txt', 'w')
        for linha in self.linhas:
            if linha.split(';')[0] != matricula:
                self.arquivo.write(linha)
        self.arquivo.close()
    #alterar aluno do arquivo txt
    def alterar_aluno(self, matricula, nome, curso):
        self.arquivo = open('alunos.txt', 'r')
        self.linhas = self.arquivo.readlines()
        self.arquivo.close()
        self.arquivo = open('alunos.txt', 'w')
        for linha in self.linhas:
            if linha.split(';')[0] != matricula:
                self.arquivo.write(linha)
            else:
                self.arquivo.write(f'{matricula};{nome};{curso}\n')
        self.arquivo.close()

    #listar alunos do arquivo txt
    def listar_alunos(self):
        self.arquivo = open('alunos.txt', 'r')
        self.linhas = self.arquivo.readlines()
        self.arquivo.close()
        return self.linhas
#criar menu
def menu():
    print('1 - Inserir aluno')
    print('2 - Remover aluno')
    print('3 - Alterar aluno')
    print('4 - Listar alunos')
    print('5 - Sair')
    opcao = int(input('Digite a opção desejada: '))
    return opcao

#criar obejto aluno
if (__name__ == '__main__'):
    aluno = aluno('matricula','nome', 'curso')
    opcao = menu()
    while opcao != 5:
        if opcao == 1:
            matricula = input('Digite o matricula do aluno: ')
            nome = input('Digite a nome do aluno: ')
            curso = input('Digite o curso do aluno: ')
            aluno.inserir_aluno(matricula, nome, curso)
        elif opcao == 2:
            matricula = input('Digite a matricula do aluno: ')
            aluno.remover_aluno(matricula)
        elif opcao == 3:
            matricula = input('Digite o matricula do aluno: ')
            nome = input('Digite a nome do aluno: ')
            curso = input('Digite o curso do aluno: ')
            aluno.alterar_aluno(matricula, nome, curso)
        elif opcao == 4:
            print(aluno.listar_alunos())
        else:
            print('Opção inválida')
        opcao = menu()