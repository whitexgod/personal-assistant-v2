from process_module import process
from output_module import output
import welcome
import os
from input_module import take_command

os.system("cls")

#welcome message
welcome.greet()


while(True):

    i=take_command()
    o=process(i.lower())

    output(o)
