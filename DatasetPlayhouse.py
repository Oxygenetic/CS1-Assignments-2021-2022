'''
Created on 14 Apr 2022
@author: FHentsch-Cowles24
Description:
    Playing with large amounts of data. This program can read any csv file in the same directory. Using a
variety of searching and rewriting functions, the DatasetPlayhouse can find any field value in any row of
the file, add or delete rows, or change specific values within a field of a row. The user always has the
option to change their file while the program is running..

Log:
    -4/14/2022-5/11/2022: Creating fundamental functions which define the groundwork of the program.
    -5/12/2022: All code up to this point (line 374) reviewed and documented. (I learned my lesson).
    -5/13/2022: Match result percentile feature added to search and advanced queries.
    -5/16/2022: Changed open file catch 'FileNotFoundError' to 'OSError' in order to catch invalid
                file inputs.
    -5/16/2022: Copied variable assignments of row_total, available_fields, and field_count inside of
                main so that added rows are considered in edit row without having to reselect the
                original file name.
    -5/17/2022: Added row reference numbers to accompany printed rows in dataset preview.
Bugs:
    
Initiatives:
    -Code is well organized by pseudo, functions, and descriptions.
    -Can update and change information in fields in records of the database
    -Can delete records from the database
    -Program repeats
    -Main menu
    -User can not only enter filename, but change the file during the program run
    -Advanced search function which can search for rows with shared values from multiple fields
    -Can preview the dataset
    -Can read any csv file and automatically adapt regardless of its fields
    -Can read by a '|' delimiter so that name values with commas (last, first) aren't split into separate
     fields
    -Creates a temporary 'program_file' to read from so that original file formats and values are preserved
    -Provides search query match result percentiles

Last edited on 05/17/2022
'''
import csv

def main():
    '''Description:
    Main function which retrieves the file and calls the program, assigning variables which
    will be used to read and manipulate the file.
    '''
    named_file = file_namer()                                                               #Retrieves user input for file name
    open_file = file_opener(named_file)                                                     #Assigns an open file
    available_fields = field_reader(open_file)                                              #Creates a list of fields in the file
    open_file = reader_reset(open_file)                                                     #Closes and re-opens file
    field_count = field_counter(available_fields)                                           #Assigns total number of fields in file
    row_total = str(row_counter(open_file))                                                 #Assigns total number of rows in file
    open_file = reader_reset(open_file)                                                     #Closes and re-opens file
    
    menu(available_fields, field_count, open_file, row_total,named_file)                    #Calls main menu

def menu(available_fields,field_count,open_file,row_total,named_file):
    '''Description:
    Main menu is a loop that provides user with a range of executable program functions.
    
    Arg1 (available_fields): All available fields
    Arg2 (field_count): Number of fields
    Arg3 (open_file): The open file
    Arg4 (row_total): Number of rows
    Arg5 (named_file): Name of file originally opened
    '''

    while True:
        open_file = reader_reset(open_file)                                                 #Resets open file at the start of each loop
        open_file = file_opener(named_file)                                                 #Re-opens file at the beginning of each loop
        available_fields = field_reader(open_file)                                          #Creates a list of fields in the file
        open_file = reader_reset(open_file)                                                 #Closes and re-opens file
        field_count = field_counter(available_fields)                                       #Assigns total number of fields in file
        row_total = str(row_counter(open_file))                                             #Assigns total number of rows in file
        open_file = reader_reset(open_file)                                                 #Closes and re-opens file
        try:
            task = input("Main Menu ("+named_file+")\n"\
                         "1 - Preview Dataset (view 1st 10 items)\n"\
                         "2 - Search query\n"\
                         "3 - Advanced search query\n"\
                         "4 - Add or delete row\n"\
                         "5 - Edit field in row\n"
                         "x - Change file\n")                                               #Main menu user interface
            if task == str(1):                                                              #Previews first ten rows of file
                dataset_preview(open_file)
                open_file = reader_reset(open_file)
            elif task == str(2):                                                            #Search using a single field criteria
                search_query(available_fields,field_count,open_file,row_total)
                open_file = reader_reset(open_file)
            elif task == str(3):                                                            #Search using multiple field criteria
                advanced_search(available_fields,field_count,open_file,row_total)
                open_file = reader_reset(open_file)
            elif task == str(4):                                                            #Add or delete rows to a named file
                open_file = writer_main(open_file,available_fields,field_count,row_total,named_file)
                file_info = str(open_file)
                print("New file with changes created:\n"+file_info+"\n")
            elif task == str(5):                                                            #Edit values within columns of rows in current file
                open_file = row_editor(row_total, available_fields, field_count, open_file, named_file)
                file_info = str(open_file)
                print("Current file edited:\n"+file_info+"\n")
            elif task == str('x'):                                                          #Reset program to choose a different file
                main()
            else:
                raise AttributeError
        except AttributeError:
            print("Invalid task. Enter a number.")

