import pyfiglet
import sys
import random


fonts = pyfiglet.FigletFont.getFonts()

if len(sys.argv) == 1:
    
    font = random.choice(fonts)

elif len(sys.argv) == 3:
   
    if sys.argv[1] not in ["-f", "--font"]:
        sys.exit("Invalid flag. Use -f or --font")
    if sys.argv[2] not in fonts:
        sys.exit("Invalid font name.")
    font = sys.argv[2]

else:
    sys.exit("Usage: python figlet.py [-f font]")

text = input("Input: ")

print(pyfiglet.figlet_format(text, font=font))
