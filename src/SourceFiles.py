#!/usr/bin/python3
from pathlib import PurePath, Path, PurePosixPath, PureWindowsPath


class SourceFiles:
    def __init__(self, source):
        source_paths = Path(source)
        self.records_file = []
        self.records_folder = []
        self.records = {}

        # keeps track of each path and whether it's a file/folder
        for path in source_paths.iterdir():
            if path.is_file():
                self.records[path] = 0
                self.records_file.append(path)
            elif path.is_dir():
                self.records[path] = 1
                self.records_folder.append(path)

    def get_record(self):
        return self.records

    '''
    
    '''
    def to_text_file(self, path):
        if path.is_absolute():
            file = Path(path)
        else:
            current_directory = Path.cwd()
            absolute_path = Path.joinpath(current_directory, path)
            file = Path.joinpath(absolute_path, 'textfile.txt')

        with open(file, 'w', encoding='utf-8') as f:
            f.write('Directories\n')
            for folder in self.records_folder:
                f.write('{}{}'.format(str(folder), '\n'))
            f.write('\nFiles\n')
            for file in self.records_file:
                f.write('{}{}'.format(str(file), '\n'))
