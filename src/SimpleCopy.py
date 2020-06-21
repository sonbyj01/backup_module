#!/usr/bin/env python3
from shutil import copy2
from pathlib import Path
import sys

from .SourceFiles import SourceFiles


class SimpleCopy:
    def __init__(self, source):
        assert isinstance(source, SourceFiles), 'Not a SourceFiles object.'
        self.source_object = source
        self.source_parent = self.source_object.source_path.parents[0]

    def simple_copy2(self, target):
        try:
            target_folder = Path(target)
        except TypeError as fnf:
            sys.exit()

        if not target_folder.exists():
            target_folder.mkdir(parents=True)

        for source_folder_path in self.source_object.records_folder:
            source_folder_path = Path(source_folder_path)
            source_folder_relative_path = source_folder_path.relative_to(self.source_parent)

            target_absolute = target_folder.joinpath(source_folder_relative_path)

            if not target_absolute.exists():
                target_absolute.mkdir(parents=True)

        for source_file_path in self.source_object.records_file:
            source_file_path = Path(source_file_path)
            source_file_relative_path = source_file_path.relative_to(self.source_parent)

            target_absolute = target_folder.joinpath(source_file_relative_path)

            copy2(source_file_path, target_absolute)