def search_query(available_fields,field_count,open_file,row_total):
    '''Description:
    Search query allows user to search for a value in a single field throughout every
    row in the file. User is asked to select a field and then choose the value they
    wish to search for.
    
    Arg1 (available_fields): All available fields
    Arg2 (field_count): Number of fields
    Arg3 (open_file): The open file
    Arg4 (row_total): Number of rows
    '''
    field = field_selector(available_fields, field_count)                                   #User selects field
    match_count = field_searcher(field, open_file,available_fields)                         #User selects search value
    if match_count != 'No Match':
        percentage = round((int(match_count)/int(row_total))*100,1)                             #Finds the match percentile within the row total
        print("Matching Results: "+str(match_count)\
              +"/"+row_total+" ("+str(percentage)+"%)\n")                                       #Print number of matching results
    else:
        print("No match")

def field_selector(available_fields,field_count):
    '''Description:
    Field selector allows user to input the field in which they wish to search. Once
    the string of the desired field is known, the field assign function finds the
    field's reference number according to the field count, which is later used when
    reading through rows and identifying desired values within the respective field.
    
    Arg1 (available_fields): All available fields
    Arg2 (field_count): Number of fields
    
    Return (field): Returns the selected field in its 'field count form', which
    facilitates reading rows for values later on.
    '''
    while True:
        try:
            field_choose = input("Enter one of the data fields below:\n"\
                       +str(available_fields)+"\n"\
                       +str(field_count)+" Fields"+"\n")                                    #Available fields are shown to user and they are prompted to choose
            select_field = field_choose.lower()
            field = field_assign(select_field,available_fields)                             #Reads input and matches it with its reference number
            if field == 'invalid':                                                          #If field assign does not recognize input as an existing field, try loop is repeated
                raise AttributeError
            else:
                return field                                                                #Returns the selected field as an integer location in field count
                break
        except AttributeError:
            print("Invalid Field")

def file_namer():
    '''Description:
    File namer prompts the user to select the file they would like to use for the
    program. It makes sure that the input includes a .csv at the end, to ensure that the
    correct type of file is given.
    
    Return (file_choose): Returns the chosen file name.
    '''
    while True:
        try:
            file_choose = input("Enter filename.csv:\n"\
                                "(must be in same directory)\n")
            if file_choose[-4:] == '.csv':                                                  #If input ends in .csv, it is returned
                return file_choose
            else:                                                                           #Repeats prompt if input does not end in .csv
                raise AttributeError
        except AttributeError:
            print("Must end in '.csv'")
    
def file_opener(file_choose):
    '''Description:
    File opener opens and reads the file_name retrieved by file namer and then rewrites
    it into a new file (program_file.csv), setting the new delimiter as '|'. This
    delimiter is used so that the program's search queries will not confuse commas in
    'Last, First' names,splitting them as two separate fields. The use of the program
    file ensures that the original file will not be permanently changed unless one of
    the adding, deleting, or editing functions are used. It is a temporary file that
    makes original files readable by the program.
    
    Arg1 (file_choose): File choose is the file name provided by the user
    
    Return [open('program_file.csv')]: Program file is returned as a readable copy of
                                       the file originally provided.
    '''
    while True:
        try:
            with open(file_choose, newline='') as raw_file, open('program_file.csv', 'w', newline='') as outfile:
                reader = csv.reader(raw_file, delimiter=',')                                #Reads the chosen file
                writer = csv.writer(outfile, delimiter='|')                                 #Prepares to write the program file using '|' as delimiter
                for row in reader:                                                          #Rewrites every row from chosen file to program file
                    writer.writerow(row)
            return open('program_file.csv')                                                 #Returns program file for the program to use as open file
            break
        except OSError:                                                           #Restarts the program if the chosen file could not be found in the directory
            print("File not found")
            main()

