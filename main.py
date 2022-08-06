import subprocess

class ComputerRenamer:
    def __init__(self):
    
        self.domain = input('\nput the local domain without @ or \: ')
        self.username = input('\nput your username of domain: ')
        self.password = input('\nput your password: ')

       
    def get_serial_number(self, server):
        arguments = r"wmic bios get serialnumber"
        psexec = r'C:\\PSTools\\psexec \\'
        command = f'{server} {arguments}'
        cmd = psexec+command
        
        try:
            prompt = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE)
            result = prompt.communicate()[0].decode('utf-8')
            print(result)
                
        except:
            pass
        
        rename_computer = input('\nWant to rename the computer? y/n:\n ')
        
        if self.verify_confirmation(rename_computer, afirmation1='y', afirmation2='Y') == True:
            renamer.rename(server)
        else:
            pass
        
        repeat_command = input('\nDo you want start a new process? y/n:\n ')
        
        if self.verify_confirmation(repeat_command, afirmation1='y', afirmation2='Y') == True:
            loop = False
        if self.verify_confirmation(repeat_command, afirmation1='n', afirmation2='N') == True:
            loop = True        
        return loop
    
    def rename(self, old_name):
        
        new_name = input('\nenter the new machine name: ')
        command = r'netdom renamecomputer \\'
        try:
            cmd = command+old_name+f' /newname: {new_name} /userd:{self.domain}\{self.username} /passwordd:{self.password} /reboot 0 /force'
            
        except:
            pass
        confirm = input(f'\nyou really want to change the name of computer {old_name} to {new_name}? y/n:\n ')
        if self.verify_confirmation(confirm, 'y', 'Y') == 'y':
            
            process = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE)
            output = process.communicate()[0]
            print('\n', output)
        

    def verify_confirmation(self, confirmation, afirmation1, afirmation2):
        if confirmation == afirmation1 or confirmation == afirmation2:
            return True
        
renamer = ComputerRenamer()
loop = False

while loop == False:
    computer_name = input('\nPut the name of the computer: ')
    loop = renamer.get_serial_number(computer_name)
    