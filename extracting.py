import gzip
import os

def extract(file_name, new_name):
    with gzip.GzipFile(file_name, 'rb') as gz:
        full_path = new_name.split('/')
        with open(full_path[-1], 'wb') as fp:
            while True:
                data = gz.read(2048)
                if data:
                    fp.write(data)
                else:
                    break
            fp.close()
        gz.close()
