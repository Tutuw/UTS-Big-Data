import nltk
Nama = input ( "Nama Lengkap: ")
NIM = input ("NIM: ")
Kelas = input ( "Kelas : ")
Kampus = input ( "Kampus : ")

print("\n===============================")
print("Biodataku")
print("===============================")
print("Nama Lengkap : ", Nama)
print("NIM : ", NIM)
print("Kelas : ", Kelas)
print("Kampus: ", Kampus)

s= ("\nNama saya adalah Fath Ul Mawaddah dengan NIM 04318016, saya dari kelas A yang melaksanakan pendidikan di Universitas Narotama")
print (s)
x= s.split()
print ("\n".join(x))
