'''
Created on 18 Nov 2021
@author: FHentsch-Cowles24
Description:
    This program requests the user for their preferred prefix and full name. They are then directed
    to a menu that provides their prefix + full name (capitalized) and prompts them to choose a
    function. They can request for linguistic information, reverse any of their names (first, middle,
    etc.), and scramble any of their names. After their functions are performed, they are returned to
    the main menu. They also have the option to change their name at any point from the menu. Behind
    the scenes, the program performs upper, lower, and capitalization methods using 'homemade'
    functions. There are no global variables, except for random (imported).
    
    To determine the number of syllables in a word that ends in -[vowel][consonant]es, the user chooses
    if they think the word "miles" has one or two syllables... an ongoing debate with a classmate.
Log:
    
Bugs:
    -If only one word* is provided in name input then there is no middle name and the last and first
     names are the same
    -If there are two or more spaces either before or after the entire name is input, there will be an
     index error in the case functions.
     
    *Commonly used term 'word' meaning a first, middle, or last name separated by spaces in the name
     input prompt.
    
Initiatives:
    -Prefixes
    -Menus
    -Syllable counter (that was hard)
    -Hyphen identifier
    -Palindrome identifier
    -Name scrambler
    -Return full name as sorted array of characters
    -Two ways to count syllables'
    -Quit feature
    -Change name option
    -Change prefix option
    -Option to reverse specific parts of name
    -Option to scramble specific parts of name
    
Last edited on 10/22/2021
'''
import random

def main():
    
    print("    Welcome to the Nomenipulation Game. When presented with a menu you will see\n"\
          " numbers on the left-hand side accompanied by a description. To make your\n"\
          " selection, just type in a number and press enter.\n")
    
    naming()

def my_lower(name):
#description = Lowercase function. string goes in, all-lowercase comes out.
#arg1 - name = a name-type, like first, middle, last, or full name. String.
#return converted_name = Returns name converted to all lowercase characters.

    converted_name = ''
    for character in name:
        if ord(character) in range(65,90):                                          #Checks if char is upper
            character = chr(ord(character) + 32)                                    #If upper, converts to lower
        converted_name = converted_name + character                                 #Adds char to new string
    return converted_name

def my_upper(name):
#description = Uppercase function. string goes in, all-uppercase comes out.
#arg1 - name = a name-type, like first, middle, last, or full name. String.
#return converted_name = Returns name converted to all upperrcase characters.

    converted_name = ''
    for character in name:
        if ord(character) in range(97,122):                                         #Checks if char is lower
            character = chr(ord(character) - 32)                                    #If lower, converts to upper
        converted_name = converted_name + character                                 #Adds char to new string
    return converted_name

def my_capitalize(name):
#description = #Capitalize function. string goes in, first character come out capitalized 
#arg1 - name = a name-type, like first, middle, last, or full name. String.
#return converted_name = Returns name converted to a capitalized string. First character is upper, rest are lower.

    name = name.split(' ')
    converted_name = ''
    for word in name:
        first_letter = word[0]
        if ord(first_letter) in range(97,122):                                      #Checks first char in word for lower
            first_letter = chr(ord(word[0]) - 32)                                   #If lower, converts to upper
        word = first_letter + word[1:]                                              #Replaces first letter with converted
        converted_name = converted_name + " " + word                                #Combines words with spaces
    return converted_name[1:]