def field_reader(open_file):
    '''Description:
    Field reader creates a list of fields by reading the first row of the csv file and
    assuming that it titles the fields for each column. It splits the row by the '|'
    delimiter and appends each value as a field in a list called fields. If there is an
    UnboundLocaError, the file is empty and the program is restarted.
    
    Arg1 (open_file): The open file (now program file)
    
    Return (fields): Returns the list of fields in the dataset.
    '''
    try:
        fields = []
        for row in open_file:                                                               #Reads and splits first row in file. Breaks after first loop
            items = row.split('|')
            break
        for item in items:                                                                  #Adds each field from first row into the fields list
            stripped = item.strip()
            fields.append(stripped)
        return fields                                                                       #Returns the field list to the program
    except UnboundLocalError:                                                               #Restarts program if file is empty
        print("This file is empty!")
        main()

def field_counter(available_fields):
    '''Description:
    Field counter simply counts the number of fields (columns) that are in the open
    file. Using available fields, it adds to the count for each field in the list.
    
    Arg1 (available_fields): All available fields
    
    Return (count): Returns the number of fields in available fields
    '''
    count = 0
    for field in available_fields:
        count = count + 1
    return count

def row_counter(open_file):
    '''Description:
    Row counter counts the number of rows in the open file. For each row in open file,
    one is added to the count.

    Arg1 (open_file): The open file
    
    Return (count): Returns the row count to the program
    '''
    count = -2
    for row in open_file:
        count = count + 1
    return count

def field_assign(select_field,available_fields):
    '''Description:
    Field assign assigns the field selected from available fields an integer according to
    its location in the list of fields. 
    
    Arg1 (select_field): Field selected by user in field selector
    Arg2 (available_fields): All available fields
    
    Return (count): Returns location of selected field in available fields
    Return (0): Returns 0 if a count higher than 0 is not returned
    Return ('invalid'): Returns invalid if selected field is not matched with an available field
    '''
    count = -1
    try:
        while select_field != available_fields[0].lower():
            count = count + 1
            if select_field == available_fields[count].lower():                             #If selected field matches a field in the list indexed by count return count as location
                return count
        return 0
    except IndexError:
        return 'invalid'

def field_searcher(field,open_file,available_fields):
    '''Description:
    Field searcher prompts the user to input the value they would like to search for.
    Using field and available fields, it prints rows whose value of a respective field
    match the value provided by the user. Apart from printing the row, a result count is
    kept and returned.
    
    Arg1 (field): Field location gathered from field assign
    Arg2 (open_file): The open file
    Arg3 (available_fields): All available fields
    
    Return (result_count): Returns the count of total rows whose field values match the search query.
    '''
    field_name = available_fields[field]
    field_search = input("Enter value you would like to search for"\
                         " in the '"+field_name+"' field.\n")
    field_search = field_search.lower()
    result_count = 0
    field_count = -1
    for row in open_file:                                                                   #Reads each row in the open file
        field_count = field_count + 1
        row_field = row.split('|')                                                          #Splits rows by the '|' delimiter
        safe_row_field = []                                                                 #Creates a list which will store stripped rows
        for unstripped_row in row_field:                                                    #Removes any newlines from row values and adds products to safe row list
            stripped_row = unstripped_row.replace('\n','')
            safe_row_field.append(stripped_row)
        if str(safe_row_field[field]).lower() == str(field_search):                         #If row field value matches field search, count increases by one and print row
            result_count = result_count + 1
            print("[Ref. "+str(field_count)+"]\n"+row)                                      #Prints the row with a reference number, which is its line location within the file
    if result_count == 0:                                                                   #If there are no matches, 'No Match' is returned as result_count
        result_count = 'No Match'
    return result_count

