import streamlit as st
import random

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Home", "Ganjil/Genap", "TDL", "Games", "TESTING", "APLIKASI SEDERHANA"])

with tab1:
    st.title("Halaman Utama")
    st.write("Selamat datang di halaman utama.")
    st.write( "Jika ingin keinginan terwujud, perbanyaklah bersujud 🤘😝🤘")
    st.write("[Coba Klik](https://youtu.be/2Iyj3CBsxTk)")
    st.image("IMG_20250522_091017.jpg", width=2000)
    botak = st.text_input("nama orang diatas siapa 🫵😠")
    if botak == "GANIBOTAK":
                          st.write("bener 🥰")
    elif botak == "":
        st.write("Tebak")
    else:
                          st.write("salah 😡")

with tab2:
    st.title("Aplikasi Ganjil Genap")
          
    angka = st.number_input("Tulis sebuah angka:", value=0, step=1)
    if (angka % 2) ==0:
      st.write(f"{angka} adalah Bilangan Genap")
    else:
      st.write(f"{angka} adalah Bilangan Ganjil")

with tab3:
    st.title("To Do List")
    mantap1 = st.checkbox("Ngerjain tugas")
    mantap2 = st.checkbox("ngedate sama ayang")
    mantap3 = st.checkbox("menyelamatkan dunia")
    mantap4 = st.checkbox("menjadi presiden Indonesia")

    
    if mantap1 and mantap2 and mantap3 and mantap4:
              st.write("mantap")
    else:
      pass
        
with tab4:
    st.title("Gacha")

    nomor = st.number_input("Pilih angka random antara 1-100", value=0, step=1, min_value=0, max_value=100)

    sigma = ("selamat!!")
    skibidi = ("ayo coba lagi")
    slebew = ("Ayo Mulai")

    berhasil = (nomor == random.randint(1,10))
    idle = (nomor == 0)
    gagal = (nomor != 'berhasil' and nomor != 0)

    if berhasil:
        st.write(sigma)
        st.image("31284410-3d-rendering-of-business-person-standing-with-correct-right-check-tick-mark-3d-illustration-of-human.jpg", width=2500)
    elif gagal:
        st.write(skibidi)
        st.image("d-sad-depressed-person-rendering-frustrated-man-sitting-plastic-stool-white-people-man-character-51186816.webp", width=2500)
    elif idle:
        st.write(slebew)

with tab5:
    st.title("TESTING")

   
    if 'button' not in st.session_state:
       st.session_state.button = False

    def click_button():
       st.session_state.button = not st.session_state.button

    st.button('tes keberuntungan', on_click=click_button)
    hoki = (111, 222, 333, 444, 555, 666, 777, 888, 999)
    if st.session_state.button:
       gacha = st.write(random.randint(100, 999))
       if gacha == hoki:
            st.write("hoki bet anjay")
       elif gacha != hoki:
            st.write("gagal")
        
    else:
       st.write('Ayo pencet aku')
with tab6:
  st.title("Aplikasi Sederhana")

# Menggunakan layout kolom
  col1, col2 = st.columns(2)

  with col1:
      st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
      angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)

      if (angka % 2) == 0:
          st.write(f"{angka} adalah Bilangan Genap")
      else:
          st.write(f"{angka} adalah Bilangan Ganjil")

  with col2:
      st.header("Aplikasi menghitung Total Belanja")

      def hitung_total(harga, jumlah):
          return harga * jumlah

      harga_barang = st.number_input("Masukkan Harga Barang:", value=0, step=1000)
      jumlah_barang = st.number_input("Masukkan Jumlah Barang:", value=0, step=1)
      total_harga = hitung_total(harga_barang, jumlah_barang)

      if total_harga > 100000:
          total_harga_diskon = total_harga - 0.05 * total_harga
          st.write(f"Total Harga (dengan diskon): Rp. {total_harga_diskon:,.0f}")
      else:
          st.write(f"Total Harga: Rp. {total_harga:,.0f}")

      bayar = st.number_input("Masukkan Jumlah Uang:", value=0, step=10000)

      if bayar >= total_harga:
          kembalian_uang = bayar - total_harga
          st.write(f"Uang Kembalian: Rp. {kembalian_uang:,.0f}")
      else:
          st.write("Uang yang anda bayarkan kurang ")
with tab 6:
st.title ("test")
col1, col2 = st.columns(2)

     with col1:
        st.write("Ini di kiri")

    with col2:
        st.write("Ini di kanan")
