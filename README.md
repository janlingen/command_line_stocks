# Welcome to CommandLineStocks.

## how to install:
  - install needed packages
    - `pip install -r requirements.txt`

## how to create a level yourself:
  - create a normal .txt file
  - <strong>\# </strong>are walls
      - it is important that there are no gaps in the created walls
      - to get a better feel for whats possible just take a look into the level folder
  - <strong>S</strong> is the player
      - only one player is allowed
  - <strong>A</strong> is the exit
      - you can place several exits
  - <strong><, >, ^, v</strong> are the monsters and their movement direction
  
  ## which options are avaliable:
  - <strong>-i inputfilename</strong>
    - enables you to predefine a sequence of inputs W, A, S, D in an .txt file
  - <strong>-o outputfilename</strong>
    - enables you to choose an outputfile
  - for example <strong>./dungeon -i inputs.txt -o output.txt level/3.txt  </strong>
  
