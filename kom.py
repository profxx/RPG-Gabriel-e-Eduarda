from time import sleep
print('--------------------------------------------------------')
print('          BEM VINDO AO THE KING OF MONSTERS')
print('--------------------------------------------------------')
sleep(2)
print()
print()
input('Precione enter para começar!')

#menu de escolha

nome = input('Digite o nome do seu personagem: ')
print(f'{nome}! Ótima escolha!')

print('Agora que já escolheu personagem vamos começar.')
print()
input('Precione enter para continuar!')
print()
print('Oh não(☉｡☉)!')
sleep(3)
print('Um monstro acaba de aparecer,você deve derrota-lo!')
print('Ou ele vai destruir todo o vilarejo(●__●).')
sleep(3)
#primeira batalha

print('''Escolha de que forma pretende atacar o mostro.
        
--------------------
{1}Força Mágica
dano:-260

{2}Lança Divina 
dano:-300

{3}Poção petrificadora
dano:-250

{4}Combate corpo a corpo rápido
dano:-210

MONSTRO: 350 HP
VOCÊ: 100 HP

''')

#ataque
a1 = 260
a2 = 300
a3 = 250
a4 = 210
atq = input('Escolha seu ataque: ')
if atq == '1':
	print(f'O monstro agora está com {350 - a1} de HP. Você recebeu forte ataque e está com 70HP.')
elif atq == '2':
	print(f'O monstro está com {350 - a2}HP. Você foi atacado e está com 80HP.')
elif atq == '3':
	print(f'O monstro está com {350 - a3}HP. Você recebeu uma pancada e está com 75HP.')
elif atq == '4':
	print(f'O monstro está com {350 - a4}HP')
print('ELE ESTÁ FRACO, ATAQUE-O COM FORÇA TOTAL!!')
print('''Escolha seu ataque:
--------------------
{1}Força Mágica
dano:-260

{2}Lança Divina 
dano:-300

{3}Poção petrificadora
dano:-250

{4}Combate corpo a corpo rápido
dano:-210

{5}Fugir
		''')
atq2 = int(input('Escolha seu ataque: '))

if atq2 == 5:
	print('Ele te alcançou')
	print()
	sleep(3)
	print('GAME OVER')
	quit()
else:
	print('ELE FOI DERROTADO!')
sleep(3)
print('')
sleep(2)
input(' Precione enter para continuar.')
print()
L1 = 'Praça das Pétalas'
L2 = 'Lago dos Desejos'
L3 = 'Casa da Lua Branca'
L4 = 'Ponte mil Olhares'
print()

print('Parabéns pela vitória!')
print()
sleep(3)
print('Agora é hora de descançar um pouco.')
print('Vamos dar uma volta pra você conhecer o vilarejo')
print()
#passeio
print('''Qual lugar você quer descansar? 

--------------------
{1}Praça das Pétalas
{2}Lago dos Desejos
{3}Casa da Lua Branca
{4}Ponte dos Mil Olhares

''')

escolha_do_usuário = int(input('Digite o número escolhido: '))
if escolha_do_usuário  == 1:
  print('Ótima escolha,a Praça das Pétalas tem lindas flores.')
elif escolha_do_usuário  == 2:
  print('Uau, escolheu um lugar perfeito pra comçar o tour!')
  print('No Lago dos Desejos tem lindos peixes dourados.')
elif  escolha_do_usuário  == 3:
  print('Escolheu bem,a Casa da Lua Branca serve ótimos bolinhos de arroz com suco de Maracujá!')
elif  escolha_do_usuário  == 4:
  print('Fez uma excelente escolha, a Ponte dos Mil Olhares tem as melhores vistas do vilarejo!')
sleep(1)
print('.')
sleep(1)
print('.')
sleep(1)
print('.')
sleep(1)
print('Está na hora de partir... ')
sleep(1)
print()

#Essa parte é depois que o usuário descansou o lugar

input('Precione enter pra continuar.')

print('')

