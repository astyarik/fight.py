import random

health = 10
enemy = 10
atc = 0

def attack():
    global enemy
    hit = random.randint(1, 3)
    enemy -= hit
    print(f"Ты нанес {hit} урона!")

def damage():
    global health
    atc = random.randint(1, 3)
    health -= atc
    print(f"Ты потерял {atc} жизней!")

def defence():
	print("Вы поставили перед собой щит!")
	
def heal():
	global health
	heall = random.randint(1, 3)
	health += heall
    
	if health > 10:
		health = 10
		print("Ой-ой! Достигнуто максимальное количество жизней!")
	else:
		print(f"Ты восстановил {heall} жизней!")
		
def regen():
    global enemy
    regenn = random.randint(1, 3)
    enemy += regenn
    print(f"Враг восстановил {regenn} жизней!")
 
def pair():
	 global passed
	 print("Враг защищается!")
    
print("""
	░░░░░░░░░░░░▄▐
	░░░░░░▄▄▄░░▄██▄
	░░░░░▐▀█▀▌░░░░▀█▄
	░░░░░▐█▄█▌░░░░░░▀█▄
	░░░░░░▀▄▀░░░▄▄▄▄▄▀▀
	░░░░▄▄▄██▀▀▀▀
	░░░█▀▄▄▄█░▀▀
	░░░▌░▄▄▄▐▌▀▀▀
	▄░▐░░░▄▄░█░▀▀
	▀█▌░░░▄░▀█▀░▀
	░░░░░░░▄▄▐▌▄▄
	░░░░░░░▀███▀█░▄
	░░░░░░▐▌▀▄▀▄▀▐▄
	░░░░░░▐▀░░░░░░▐▌
	░░░░░░█░░░░░░░░█
	░░░░░▐▌░░░░░░░░░█
	░░░░░█░░░░░░░░░░▐▌ """)
	
while True:
	while health > 0 and enemy > 0:
		
		enemy_ch = random.randint(1, 3)
		
		choise = int(input(f"\n\nНа вас напал скелет!\nВаши жизни - {health}, его - {enemy}\nПожалуйста, выберете действие:\n1. Атака, 2. Защита, 3. Лечение\n>>> "))
		if choise == 1:
			if enemy_ch == 3:
				print("Атака парирована!")
			else:
				attack()
				
		if choise == 2:
			defence()
			
		if choise == 3:
			heal()
		
		if enemy_ch == 1:
			if choise == 2:
				print("Урон успешно отражен!")
			else:
				damage()
		
		if enemy_ch == 2:
			regen()
			if enemy > 10:
				print("Враг попытался излечиться, но он достиг максимальное количество жизней!")
				enemy = 10
				
		if enemy_ch == 3:
			pair()
				
	if health <= 0:
		print("Увы! Вы проиграли!")
	
	if enemy <= 0:
		print("Ура! Вы победили!")

	answer = int(input("Хотите ещё раз?\n1. Да\n2. Нет\n>>> "))

	if answer == 2:
		print("Ну что-ж, пока!")
		break 
		
	if answer == 1:
		health = 10
		enemy = 10
		
		print("*Би-и-п! Одно новое сообщение!*")
		print("""
		╭━━━━━━━━━━━━━╮
		┃　　 ● ══ 　 ┃
		┃█████████████┃
		┃█████████████┃
		┃█████████████┃
		┃█тебе конец █┃
		┃█ за тобой ██┃
		┃█ уже едут ██┃
		┃█████████████┃
		┃█████████████┃
		┃  　  ○  　  ┃
		╰━━━━━━━━━━━━━╯ """)
		print("Скелет решил взять реванш!")
