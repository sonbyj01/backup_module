#!/usr/bin/env python3
from pathlib import Path
import hashlib
import sys


class SourceFiles:
    def __init__(self, source):
        if Path(source).is_absolute():
            self.source_path = Path(source)
        else:
            current_directory = Path.cwd()
            self.source_path = Path.joinpath(current_directory, source)

        self.records_text_name = 'records.txt'
        self.records_text_path = Path.joinpath(self.source_path, self.records_text_name)

        try:
            with open(self.records_text_path, 'r', encoding='utf-8') as f:
                self.hash = f.readline()
        except FileNotFoundError as fnf:
            pass

        self.records_file = []
        self.records_folder = []
        self.records = {}

        # keeps track of each path and whether it's a file/folder
        for path in self.source_path.glob('**/*'):
            if path.is_file():
                if path != self.records_text_path:
                    self.records[path] = 0
                    self.records_file.append(path)

            elif path.is_dir():
                self.records[path] = 1
                self.records_folder.append(path)

        # self._generate_hash()
        self.generate_text_file()

    def _generate_hash(self):
        self.hash = hashlib.md5()
        for record in self.records.keys():
            if record != self.records_text_path:
                self.hash.update(str(record).encode('utf-8'))

    def get_record(self):
        return self.records

    def generate_text_file(self, path=None):
        if path is None:
            absolute_path = self.source_path
        elif Path(path).is_absolute():
            absolute_path = Path(path)
        else:
            absolute_path = Path.joinpath(self.source_path, path)

        file = Path.joinpath(absolute_path, self.records_text_name)

        with open(file, 'w', encoding='utf-8') as f:
            # f.write('{}{}'.format(self.hash.hexdigest(), '\n\n'))
            f.write('Directories\n')
            for folder in self.records_folder:
                f.write('{}{}'.format(str(folder), '\n'))
            f.write('\nFiles\n')
            for file in self.records_file:
                f.write('{}{}'.format(str(file), '\n'))
