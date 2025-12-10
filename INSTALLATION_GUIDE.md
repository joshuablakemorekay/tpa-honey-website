# 🍯 T.P.A. Honey Farm Website - Complete Installation Guide

## 📥 What You Got

A complete, modern website for T.P.A. Honey Farm with:
- ✅ **110 product images** extracted from your PDF
- ✅ **5 HTML pages**: Home, Products, Product Details, Contact
- ✅ **Modern 2025 design** with animations and responsive layout
- ✅ **Flask web application** ready to run in PyCharm
- ✅ **Bilingual content** (Thai and English)

## 🎯 Quick Start (3 Steps!)

### Step 1: Download and Extract
1. Download the `tpa_honey_website` folder
2. Save it anywhere on your computer
3. You should see these files:
   ```
   tpa_honey_website/
   ├── start.py           ← Double-click this to start!
   ├── app.py
   ├── requirements.txt
   ├── README.md
   ├── templates/         (5 HTML files)
   └── static/images/     (110 product images)
   ```

### Step 2: Install Python (if needed)
- Download Python from: https://www.python.org/downloads/
- **Important**: Check "Add Python to PATH" during installation

### Step 3: Run the Website

**Option A: Super Easy Way**
- Double-click `start.py`
- Wait for it to install dependencies (first time only)
- Browser will automatically open to http://localhost:5000

**Option B: Using PyCharm**
1. Open PyCharm
2. File → Open → Select `tpa_honey_website` folder
3. Right-click `start.py` or `app.py`
4. Click "Run"
5. Open browser to: http://localhost:5000

**Option C: Command Line**
```bash
cd tpa_honey_website
pip install -r requirements.txt
python app.py
```

## 🌐 Using the Website

Once running, you can:
- **Homepage**: View farm introduction and all products
- **Products**: Browse all 8 product categories
- **Product Details**: Click any product to see images and sizes
- **Contact**: View address, phone, email, and map

## 🎨 What Makes This Website Special

### Modern Features
- **Honeycomb background pattern** - subtle bee theme
- **Smooth animations** - cards lift when you hover
- **Mobile-friendly** - works on phones, tablets, computers
- **Fast loading** - optimized images and code
- **Professional design** - clean, modern aesthetic

### Product Categories
1. 🍯 น้ำผึ้ง (Honey) - 5 different sizes
2. 🌼 เกสรผึ้ง (Bee Pollen) - health supplement
3. 👑 นมผึ้ง (Royal Jelly) - premium product
4. ⬡ รวงผึ้ง (Honey Comb) - natural honeycomb
5. 🍵 ชาเขียว (Green Tea) - with honey
6. 💊 พรอพพอลิส (Propolis) - bee propolis
7. 🧽 ใยบวบ (Luffa) - natural scrub
8. ✨ สปา (Spa) - 16 beauty products

## 🔧 Troubleshooting

### "Port 5000 is already in use"
Open `app.py`, change the last line to:
```python
app.run(debug=True, host='0.0.0.0', port=8000)
```
Then use: http://localhost:8000

### "Module not found" errors
Run in terminal:
```bash
pip install flask PyMuPDF
```

### Images not showing
All 110 images are in: `static/images/`
If missing, you can re-extract from PDF by running:
```bash
python extract_images.py
```

## 📱 Testing on Mobile

1. Find your computer's IP address:
   - Windows: `ipconfig` in Command Prompt
   - Mac/Linux: `ifconfig` in Terminal

2. On your phone's browser, go to:
   ```
   http://YOUR_IP_ADDRESS:5000
   ```
   (e.g., http://192.168.1.100:5000)

## 🚀 Next Steps

### To customize the website:
- **Change colors**: Edit CSS in `templates/base.html`
- **Add products**: Update the `PRODUCTS` dictionary in `app.py`
- **Change contact info**: Update `CONTACT_INFO` in `app.py`
- **Modify layout**: Edit HTML files in `templates/`

### To deploy online:
1. Choose a hosting service (PythonAnywhere, Heroku, DigitalOcean)
2. Upload your project
3. Set up domain name
4. Configure for production (set debug=False)

## 📞 Support

For questions or help with the website:
- Read the detailed README.md
- Check Flask documentation: https://flask.palletsprojects.com/
- Python documentation: https://docs.python.org/

## ✨ Features Checklist

- ✅ Modern responsive design
- ✅ All 110 product images included
- ✅ Bilingual (Thai/English)
- ✅ Mobile-friendly
- ✅ Contact page with map
- ✅ Product categories
- ✅ Smooth animations
- ✅ Professional color scheme
- ✅ Easy to run in PyCharm
- ✅ Complete documentation

---

## 🎉 You're All Set!

Your T.P.A. Honey Farm website is ready to use. Just run `start.py` and enjoy your beautiful, modern website!

**Built with Flask, Python, and lots of 🍯**
**2025 Edition - Fully Updated and Modernized**
