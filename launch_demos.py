#!/usr/bin/env python3
"""
DEMO LAUNCHER - Lancer les démos en 1 commande
Démarre soit les démos statiques (HTML), soit l'API backend (Flask)
"""

import os
import sys
import subprocess
from pathlib import Path
from typing import Optional

def launch_static_demos():
    """Lancer les démos statiques (HTML - zéro dépendances)"""
    print("🚀 Launching Static Demos (HTML)...")
    print("\n" + "="*60)
    print("📚 Available Demos:")
    print("="*60)
    
    demos = {
        "demos.html": "🎬 Interactive Demos (Email, PDF, Excel)",
        "demo-guide.html": "📖 Complete Guide for Clients",
        "index.html": "🏠 Landing Page"
    }
    
    base_path = Path(__file__).parent
    
    for filename, desc in demos.items():
        path = base_path / filename
        if path.exists():
            size = path.stat().st_size
            print(f"  ✅ {filename:<20} - {desc:<40} ({size:,} bytes)")
            print(f"     → file://{path.absolute()}")
        else:
            print(f"  ❌ {filename:<20} - NOT FOUND")
    
    print("\n" + "="*60)
    print("📖 To view demos:")
    print("="*60)
    print("  1. Open demos.html in your browser")
    print("  2. Test Email Classifier, PDF Generator, Excel Analyzer")
    print("  3. All data stays 100% local (no backend required)")
    print("\n✅ Static Demos Ready!")


def launch_api_backend():
    """Lancer l'API Flask backend"""
    print("🚀 Launching Backend API (Flask)...")
    print("\n" + "="*60)
    print("📊 API Endpoints:")
    print("="*60)
    
    endpoints = {
        "GET /api/health": "Health check",
        "POST /api/email/classify": "Classify email",
        "POST /api/pdf/generate": "Generate PDF",
        "POST /api/excel/analyze": "Analyze Excel/CSV"
    }
    
    for endpoint, desc in endpoints.items():
        print(f"  {endpoint:<30} - {desc}")
    
    print("\n" + "="*60)
    print("⚙️  Installation:")
    print("="*60)
    
    # Check if Flask is installed
    try:
        import flask
        print("  ✅ Flask is installed")
    except ImportError:
        print("  ❌ Flask not installed")
        print("\n  Install with:")
        print("  pip install flask flask-cors")
        print("\n  Then run:")
        print("  python demo_api.py")
        return
    
    # Launch the API
    print("\n" + "="*60)
    print("🌐 Starting API Server...")
    print("="*60)
    
    api_path = Path(__file__).parent / "demo_api.py"
    if api_path.exists():
        try:
            subprocess.run([sys.executable, str(api_path)])
        except KeyboardInterrupt:
            print("\n\n🛑 API Server stopped")
    else:
        print(f"  ❌ demo_api.py not found at {api_path}")


def main():
    """Main menu"""
    print("\n" + "="*60)
    print("🎯 DEMO LAUNCHER")
    print("="*60)
    print("\nChoose a demo mode:\n")
    print("  1️⃣  Static Demos (HTML - Recommended)")
    print("       • No backend required")
    print("       • Fast & instant")
    print("       • Perfect for initial testing")
    print("")
    print("  2️⃣  API Backend (Flask)")
    print("       • Full-featured backend")
    print("       • REST API endpoints")
    print("       • Integration ready")
    print("")
    print("  0️⃣  Exit")
    print("")
    
    try:
        choice = input("Select option (0-2): ").strip()
        
        if choice == "1":
            launch_static_demos()
            print("\n📖 Next steps:")
            print("  1. Open demos.html in your browser")
            print("  2. Test the 3 interactive demos")
            print("  3. Share with clients!")
            
        elif choice == "2":
            launch_api_backend()
            
        elif choice == "0":
            print("👋 Goodbye!")
            
        else:
            print("❌ Invalid option")
            main()
    
    except KeyboardInterrupt:
        print("\n\n👋 Demo launcher stopped")
        sys.exit(0)


if __name__ == "__main__":
    main()
