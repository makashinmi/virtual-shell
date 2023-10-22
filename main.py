import sys
from zipfile import BadZipFile
from vshell import VShell

if __name__ == '__main__':
    try:
        target_filename = sys.argv[1]
        vsh = VShell(target_filename)
    except IndexError:
        print('No zip file provided')
    except FileNotFoundError:
        print(f'No such file: {target_filename}')
    except BadZipFile:
        print(f'Not a zip file: {target_filename}')
    else:
        print('\n' * 100)

        while 2 + 2 != 5:
            try:
                command_input = input(f'[vsh@{vsh.file.filename} {"/" if vsh.current_dir.name == vsh.file.filename else vsh.current_dir.name}] > ').split()
            except KeyboardInterrupt:
                vsh.file.close()
                print('\nExiting...')
                break
            else:
                if command_input:
                    command = command_input[0]
                    args = command_input[1:] if len(command_input) > 1 else ['']
                command_output = None

                match command:
                    case 'cat':
                        command_output = vsh.cat(args[0])
                    case 'cd':
                        command_output = vsh.cd(args[0])
                    case 'ls':
                        command_output = vsh.ls(args[0])
                        # ls may return both a list of files and a string with an exception's message
                        command_output = '\t'.join(command_output) if type(command_output) is list else command_output
                    case 'pwd':
                        command_output = vsh.pwd()
                    case '':
                        pass
                    case _:
                        print(f'Unknown command: {command}')

                if command_output:
                    print(command_output)