def naming():
#description = Name selection menu. Can be seen as "user info input prompt" which redirects to function menu()

    while True:
        try:
            prefix = int(input("Prefix:\n"\
                           "'0' - None\n"\
                           "'1' - Dr.\n"\
                           "'2' - Sir\n"\
                           "'3' - Madame\n"\
                           "'4' - Esq\n"\
                           "'5' - Ph.d\n"))
            if prefix in range(0, 6):
                if prefix == 0:
                    prefix = ''
                elif prefix == 1:
                    prefix = 'Dr. '
                elif prefix == 2:
                    prefix = 'Sir '
                elif prefix == 3:
                    prefix = 'Madame'
                elif prefix == 4:
                    prefix = 'Esq '
                elif prefix == 5:
                    prefix = 'Ph.d '
                break
            else:
                raise AttributeError
        except AttributeError:
            print("Invalid response")
        except ValueError:
            print("Invalid response")
    
    print("Please note that when entering in name information, you must provide at "\
          "least three words\names separated by spaces. [First Middle Last], you can"\
          " have multiple middle names and hyphenated last names.\n")
    full_name = input("Name: First Middle(s) Last\n")
    if full_name[0] == ' ':                                                         #Removes starting space if there is one
        full_name = full_name[1:]
    if full_name[-1] == ' ':                                                        #Removes extra space if there is one
        full_name = full_name[:-1]
    full_name = my_lower(name=full_name)                                            #Defines full_name from user input
    full_name_list = full_name.split(' ')
    first = full_name_list[0]                                                       #Defines first, splitting full_name and using 1st item
    last = full_name_list[-1]                                                       #Defines last, splitting full_name and using last item
    last_list = last.split("-")
    last_capitalized = ''
    for name in last_list:                                                          #Creates capitalized last_name variable, accounts for '-'s
        name = my_capitalize(name)
        last_capitalized = last_capitalized + '-' + name
    last_capitalized = last_capitalized[1:]
    middle_list = full_name_list[1:-1]                                              #Creates a list of middle names from split full_name, excludes 1st and last
    middle_capitalized = ''
    for name in middle_list:                                                        #Capitalizes each item in middle_list
        name = my_capitalize(name)
        middle_capitalized = middle_capitalized + ' ' + name
    middle_capitalized = middle_capitalized[1:]
    middle = ' '.join(middle_list)
    full_name_capitalized = my_capitalize(first) + ' ' + middle_capitalized + ' ' + last_capitalized        #Creates a presentable full name w/ prefix
    menu(prefix, full_name, first, middle, middle_list, last, last_list, full_name_capitalized)             #Calls function menu with all name data


def menu(prefix, full_name, first, middle, middle_list, last, last_list, full_name_capitalized):
#description = Once name is given, user is brought to menu where they can interact with the name.
#arg1 - prefix = Chosen prefix from name menu
#arg2 - full_name = Full name provided by user
#arg3 - first = First name split from full_name
#arg4 - middle = Middle name(s) split from full_name
#arg5 - first = Last name split from full_name
#arg6 - last_list = Last name split by '-'
#arg7 - full_name_capitalized = Prefix + capitalized full_name

    while True:
        try:
            menu = int(input("Nomenipulation Menu\n"\
                              "    " + prefix + full_name_capitalized + "\n"\
                             "'0' - Change name\n"\
                             "'1' - Name information\n"\
                             "'2' - Reverse name\n"\
                             "'3' - Scramble name\n"\
                             "'4' - Quit/Terminate Program\n"))
            if menu == 0:
                naming()
            elif menu == 1:
                info(prefix, full_name, first, middle, last)
            elif menu == 2:
                while True:
                    try:
                        reverse_menu = int(input("Name Reversal Menu\n"\
                                                 "'0' - Back to menu\n"\
                                                 "'1' - Reverse full name\n"\
                                                 "'2' - Reverse first name\n"\
                                                 "'3' - Reverse middle name(s)\n"\
                                                 "'4' - Reverse last name\n"))
                        if reverse_menu == 0:
                            break
                        elif reverse_menu == 1:
                            print('Full_name reversed: ' + reverse(name=full_name, name_type='Full_name'))
                        elif reverse_menu == 2:
                            print('First_name reversed: ' + reverse(name=first, name_type='First_name'))
                        elif reverse_menu == 3:
                            print('Middle_name reversed: ' + reverse(name=middle, name_type='Middle_name'))
                        elif reverse_menu == 4:
                            print('Last_name reversed: ' + reverse(name=last, name_type='Last_name'))
                        else:
                            raise AttributeError
                    except AttributeError:
                        print("Invalid response")
                    except ValueError:
                        print("Invalid response")
            elif menu == 3:
                while True:
                    try:
                        scramble_menu = int(input("Name Scramble Menu\n"\
                                                 "'0' - Back to menu\n"\
                                                 "'1' - Scramble full name\n"\
                                                 "'2' - Scramble first name\n"\
                                                 "'3' - Scramble middle name(s)\n"\
                                                 "'4' - Scramble last name\n"))
                        if scramble_menu == 0:
                            break
                        elif scramble_menu == 1:
                            print("Full_name scrambled: " + scramble(name=full_name))
                        elif scramble_menu == 2:
                            print("First_name scrambled: " + scramble(name=first))
                        elif scramble_menu == 3:
                            print("Middle_name scrambled: " + scramble(name=middle))
                        elif scramble_menu == 4:
                            print("Last_name scrambled: " + scramble(name=last))
                        else:
                            raise AttributeError
                    except AttributeError:
                        print("Invalid response")
                    except ValueError:
                        print("Invalid response")
            elif menu == 4:
                quit()
        except AttributeError:
            print("Invalid response")
        except ValueError:
            print("Invalid response")


