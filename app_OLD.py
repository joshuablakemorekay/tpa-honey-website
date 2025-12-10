"""
T.P.A. Honey Farm - Modern Web Application
ฟาร์มผึ้งเทพภักดี
Run with: python app.py
"""
from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tpa-honey-farm-2025'

# Product data from PDF
PRODUCTS = {
    'honey': {
        'title_th': 'น้ำผึ้ง',
        'title_en': 'HONEY',
        'description_th': 'น้ำผึ้งแท้ 100% คุณภาพสูงจากธรรมชาติ',
        'description_en': '100% Pure Natural Honey',
        'products': [
            {'name': 'Pure Honey 1050g', 'size': '1050 g', 'image': 'product_1_3.png'},
            {'name': 'Pure Honey 1000g', 'size': '1000 g', 'image': 'product_1_4.png'},
            {'name': 'Pure Honey 650g', 'size': '650 g', 'image': 'product_2_1.png'},
            {'name': 'Pure Honey 300g', 'size': '300 g', 'image': 'product_2_2.png'},
            {'name': 'Pure Honey 280g', 'size': '280 g', 'image': 'product_2_3.png'},
        ]
    },
    'bee_pollen': {
        'title_th': 'เกสรผึ้ง',
        'title_en': 'BEE POLLEN',
        'description_th': 'เกสรผึ้ง อุดมไปด้วยโปรตีน วิตามิน และแร่ธาตุ',
        'description_en': 'Rich in Protein, Vitamins and Minerals',
        'products': [
            {'name': 'Bee Pollen Bottle', 'name_th': 'เกสรผึ้งขวด', 'image': 'IMG_4813.JPG'},
            {'name': 'Bee Pollen Pack 500g', 'name_th': 'เกสรผึ้งซอง 500g', 'image': 'IMG_4815.JPG'},
            {'name': 'Bee Pollen Pack (Front)', 'name_th': 'เกสรผึ้งซอง (ด้านหน้า)', 'image': 'IMG_4816.JPG'},
            {'name': 'Bee Pollen Collection', 'name_th': 'ชุดเกสรผึ้ง', 'image': 'IMG_4822.JPG'},
            {'name': 'Bee Pollen Jar 100g', 'name_th': 'เกสรผึ้งโหล 100g', 'image': 'IMG_4823.JPG'},
            {'name': 'Bee Pollen Bottles (Pair)', 'name_th': 'เกสรผึ้งขวดคู่', 'image': 'IMG_4824.JPG'},
            {'name': 'Bee Pollen Bottle (Single)', 'name_th': 'เกสรผึ้งขวดเดี่ยว', 'image': 'IMG_4825.JPG'},
            {'name': 'Bee Pollen Bottles (Triple)', 'name_th': 'เกสรผึ้งขวด 3 ขวด', 'image': 'IMG_4826.JPG'},
            {'name': 'Bee Pollen Bottle (Large)', 'name_th': 'เกสรผึ้งขวดใหญ่', 'image': 'IMG_4827.JPG'},
        ]
    },
    'royal_jelly': {
        'title_th': 'นมผึ้ง',
        'title_en': 'ROYAL JELLY',
        'description_th': 'นมผึ้งสด บำรุงสุขภาพ ชะลอวัย',
        'description_en': 'Fresh Royal Jelly for Health and Anti-aging',
        'products': [
            {'name': 'Royal Jelly 500g', 'size': '500 g', 'image': 'product_2_5.png'},
            {'name': 'Royal Jelly 250g', 'size': '250 g', 'image': 'product_2_5.png'},
            {'name': 'Royal Jelly 100g', 'size': '100 g', 'image': 'product_2_5.png'},
        ]
    },
    'honey_comb': {
        'title_th': 'รวงผึ้ง',
        'title_en': 'HONEY COMB',
        'description_th': 'รวงผึ้งแท้ จากธรรมชาติ',
        'description_en': 'Natural Honey Comb',
        'products': [
            {'name': 'Honey Comb 250g', 'size': '250 g', 'image': 'product_3_1.png'},
            {'name': 'Honey Comb 400g', 'size': '400 g', 'image': 'product_3_1.png'},
        ]
    },
    'green_tea': {
        'title_th': 'ชาเขียว',
        'title_en': 'GREEN TEA',
        'description_th': 'ชาเขียวใบหม่อนผสมน้ำผึ้ง',
        'description_en': 'Mulberry Green Tea with Honey',
        'products': [
            {'name': 'Green Tea 70g', 'size': '70 g', 'image': 'product_19_2.png'},
            {'name': 'Green Tea Sachets', 'size': '20 sachets', 'image': 'product_3_2.png'},
        ]
    },
    'propolis': {
        'title_th': 'พรอพพอลิส',
        'title_en': 'BEE PROPOLIS',
        'description_th': 'พรอพพอลิส สารสกัดจากผึ้ง',
        'description_en': 'Bee Propolis Extract',
        'products': [
            {'name': 'Bee Propolis', 'image': 'product_3_3.png'},
        ]
    },
    'luffa': {
        'title_th': 'ใยบวบ',
        'title_en': 'LUFFA',
        'description_th': 'ใยบวบธรรมชาติ สำหรับผิวพรรณ',
        'description_en': 'Natural Luffa for Beautiful Skin',
        'products': [
            {'name': 'Luffa Products', 'image': 'product_20_4.png'},
            {'name': 'Luffa Slippers', 'image': 'product_22_4.png'},
        ]
    },
    'spa': {
        'title_th': 'ผลิตภัณฑ์เพื่อความงาม',
        'title_en': 'SPA PRODUCTS',
        'description_th': 'ผลิตภัณฑ์บำรุงผิว จากน้ำผึ้งและสมุนไพร',
        'description_en': 'Beauty Products with Honey and Herbs',
        'products': [
            {'name': 'Facial Scrub', 'name_th': 'ขมิ้นน้ำผึ้งขัดผิวหน้า', 'image': 'product_4_1.png'},
            {'name': 'Body Scrub', 'name_th': 'ขมิ้นน้ำผึ้งผสมน้ำแร่', 'image': 'product_4_2.png'},
            {'name': 'Honey Soap', 'name_th': 'สบู่น้ำผึ้ง', 'image': 'product_4_3.png'},
            {'name': 'Herbal Set', 'name_th': 'ชุดสมุนไพรบำรุงผิว', 'image': 'product_4_4.png'},
            {'name': 'Slimming Cream', 'image': 'product_4_5.png'},
            {'name': 'Shower Salt & Scrub', 'image': 'product_5_1.png'},
            {'name': 'Gel Collagen Eye Serum', 'image': 'product_5_2.png'},
            {'name': 'Facial Cream', 'image': 'product_5_3.png'},
            {'name': 'Anti Cellulite', 'image': 'product_6_1.png'},
            {'name': 'Shampoo + Honey', 'image': 'product_6_2.png'},
            {'name': 'Foot Massage Cream', 'image': 'product_6_3.png'},
            {'name': 'Ginseng Balm', 'image': 'product_7_1.png'},
            {'name': 'Herbal Salt', 'image': 'product_7_2.png'},
            {'name': 'Body Spray', 'image': 'product_7_3.png'},
            {'name': 'Yellow Oil', 'image': 'product_8_4.png'},
            {'name': 'Powder', 'name_th': 'แป้งพัพ', 'image': 'product_8_5.png'},
        ]
    }
}

