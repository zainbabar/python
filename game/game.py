player = {'name': 'Manuel', 'attack': 100, 'heal': 160, 'health': 1000}
monster = {'attack': 120, 'health': 1000
game_running = True

while game_running == True:

print('Please select action')
print('1) Attack')
print('2) Heal')

player_choice = input()

if player_choice == '1':
    monster['health'] = monster['health'] - player['attack']
    if monster['health'] <= 0:
        pass
    else:
        player['health'] = player['health'] - monster['attack']
        if player['health'] <= 0:
    
    print(monster['health'])
    print(player['health'])


elif player_choice == '2':
    print('Heal player')
else: 
    print('Invalid Input' )

if player['health'] <= 0 or monster['health'] <=0:
    game_running = False