'''
Created on 18 Nov 2021

@author: FHentsch-Cowles24
'''
import random

def main():
    
    naming()

def my_lower(name):
    converted_name = ''
    for character in name:
        if ord(character) in range(65,90):
            character = chr(ord(character) + 32)
        converted_name = converted_name + character
    return converted_name

def my_upper(name):
    converted_name = ''
    for character in name:
        if ord(character) in range(97,122):
            character = chr(ord(character) - 32)
        converted_name = converted_name + character
    return converted_name

def my_capitalize(name):
    name = name.split(' ')
    converted_name = ''
    for word in name:
        first_letter = word[0]
        if ord(first_letter) in range(97,122):
            first_letter = chr(ord(word[0]) - 32)
        word = first_letter + word[1:]
        converted_name = converted_name + " " + word
    return converted_name[1:]

def naming():
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
    
    full_name = input("Name: First Middle(s) Last\n")
    full_name = my_lower(name=full_name)
    full_name_list = full_name.split(' ')
    first = full_name_list[0]
    last = full_name_list[-1]
    last_list = last.split("-")
    last_capitalized = ''
    for name in last_list:
        name = my_capitalize(name)
        last_capitalized = last_capitalized + '-' + name
    last_capitalized = last_capitalized[1:]
    middle_list = full_name_list[1:-1]
    middle_capitalized = ''
    for name in middle_list:
        name = my_capitalize(name)
        middle_capitalized = middle_capitalized + ' ' + name
    middle_capitalized = middle_capitalized[1:]
    middle = ' '.join(middle_list)
    full_name_capitalized = my_capitalize(first) + ' ' + middle_capitalized + ' ' + last_capitalized
    menu(prefix, full_name, first, middle, middle_list, last, last_list, full_name_capitalized)


def menu(prefix, full_name, first, middle, middle_list, last, last_list, full_name_capitalized):
    while True:
        try:
            menu = int(input("Nomenipulation Menu\n"\
                             "    " + prefix + full_name_capitalized + "\n"\
                             "'0' - Change name\n"\
                             "'1' - Name information\n"\
                             "'2' - Reverse name\n"\
                             "'3' - Scramble name\n"))
            if menu == 0:
                naming()
            elif menu == 1:
                info(full_name, first, middle, last)
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
                            reverse(name=full_name,announce_name='Full_name')
                        elif reverse_menu == 2:
                            reverse(name=first,announce_name='First_name')
                        elif reverse_menu == 3:
                            reverse(name=middle,announce_name='Middle_name')
                        elif reverse_menu == 4:
                            reverse(name=last,announce_name='Last_name')
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
                            print("Full_name scrambled: " + scramble(name=full_name,announce_name='Full_name'))
                        elif scramble_menu == 2:
                            print("First_name scrambled: " + scramble(name=first,announce_name='First_name'))
                        elif scramble_menu == 3:
                            print("Middle_name scrambled: " + scramble(name=middle,announce_name='Middle_name'))
                        elif scramble_menu == 4:
                            print("Last_name scrambled: " + scramble(name=last,announce_name='Last_name'))
                        else:
                            raise AttributeError
                    except AttributeError:
                        print("Invalid response")
                    except ValueError:
                        print("Invalid response")
        except AttributeError:
            print("Invalid response")
        except ValueError:
            print("Invalid response")


def info(full_name, first, middle, last):
    vowels(name=full_name, announce_name='Total')
    vowels(name=first, announce_name='First_name')
    vowels(name=middle, announce_name='Middle_name')
    vowels(name=last, announce_name='Last_name')
    consonants(name=full_name, announce_name='Total')
    consonants(name=first, announce_name='First_name')
    consonants(name=middle, announce_name='Middle_name')
    consonants(name=last, announce_name='Last_name')
    hyphen(full_name)
    palindrome(name=first, announce_name='First_name')
    palindrome(name=middle, announce_name='Middle_name')
    palindrome(name=last, announce_name='Last_name')
    syllable(name=full_name, announce_name='Total')

    
def vowels(announce_name, name):
    count = 0
    for letter in name:
        if (letter == 'a') or (letter == 'e') or (letter == 'i') or (letter == 'o') or (letter == 'u'):
            count = count + 1
    print(announce_name + " Vowels: " + str(count))