CONTACT_INFO = {
    'address_th': 'ฟาร์มผึ้งเทพภักดี 143/139 อรุณอมรินทร์ บางกอกน้อย กรุงเทพ 10700 ประเทศไทย',
    'address_en': 'TPA Beekeeping Farm / ฟาร์มผึ้งเทพภักดี, 143/139 Arun Amarin, Bangkok Noi, Bangkok 10700, Thailand',
    'phone': '02-884 6177, 434 3031',
    'fax': '02-884 5225',
    'email': 'tpa_farm@yahoo.com'
}

@app.route('/')
def index():
    return render_template('index.html', products=PRODUCTS, contact=CONTACT_INFO)

@app.route('/products')
def products():
    return render_template('products.html', products=PRODUCTS, contact=CONTACT_INFO)

@app.route('/products/<category>')
def product_category(category):
    if category in PRODUCTS:
        return render_template('product_detail.html', 
                             category=category, 
                             product=PRODUCTS[category],
                             contact=CONTACT_INFO)
    return "Product not found", 404

@app.route('/contact')
def contact():
    return render_template('contact.html', contact=CONTACT_INFO)

@app.route('/about')
def about():
    return render_template('about.html', contact=CONTACT_INFO)

@app.route('/health-products')
def health_products():
    return render_template('health_products.html', contact=CONTACT_INFO)

@app.route('/skincare')
def skincare():
    return render_template('skincare.html', contact=CONTACT_INFO)

@app.route('/gallery')
def gallery():
    return render_template('gallery.html', contact=CONTACT_INFO)

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    print("=" * 60)
    print("🍯  T.P.A. Honey Farm - ฟาร์มผึ้งเทพภักดี")
    print("=" * 60)
    print("\n✅ Server starting...")
    print("🌐 Open your browser and go to: http://localhost:5000")
    print("⏹️  Press Ctrl+C to stop the server\n")
    print("=" * 60)
    app.run(debug=True, host='0.0.0.0', port=5000)
