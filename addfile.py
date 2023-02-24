import argparse
import sys
import os
import shutil
import csv

#creo la CLI per spostare il file in input nella relativa cartella
parser = argparse.ArgumentParser(description=
                                 'Move a file in its appropriate folder')
parser.add_argument('file', type=str, help=
                    'Enter the file you want to move')
args = parser.parse_args()



#creo le sottocartelle
for dirname in ['images', 'docs', 'audio']:
    if not os.path.exists(dirname):
        os.makedirs(dirname)

#creo dizionario con le liste dei formati accettati
dict_file = {'img_ext': ['.png', '.jpeg', '.jpg'], 'doc_ext': ['.txt', '.odt'], 'audio_ext': ['.mp3']}

#se il file di recup non esiste lo creo e scrivo gli header del csv
if not os.path.exists('recap.csv'):
    fields = ['name', 'type', 'size(B)']
    with open('recap.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)


else:

    if os.path.exists('recap.csv'):#se il file in input esiste nella directory
        with open('recap.csv', 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)


            name, ext = os.path.splitext(args.file)#separo nome file ed estensione
                
            if os.path.exists(args.file):
            
                if ext in dict_file['img_ext']:#verifico estensione
                    size = os.path.getsize(args.file)#calcolo le dimensioni del file
                    print(f'{name} type:image size:{size}B')#stampo le info del file
                    csvwriter.writerow([name, 'image', size])#appendo le info del file a recup.csv
                    shutil.move(args.file, 'images/')#sposto il file nella relativa sottocartella

                elif ext in dict_file['doc_ext']:
                    size = os.path.getsize(args.file)
                    print(f'{name} type:doc size:{size}B')
                    csvwriter.writerow([name, 'doc', size])
                    shutil.move(args.file, 'docs/')

                elif ext in dict_file['audio_ext']:
                    size = os.path.getsize(args.file)
                    print(f'{name} type:audio size:{size}B')
                    csvwriter.writerow([name, 'audio', size])
                    shutil.move(args.file, 'audio/')
                else:
                    pass
            else:
                print('Missing file in the actual directory')#se il file non è presente il programma avvisa l'utente
    