def consonants(name, announce_name):
    count = 0
    for letter in name:
        if letter == 'b' or letter == 'c' or letter == 'd' or letter == 'f' or letter == 'g'\
        or letter == 'h' or letter == 'j' or letter == 'k' or letter == 'l' or letter == 'm'\
        or letter == 'n' or letter == 'p' or letter == 'q' or letter == 'r' or letter == 's'\
        or letter == 't' or letter == 'v' or letter == 'w' or letter == 'x' or letter == 'y'\
        or letter == 'z':
            count = count + 1
    print(announce_name + " Consonants: " + str(count))

    
def hyphen(full_name):
    hyphen = False
    for character in full_name:
        if character == '-':
            hyphen = True
            
    print("Hyphen: " + str(hyphen))


def palindrome(name, announce_name):
    palindrome = False
    if name == name[::-1]:
        palindrome = True
    
    print(announce_name + " Palindrome: " + str(palindrome))


def syllable(name, announce_name):
    while True:
        try:
            miles_question = input("Do you consider the word 'miles' to have one or two syllables?\n"\
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
    name_list = name.split(' ')
    shortened_name = ''
    for name in name_list:
        if name[-1] == 'e':
            name = name[:-1]
        shortened_name = shortened_name + " " + name
    vowel_count = 0
    most_recent_letter = ''
    for character in shortened_name:
        if character == '-':
            super_shortened_name = shortened_name.split('-')
            super_shortened_name = ' '.join(super_shortened_name)
            break
        else:
            super_shortened_name = shortened_name
    for letter in super_shortened_name:
        if (letter == 'a') or (letter == 'e') or (letter == 'i') or (letter == 'o') or (letter == 'u'):
            vowel_count = vowel_count + 1
            if letter == most_recent_letter:
                vowel_count = vowel_count - 1
            elif most_recent_letter == 'q' and letter == 'u':
                vowel_count = vowel_count - 1
        most_recent_letter = letter
    shortened_name_list = super_shortened_name.split(' ')
    if es_parser == True:
        for name in shortened_name_list[1:]:
            minus_1 = name[len(name)-1]
            minus_2 = name[len(name)-2]
            minus_4 = name[len(name)-4]
            minus_5 = name[len(name)-5]
            if (minus_1 == 's') and (minus_2 == 'e'):
                if (minus_4 == 'a') or (minus_4 == 'e') or (minus_4 == 'i') or (minus_4 == 'o') or (minus_4 == 'u'):
                    vowel_count = vowel_count - 1
                elif (minus_4 =='w') or (minus_4 =='y'):
                    if (minus_5 == 'a') or (minus_5 == 'e') or (minus_5 == 'i') or (minus_5 == 'o') or (minus_5 == 'u'):
                        vowel_count = vowel_count - 1
    
        
    print(announce_name + " syllables: " + str(vowel_count))
    
    
def reverse(name,announce_name):
    
    reversed_name = name[::-1]
    
    if announce_name == 'Full_name':
        name_list = reversed_name.split(' ')
        reversed_last_list = name_list[0]
        reversed_last_list = reversed_last_list.split('-')
        reversed_last = ''
        for name in reversed_last_list:
            name = my_capitalize(name)
            reversed_last = reversed_last + "-" + name
        reversed_last = reversed_last[1:]
        reversed_name = reversed_last
        for word in name_list[1:]:
            word = my_capitalize(word)
            reversed_name = reversed_name + " " + word
    if announce_name == 'First_name':
        reversed_name = my_capitalize(reversed_name)
    if announce_name == 'Middle_name':
        if name == '':
            print("No middle name provided")
        else:
            print(reversed_name)
            reversed_middle_list = reversed_name.split(' ')
            reversed_name = ''
            for name in reversed_middle_list:
                name = my_capitalize(name)
                reversed_name = reversed_name + " " + name
            reversed_name = reversed_name[1:]
    if announce_name == 'Last_name':
        reversed_last_list = reversed_name.split('-')
        reversed_name = ''
        for name in reversed_last_list:
            name = my_capitalize(name)
            reversed_name = reversed_name + "-" + name
        reversed_name = reversed_name[1:]
        
    print(announce_name + " Reversed: " + reversed_name)


def scramble(name, announce_name):
    
    word_list = name.split(' ')
    scrambled_name = ''
    for word in word_list:
        word = list(word)
        random.shuffle(word)
        word = ''.join(word)
        word = my_capitalize(word)
        scrambled_name = scrambled_name + " " + word
    return scrambled_name[1:]
    
        
        


if __name__ == '__main__':
    main()
