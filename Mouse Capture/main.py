from win32 import win32gui
from time import localtime, sleep
from os.path import dirname
from os import makedirs, system, listdir, remove
import mouse

system('cls')
TIME = str(localtime().tm_year) +'_'+ str(localtime().tm_mon) +'_'+ str(localtime().tm_mday) +'_'+ str(localtime().tm_hour)
LOG_FILE_DIR = str(dirname(__file__)) + '\\log\\'
FILE_ADDR = LOG_FILE_DIR + TIME + '_'

# Making Sure LOG Folder is created
try:
    f = open(FILE_ADDR + str(localtime().tm_min) + '.txt', 'a')
    f.close()
    remove(FILE_ADDR + str(localtime().tm_min) + '.txt')
# If not, Create a LOG Folder
except:
    makedirs(LOG_FILE_DIR)

SECOND_TO_CAPTURE = 10 # 10 MIN of recording mouse movements
# 1 SECONDs wait before capture next mouse position
SECOND_TO_WAIT = 1/50 # SETTING INTEGERES LARGER THAN 1 WILL MAKE THE APP FAIL!!!
CLEAR = 'cls' # This Used to clear screen, if using Linux use "clear"

# MAIN LOOP
while 1:
    system(CLEAR)
    # Menu
    choice = 123456789
    while choice != 1 and choice != 2 and choice != 3:
        print('Enter 1: Start Mouse Recording.')
        print('Enter 2: Start Mouse Performing.')
        print('Enter 3: Exit the App')
        choice = int(input('>>> '))
        if choice != 1 and choice != 2 and choice != 3 and choice != 123456789:
            print('Wrong Input!!')
            sleep(1)
            system(CLEAR)

    # Capturing
    if choice == 1:
        system(CLEAR)
        # Getting prefered Second to capture
        while 1:
            try:
                SECOND_TO_CAPTURE = int(input('How many seconds you want to Capture?\n>>> '))
            except:
                print('You should enter an integer!!')
                sleep(1)
                continue
            break
        # Started to Capture 
        for i in range(int(SECOND_TO_CAPTURE * (1//SECOND_TO_WAIT))):
            cur_min = localtime().tm_min # store Current minute
            with open(FILE_ADDR + str(cur_min) + '.txt', 'a') as cur_file:
                flags, hcursor, (x,y) = win32gui.GetCursorInfo()
                print(x, y)
                mouse_pos =  ' ' + str(x) + ' ' + str(y)
                cur_file.write(str(localtime().tm_sec) + mouse_pos + '\n')
                sleep(SECOND_TO_WAIT)
        print('Recording is Finished!!')
        sleep(1)

    # Exit the program
    if choice == 3:
        print('Have a Happy Day!! :)')
        sleep(2)
        break

    # Performing recorded mouse movement
    if choice == 2:
        if listdir(path=LOG_FILE_DIR): # Check we have at least one record
            # Getting a file name
            while 1:
                system(CLEAR)
                try:
                    print('These files are recorded:\n\t', end='')
                    print(*listdir(path=LOG_FILE_DIR), sep='\n\t')
                    cur_file = input('Which file do you want to perform its movements?\n>>> ')
                    if cur_file not in listdir(path=LOG_FILE_DIR):
                        raise Exception('404')
                except Exception as exp:
                    if exp.args[0] == '404':
                        print('File Not Found!! Try Again...')
                        sleep(1)
                        continue
                    else:
                        print('Unkown Error Occured!!')                    
                        sleep(1)
                        continue
                break
            
            # Start Performing
            system(CLEAR)
            print('Running Mouse Movements of ',cur_file)
            with open(LOG_FILE_DIR + cur_file, 'r') as cur_file:
                lines = cur_file.readlines()
                for line in lines:
                    t, x, y = line.split()
                    print(t, x, y)
                    mouse.move(x,y)
                    sleep(SECOND_TO_WAIT)
            print('Performing is Finished!!')

        else:
            print('No Record history, Start a record first.!')
        sleep(2)