def reader_reset(open_file):
    '''Description:
    Reader reset closes the open file and re-opens it. This is essential, as once the
    open file is read it must be reset so that the reader starts from the beginning.
    
    Arg1 (open_file): File that is currently open
    
    Return [open(file_name)]: Returns the open file
    '''
    file_name = (open_file.name)
    open_file.close()
    return open(file_name)

def dataset_preview(open_file):
    '''Description:
    Dataset preview prints the first ten rows of the file (exluding the first 'field'
    row) so that the user can get a sample of the information stored.
    
    Arg1 (open_file): The open file
    '''
    count = 0
    for row in open_file:
        count = count + 1
        print("[Ref. "+str(count-1)+"]\n"+row)
        if count == 11:                                                                     #Loop stops at 10 rows
            break

def advanced_search(available_fields,field_count,open_file,row_total):
    '''Description:
    Advanced search allows the user to make a search query providing a field value in
    multiple fields. Similar to the search query function, the advanced search prints
    matching rows and prints the result/match count.
    
    Arg1 (available_fields): All available fields
    Arg2 (field_count): Number of fields
    Arg3 (open_file): The open file
    Arg4 (row_total): Number of rows
    '''
    loop = True
    field_list = []
    while loop == True:                                                                     #A loop that allows the user to choose multiple fields to search with
        try:
            decision = input("Enter 'yes' to add a field to the search.\n"\
                             "Enter 'done' to continue with the search.\n")
            decision = decision.lower()
            if decision == 'yes':                                                           #If yes, runs the field selector and adds the chosen field to a list
                add_field = field_selector(available_fields, field_count)
                field_list.append(add_field)
            elif decision == 'done':                                                        #If done, proceeds to request for search values with the chosen fields
                loop = False
                break
            else:
                raise AttributeError
        except AttributeError:
            print("Invalid response.")
    count = 0
    valid_rows = []                                                                         #A list that will contain locations of rows that match any of the field searches
    for field in field_list:
        count = count + 1
        valid_rows.extend(value_locator(field,available_fields,open_file))                  #Value locator finds the row locations of matching field values
        open_file = reader_reset(open_file)
        
    matching_rows = set([row for row in valid_rows if valid_rows.count(row) > count-1])     #Assigns row locations that matched for every field search to matching rows
    matching_results = list(matching_rows)                                                  #Converts matching rows a list
    target_results = []
    for result in matching_results:                                                         #Transfers values from matching rows to target results as integers
        target_results.append(int(result))
    target_results.sort()                                                                   #Sorts the integers (matching row locations) in numerical order
    match_count = 0
    for result in target_results:                                                           #Uses field seeker to find and print each matching row in open file by its location
        match_count = match_count + 1                                                       #Adds to match count
        field_seeker(result, open_file)
        open_file = reader_reset(open_file)                                                 #Resets the open file each time for re-reading
    if match_count == 0:                                                                    #If no matches, print no match
        print("No Match\n")
    else:        
        percentage = round((int(match_count)/int(row_total))*100,1)                         #Finds the match percentile within the row total                                                                           #If there are matches, print the result/match count
        print("Matching Results: "+str(match_count)\
          +"/"+row_total+" ("+str(percentage)+"%)\n")

def value_locator(field,available_fields,open_file):
    '''Description:
    Value locator is used to find and return the location of rows whose field values
    match the field search. User input is request to determine the field search.
    
    Arg1 (field): Field location provided
    Arg2 (available_fields): All available fields
    Arg3 (open_file): The open file
    
    Return (valid_rows): Returns all rows whose field values match the field search.
    '''
    field_name = available_fields[field]
    field_search = input("Enter value you would like to search for"\
                          " in the '"+field_name+"' field.\n")
    field_search = field_search.lower()
    row_location = 0
    valid_rows = []
    
    for row in open_file:                                                                   #Splits field values in each row by delimiter '|'
        row_location = row_location + 1
        row_field = row.split('|')
        safe_row_field = []                                                                 #Creates a list to store stripped rows
        for unstripped_row in row_field:                                                    #Strips rows by using replace() to remove newlines in field values
            stripped_row = unstripped_row.replace('\n','')
            safe_row_field.append(stripped_row)
        if str(safe_row_field[field]).lower() == str(field_search):                         #If row field value matches field search, append row location to valid rows list
            valid_rows.append(row_location)
    return valid_rows

