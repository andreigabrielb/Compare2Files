import Tkinter # Library for UI 
import random  # import for random genaration 

def random_number():
    #This function returns a random number
    my_random = random.randint(1, 10)
    dice_thrown.configure(text = "Chance was: " + str(my_random))


main_window = Tkinter.Tk("Main")
    
MyTitle = Tkinter.Label(main_window, text="Generate random number")
MyTitle.pack()

generate_button = Tkinter.Button(main_window, text = "Generate", command  = random_number)
generate_button.pack()

dice_thrown = Tkinter.Label(main_window)
dice_thrown.pack()
   
main_window.mainloop()

