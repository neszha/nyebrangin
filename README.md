# PYTHON GAME BY PULANGMEN

<img src="docs/text-logo.png" width="100%">

## Deskripsi Game
Game `nyebrangin` menggambarkan tentang player yang ingin membantu civillian untuk menyebrangi jalan ke tujuan yang diinginkan. 

Player memiliki beberapa kesempatan bermain berupa nyawa yang akan berkurang setiap kali tertabrak kendaraan atau jatuh ke dalam lubang. Misi utama seorang player yaitu membantu civilian yang ingin menyebrang dalam durasi waktu tertentu untuk dapat ke level yang lebih tinggi. Semakin tinggi tingkatan level, maka tingkat kesulitan juga akan semakin tinggi.

## Dependensi atau Library
- pygame: Library utama untuk menjalankan game di python.
- random: Library untuk menghandle fungsi-fungsi yang bersifat random. 
- os: Library ini digunakan unuk berintraksi dengen sistem operasi.
- datetime: Library ini digunakan untuk menggenerate data waktu.
- json: Library ini digunakan unuk mengelola data dengen tipe data JSON.

## Menjalankan Game (Container Docker)
Membuat docker image: 
```
# docker build -t nyebrangin .
```

Game tidak akan langsung terbuka seteleh image berhasil terbuat. Maka, image perlu dibuat menjadi sebuah container yang nantinya dapat menjalankan kode game yang ada di dalamnya.

Membuat dan menjalankan container dari sebuah image:
```
# docker run -it nyebrangin
```
`~ NOTE:` Container pada docker sebenernya tidak mendukung program GUI. Untuk itu, diperlukan program pihak ketiga sebagai jembatan antara container dengan sistem operasi yang menjalankannya. Jika mengunakan windows, anda perlu menginstall program <a href="https://sourceforge.net/projects/vcxsrv/">Windows X Server</a> sebelum menjalankan container.

`~ NOTE:` Saat ini, container yang dibuat belum dapat menjalankan kode game yang sebenarnya dikarenakan masalah device audio pada pygame yang belum bisa diexpose keluar container. Kami belum menemukan cara untuk menyelesaikannya. Namun, untuk menerapkannya, kami membuat file `blank.py` sebagai penggantinya yang tidak menggunakan fitur audio pada pygame.

[![BUILD PYTHON GAME INTO DOCKER CONTAINER - IF2223 - PyGame Project](https://img.youtube.com/vi/Zk7xnmVfwHc/0.jpg)](https://www.youtube.com/watch?v=Zk7xnmVfwHc)
</br>
<a href="https://www.youtube.com/watch?v=Zk7xnmVfwHc">BUILD PYTHON GAME INTO DOCKER CONTAINER</a>

## Menjalankan Game
Sebelum menjalankan game, pastikan semua paket atau library sudah terinstall:

```
# pip install pygame
# pip3 install pygame (alternative command)
```
Perintah untuk menjalankan game:
```
# python nyebrangin.py
# python3 nyebrangin.py (alternative command)
# py nyebrangin.py (alternative command)
```

<img src="docs/menu.png" width="100%"> 
<img src="docs/01-level-list.png" width="100%"> 

Setelah game dijalankan, maka akan muncul tampilan menu utama seperti gambar di atas. Setelah itu, klik tombol `Start` untuk membuka daftar level yang tersedia. Setelah itu, pilih tingkatan level yang ingin dimainkan.

<img src="docs/game-run.png" width="100%"> 

Setelah level terbuka, misi player yaitu membantu para civilian untuk menyebrangi jalan ke tujuan tertentu. Player harus menyelasaikan misi tersebut dalam jangka waktu tertentu. Jika waktu atau nyawa player habis, maka game akan bergenti dan akan menampilkan popup `Game Over`. Jika misi telah selesai, maka game akan menampilkan popup `Game Finish` dan player berhak untuk dapat memainkan game di level berikutnya.  

<img src="docs/game-finish.png" width="100%"> 
<img src="docs/02-level-list.png" width="100%"> 

## Ketentuan Game
- Nyawa player akan berkurang jika player jatuh ke lubang atau ditabrak oleh kendaraan yang sedang melintas. Pada kondisi ini player sedang membawa civilian, maka civilian akan kembali ke poisis awal.
- Civilian akan kembali ke poisis awal jika ia ditabrak oleh kendaraan atau masuk ke dalam lubang.
- Tujuan civilian akan terlihat jika player menyentuh civilian.
- Level selanjutnya akan terbuka jika telah menyelesaikan misi pada level tersebut.
- Game Over: Terjadi apabila durasi hitungan mundur telah habis atau player kehabisan nyawa.
- Game Finish: Terjadi apabila semua civilian berhasil sampai ke tujian dengen durasi waktu dan nyawa player yang masih tersisa.

## Kontrol Game
- `Control Key`: Digunakan untuk menggerakan player ke atas, bawah, kanan, dan kiri.
- `w`: Digunakan untuk mengaktifkan `walk mode` pada player. Karena secara default, player menggunaka  `run mode` dalam bergerak.
- `SPACE`: Digunakan untuk membawa dan melepas civilian.
- `esc`: Digunakan untuk menghentikan game sementara.

## UML Class Diagram
<img src="docs/uml-class.png" width="800">

## Pengembang Game
 
| PULANGMEN TEAM |
| ---------------- |

| NIM | Kelas  | Nama | Sebagai |
| ----- | ----- | --- | --- |
| 120140043  | RB | Irsan Romardi Harahap  | Leader and Tester |
| 120140149  | RB | Dewi Anggraini  | Level Designer |
| 119140117  | - | Chantika Aurrelia  | Game Designer and Artist |
| 120140039  | RB | Tara Nadani Mozart  | Game Designer and Artist |
| 120140189  | RB | Fanesa Hadi Pramana  | Programmer |
| 120140071  | RB | Muhammad Rizky Fahreza Gusti  | Programmer |
