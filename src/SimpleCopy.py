#!/usr/bin/python3
from shutil import copy2
from pathlib import Path
from .SourceFiles import SourceFiles


class SimpleCopy:
    def __init__(self, source):
        assert isinstance(source, SourceFiles), 'Not a SourceFiles object.'
        self.source_object = source

    def _make_directory(self, target):
        self.target_folder = Path(target)
        if not self.target_folder.exists():
            self.target_folder.mkdir(parents=True)

    def simple_copy2(self, target):
        self._make_directory(target)
        # self.source_object.to_text_file(target_folder)

        for folder_path in self.source_object.records_folder:
            print('4')
            source_drive = folder_path.anchor
            source_folder = Path(folder_path)
            source_relative = source_folder.relative_to(source_drive)

            new_path = self.target_folder.joinpath(source_relative)
            print(new_path)

            if not new_path.exists():
                new_path.mkdir(parents=True)

        # for file_path in self.source_object.records_file:
        #     source_drive = file_path.anchor
        #     source_folder = Path(file_path)
        #     source_relative = source_folder.relative_to(source_drive)
        #
        #     new_path = self.target_folder.joinpath(source_relative)
        #
        #     print('5')
        #     copy2(file_path, new_path)
        #     print('6')

    def something(self):
        pass
