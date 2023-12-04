import random

print("*********************")


def choose_option ():
  opciones=("piedra", "papel", "tijera")
  usuario_opcion = input ("piedra, papel o tijera ")
  usuario_opcion=usuario_opcion.lower()
  
  if not usuario_opcion in opciones:
    print("la opcion no es valida")
   #continue 
    return None, None
  
  computer_opcion= random.choice(opciones) # la funcion random que se importo arriba, sirve para que la opcion del computador sea aleatoria y no sesgada
  
  print ("opcion de usuario: ", usuario_opcion)
  print ("opcion del computador: ",computer_opcion)
  return usuario_opcion, computer_opcion


def check_rules( usuario_opcion, computer_opcion, computer_wins, user_wins):
  if usuario_opcion == computer_opcion: 
    print("empate")
  elif usuario_opcion == "piedra":
   if computer_opcion == "tijera":
     print("piedra gana a tijeras")
     print("el usuario gano")
     user_wins += 1
   else:
     print("papel gana a piedra")
     print("computer gano")
     computer_wins += 1
     
  elif usuario_opcion == "papel":
   if computer_opcion == 'piedra':
       print('papel gana a piedra')
       print('user gano') 
       user_wins += 1
   else:
      print('tijera gana a papel')
      print('computer gano!')
      computer_wins += 1
      
  elif usuario_opcion == "tijera":
   if computer_opcion == "papel":
     print("tijera gana a papel")
     print("el usuario gano")
     user_wins += 1
   else:
     print("piedra gana a tijera")
     print("computer gano")   
     computer_wins += 1
  return user_wins, computer_wins

def run_game():
  computer_wins = 0
  user_wins = 0
  ronda= 1
  
  while True:
   print ("*"* 10)
   print("Ronda", ronda)
   print ("*"* 10)

   print ("computer_wins", computer_wins)
   print ("user_wins", user_wins)
   ronda += 1
 
   usuario_opcion, computer_opcion = choose_option()
   computer_wins, user_wins = check_rules( usuario_opcion, computer_opcion, computer_wins, user_wins )
     
   if computer_wins == 2:
    print ("el ganador es la computadora")
    break 
   if user_wins == 2:
    print ("El ganador es el usuario")
    break

run_game()