# import necessary libraries for the game
import random
import curses
import shutil

# creat screen
screen = curses.initscr()

# hide the mouse in the screen
curses.curs_set(0)

# get max screen height and width
screen_h , screen_w = screen.getmaxyx()

# creat a new window 
window = curses.newwin(screen_h,screen_w,0,0)

# allow window to receive input from the keybord 
window.keypad(1)

# set the delay for ubdating the screen 
window.timeout(150)

# set the x,y of start position of snake head 
snake_x = screen_w // 4
snake_y = screen_h // 2

# set initial position for snake body 
snake =[[snake_y,snake_x],
        [snake_y,snake_x-1],
        [snake_y,snake_x-2]
       ]
# creat the food
food = [screen_h // 2,screen_w // 2]

# show the food in window using curses library
window.addch(food[0],food[1],curses.ACS_DIAMOND)

# set initial movement diraction
key = curses.KEY_UP
Score = 0;
columns = shutil.get_terminal_size().columns
# creat game loop that loops end when player lose
while True:
  
  # get the next key pressed by user 
  next_key = window.getch()
  
  # key will remains same the user doesnot presse 
  # anything else update key
  key = key if next_key == -1 else next_key 
  
  # check if snake hit the walls our it self
  if snake[0][0] in [0,screen_h] or snake[0][1] in [0,screen_w] or snake[0] in snake[1:]:
    
    curses.endwin()  # close the window
    print("GAME OVER".center(columns))
    print("")
    print("YOUR SCORE: ".center(columns)+str(Score).center(columns))
    quit()  # end the program

  # set the new position of the snake head 
  new_head = [snake[0][0],snake[0][1]]
  
  if key == curses.KEY_RIGHT:
    new_head[1] +=1
  if key == curses.KEY_LEFT:
    new_head[1] -=1
  if key == curses.KEY_UP:
    new_head[0] -=1
  if key == curses.KEY_DOWN:
    new_head[0] +=1

  # set the new head
  snake.insert(0,new_head)
  # check if snake eat the food 
  if snake[0] == food:
    Score +=100
    # remove food if snaeke ate it
    food = None
    # while food is none generate new food in random place in the screen
    while food is None:
      new_food = [
        random.randint(1,screen_h-1),
        random.randint(1,screen_w-1)]
      food = new_food if new_food not in snake else None
      
    # show new food in the window
    window.addch(food[0],food[1],curses.ACS_DIAMOND)
    
    # otherwise remove snake tail
  else:
    tail = snake.pop()
    window.addch(tail[0],tail[1],' ')

  #update the position of the snake on window
  window.addch(snake[0][0],snake[0][1],curses.ACS_BOARD)
    
    
    
    
  

       


