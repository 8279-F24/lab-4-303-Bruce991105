import time
from adafruit_circuitplayground import cp

cp.pixels.auto_write = False
cp.pixels.brightness = 0.3

def fade_color(red, green, blue):
    max_value = 255  # Initial intensity
    step = 10  # Step size for decrementing

    while max_value >= 0:
        for i in range(10):
            cp.pixels[i] = (red * max_value // 255, green * max_value // 255, blue * max_value // 255)
        cp.pixels.show()
        time.sleep(0.1)
        max_value -= step

def main():
    while True:  # Start a loop to repeat runnings
        print("\nMenu:")
        print("1: Red")
        print("2: Green")
        print("3: Blue")
        print("Press 'q' to quit")

        choice = input("Choose a color option (1, 2, 3) or press 'q' to quit: ")

        if choice.lower() == 'q':  # break condition
            print("Exiting the program. Goodbye!")
            break

        try:
            option = int(choice)

            if option == 1:
                print("You chose Red. Fading red LEDs.")
                fade_color(255, 0, 0)  # LED red
            elif option == 2:
                print("You chose Green. Fading green LEDs.")
                fade_color(0, 255, 0)  # LED green
            elif option == 3:
                print("You chose Blue. Fading blue LEDs.")
                fade_color(0, 0, 255)  # LED blue
            else:
                print("Invalid option. Please choose 1, 2, or 3.")  # Out-of-range input
        except ValueError:
            print("Invalid input. Please enter a number (1, 2, or 3).")

# Run the main program
if __name__ == "__main__":
    main()