print('Olha encotramos um Baú de Ouro!')
input('Escreva as palavras mágicas para abri-lo: ')
print('')
print('O baú foi aberto. Parabéns!')
sleep(2)
print('''* Recursos novos encotrados dentro do baú *
--------------------
1-Sopa Revitalizadora
2-Capa da Invisibilidade
3-Nova skin
4-Poeira da Sorte
5-Armadura de Diamante
--------------------
''')
print()
sleep(3)
input('Para adquir os recursos do Baú de Ouro da sorte, escreva a seguir REIVINDICAR: ')
print('')
print()
print('Recursos resgatados com sucesso!')
print()
print('Deseja utilizar sua nova skin?')

#resposta sobre a skin

resposta = input('sim ou não? ')
if resposta == 'sim':
	print('UAU, esse novo look está incrível!')
else:
	print('Tudo bem!')
sleep(3)
print()
print('-UMA MAÇÃ! Veio em uma boa hora.')
print()
sleep(2)
print('* AAAAAARRRRGH *')
print()
print('-O QUE FOI ISSO???')
print('-QUEM É VOCÊ? POR QUE NÃO ESTOU SENTINDO MEUS PODERES??')
print()
sleep(4)
print('* Você é tão burro que chega a ser patético')
print('* Imagino que essa maçã drenadora de magia estava maravilhosa, e obrigado pelos poderes, a propósito.')
print()
sleep(4)
print('-NÃO PODE SER, EU HAVIA TE MATADO. VOLTE AQUI!')
print()
sleep(4)
print()
print('* O monstro sumiu *')
print()
sleep(4)
print('-E agora? O que eu faço?')
print()
sleep(4)
print()
print('* Algo se aproxima *')
print()
sleep(4)
print('-UM ORK!!!')
print('-Sem meus poderes eu fico vulnerável.')
#lutar ou fugir
luta_foge = input('Lutar ou fugir?')
print()
if luta_foge == 'lutar':
	print('Você arremessa uma pedra no ork e ele se enfurece.')
	print('Uma madeira! Isso deve servir.')
	print('POW!')
	print('* O ork desmaiou e você fugiu.')
else:
	print('Você não conseguiu fugir e o ork te alcançou.')
	print()
	print('* Você arremessa uma pedra no ork e ele se enfurece *')
	print()
	print('Uma madeira! Isso deve servir.')
	print()
	print('POW!')
	print()
	print('* O ork desmaiou e você fugiu.')
print('')
print('-UOU, isso foi perigoso. Preciso de uma nova espada.')
print('-Vou até a cidade conseguir uma nova arma.')
print()
print('-Antes de partir vou usar minha sopa revitalizadora.')
print()
sleep(3)
print('AAAAAH, que delícia!')
print()
print('.')
sleep(2)
print('.')
sleep(3)
print('.')
sleep(3)
print('Depois de longos dias a cidade já pode ser vista.')
print('')
print('Uau essa cidade é linda!')
print()
sleep(1)
print('.')
sleep(1)
print('.')
sleep(1)
print('-Boa tarde! O senhor poderia me vender uma espada?')
sleep(5)
print()
print('Claro! Custa 1500 dólares.')
print()
sleep(5)
print('-Eu não tenho dinheiro :(')
print()
print()
sleep(5)
print('Não posso fazer nada por você, vá arranjar um emprego!')
print()
sleep(4)
print('BOOM!')
print('')
sleep(3)
print('O QUE FOI ISSO???????')
print('')
sleep(3)
print('Toma jovem, leve essa espada e veja o que está acontecendo. RÁPIDO!')
print('* Estrondos altíssimos *')
print()
sleep(3)
print('')
print('-SEU MONSTRO ASQUEROSO! PARE JÁ AGORA!')
print()
sleep(3)
print('Ou o que? Perdeu seus poderes, vai ter a coragem de me enfrentar?')
print('')
print('O que deseja fazer?')
#decisão
dec = input('enfrentar ou fugir?')
if dec == 'enfrentar':
	print(f'Foi um ato de coragem, mas infelizmente {nome} não aguentou (●__●)!')
	print('GAME OVER!')
	quit()
