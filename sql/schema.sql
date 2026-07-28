-- Jalankan query ini di database MySQL Filess.io Anda sebelum menjalankan server

CREATE TABLE IF NOT EXISTS pesanan_jastip (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nama_pemesan VARCHAR(150) NOT NULL,
  produk VARCHAR(255) NOT NULL,
  jumlah INT NOT NULL,
  harga_satuan DECIMAL(12,2) NOT NULL,
  catatan TEXT NULL,
  status VARCHAR(50) NOT NULL DEFAULT 'diproses',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
