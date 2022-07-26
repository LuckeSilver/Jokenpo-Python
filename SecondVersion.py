from ast import Break
from random import randint
from time import sleep
from simple_chalk import chalk

print(chalk.blue('*'*30))
print(chalk.yellow('-------- Jokenpô Game --------'))
print(chalk.blue('*'*30))

nome = input(chalk.yellow('Digite seu nome: '))
print(chalk.green(f'Seja muito bem vindo(a) {nome}!!'))
sleep(0.8)
print(chalk.yellow("Vamos começar!!"))
sleep(0.8)

escolhas = ('PEDRA', 'PAPEL', 'TESOURA')

print(chalk.blue('\nSuas opções:'))
print(chalk.yellow('\n[ 0 ] PEDRA'))
print(chalk.yellow('[ 1 ] PAPEL'))
print(chalk.yellow('[ 2 ] TESOURA'))

computador = randint(0,2)
jogar = 3
while True:
    try:
        jogador = int(input(chalk.blue('\nQual a sua jogada? ')))
        if jogador > 2 or jogador < 0:
            #Testa joga inválida
            print(chalk.red(f'{nome} FEZ UMA JOGADA INVÁLIDA!'))
            print(chalk.green('Tente novamente: '))
        else:
            print(chalk.red('JO'))
            sleep(0.8)
            print(chalk.red('KEN'))
            sleep(0.8)
            print(chalk.red('PO!!!'))
            sleep(0.8)

            #Printa o que foi jogado pelo computaro e pelo jogador
            print(chalk.red('-=-'*8))
            print(chalk.blue('Computar jogou: {}'.format(chalk.red(escolhas[computador]))))
            print(chalk.blue('{} jogou: {}'.format( chalk.yellow(nome),chalk.yellow(escolhas[jogador]))))
            print(chalk.red('-=-'*8))

            #Testa possibilidades
            if computador == jogador:
                print(chalk.yellow('EMPATE!'))
            elif computador == 0: #Computador jogou pedra
                if jogador == 1: #Jogador jogou papel
                    print(chalk.green(f'{nome} VENCEU!'))
                elif jogador == 2: #Jogador jogou tesoura
                    print(chalk.red('COMPUTADOR VENCEU!'))
            elif computador == 1: #Computador jogou papel
                if jogador == 0: #Jogador jogou pedra
                    print(chalk.red('COMPUTADOR VENCEU!'))
                elif jogador == 2: #Jogador jogou tesoura
                    print(chalk.green(f'{nome} VENCEU!'))
            else: #Computador jogou tesoura
                if jogador == 0: #Jogador jogou pedra
                    print(chalk.green(f'{nome} VENCEU!'))
                elif jogador == 1: #Jogador jogou papel
                    print(chalk.red('COMPUTADOR VENCEU!'))
            break
    except ValueError:
        print(chalk.red(f'{nome} FEZ UMA JOGADA INVÁLIDA!'))
        print(chalk.green('Tente novamente: '))