from flask import Flask, redirect, url_for
from config import Config

from routes.jastip import jastip_bp

def create_app():
    """
    Membuat dan mengkonfigurasi aplikasi Flask.
    """
    app = Flask(__name__)

    # Memuat konfigurasi aplikasi
    app.config.from_object(Config)

    # Mendaftarkan Blueprint
    app.register_blueprint(jastip_bp)

    @app.route('/')
    def home():
        return redirect(url_for('jastip.index'))

    return app

app = create_app()

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5001,
        debug=Config.DEBUG
    )