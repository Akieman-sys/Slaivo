# GAPS indispensables v1 — SLAIVO CARGO

## 1. Objectif
Ce document liste les principaux trous de connaissance à traiter pour sécuriser le design, le build et le pilote de SLAIVO CARGO v1.

Un GAP est un point important que l’équipe ne maîtrise pas encore suffisamment et qui peut fragiliser le produit si rien n’est vérifié.

## 2. Principe
Les GAPS v1 doivent être :
- concrets
- liés au terrain réel
- liés à un risque produit ou opérationnel
- associés à une méthode de validation
- associés à une sortie attendue

## 3. GAP 1 — WhatsApp Cloud API réalité locale
### Ce qu’on ne sait pas encore assez bien
La réalité pratique du canal WhatsApp pour notre cas v1 :
- templates
- contraintes d’envoi
- limites conversationnelles
- coûts
- comportement réel sur les scénarios tracking / relance

### Pourquoi c’est important
SLAIVO CARGO est WhatsApp-first.
Une mauvaise compréhension du canal peut casser le wedge v1 ou dégrader les relances.

### Risques
- scénario produit non réaliste
- messages mal conçus
- coûts mal estimés
- contraintes non anticipées

### Validation
- revue de documentation utile
- test pratique ou sandbox
- simulation des scénarios v1 principaux

### Sortie attendue
- document `docs/research/whatsapp-reality-check.md`
- contraintes concrètes notées
- décisions de design confirmées ou ajustées

### Timing
À traiter avant ou au tout début du build MVP

## 4. GAP 2 — Process cargo réel
### Ce qu’on ne sait pas encore assez bien
La diversité réelle des statuts, termes, étapes et pratiques des agences cargo à Kinshasa.

### Pourquoi c’est important
Notre modèle Shipment et notre machine de statut doivent rester suffisamment proches du terrain pour être adoptables.

### Risques
- mauvais mapping de statuts
- faible adoption agence
- relances mal déclenchées
- vocabulaire produit déconnecté du réel

### Validation
- interviews terrain
- collecte de statuts réels
- collecte de fichiers ou exemples opérateurs
- mapping entre terrain et modèle v1

### Sortie attendue
- document `docs/research/cargo-status-mapping.md`
- liste des termes observés
- mapping vers la machine v1
- liste des écarts à gérer

### Timing
À traiter avant ou au début du build MVP

## 5. GAP 3 — Copywriting terrain
### Ce qu’on ne sait pas encore assez bien
Les formulations les plus efficaces pour :
- rassurer
- informer
- relancer
- escalader
- calmer un client frustré

### Pourquoi c’est important
Sur WhatsApp, la qualité perçue dépend énormément du ton, de la longueur et de la clarté des messages.

### Risques
- messages trop longs
- ton robotique
- incompréhension
- irritation client
- faible efficacité des CTA

### Validation
- collecte de messages terrain
- création de variantes
- retours utilisateurs/agences
- itération sur templates

### Sortie attendue
- document `docs/research/copywriting-pack-v1.md`
- pack de templates v1
- variantes recommandées par cas d’usage

### Timing
À démarrer avant build et à améliorer pendant MVP/pilote

## 6. GAP 4 — Balance / paiement sans PSP
### Ce qu’on ne sait pas encore assez bien
La manière réelle dont les agences gèrent :
- solde restant
- instruction de paiement
- preuve de paiement
- relance financière
sans paiement intégré au produit

### Pourquoi c’est important
La balance est sensible.
Une mauvaise formulation ou une mauvaise donnée peut créer conflit, confusion ou perte de confiance.

### Risques
- messages financiers mal reçus
- données non fiables
- erreurs de communication
- litiges

### Validation
- interviews agences
- collecte de cas réels
- analyse des messages existants
- définition d’une politique prudente v1

### Sortie attendue
- document `docs/research/balance-without-psp-v1.md`
- politique v1 sur balance
- cas supportés et non supportés
- messages recommandés

### Timing
À travailler en parallèle du MVP et à raffiner pendant le pilote

## 7. Résumé
Les quatre GAPS prioritaires de SLAIVO CARGO v1 sont :
- réalité WhatsApp
- réalité process cargo
- qualité du copywriting terrain
- gestion de balance sans paiement intégré

Ces GAPS doivent être traités de manière explicite pour réduire le risque produit et améliorer la qualité du MVP.