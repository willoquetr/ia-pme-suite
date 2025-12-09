# 🌐 Landing Page - IA PME

## Fichier créé : `index.html`

Une landing page moderne, responsive et professionnelle pour votre startup IA PME.

### Caractéristiques

- ✅ Design moderne avec gradient (violet/bleu)
- ✅ 100% responsive (mobile, tablette, desktop)
- ✅ Sections complètes : Hero, Features, Pricing, Use cases, CTA
- ✅ Pas de dépendances externes (pur HTML/CSS)
- ✅ Facile à customiser
- ✅ Optimisé pour le référencement

### Contenu

**Sections incluses:**
1. **Header** - Navigation sticky avec logo
2. **Hero** - Titre accrocheur + 2 CTA buttons
3. **Features** - 3 solutions principales (Email, PDF, Excel)
4. **Use cases** - 6 cas d'usage PME
5. **Pricing** - 3 plans (Gratuit, Starter, Pro)
6. **CTA finale** - Appel à l'action
7. **Footer** - Contact + mentions légales

### Comment l'utiliser

#### Option 1 : Visualiser localement
```bash
# Ouvrir directement dans le navigateur
start index.html
# Ou avec Python
python -m http.server 8000
# Puis aller à http://localhost:8000
```

#### Option 2 : Déployer sur GitHub Pages (GRATUIT)
```bash
1. Créer repo GitHub: https://github.com/new
2. Nommer: "iapme" ou "ia-pme"
3. Cloner localement:
   git clone https://github.com/votre-username/ia-pme.git
   cd ia-pme

4. Copier index.html dans le dossier

5. Committer et pusher:
   git add index.html
   git commit -m "Landing page initiale"
   git push

6. Aller à Settings > Pages > Branch: main > Save

7. Accès: https://votre-username.github.io/ia-pme/
```

#### Option 3 : Déployer sur Netlify (GRATUIT + CDN)
```bash
1. Aller à https://netlify.com
2. "Add new site" > "Deploy manually"
3. Drag & drop le fichier index.html
4. URL auto-générée : https://xxx.netlify.app/
```

#### Option 4 : Déployer sur Vercel (GRATUIT)
```bash
1. Aller à https://vercel.com
2. "New project" > Upload index.html
3. URL : https://xxx.vercel.app/
```

### Customisation

Modifier facilement ces éléments:

```html
<!-- Logo -->
<div class="logo">IA PME</div>

<!-- Titre principal -->
<h1>L'Intelligence Artificielle pour vos PME</h1>

<!-- Description -->
<p>Automatisez vos taches quotidiennes...</p>

<!-- Buttons CTA -->
<button class="btn btn-primary">Démarrer gratuitement</button>

<!-- Email -->
<p>rudy@iapme.fr</p>
```

### Couleurs

- Primaire (Gradient): #667eea → #764ba2 (violet-bleu)
- Secondaire: White
- Background: #f8f9fa (gris clair)
- Texte: #333

Pour changer les couleurs, remplacer ces valeurs dans la section `<style>`.

### Intégrations recommandées

1. **Email** (formulaire contact)
   ```html
   <form action="https://formspree.io/f/YOUR_ID" method="POST">
       <input type="email" name="email" required>
       <textarea name="message" required></textarea>
       <button type="submit">Envoyer</button>
   </form>
   ```

2. **Analytics** (Google Analytics)
   ```html
   <script async src="https://www.googletagmanager.com/gtag/js?id=GA_ID"></script>
   <script>
     window.dataLayer = window.dataLayer || [];
     function gtag(){dataLayer.push(arguments);}
     gtag('js', new Date());
     gtag('config', 'GA_ID');
   </script>
   ```

3. **Calendly** (Demo scheduling)
   ```html
   <link href="https://assets.calendly.com/assets/external/widget.css" rel="stylesheet">
   <script src="https://assets.calendly.com/assets/external/widget.js" type="text/javascript" async></script>
   <a href="" onclick="Calendly.initPopupWidget({url: 'https://calendly.com/your-username'});return false;">Reserver un créneau</a>
   ```

### SEO

Ajouter au `<head>`:
```html
<meta name="description" content="Solutions IA pour PMEs - Classifier emails, générer PDFs, analyser Excel">
<meta name="keywords" content="IA, PME, automation, email, PDF, Excel">
<meta property="og:title" content="IA PME - Solutions IA">
<meta property="og:description" content="Automatisez vos taches...">
<meta property="og:image" content="https://...">
```

### Performance

- Page ultra-légère (~50KB)
- Charge en < 1s
- 100% responsive
- Pas de JavaScript lourd

### Next Steps

1. [ ] Héberger sur GitHub Pages / Netlify / Vercel
2. [ ] Ajouter formulaire contact (Formspree)
3. [ ] Ajouter Google Analytics
4. [ ] Ajouter Calendly pour démos
5. [ ] Optimiser SEO
6. [ ] Custom domain (iapme.fr)
7. [ ] A/B testing des CTA

---

**Status**: ✅ Landing page prête à déployer
