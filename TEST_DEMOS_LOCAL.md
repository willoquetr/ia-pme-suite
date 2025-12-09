# 📋 TEST PLAN - Démos Interactives (Local)

## Préparation

```powershell
cd "d:\DevPortable\Projects"
python -m http.server 8000
```

Puis ouvre: **http://localhost:8000/demos.html**

---

## 🧪 Test 1: Email Classifier Upload

**Fichier:** `test_email_sample.txt`

**Étapes:**
1. Scroll à la section "📧 Email Classifier AI"
2. Clique sur le bouton "📎 Fichier" (input file)
3. Sélectionne `test_email_sample.txt`
4. Observe que le texte remplit la textarea
5. La classification doit se lancer auto et montrer: **FACTURE** (confidence ~80-90%)

**Résultat attendu:**
- ✅ Textarea remplie avec le contenu du fichier
- ✅ Catégorie détectée: "FACTURE"
- ✅ Confiance: 80%+ (mots-clés: "facture", "montant", "paiement", "échéance")

---

## 📊 Test 2: Excel Analyzer Upload

**Fichier:** `test_excel_sample.csv`

**Étapes:**
1. Scroll à la section "📊 Excel Analyzer AI"
2. Clique sur le bouton "📎 Fichier CSV" (input file)
3. Sélectionne `test_excel_sample.csv`
4. Observe que les données remplissent la textarea
5. L'analyse doit se lancer auto et détecter les anomalies

**Résultat attendu:**
- ✅ Textarea remplie (9 lignes de données)
- ✅ Résumé: "8 lignes × 5 colonnes"
- ✅ Anomalies détectées:
  - ⚠️ **Valeurs manquantes** en colonne "Email" (1 occurrence)
  - ⚠️ **Valeurs manquantes** en colonne "Montant" (1 occurrence)
  - ⚠️ **Valeurs manquantes** en colonne "Date" (1 occurrence)
  - ⚠️ **Doublons** (1 ligne: Alice Dupont apparaît 2× avec même email)

---

## 📄 Test 3: PDF Generator (Formulaire)

**Étapes:**
1. Scroll à la section "📄 PDF Generator AI"
2. Vérifie que le dropdown affiche: Devis, Facture, Lettre, Contrat, Rapport
3. Laisse "Devis" sélectionné
4. Remplis les champs requis:
   - Nom du client: `Entreprise XYZ`
   - Email: `contact@xyz.fr`
   - Description: `Mise en place solution IA sur 3 mois`
   - Montant HT (€): `5000`
   - Validité (jours): `60` (pré-rempli)
5. Clique "📋 Générer aperçu"

**Résultat attendu:**
- ✅ Aperçu généré avec les données
- ✅ Format: "DEVIS" en titre centré
- ✅ Affiche: Pour, Email, Description, Montant, Validité

---

## ✅ Checklist Finale

- [ ] Email upload fonctionne
- [ ] Excel upload fonctionne
- [ ] Classification détecte "FACTURE"
- [ ] Analyse Excel détecte 3+ anomalies
- [ ] PDF aperçu se génère correctement
- [ ] Pas d'erreurs console (F12)
- [ ] Page responsive mobile (resize navigateur)

---

## 🐛 Troubleshooting

| Problème | Solution |
|----------|----------|
| "Fichier non trouvé" | Assure-toi que les fichiers sont dans `d:\DevPortable\Projects\` |
| Upload ne remplit pas textarea | Vérifier console (F12) pour erreurs FileReader |
| SheetJS non chargé (.xlsx) | CDN peut être bloqué — utilise CSV à la place |
| Serveur ne démarre pas | `python -m http.server 8000` doit être dans le venv activé |

---

**Qui tester?** Toi d'abord localement, ensuite un client réel sur GitHub Pages (après `git push`).
