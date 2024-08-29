#MadLib.py
#Name: Jace Sanders
#Date: 8/28/2024
#Assignment: MadLib.py

def main():
  print("Madlib")
  #Ask user for words
  print ("Let's write a story, I'll need a few words.")
  noun1 = input(" Enter an Adjective : ")
  noun2 = input("A Person's Name : ")
  noun3 = input("A Country : ")
  noun4 = input("An Kingdom Name : ")
  noun5 = input("A Plural Noun : ")
  noun6 = input("A Verb : ")
  noun7 = input("A Color : ")

  #Print the story with the user supplied words.
  Print("Once upon a time, there was a " +noun1 +" Princess named " +noun2 +" she was from " +noun3 +". She lived in a beautiful kingdom on the hills called " +noun4 +" She had five " +noun5 +" while she was " +noun6 +" the horse. She fell off and her dress stained " +noun7 +"."")


#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
