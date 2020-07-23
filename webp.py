import glob, os
from PIL import Image
from pathlib import Path

os.chdir("photos")

photo_collection = []

for file in glob.glob("*.webp"):
    photo_collection.append(file)
    for photo in photo_collection:
        im = Image.open(photo).convert('RGB')
        new = Path(photo).stem
        im.save((str(new)+'.png'), 'png')
        print(im)

    print(file)
    print(photo_collection)