def field_seeker(result,open_file):
    '''Description:
    Field seeker uses result, a provided row location, to print that row.
    
    Arg1 (result): Provided row location
    Arg2 (open_file): The open file
    '''
    count = 1
    for row in open_file:
        if count == result:
            print("[Ref. "+str(result-1)+"]\n"+row)
            break
        count = count + 1

def writer_main(open_file,available_fields,field_count,row_total,named_file):
    '''Description:
    Writer main serves as a menu for adding or delete rows. It calls upon add or delete
    row functions and stores their outputs in their respective lists. Those lists are
    then utilized by new file maker to read and rewrite the current file with the user's
    changes under a chosen file name.

    Arg1 (open_file): The open file
    Arg2 (available_fields): All available fields
    Arg3 (field_count): Number of fields
    Arg4 (row_total): Number of rows
    Arg5 (named_file): Name of file originally opened
    
    Return (open_file): Returns the file written by new file maker.
    '''
    loop = True
    added_rows = []                                                                         #Creates list to store user's added rows
    deleted_rows = []                                                                       #Creates list to store user's deleted row locations
    while loop == True:
        try:
            decision = input("Enter 'add' to add a row.\n"\
                             "Enter 'delete' to delete a row.\n"\
                             "Enter 'done' to continue.\n")
            decision = decision.lower()
            if decision == 'add':                                                           #If add, calls add row to customize new row
                row = add_row(available_fields, field_count)
                added_rows.append(row)
            elif decision == 'delete':                                                      #If delete, calls row referencer to take location of deleted row
                ref_row = row_referencer(row_total)
                deleted_rows.append(ref_row)
            elif decision == 'done':                                                        #If done, proceeds to call new file maker
                loop = False
                break
            else:
                raise AttributeError
        except AttributeError:
            print("Invalid response.")
    open_file = new_file_maker(open_file, added_rows,available_fields,field_count,row_total,deleted_rows,named_file)
    return open_file

def add_row(available_fields,field_count):
    '''Description:
    Add row asks user which values they would like for each field of their row and then
    returns a complete list of all row values in order.

    Arg1 (available_fields): All available fields
    Arg2 (field_count): Number of fields
    
    Return (row_values): Returns a list of chosen row values for each field.
    '''
    count = 0
    row_values = []                                                                         #Creates list to store all row field values
    while count < field_count:                                                              #Continues to accept row values until number of fields is reached
        target_field = available_fields[count]
        count = count + 1
        decision = input("Set value for the "\
                         +target_field+" field.\n")
        row_values.append(str(decision))
    return row_values

def row_referencer(row_total):
    '''Description:
    Row referencer is very useful for accepting a row's reference number, which is
    essentially its line location in the file. It does not accept inputs that are not an
    integer within the range of the file's row total count.

    Arg1 (row_total): Number of rows

    Return (chosen_row): Returns the chosen row location (ref. number) if it is within the row total range.
    '''
    try:
        decision = input("Enter a row reference number.\n")
        chosen_row = int(decision)
        
        row_total = int(row_total)+2
        row_range = range(0,row_total)
        if chosen_row in row_range:
            return chosen_row
        else:
            raise AttributeError
    except AttributeError:
        print("Invalid response. Must be within range of rows.")