def info(prefix, full_name, first, middle, last):
#description = Info function calls functions that provide linguistic data
#arg1 - full_name = Full_name for name information
#arg2 - first = First name for name information
#arg3 - middle = Middle name for name information
#arg4 - last = Last name for name information
    
    print('Prefix: ' + prefixer(prefix))
    print('Total vowels: ' + vowels(name=full_name))
    print('First_name vowels: ' + vowels(name=first))
    print('Middle_name vowels: ' + vowels(name=middle))
    print('Last_name vowels: ' + vowels(name=last))
    print('Total consonants: ' + consonants(name=full_name))
    print('First_name consonants: ' + consonants(name=first))
    print('Middle_name consonants: ' + consonants(name=middle))
    print('Last_name consonants: ' + consonants(name=last))
    print('Hyphen: ' + hyphen(full_name))
    print('First_name palindrome: ' + palindrome(name=first))
    print('Middle_name palindrome: ' + palindrome(name=middle))
    print('Last_name palindrome: ' + palindrome(name=last))
    print('Syllables: ' + syllable(name=full_name) + '\n')


def prefixer(prefix):
    if prefix == '':
        prefix_presence = 'False'
    else:
        prefix_presence = 'True'
    return prefix_presence
    
def vowels(name):
#description = Tells user how many vowels are in a string
#arg1 - name = String to analyze
#return str(count) = Returns number of vowels in string

    count = 0
    for letter in name:
        if (letter == 'a') or (letter == 'e') or (letter == 'i') or (letter == 'o') or (letter == 'u'):
            count = count + 1
    return str(count)


def consonants(name):
#description = Tells user how many consonants are in a string
#arg1 - name = String to analyze
#return str(count) = Returns number of consonants in string

    count = 0
    for letter in name:
        if letter == 'b' or letter == 'c' or letter == 'd' or letter == 'f' or letter == 'g'\
        or letter == 'h' or letter == 'j' or letter == 'k' or letter == 'l' or letter == 'm'\
        or letter == 'n' or letter == 'p' or letter == 'q' or letter == 'r' or letter == 's'\
        or letter == 't' or letter == 'v' or letter == 'w' or letter == 'x' or letter == 'y'\
        or letter == 'z':
            count = count + 1
    return str(count)

    
def hyphen(full_name):
#description = Tells user if a hyphen is present in a string
#arg1 - full_name = String to analyze
#return str(count) = Returns boolean of hyphen presence

    hyphen = False
    for character in full_name:
        if character == '-':
            hyphen = True
            
    return str(hyphen)


def palindrome(name):
#description = Tells user if a palindrome is in a string
#arg1 - name = String to analyze
#return str(count) = Returns boolean of palindrome presence

    palindrome = False
    if name == name[::-1]:
        palindrome = True
    
    return str(palindrome)


