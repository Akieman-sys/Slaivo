# Scope v1 — SLAIVO CARGO

## 1. Objectif du scope v1
Le scope v1 définit la frontière officielle de ce que SLAIVO CARGO construit pour prouver la valeur du wedge initial.

Le but n’est pas de construire tout le produit final, mais de livrer une première version vendable, claire, simple à comprendre, et suffisamment utile pour une agence pilote.

## 2. Principes de scope
Le scope v1 doit rester :
- centré sur le wedge principal
- rapide à implémenter
- simple à démontrer
- contrôlable opérationnellement
- limité en risques produit et techniques

Tout ce qui n’est pas nécessaire pour prouver la valeur du wedge v1 est hors scope.

## 3. Ce que SLAIVO CARGO fait en v1

### 3.1 Canal unique
SLAIVO CARGO v1 utilise un seul canal de communication :
- WhatsApp

### 3.2 Tracking self-serve
Le système permet à un client de demander le suivi de son colis via un tracking_id.

La réponse v1 doit pouvoir fournir :
- le statut actuel
- l’ETA si disponible
- la prochaine action attendue

### 3.3 FAQ métier simple
Le système répond aux questions fréquentes sur :
- tarifs
- départs
- adresses entrepôts
- horaires
- conditions simples

### 3.4 Relances automatiques v1
Le système envoie des relances automatiques au minimum sur les événements :
- ARRIVED_KIN
- READY_FOR_PICKUP

### 3.5 Inbox opérateurs
L’agence dispose d’une inbox simple pour :
- voir les conversations
- reprendre la main
- assigner un agent
- ajouter des tags
- ajouter des notes internes

### 3.6 Escalade humaine
Le système doit pouvoir escalader vers un humain dans les cas suivants :
- réponse inconnue
- prix inconnu
- tracking introuvable
- question sensible
- client frustré ou agressif
- cas douane ou opération spéciale

## 4. Ce que SLAIVO CARGO refuse en v1

### 4.1 Paiements intégrés
Le système ne gère pas encore :
- mobile money intégré
- paiement par carte
- checkout
- preuve de paiement automatisée complète

### 4.2 IA générative avancée
Le système ne repose pas en v1 sur une IA autonome ouverte.
La logique v1 privilégie :
- règles
- templates
- réponses contrôlées
- escalade humaine

### 4.3 Multi-agences complexes
Le système ne cible pas en v1 la gestion avancée de nombreuses agences avec structures complexes.

### 4.4 Multi-branches avancé
Le système ne gère pas encore les structures complexes avec plusieurs branches et permissions fines.

### 4.5 Analytics avancés
Le système ne fournit pas encore de dashboards avancés ni d’analyses profondes.

### 4.6 Evidence packs complets
Le système ne produit pas encore de packs PDF complets anti-litige.

### 4.7 Intégrations lourdes
Le système n’intègre pas encore des ERP, CRM ou systèmes complexes tiers.

## 5. Pourquoi ces refus sont nécessaires
Ces refus permettent de :
- protéger la vitesse d’exécution
- réduire le risque technique
- éviter la surcharge produit
- garder un MVP compréhensible
- valider le wedge avant d’élargir

## 6. Résumé du scope v1
SLAIVO CARGO v1 se concentre sur :
- WhatsApp
- tracking self-serve
- FAQ tarifs/départs/adresses
- relances ARRIVED_KIN et READY_FOR_PICKUP
- inbox opérateurs
- escalade humaine

Tout le reste est explicitement hors scope v1.