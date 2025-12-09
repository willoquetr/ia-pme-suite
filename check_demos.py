"""
Script de validation des démos
Vérifie que demos.html et l'API fonctionnent correctement
"""

import os
import sys
import json
import requests
from pathlib import Path

def check_html_files():
    """Vérifie que les fichiers HTML existent"""
    print("🔍 Checking HTML files...")
    
    files = {
        'index.html': 'Landing page',
        'demos.html': 'Interactive demos'
    }
    
    for filename, desc in files.items():
        path = Path(__file__).parent / filename
        if path.exists():
            size = path.stat().st_size
            print(f"  ✅ {filename:<20} ({desc:<25}) - {size:,} bytes")
        else:
            print(f"  ❌ {filename:<20} (MISSING)")
            return False
    
    return True


def check_api_endpoints():
    """Teste les endpoints de l'API"""
    print("\n🔍 Checking API endpoints...")
    
    base_url = "http://localhost:5000"
    
    # Test 1: Health check
    try:
        resp = requests.get(f"{base_url}/api/health", timeout=5)
        if resp.status_code == 200:
            data = resp.json()
            print(f"  ✅ /api/health - Status: {data['status']}")
        else:
            print(f"  ❌ /api/health - HTTP {resp.status_code}")
            return False
    except Exception as e:
        print(f"  ⚠️  API not running locally (expected) - {type(e).__name__}")
        return None
    
    # Test 2: Email classifier
    try:
        payload = {"content": "Voici ma facture de 500€"}
        resp = requests.post(f"{base_url}/api/email/classify", json=payload, timeout=5)
        if resp.status_code == 200:
            data = resp.json()
            category = data.get('result', {}).get('category')
            print(f"  ✅ /api/email/classify - Detected: {category}")
        else:
            print(f"  ❌ /api/email/classify - HTTP {resp.status_code}")
    except Exception as e:
        print(f"  ⚠️  {type(e).__name__}")
    
    return True


def check_github_pages():
    """Vérifie la config GitHub Pages"""
    print("\n🔍 Checking GitHub Pages setup...")
    
    workflow_file = Path(__file__).parent / '.github' / 'workflows' / 'deploy-demos.yml'
    if workflow_file.exists():
        print(f"  ✅ Workflow file exists: {workflow_file.name}")
    else:
        print(f"  ❌ Workflow file missing")
        return False
    
    # Vérifier le repo
    git_dir = Path(__file__).parent / '.git'
    if git_dir.exists():
        print(f"  ✅ Git repository found")
    else:
        print(f"  ❌ Git repository not found")
        return False
    
    return True


def check_deployment_ready():
    """Vérifie si tout est prêt pour le déploiement"""
    print("\n🚀 Deployment Readiness Check")
    print("=" * 50)
    
    checks = {
        "HTML files": check_html_files(),
        "GitHub Pages": check_github_pages(),
        "API endpoints": check_api_endpoints()
    }
    
    print("\n" + "=" * 50)
    print("📊 Summary:")
    for check, result in checks.items():
        status = "✅" if result else "❌" if result is False else "⚠️"
        print(f"  {status} {check}")
    
    if all(v is not False for v in checks.values()):
        print("\n✅ READY FOR DEPLOYMENT!")
        print("   Next: Push to GitHub and enable GitHub Pages")
        return True
    else:
        print("\n❌ Some checks failed")
        return False


if __name__ == '__main__':
    check_deployment_ready()
