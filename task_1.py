import sys
from pathlib import Path
import shutil
from concurrent.futures import ThreadPoolExecutor
import time


class FileManager:
    def __init__(self, source_dir:str, target_dir:str):
        self.source_dir = Path(source_dir).resolve()
        self.target_dir = Path(target_dir).resolve()
        self.dirs = []
        if not self.source_dir.is_dir():    # Перевіряємо наявність джерельної директорії та створюємо цільову директорію.
            raise ValueError(f"Помилка: Джерельна директорія {self.source_dir} не існує або не є директорією.")
        self.target_dir.mkdir(parents = True, exist_ok = True)

    def copy_files(self, file_path:Path):
        ext = file_path.suffix.lstrip('.')    #отримати розширення файла
        if not ext:
            ext = 'without_ext'
        target_path = self.target_dir / ext   #створити шлях для копіювання
        target_path.mkdir(parents = True, exist_ok = True)
        try:
            shutil.copy(file_path, target_path)
        except Exception:
            print(f'Помилка копіювання файлу {file_path}')
            return
        
    def get_files(self):
        def scan_directory(path: Path):
            for item in path.iterdir():
                if item.is_dir() and item != self.target_dir :
                    futures.append(executor.submit(scan_directory, item))
                elif item.is_file():
                    self.copy_files(item)

        futures = []
        with ThreadPoolExecutor(max_workers=10) as executor:
            scan_directory(self.source_dir)
            for future in futures:
                future.result()



def get_cli()->list:
        if 1<len(sys.argv)<4:
            source = sys.argv[1]
            target = 'dist'
            if len(sys.argv)==3: target = sys.argv[2]
            return [source, target]
        else:
            raise ValueError(f'Використання: {sys.argv[0]} <стартовий каталог> [цільовий каталог]')


def main():
    try:
        source, target = get_cli()
    except Exception as e:
        print(e)
        return
    fm = FileManager(source, target)
    print('Трохи почекайте...')
    current_time  = time.time()
    fm.get_files()
    timer = time.time()-current_time
    print (f'Файли успішно скопійовано за {timer} секунд!')

if __name__ == '__main__':
    main()