from random import randint
from time import sleep
from simple_chalk import chalk

print(chalk.blue('*'*30))
print(chalk.yellow('-------- Jokenpô Game --------'))
print(chalk.blue('*'*30))

print(chalk.blue('\nSuas opções:'))
print(chalk.yellow('\n[ 0 ] PEDRA'))
print(chalk.yellow('[ 1 ] PAPEL'))
print(chalk.yellow('[ 2 ] TESOURA'))

jogada_pc = randint(0,2)
if jogada_pc == '0':
    jogada_pc = 'PEDRA'
elif jogada_pc == '1':
    jogada_pc = 'PAPEL'
else:
    jogada_pc = 'TESOURA'

jogada = input(chalk.blue('\nQual a sua jogada? '))
if jogada == '0':
    jogada = 'PEDRA'
elif jogada == '1':
    jogada = 'PAPEL'
else:
    jogada = 'TESOURA'

for i in range(1):
    print(chalk.red('JO'))
    sleep(0.8)
    print(chalk.red('KEN'))
    sleep(0.8)
    print(chalk.red('PO!!!'))
    sleep(0.8)
print(chalk.red('-=-'*8))
print(chalk.blue('Jogador jogou: {}'.format(chalk.yellow(jogada))))
print(chalk.blue('Computar jogou: {}'.format(chalk.red(jogada_pc))))
print(chalk.red('-=-'*8))
if jogada == jogada_pc:
    print(chalk.yellow('EMPATE!'))
elif jogada == 'PEDRA' and jogada_pc == 'PAPEL':
    print(chalk.red('COMPUTADOR VENCE!'))
elif jogada == 'PEDRA' and jogada_pc == 'TESOURA':
    print(chalk.green('JOGADOR VENCE!'))
elif jogada == 'PAPEL' and jogada_pc == 'PEDRA':
    print(chalk.green('JOGADOR VENCE!'))
elif jogada == 'PAPEL' and jogada_pc == 'TESOURA':
    print(chalk.red('COMPUTADOR VENCE!'))
elif jogada == 'TESOURA' and jogada_pc == 'PEDRA':
    print(chalk.red('COMPUTADOR VENCE!'))
else:
    print(chalk.green('JOGADOR VENCE!'))
