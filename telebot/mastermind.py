def get_response(msg):
    if msg == '/start':
        return """
            Selamat Datang di Telegram Tentang Statistika FMIPA UNTAD\n
            Berikut beberapa dan cara mengetahui informasi:
            /ukt = tentang ukt
            /kuliah = tentang kuliah
               """
    elif msg == '/ukt':
        return "UKT adalah singkatan dari uang kuliah tunggal yang merupakan beban yang wajib dibayar mahasiswa setiap semesternya"
    elif msg == '/kuliah':
        return """ Mahasiswa wajib melulusi 144 sks """
    else:
        return 'Masih belum tersedia'
    
    
