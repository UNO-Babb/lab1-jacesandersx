#FirstProgram.py
#Name: Jace Sanders
#Date: 8/28/2024
#Assignment: Birthday

def main():
  print("Hello")
  name = input("What's your name? ")
  age = input("What year were you born? ")
  age = int(age)
  birthYear = 2024 - age
  print(birthYear)

#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
