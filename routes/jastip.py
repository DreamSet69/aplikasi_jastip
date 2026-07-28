from flask import Blueprint, render_template, request, redirect, url_for, flash
from database import get_connection
import pymysql

jastip_bp = Blueprint('jastip', __name__, url_prefix='/jastip')

@jastip_bp.route('/')
def index():
    conn = get_connection()
    if conn is None:
        return "Database connection error", 500
    
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM pesanan_jastip ORDER BY created_at DESC")
    pesanan = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return render_template('jastip/index.html', pesanan=pesanan)

@jastip_bp.route('/tambah', methods=['GET', 'POST'])
def tambah():
    if request.method == 'POST':
        nama_pemesan = request.form.get('nama_pemesan')
        produk = request.form.get('produk')
        jumlah = request.form.get('jumlah')
        harga_satuan = request.form.get('harga_satuan')
        gambar_url = request.form.get('gambar_url')
        catatan = request.form.get('catatan')
        
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO pesanan_jastip (nama_pemesan, produk, gambar_url, jumlah, harga_satuan, catatan)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (nama_pemesan, produk, gambar_url, jumlah, harga_satuan, catatan))
        conn.commit()
        cursor.close()
        conn.close()
        
        return redirect(url_for('jastip.index'))
        
    return render_template('jastip/form.html')

@jastip_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    
    if request.method == 'POST':
        nama_pemesan = request.form.get('nama_pemesan')
        produk = request.form.get('produk')
        jumlah = request.form.get('jumlah')
        harga_satuan = request.form.get('harga_satuan')
        gambar_url = request.form.get('gambar_url')
        catatan = request.form.get('catatan')
        status = request.form.get('status')
        
        query = """
            UPDATE pesanan_jastip 
            SET nama_pemesan=%s, produk=%s, gambar_url=%s, jumlah=%s, harga_satuan=%s, catatan=%s, status=%s
            WHERE id=%s
        """
        cursor.execute(query, (nama_pemesan, produk, gambar_url, jumlah, harga_satuan, catatan, status, id))
        conn.commit()
        cursor.close()
        conn.close()
        
        return redirect(url_for('jastip.index'))
        
    cursor.execute("SELECT * FROM pesanan_jastip WHERE id = %s", (id,))
    pesanan = cursor.fetchone()
    cursor.close()
    conn.close()
    
    return render_template('jastip/form.html', pesanan=pesanan)

@jastip_bp.route('/selesai/<int:id>', methods=['POST'])
def selesai(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE pesanan_jastip SET status='selesai' WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    
    return redirect(url_for('jastip.index'))

@jastip_bp.route('/hapus/<int:id>', methods=['POST'])
def hapus(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM pesanan_jastip WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    
    return redirect(url_for('jastip.index'))
