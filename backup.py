#!/bin/bash
from src.SimpleCopy import SimpleCopy
from src.SourceFiles import SourceFiles

src_path = r'D:\_Games\Gameboy'
# source = input("Enter source drive/directories with full path: ")
target = r'D:\_Games\Gameboy\backup'
# target = input("Enter destination drive/directories with full path: ")'

x = SourceFiles(src_path)
y = SimpleCopy(x)
y.simple_copy2(target)
