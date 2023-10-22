import zipfile
import custom_exceptions as ce


class VShell:
    def __init__(self, filename: str):
        self.file = zipfile.ZipFile(filename)
        self.current_dir = zipfile.Path(self.file) 

    def _construct_path(self, path: str):
        steps = path.split('/')
        cur_path = zipfile.Path(self.file) if path and path[0] == '/' else self.current_dir
        for step in steps:
            match step:
                case '':
                    pass
                case '..':
                    # 'root.zip/root/'.split('/') will return ['root.zip', 'root', '']
                    if len(cur_path.at.split('/')) > 1:
                        cur_path = zipfile.Path(cur_path.root).joinpath('/'.join(cur_path.at.split('/')[:-2]))
                    else:
                        pass
                case _:
                    cur_path = cur_path.joinpath(f'{step}')

                    if cur_path.exists(): continue
                    else: raise ce.NoSuchFODError(path) 
        return cur_path

    def _assure_is_file(func):
        def wrapper(self, path_input: str, path: zipfile.Path):
            if path.is_file():
                return func(self, path)
            raise ce.NotAFileError(f'{func.__name__}: {path_input}')
        return wrapper

    def _assure_is_dir(func):
        def wrapper(self, path_input: str, path: zipfile.Path):
            if path.is_dir():
                return func(self, path)
            raise ce.NotADirectoryError(f'{func.__name__}: {path_input}')
        return wrapper

    def _validate_path(func):
        def wrapper(self, path_input: str):
            try:
                target_path = self._construct_path(path_input)
                result = func(self, path_input, target_path)
            except ce.NoSuchFODError as error:
                return f'{error}: No such file or directory'
            except ce.NotADirectoryError as error:
                return f'{error}: Not a directory'
            except ce.NotAFileError as error:
                return f'{error}: Not a file'
            else:
                return result 
        return wrapper

    @_validate_path
    @_assure_is_file
    def cat(self, path: zipfile.Path):
        with self.file.open(path.at) as file:
            return ''.join((line.decode('utf-8') for line in file.readlines()))

    @_validate_path
    @_assure_is_dir
    def cd(self, path: zipfile.Path):
        self.current_dir = path

    @_validate_path
    @_assure_is_dir
    def ls(self, path: zipfile.Path):
        return list(dir_.name for dir_ in path.iterdir())

    def pwd(self):
        return f'/{"".join(self.current_dir.at.split("/"))}'
