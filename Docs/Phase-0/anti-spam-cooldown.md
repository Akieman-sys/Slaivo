# Anti-Spam & Cooldown v1 — SLAIVO CARGO

## 1. Objectif
Ce document définit les garde-fous anti-spam et les règles de cooldown de SLAIVO CARGO v1.

Le but est de protéger :
- l’expérience client
- la réputation du canal WhatsApp
- la cohérence conversationnelle
- le système contre les doublons et les boucles

## 2. Principes
Les messages automatiques ne doivent pas être envoyés sans contrôle.

La politique v1 combine :
- déduplication
- cooldown
- limitation de fréquence
- pause après intervention humaine
- détection de boucle

## 3. Règle 1 — Cooldown par téléphone et par intent
### Clé
`client_phone + intent`

### Politique
Si le même numéro déclenche le même intent dans une fenêtre de 60 secondes, le système ne doit pas renvoyer une réponse automatique complète identique.

### Réponse possible
Le système peut :
- ne rien renvoyer
- renvoyer une version plus courte
- escalader vers un humain si le comportement semble anormal

### Intentions concernées v1
- tracking_lookup
- pricing_query
- departure_query
- warehouse_address

## 4. Règle 2 — Cooldown relance événementielle par shipment
### Clé
`shipment_id + event_type`

### Politique v1
- une relance automatique `ARRIVED_KIN` ne doit pas être renvoyée plus d’une fois dans une fenêtre de 24h pour le même shipment
- une relance automatique `READY_FOR_PICKUP` de même niveau ne doit pas être renvoyée plus d’une fois dans une fenêtre de 24h pour le même shipment

## 5. Règle 3 — Limite globale de messages automatiques par téléphone
### Clé
`client_phone`

### Politique
Le système ne doit pas envoyer plus de 5 messages automatiques au même numéro dans une fenêtre glissante de 15 minutes.

### En cas de dépassement
- bloquer les messages automatiques non critiques
- journaliser la raison du blocage
- permettre une revue humaine si nécessaire

## 6. Règle 4 — Une seule réponse automatique par message entrant
### Clé
`provider_message_id` ou `dedupe_key`

### Politique
Un même message entrant ne doit produire qu’une seule réponse automatique.

Cette règle protège contre :
- retries
- webhooks dupliqués
- traitements répétés
- erreurs d’idempotence

## 7. Règle 5 — Pause après intervention humaine
### Clé
`conversation_id`

### Politique
Après une réponse manuelle d’un agent, le bot doit rester silencieux pendant 5 minutes sur cette conversation, sauf cas critique explicitement autorisé.

### Objectif
Éviter qu’un message automatique interrompe ou contredise un agent humain.

## 8. Règle 6 — Détection de boucle
### Clé
`shipment_id`

### Politique
Si plus de 3 tentatives d’envoi automatiques liées au même shipment surviennent dans une fenêtre de 10 minutes :
- bloquer les envois automatiques supplémentaires liés à ce shipment
- journaliser un événement `possible_loop_detected`
- créer un signal de revue humaine si applicable

## 9. Exceptions et prudence
Les garde-fous anti-spam ne doivent pas empêcher :
- une escalade humaine légitime
- une première réponse utile
- une action critique explicitement autorisée

Toute exception doit rester traçable.

## 10. Journalisation minimale
Le système doit pouvoir tracer :
- la clé de cooldown utilisée
- le type de règle appliquée
- l’heure du blocage ou de l’autorisation
- la raison d’un non-envoi
- l’éventuelle détection de boucle

## 11. Résumé
SLAIVO CARGO v1 applique une politique anti-spam simple mais ferme :
- répétitions limitées
- relances contrôlées
- fréquence bornée
- coordination humain/bot
- blocage des boucles