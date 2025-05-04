def comparesFile(fsatu, fdua):
     with open(fsatu) as f1, open(fdua) as f2:
         baris1 = f1.readlines()
         baris2 = f2.readlines()
     for i, (b1, b2) in enumerate(zip(baris1,baris2)):
         if b1 != b2:
             print(f"Perbedaan di baris {i+1}:")
             print(f"File 1: {b1.strip()}")
             print(f"File 2: {b2.strip()}\n")
     if len(baris1) > len(baris2) :
         print(f"File 1 memiliki {len(baris1)-len(baris2)} baris tambahan")
     elif len(baris2) > len(baris1) :
         print(f"File 2 memiliki {len(baris2)-len(baris1)} baris tambahan")
 
print(comparesFile('isifile1.txt', 'isifile2.txt'))
