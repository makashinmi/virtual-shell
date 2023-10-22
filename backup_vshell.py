import zipfile
from custom_exceptions import *


class VShell:
    def __init__(self, filename: str):
        self.file = zipfile.ZipFile(filename)
        self.current_dir = zipfile.Path(self.file) 

    def _construct_path(self, path: str):
        steps = path.split('/')
        cur_dir = zipfile.Path(self.file) if path and path[0] == '/' else self.current_dir

        for step in steps:
            match step:
                case '':
                    pass
                case '..':
                    # 'root.zip/root/'.split('/') will return ['root.zip', 'root', '']
                    if len(cur_dir.at.split('/')) > 1:
                        cur_dir = zipfile.Path(cur_dir.root).joinpath('/'.join(cur_dir.at.split('/')[:-2]))
                    else:
                        pass
                case _:
                    if step in [dir_.name for dir_ in cur_dir.iterdir()]:  # somehow figure out if the step is in current dir
                        cur_dir = cur_dir.joinpath(f'{step}/')
                    else:
                        raise NoSuchFODError('


    def cat(self):
        pass

    def cd(self, path: str):

    def ls(self, path: str = ''):
        if path and path[0] == '/':
            target_path = zipfile.Path(file).joinpath(path)
        else:
            target_path = self.current_dir.joinpath(path)
        try:
            return list(dir_.name for dir_ in target_path.iterdir())
        except ValueError:
            return [f'{target_path}: No such file or directory']

    def pwd(self):
        return self.current_dir
