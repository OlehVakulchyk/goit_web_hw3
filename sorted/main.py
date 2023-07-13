"""
Відсортувати файли в папці.
"""

import argparse
from pathlib import Path
from shutil import copyfile
from threading import Thread
import logging
import time

"""
--source [-s] 
--output [-o]
"""

parser = argparse.ArgumentParser(description="Sorting folder")
parser.add_argument("--source", "-s", help="Source folder", required=True)
parser.add_argument("--output", "-o", help="Output folder", default="dist")

args = vars(parser.parse_args())

source = Path(args.get("source"))
output = Path(args.get("output"))

folders = []


def grabs_folder(path: Path) -> None:
    threads = []
    for el in path.iterdir():
        if el.is_dir():
            folders.append(el)
            # grabs_folder(el)
            th = Thread(target=grabs_folder, args=(el,))
            th.start()
            threads.append(th)            
    [th.join() for th in threads]

def copy_file(path: Path) -> None:
    for el in path.iterdir():
        if el.is_file():
            ext = el.suffix[1:]
            if not ext:
                ext = 'not_ext'
            new_path = output / ext
            try:
                new_path.mkdir(exist_ok=True, parents=True)
                copyfile(el, new_path / el.name)
            except OSError as error:
                logging.error(error)


if __name__ == "__main__":
    start = time.time()
    logging.basicConfig(level=logging.ERROR, format="%(threadName)s %(message)s")
    print(source, output)
    folders.append(source)
    grabs_folder(source)
    threads = []
    for folder in folders:
        # copy_file(folder)
        th = Thread(target=copy_file, args=(folder,))
        th.start()
        threads.append(th)       
    [th.join() for th in threads]

    print("Можно видалити стару папку, якщо треба")
    end = time.time()
    print(f'\nEnd! Total time: {end - start} sec')
