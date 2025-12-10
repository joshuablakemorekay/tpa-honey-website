#!/usr/bin/env python3
"""
T.P.A. Honey Farm Website - Quick Start Script
Run this file to start the website
"""

import subprocess
import sys
import os

def check_dependencies():
    """Check if required packages are installed"""
    try:
        import flask
        print("✅ Flask is installed")
    except ImportError:
        print("❌ Flask not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "flask"])
    
    try:
        import fitz
        print("✅ PyMuPDF is installed")
    except ImportError:
        print("❌ PyMuPDF not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "PyMuPDF"])

def main():
    print("=" * 70)
    print("🍯  T.P.A. HONEY FARM WEBSITE - 2025 EDITION  🐝")
    print("=" * 70)
    print()
    
    # Check dependencies
    print("📦 Checking dependencies...")
    check_dependencies()
    print()
    
    # Start the application
    print("🚀 Starting web server...")
    print()
    print("=" * 70)
    print("🌐 Website will open at: http://localhost:5000")
    print("⏹️  Press Ctrl+C to stop the server")
    print("=" * 70)
    print()
    
    # Import and run the Flask app
    from app import app
    app.run(debug=True, host='0.0.0.0', port=5000)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Server stopped. Thank you for using T.P.A. Honey Farm Website!")
        sys.exit(0)
