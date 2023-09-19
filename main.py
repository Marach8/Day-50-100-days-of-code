import random, time, os

def add():
  a = open('my.ideas', 'a+')
  print()
  ask1 = input('Enter the idea: ').strip()
  a.write(f'{ask1}\n')
  a.close()
  time.sleep(1)
  print()
  print('\033[32mIdea Added Successfully😎\033[0m')
  time.sleep(1.5)
  os.system('clear')


def view():
  y = []
  try:
    t = open('my.ideas', 'r')
    while True:
      k = t.readline().strip()
      if k == '':
        break
      y.append(k)
    u = random.randint(0, len(y)-1)
    print()
    print(y[u])
    time.sleep(6)
    t.close()
    os.system('clear')
    menu()
  except FileNotFoundError:
    print()
    print('\033[31mYou do not have any idea to view! Add ideas first!\033[0m')
    time.sleep(3)
    os.system('clear')
    menu()

  
def menu():
  while True:
    print()
    ask = input('''Enter:
  1 to Add and idea
  2 to randomly view an idea
    >> ''')
    if ask == '1':
      add()
    elif ask == '2':
      view()

menu()