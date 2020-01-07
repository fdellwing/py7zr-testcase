#!/usr/bin/env python3.7

import py7zr
import subprocess
archive = py7zr.SevenZipFile(f'test.7z', 'w')
archive.writeall("file")
archive.close()

subprocess.run("7z l test.7z", shell=True)
