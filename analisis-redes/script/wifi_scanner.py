import subprocess
import re 


class Terminal:
    '''
        :command(str) sudo iwlist wlan0 scanning    
    '''
    def __init__(self):
        self._response: str = '' 
        self._command  = None

    def _unpack_response(self):
        pass
    
    def _split_command(self, command):
        command = command.strip()
        if command == '':
            raise ValueError('Without command')
        return command.split()

    def run(self, command: str):
        self._command = self._split_command(command)
        self._response = subprocess.run(
            self._command,
            check=True,
            stdout=subprocess.PIPE,
            universal_newlines=True
        )
        print(self._response)
        
if __name__=='__main__':
    
    ter = Terminal()

    while True:
        try:
            command = input('> ')
            ter.run(command)
        except Exception as e:
            print(e)
