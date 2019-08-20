from os import getcwd, walk, path
from sys import argv
from PIL import Image

cwd = getcwd()
extension = '.' + argv[1]
new_width = int(argv[2])
new_height = int(argv[3])

files = []
for r, d, f in walk(cwd):
    for file in f:
        if extension in file:
            files.append(path.join(r, file))

for single_file in files:
    img = Image.open(single_file)
    img = img.resize((new_width, new_height), Image.ANTIALIAS)
    img.save(single_file[:-len(extension)] + '_modified' + extension)