def new_file_maker(open_file,added_rows,available_fields,field_count,row_total,deleted_rows,named_file):
    '''Description:
    New file maker asks the user for a desired file name under which their add/delete
    row changes will be written. They can choose to cancel and return to menu as well.
    Once a new file name is provided (the current file name can also be used to
    overwrite it), the current open file is read and the chosen file name is written.
    Every current row in open file is written to the new file except for rows with a
    location that exists in the deleted rows list. Finally, all added rows are written
    at the end of the new file. The new file is returned.

    Arg1 (open_file): The open file
    Arg2 (added_rows): List of rows to add to the new file
    Arg3 (available_fields): All available fields
    Arg4 (field_count): Number of fields
    Arg5 (row_total): Number of rows
    Arg6 (deleted_rows): List of row locations to exclude from the new file
    Arg7 (named_file): Name of file originally opened
    
    Return (new_file_name): Returns the new file written.
    '''
    valid_rows = list()                                                                     #Valid rows is a list of all the rows that will be included in the new file
    while True:
        try:
            file_choose = input("Enter a new file name:\n"\
                                "(must end in '.csv')\n"\
                                "*Enter 'x' to cancel*\n")
            if file_choose[-4:] == '.csv':
                new_file_name = file_choose
                break
            elif file_choose == 'x':                                                        #Returns user to main menu
                menu(available_fields, field_count, open_file, row_total,named_file)
            else:
                raise AttributeError
        except AttributeError:
            print("Must end in '.csv'")
    
    with open(open_file.name, newline='') as infile, open(new_file_name, 'w', newline='') as outfile:
        reader = csv.reader(infile, delimiter = '|')                                        #Reads open file
        
        for row_number, row in enumerate(reader, start=0):                                  #Appends all rows to valid rows except for deleted rows
            if(row_number not in deleted_rows):
                valid_rows.append(row)
        
        writer = csv.writer(outfile)                                                        #Writes new file
        writer.writerows(valid_rows)                                                        #Writes all valid rows to new file
        for row in added_rows:                                                              #Adds every row in added rows to new file
            writer.writerow(row)
    return open(new_file_name)

def row_editor(row_total,available_fields,field_count,open_file,named_file):
    '''Description:
    Row editor edits specific values within specific fields of specific rows. Using row
    referencer, it asks the user to select which row they would like to edit. Then it
    calls field selector to allow the user to choose which field value they would like
    to change. Finally, the user is prompted to enter the desired value, which would
    replace the current value.

    Arg1 (row_total): Number of rows
    Arg2 (available_fields): All available fields
    Arg3 (field_count): Number of fields
    Arg4 (open_file): The open file
    Arg5 (named_file): Name of file originally opened
    
    Return (open_file): Returns an edited open file
    '''
    row_ref = row_referencer(row_total)                                                     #Row is selected
    field_ref = field_selector(available_fields,field_count)                                #Field is selected
    desired_value = input("Enter desired value for Row "\
                          +str(row_ref)+" field "+available_fields[field_ref]+".\n"\
                          "(Case-sensitive)\n")                                             #Value is selected
    row_count = -1
    edited_row = []                                                                         #Creates a list to store values of the edited row
    for row in open_file:
        row_count = row_count + 1
        row_field = row.split('|')                                                          #Splits row in open file into row field values
        safe_row_field = []                                                                 #Creates a list to store stripped row values
        count = -1
        if row_count == row_ref:                                                            #If the count matches the row location (ref. number):
            for unstripped_row in row_field:                                                #Removes any newlines from row values
                stripped_row = unstripped_row.replace('\n','')
                safe_row_field.append(stripped_row)                                         #Adds stripped row values to safe row field list
            for field in safe_row_field:                                                    #For each value in row, looks for specific chosen field
                count = count + 1
                if count == field_ref:                                                      #Appends the desired value to edited row when chosen field is matched
                    edited_row.append(desired_value)
                else:                                                                       #When chosen field is not matched, current values are appended to edited row
                    edited_row.append(field)
    valid_rows = list()                                                                     #Creates list to store rows which will be written
    with open(open_file.name, newline='') as infile, open(named_file, 'w', newline='') as outfile:
        reader = csv.reader(infile, delimiter = '|')                                        #Read open file
        for row_number, row in enumerate(reader, start=0):                                  #For each row location in open file:
            if(row_number != row_ref):                                                      #If location is not the chosen edited row append the normal row
                valid_rows.append(row)
            else:                                                                           #Otherwise, append the edited row
                valid_rows.append(edited_row)
        writer = csv.writer(outfile)                                                        #Write originally named file
        writer.writerows(valid_rows)                                                        #Writes all valid rows
    open_file = open(open_file.name)
    return open_file

if __name__ == '__main__':
    main()