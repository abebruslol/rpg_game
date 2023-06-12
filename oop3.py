import random
import time 
class Player:
    def __init__(self,player_name,player_hp,player_dmg):
        self.name = player_name
        self.hp = player_hp
        self.dmg = player_dmg
        self.lvl = 1
        self.exp = 0

    def lvl_up(self):
        self.lvl += 1
        self.exp = 0
        self.hp += self.lvl * 10
        self.dmg += self.lvl * 5
        print(f'Поздравляю!У вас новый уровень: {self.lvl}')
        
    
    def create_weapon(self):
        weapon_dmg = 10
        weapon_rare = ['Обычная','Редкая','Эпическая','Легендарная','Мифическая']
        weapon_chance = [20,15,10,5,1]
        rare = random.choices(weapon_rare,weights=weapon_chance,k=1)
        weapon_type = ['Меч Абобы','Посох','Лук']
        weapon = random.choice(weapon_type)
        if rare[0] == weapon_rare[0]:
            weapon_dmg += weapon_dmg * 1
            self.dmg += weapon_dmg
        elif rare[0] == weapon_rare[1]:
            weapon_dmg += weapon_dmg * 2
            self.dmg += weapon_dmg
        elif rare[0] == weapon_rare[2]:
            weapon_dmg += weapon_dmg * 3
            self.dmg += weapon_dmg   
        elif rare[0] == weapon_rare[3]:
            weapon_dmg += weapon_dmg * 4
            self.dmg += weapon_dmg
        elif rare[0] == weapon_rare[4]:
            weapon_dmg += weapon_dmg * 10
            self.dmg += weapon_dmg
        return weapon,rare[0],weapon_dmg

    def create_heal(self):
        health = 10
        heal_rare = ['Обычная','Редкая','Эпическая','Легендарная','Мифическая']
        heal_chance = [20,15,10,5,1]
        rare_health = random.choices(heal_rare,weights=heal_chance,k=1)
        heal_type = ['Пиццу','Cтарость','Зелье исцеления']
        rand_heal = random.choice(heal_type)
        if rare_health[0] == heal_rare[0]:
            health += health * 1
            self.hp += health
             
        elif rare_health[0] == heal_rare[1]:
            health += health * 2
            self.hp += health
            
        elif rare_health[0] == heal_rare[2]:
            health += health * 3
            self.hp += health
               
        elif rare_health[0] == heal_rare[3]:
            health += health * 4
            self.hp += health
            
        elif rare_health[0] == heal_rare[4]:
            health += health * 10
            self.hp += health
            
        return rand_heal,rare_health[0],health


    def attack(self,victim):
        victim.hp -= self.dmg
        print(f'Ваш урон: {self.dmg}')
        time.sleep(1)
        if victim.hp <= 0:
            rand_exp = random.randint(10,20)*self.lvl
            print(f'Поздравляем. {victim.name} повержен. +{rand_exp} опыта.')
            time.sleep(.5)
            
            drop_list = [0,1,2]
            item_drop = random.choice(drop_list)
            if item_drop == 1:
                weapon_drop = self.create_weapon()
                
                print(f'Вам выпало оружие.\n{weapon_drop[0]} с редкостью {weapon_drop[1]} ')
                time.sleep(.5)
                print(f'Ваш урон {self.dmg}')
                time.sleep(.5)
            elif item_drop == 2:
                heal_drop = self.create_heal()
                print(f'Вы получили хилку.\n{heal_drop[0]} с редкостью {heal_drop[1]}' )
                time.sleep(.5)
                print(f'Ваше здоровье {self.hp}')
                time.sleep(.5)
            elif item_drop == 0:
                print ('Ничего нету')




            self.exp += rand_exp
            max_exp = self.lvl * 100
            if self.exp >= max_exp:
                self.lvl_up()
                max_exp = self.lvl * 100
                time.sleep(.57510)
                print(f'До следующего уровня {max_exp} опыта.')

            return False
        else:
            print(f'{victim.name}, осталось {victim.hp}')
            time.sleep(.5)
            return True

    @staticmethod
    def create_player(player_name,player_race,player_class):
        hp = 0
        dmg = 0
        name = player_name
        if player_race == races_list[0]:
            hp += 50
            dmg += 40
        elif player_race == races_list[1]:
            hp += 35
            dmg += 60
        elif player_race == races_list[2]:
            hp += 40
            dmg += 40
        elif player_race == races_list[3]:
            hp += 55
            dmg += 35
        else:
            print('Такой рассы нет')
            quit()

        if player_class == class_list[0]:
            hp += 15
            dmg += 50
        elif player_class == class_list[1]:
            hp += 0
            dmg += 80
        elif player_class == class_list[2]:
            hp += 30
            dmg += 40
        else:
            print('Такого класса нету')
            quit()
            
                
        return Player(name, hp, dmg)
        
class Enemy:
    def __init__(self,enemy_name,enemy_dmg,enemy_hp):
        self.name = enemy_name
        self.dmg = enemy_dmg
        self.hp = enemy_hp
    
    def create_enemy():
        enemy_names = ['Скелет', 'Обеме', 'Амогус', 'Обеликс']
        enemy_name = random.choice(enemy_names)
        enemy_dmg = random.randint(30,90) + player.lvl * 20
        enemy_hp = random.randint(60,90) + player.lvl * 20

        return Enemy(enemy_name,enemy_dmg,enemy_hp)

    def attack(self, victim):
        victim.hp -= self.dmg
        print(f'{self.name} нанёс: {self.dmg} урона')
        time.sleep(.5)
        if victim.hp <= 0:
            print('Вы проиграли')
            quit()
        else:
            print(f'Ваше здоровье {victim.hp}')
            time.sleep(.5)
         


    


         
    

#списки
races_list = ['эльф', 'гном', "хоббит", "человек"]

class_list = ['лучник', 'маг', 'рыцарь']

print('Здраствуйте, как вас зовут?')
name = input()
print(f"Приветствую {name}, к какой расе ты относишься?")

for i in races_list:
    print(i,end=' ')

print()
race = input().lower()
print("К какому классу ты относишься?")
for i in class_list:
    print(i,end=' ')
print()
class_player = input().lower()

player = Player.create_player(name, race, class_player)



print(f'Персонаж создан! \n'
f'Имя {player.name} \n'
f'Здоровье:{player.hp} \n'
f'Урон {player.dmg}\n')
time.sleep(2)

# enemy = Enemy.create_enemy()

# print(f'Персонаж создан! \n'
# f'Имя {enemy.name} \n'
# f'Здоровье:{enemy.hp} \n'
# f'Урон {enemy.dmg}\n')

def fight_choice():
    a = int(input('атаковать(1) или сбежать(2)'))
    if a == 1:
        result_attack = player.attack(enemy)
        if result_attack == True:
            enemy.attack(player)
            fight_choice()
    elif a == 2:
        running()

def running():
    plan = random.randint(0,1)
    if plan == 0:
        print('Вам удалось сбежать!')
    elif plan == 1:
        print('Вам не удалось сбежать')
        enemy.attack(player)
        fight_choice()
    


while True:
    event = random.randint(0,1)
    if event == 0:
        print('Вы некого не встретили,идём дальше...')
        time.sleep(.77)
    elif event == 1:
        enemy = Enemy.create_enemy()
        print(f'Вас заметил {enemy.name}\n'
            f'Здоровье:{enemy.hp} \n'
            f'Урон {enemy.dmg}\n')
        fight_choice()