def syllable(name):
#description = Tells user how many syllables are in a string
#arg1 - name = String to analyze
#return str(count) = Returns number of syllables in string

    while True:
        try:                                                                                #User choice determine how syllables are counted in words ending with -"v(owel)c(onsonant)es"
            miles_question = input("\nThe following question is meant to determine "\
                                   "how YOU count syllables in order to count the "\
                                   "syllables in your name. Do you consider the word "\
                                   "'miles' to have one or two syllables?\n"\
                                   "Type 'Y' if yes, 'N' if no.\n")
            miles_question = my_lower(miles_question)
            if miles_question == 'y':
                es_parser = False
                break
            elif miles_question == 'n':
                es_parser = True
                break
            else:
                raise AttributeError
        except AttributeError:
            print("Invalid response")
        except ValueError:
            print("Invalid response")
    name_list = name.split(' ')                                                             #Splits name to check for multiple words
    shortened_name = ''
    for name in name_list:                                                                  #Checks if the last letter of name = 'e'
        if name[-1] == 'e':
            name = name[:-1]                                                                #Remove 'e' from the end of name
        shortened_name = shortened_name + " " + name
    vowel_count = 0
    most_recent_letter = ''
    for character in shortened_name:                                                        #Replaces hyphens with spaces
        if character == '-':
            super_shortened_name = shortened_name.split('-')
            super_shortened_name = ' '.join(super_shortened_name)
            break
        else:
            super_shortened_name = shortened_name
    for letter in super_shortened_name:                                                     #Counts vowels in name
        if (letter == 'a') or (letter == 'e') or (letter == 'i') or (letter == 'o') or (letter == 'u'):
            vowel_count = vowel_count + 1
            if letter == most_recent_letter:
                vowel_count = vowel_count - 1
            elif most_recent_letter == 'q' and letter == 'u':                               #Excludes 'u's preceding 'q'
                vowel_count = vowel_count - 1
        most_recent_letter = letter
    shortened_name_list = super_shortened_name.split(' ')
    if es_parser == True:                                                                   #If user thinks miles has one syllable, checks for -vces ending
        for name in shortened_name_list[1:]:
            minus_1 = name[len(name)-1]                                                     #Last char in name
            minus_2 = name[len(name)-2]                                                     #Second to last char
            minus_4 = name[len(name)-4]                                                     #Fourth from last char
            minus_5 = name[len(name)-5]                                                     #Fifth from last char
            if (minus_1 == 's') and (minus_2 == 'e'):
                if (minus_4 == 'a') or (minus_4 == 'e') or (minus_4 == 'i') or (minus_4 == 'o') or (minus_4 == 'u'):
                    vowel_count = vowel_count - 1                                           #Removes vcount if vowel(then consonant) comes before -es
                elif (minus_4 =='w') or (minus_4 =='y'):                                    #Removes if 'y' or 'w' come before vowel then consonant-es
                    if (minus_5 == 'a') or (minus_5 == 'e') or (minus_5 == 'i') or (minus_5 == 'o') or (minus_5 == 'u'):
                        vowel_count = vowel_count - 1
    
        
    return str(vowel_count)
    

def reverse(name, name_type):
#description = Reverses provided string
#arg1 - name = String to analyze
#arg2 - name_type = Name identifier ie. first, middle, etc. Different protocols for each
#return str(count) = Returns reversed string

    reversed_name = name[::-1]                                                              #Reverses provided name
    
    if name_type == 'Full_name':
        name_list = reversed_name.split(' ')                                                #Splits by spaces
        reversed_last_list = name_list[0]                                                   #Gets first item in list (last_name)
        reversed_last_list = reversed_last_list.split('-')                                  #Splits last_name item by hyphens
        reversed_last = ''
        for name in reversed_last_list:                                                     #Capitalizes parts of last, then recombines with hyphen
            name = my_capitalize(name)
            reversed_last = reversed_last + "-" + name
        reversed_last = reversed_last[1:]
        reversed_name = reversed_last
        for word in name_list[1:]:                                                          #Capitalizes rest of full_name and recombines
            word = my_capitalize(word)
            reversed_name = reversed_name + " " + word
    if name_type == 'First_name':
        reversed_name = my_capitalize(reversed_name)                                        #Capitalizes reversed first_name
    if name_type == 'Middle_name':
        if name == '':                                                                      #If a middle_name wasn't provided
            print("No middle name provided")
        else:
            reversed_middle_list = reversed_name.split(' ')                                 #Splits middle_name(s) by space
            reversed_name = ''
            for name in reversed_middle_list:
                name = my_capitalize(name)                                                  #Capitalizes all middle_name(s)
                reversed_name = reversed_name + " " + name                                  #Recombines middle name(s)
            reversed_name = reversed_name[1:]
    if name_type == 'Last_name':
        reversed_last_list = reversed_name.split('-')                                       #Splits last name by hyphen
        reversed_name = ''
        for name in reversed_last_list:                                                     #Capitalizes parts of last_name and recombines with hyphen
            name = my_capitalize(name)
            reversed_name = reversed_name + "-" + name
        reversed_name = reversed_name[1:]
        
    return reversed_name


def scramble(name):
#description = Scrambles provided string
#arg1 - name = String to analyze
#return str(count) = Returns scrambled string
    
    if name == '' or name == ' ':
        response = "No middle name provided"
        return response
    else:
        word_list = name.split(' ')                                                         #Splits name
        scrambled_name = ''
        for word in word_list:                                                              #Shuffles characters of each name separated by spaces
            word = list(word)
            random.shuffle(word)
            word = ''.join(word)
            word = my_capitalize(word)
            scrambled_name = scrambled_name + " " + word                                    #Adds scrambled name to the rest
        return scrambled_name[1:]
    
        
        


if __name__ == '__main__':
    main()