else:
	print('Foi um ato inteligente!')
print()
sleep(1)
print(f'Se sentindo um covarde, {nome} vai em direção as montanhas em busca de treinamento.')
print()
sleep(4)
print('.')
sleep(4)
print('.')
sleep(4)
print('.')
sleep(4)
print('.')
sleep(2)
print(f'Longos anos de ataques de capangas do monstro assombraram a cidade, enquanto {nome} se preparava para a batalha final........... ')
print()
print()
print()
print()
print()
print()
print(f'{nome} agora se sente preparado e decide enfrentar seu destino a ser o Rei Dos Monstros!')
print()
print()
print()
print()
sleep(2)
print(f'{nome} * chegou a cidade... *')
print('-VENHA ME ENFRENTAR!!')
print()
sleep(4)
print('E você acha que tem alguma chance contra mim, ser insignificante?')
input(': ')
print()
print()
print()
print('Você sente um poder incontrolável fluindo em seu corpo.')

#batalha final
print(f'O que {nome} irá fazer?')
#o que ele vai fazer
o_que_fazer = input('Atacar ou dizer algo? ')
if o_que_fazer == 'dizer algo':
	input('Diga: ')
	print()
else:
	input('Digite "atacar" para acertar o oponente: ')
	print('Você atacou com sua espada mas o monstro nem se moveu!')
print()
print()
print('O monstro revidou e você ficou só o pó da rabiola!')
print()
sleep(4)
input('Digite "atacar" para acertar o oponente: ')
print()
print('Você ataca de novo e o processo se repete.')
print()
sleep(3)
print('ELE ESTÁ PREPARANDO UM ATAQUE, ESQUIVE IMEDIATAMENTE!')
esquivar = input('Digite "esquivar" para não ser acertado: ')
if esquivar == 'esquivar':
	print('Ufa! Foi por pouco!')
else:
	print('GAME OVER')
	quit()
print()
sleep(3)
print('ELE ESTÁ ATACANDO DE NOVO!!!')
esquivar2 = input('Digite "esquivar" para não ser acertado: ')
if esquivar == 'esquivar':
	print('Ufa! Dessa vez passou mais perto!')
else:
	print('Você morreu.')
	print('GAME OVER!')
	quit()
print()
sleep(2)
print(f'{nome} quase não se aguenta mais em pé.')
print()
print()
sleep(3)
print('Aquele poder incontrolavel volta.')
print()
print()
sleep(3)
print('BOOM!')
print('Raios saem de seu corpo.')
print('SINTA MINHA FÚRIAAAAAAA!!!!')
print()
sleep(3)
print('O smurf acha que vai me atingir com essas faíscas?')
ataque_final = input('Digite "ataque" para dispertar seu poder: ')
if ataque_final == 'ataque':
	print('O monstro cai sem reação.')
else:
	print('Ele te atacou.')
	print('GAME OVER!')
	quit()
print('')
print('O MONSTRO ESTÁ ENFRAQUECIDO! ATAQUE-O COM TUDOO!!!!!!!')
ataque_final2 = input('Digite "atacar": ')
if ataque_final2 == 'atacar':
	print('PARABÉNS HERÓI!! VOCÊ DERROTOU O TENEBROSO MONSTRO!')
else:
	print('Ele levantou e te matou.')
	print('GAME OVER!')
	quit()
print('')
sleep(3)
print(f'{nome} agora se tornou o herói da cidade.')
print('Ganhou até uma estátua em sua homenagem.')
sleep(3)
print('★★★★★★★★★★★★★★★★★★')
sleep(3)
print('PARABÉNS GUERREIRO/GUERREIRA! VOCÊ FINALIZOU E SE TORNOU O REI/RAINHA DOS MONSTROS!')
print('')
print('Obrigado por jogar ^-^ !')
print()
print()
sleep(2)
print('Desenvolvido por: Gabriel e Eduarda.')
print('Apoiado por: Alexandre.')
sleep(10)
