def main():
    with open('soal.txt', 'r') as file:
        for baris in file:
            bagian = baris.strip().split('||')
            if len(bagian) != 2:
                continue
            
            tanya = bagian[0].strip()
            jawaban_benar = bagian[1].strip().lower()  
            print(tanya)
    
            jawab_user = input("Jawab: ").strip().lower()
            if jawab_user == jawaban_benar:
                print("Jawaban benar!\n")
            else:
                print("Jawaban salah!\n")
if __name__ == "__main__":
    main()
