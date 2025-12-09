# 🌐 GUIDE COMPLET - Domaine + Email Professionnel pour IA-PME

**Objectif:** Avoir `rudy@ia-pme.fr` et site `ia-pme.fr` fonctionnels  
**Coût:** ~12€/an (domaine) + 3€/mois (email)  
**Temps:** 30 minutes

---

## 📊 **RÉSUMÉ RAPIDE**

| Item | Option | Coût | Temps |
|------|--------|------|-------|
| **Domaine** | Namecheap ou OVH | €12-15/an | 5 min |
| **Email** | Forwarder gratuit + Gmail | €0 | 10 min |
| **Email Pro** | Zoho Mail (3€/mois) | €36/an | 5 min |
| **Site** | Votre landing page | €0 | 5 min |

---

## 🎯 **ÉTAPE 1: Acheter un domaine (5 min)**

### Option 1: **Namecheap** (RECOMMANDÉ - Simple)

1. Allez sur: **https://www.namecheap.com**
2. Cherchez: `ia-pme.fr`
3. Cliquez: **Add to cart**
4. Remplissez vos infos (Rudy Willoquet)
5. Coût: ~€12-15/an
6. **Cliquez "Confirm Order"**

### Option 2: **OVH** (Français, bon support)

1. Allez sur: **https://www.ovh.fr/domaines**
2. Cherchez: `ia-pme.fr`
3. Suivez les étapes
4. Coût: ~€8-12/an
5. **Confirm**

---

## ✉️ **ÉTAPE 2: Email Professionnel (10 min)**

Vous avez 3 options:

### **Option A: Email Forwarder GRATUIT** (Basique)

**Que c'est:** Les emails à `rudy@ia-pme.fr` sont redirigés vers votre Gmail  
**Coût:** €0  
**Limitation:** Vous pouvez recevoir mais pas envoyer depuis `@ia-pme.fr`

**Procédure:**
1. Chez Namecheap/OVH, allez à **"Mail Settings"**
2. Ajoutez un **Email Forwarder:**
   ```
   Forwarder: rudy@ia-pme.fr
   Destination: votre.gmail@gmail.com
   ```
3. Activez

**Résultat:** Les emails envoyés à `rudy@ia-pme.fr` arrivent dans votre Gmail

---

### **Option B: Zoho Mail PRO** (RECOMMANDÉ)

**Que c'est:** Vrai email professionnel avec interface webmail  
**Coût:** €3/mois (~€36/an)  
**Avantage:** Vous pouvez envoyer/recevoir depuis `rudy@ia-pme.fr` facilement

**Procédure:**

1. Allez sur: **https://www.zoho.com/mail**
2. Cliquez: **Sign Up**
3. Créez un compte:
   ```
   Email: rudy@ia-pme.fr
   Mot de passe: [Secure password]
   Organisation: IA-PME
   ```
4. Configurez votre domaine:
   - Allez à **Settings** → **Domains**
   - Cliquez **Add Domain**
   - Entrez: `ia-pme.fr`
   - Zoho vous donne les **DNS Records**

5. **Configurez les DNS chez Namecheap/OVH:**
   
   Chez **Namecheap:**
   - Allez dans votre domaine
   - Cliquez **Manage DNS**
   - Remplacez les records par ceux de Zoho (MX, CNAME)
   - Sauvegardez
   
   Chez **OVH:**
   - Zone DNS
   - Ajoutez les records MX et CNAME de Zoho
   - Sauvegardez

6. Attendez 24-48h pour la propagation DNS

7. Connectez-vous à **Zoho Mail** avec `rudy@ia-pme.fr`

---

### **Option C: Gmail Custom Domain** (Gratuit mais compliqué)

**Coût:** €0  
**Limitation:** Google n'offre plus ce service gratuitement (besoin Google Workspace €6+/mois)

**Skip cette option - prenez Zoho à la place**

---

## 🌐 **ÉTAPE 3: Configurer votre site (5 min)**

### Pointer votre domaine vers GitHub Pages

**Chez Namecheap:**

1. Allez dans: **Manage Domain**
2. **Nameservers** → Change:
   ```
   Type: Custom DNS
   
   Nameserver 1: ns-1035.awsdns-30.com
   Nameserver 2: ns-302.awsdns-15.org
   Nameserver 3: ns-1763.awsdns-55.co.uk
   Nameserver 4: ns-627.awsdns-14.net
   ```
   (Fournis par GitHub)

3. Sauvegardez

**Chez OVH:**

1. Allez dans: **Zone DNS**
2. Modifiez les **NS Records** avec ceux de GitHub
3. Sauvegardez

**Dans votre repo GitHub:**

1. Settings → Pages
2. **Custom domain:** `ia-pme.fr`
3. Cliquez **Save**
4. ✅ **Enforce HTTPS**

Attendez 24-48h pour que ça se propage.

---

## 📧 **ÉTAPE 4: Ajouter à votre landing page**

Mettez à jour votre `index.html`:

Remplacez:
```html
Pour la demo: visitez https://iapme.com ou contactez rudy@iapme.fr
```

Par:
```html
Pour la demo: visitez https://ia-pme.fr ou contactez rudy@ia-pme.fr
```

Et dans les CTA buttons:
```html
<a href="mailto:rudy@ia-pme.fr?subject=Demande de démo IA-PME">
  Demander une démo
</a>
```

---

## ✅ **CHECKLIST FINALE**

- [ ] Domaine acheté (`ia-pme.fr`)
- [ ] Email configuré (Zoho Mail)
- [ ] DNS Records configurés chez Namecheap/OVH
- [ ] GitHub Pages pointe vers domaine
- [ ] HTTPS activé et fonctionne
- [ ] Email `rudy@ia-pme.fr` fonctionne
- [ ] Landing page accessible à `https://ia-pme.fr`
- [ ] Buttons email et demo fonctionnent

---

## 💡 **BUDGETS TOTAUX**

```
Domaine (1 an):       €12-15
Zoho Mail (1 an):     €36
Landing page:         €0 (GitHub Pages)
Apps (local):         €0 (Mistral free tier)

TOTAL ANNÉE 1:        €48-51
TOTAL/MOIS:           €4-4.25
```

---

## 🎯 **PROCHAINES ÉTAPES**

1. **Aujourd'hui:** Achetez domaine + configurez email
2. **Demain:** Attendez propagation DNS
3. **Jour 3:** Landing page accessible à votre domaine
4. **Jour 4:** Commencez prospection PME Rohan!

---

**Une fois ceci fait, vous êtes 100% prêt pour commercialiser! 🚀**

© 2025 IA-PME
