# 🍯 T.P.A. Honey Farm Website

**ฟาร์มผึ้งเทพภักดี**

A modern, bilingual (Thai/English) Flask web application for T.P.A. Honey Farm showcasing premium honey and bee products.

**👉 Visit the live site: https://tpa-honey-website.pages.dev**

## 🌟 Features

- **Bilingual Support**: Thai and English throughout the site
- **Product Catalog**: Honey, Bee Pollen, Royal Jelly, Honey Comb, Propolis, Luffa, and Spa Products
- **Photo Gallery**: Beautiful product photography with 14+ images
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile
- **Product Details**: Comprehensive information for each product category

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Deployment**: Render.com

## 📂 Project Structure

```
tpa_honey_website/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── render.yaml           # Render deployment config
├── templates/            # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── gallery.html
│   ├── products.html
│   └── product_detail.html
└── static/               # Static assets
    ├── css/
    └── images/          # Product images
```

## 🚀 Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/tpa-honey-website.git
   cd tpa-honey-website
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open your browser**
   ```
   http://localhost:5000
   ```

## 🌐 Deployment

This website is deployed on [Render.com](https://render.com).

**Live URL**: https://tpa-honey-website.pages.dev

The site is pre-rendered to static files by `freeze.py` and served from
Cloudflare Pages, so it loads in about 0.3 seconds and is always awake.
Every route is read-only, so there is nothing for a server to decide at
request time. To publish a change:

```
python freeze.py
wrangler pages deploy dist --project-name=tpa-honey-website --branch=main
```

The older Render deployment is still up at
https://tpa-honey-website.onrender.com but sleeps when idle, so the first
visitor after a quiet spell waits around 20 seconds.

> Hosted on Render's free tier, so the first visit after a quiet spell can take ~30 seconds to wake up. After that it's instant.

## 📧 Contact

**T.P.A. Beekeeping Farm / ฟาร์มผึ้งเทพภักดี**

- **Address**: 143/139 Arun Amarin, Bangkok Noi, Bangkok 10700, Thailand
- **Phone**: 02-884 6177, 434 3031
- **Email**: tpa_farm@yahoo.com

## 📝 License

© 2025 T.P.A. Honey Farm. All rights reserved.

---

🐝 Made with love and honey 🍯
