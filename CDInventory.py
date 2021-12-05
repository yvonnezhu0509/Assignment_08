#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# HongyiZhu, 2021-Nov-21, Added Contents into File
# HongyiZhu, 2021-Nov-26, Added Try-Except Constructs into File
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# HongyiZhu, 2021-Dec-04, Modified Contents in File
#------------------------------------------#

# -- DATA -- #
strFileName = "CDInventory.txt"
lstOfCDObjects = []
class CD:
    """Stores data about a CD:"""
    def __init__(self,cd_id,cd_title,cd_artist):
        """Method to store Args to attributes.
        
        Args:
            cd_id(integer): the ID of the CD;
            cd_title(string): the title of the CD;
            cd_artist(string): the artist name of the CD.
            
        Returns:
            None
        """
        self.__cd_id = cd_id
        self.__cd_title = cd_title
        self.__cd_artist = cd_artist
        
    @property
    def oneCD(self):
        """Function to property.
        
        Args:
            None
        Returns:
            cd(dict): use the format of dict to represent a CD.
        """
        return {'ID':self.__cd_id,'Title':self.__cd_title,'Artist':self.__cd_artist}

class FileIO:
    """Processing the data to and from text file"""
    @staticmethod
    def load_inventory(file_name):
        """Method to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.
        
        If the file gets removed or does not exist at all, then the “FileNotFound” error will occur and the program will return to menu.
        
        In the first column of CDInventory.txt text file, if the ID number here is not an integer, int(data[0]) will have the “ValueError”.
        “Try-except” construction can handle the error and print “invalid line, please modify the ID as integer”, then return to menu.

        Args:
            file_name (string): name of file used to read the data from cdInventory.txt
        Returns:
            table (list of dicts): a list of dicts which read from  
        """
        table = []
        try:
            objFile = open(file_name, 'r')
            for line in objFile:
                data = line.strip().split(',')
                dicRow = {'ID': int(data[0]), 'Title': data[1], 'Artist': data[2]}
                table.append(dicRow)
        except ValueError:
            print('The ID is not an integer, please correct it in txt file of '+ file_name)
            objFile.close()
            return table
        except FileNotFoundError:
            print('This file ' + file_name + ' does not exist,will create blank ' + file_name)
            objFile = open(file_name, 'w')
            objFile.close()
            return table
        objFile.close()
        return table
        
    @staticmethod
    def save_inventory(file_name, table):
        """Function to write the table to the file.

        Args:
             file_name (string): an string which is the file name that the user want to use for saving the data.
             table (list of dicts): a list of dicts which is the existed CDInventory 
        Returns:
             None.
        """

        objFile = open(file_name, 'w')
        for row in table:
            lstValues = list(row.values())
            lstValues[0] = str(lstValues[0])
            objFile.write(','.join(lstValues) + '\n')
    
        objFile.close()
        
# -- PRESENTATION (Input/Output) -- # 
class IO:
    @staticmethod
    def show_menu():
        """show menu to user

        Args:
            None.

        Returns:
            None.
        """
        print('\n\n---------------Menu-------------\n\n[d] show user current inventory\n[a] add data to the inventory\n[s] save inventory to file')
        print('[l] load inventory from file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """captures user's choice

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices d, a, s, l or x

        """
        choice = ' '
        while choice not in ['d', 'a', 's', 'l', 'x']:
            choice = input('Which operation would you like to perform? [d, a, s, l or x]: ').lower().strip()
        return choice

    @staticmethod
    def show_inventory(table):
        """display the current data on screen


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')


    @staticmethod
    def get_cd():
        """get CD data from user


        Args:
            None
            
        Returns:
            cd (dict):a dict like {'ID':1,'Title':'CD title','Artist':'CD artist'}

        """
        while True:
           intID = input("input an integer as CD ID:")
           if intID.isdigit():
              intID = int(intID)
              break
           else:
              print("please input an integer!")
        strTitle = input("input CD title:").strip()
        strArtist = input("input CD artist:").strip()
        cd = CD(intID,strTitle,strArtist).oneCD
        return cd

    @staticmethod
    def add_inventory(lstCD,cd):
        """add data to the inventory


        Args:
           lstCD (list of dict):a list of dicts which is the existed CDInventory
           cd (dict):a dict like {'ID':1,'Title':'CD title','Artist':'CD artist'} ,will add to lstCD
        Returns:
            None

        """
        lstCD.append(cd)

        
# -- Main Body of Script -- #
lstOfCDObjects = FileIO.load_inventory(strFileName)
while True:
    IO.show_menu()
    strChoice = IO.menu_choice()
    if strChoice == 'x':
       break
    if strChoice == 'd':
       IO.show_inventory(lstOfCDObjects)
       continue
    if strChoice == 'a':
       cd = IO.get_cd()
       IO.add_inventory(lstOfCDObjects,cd)
       IO.show_inventory(lstOfCDObjects)
       continue
    if strChoice == 'l':
       lstOfCDObjects = FileIO.load_inventory(strFileName)
       IO.show_inventory(lstOfCDObjects)
       continue
       print("WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.")
       strYesNo = input("type \'yes\' to continue and reload from file. otherwise reload will be canceled")
       if strYesNo.lower() == "yes":
          print("reloading...")
          lstOfCDObjects = FileIO.load_inventory(strFileName)
       else:
          input("canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.")
       IO.show_inventory(lstOfCDObjects)   
       continue 
    if strChoice == 's':
       FileIO.save_inventory(strFileName,lstOfCDObjects)
       IO.show_inventory(lstOfCDObjects)
       strYesNo = input("Save this inventory to file? [y/n] ").strip().lower()
       if strYesNo == 'y':
          FileIO.save_inventory(strFileName,lstOfCDObjects)
       else:
          input("The inventory was NOT saved to file. Press [ENTER] to return to the menu.")
       continue
