# Architecture 1 page — SLAIVO CARGO v1

## 1. Objectif
Cette architecture 1 page décrit la vue simple du système SLAIVO CARGO v1.

Le but est de montrer comment un message client entre dans le système, comment il est compris, comment l’information est récupérée, comment la réponse est générée, et comment les cas complexes sont transmis aux opérateurs humains.

## 2. Vue d’ensemble
Flux principal :

**WhatsApp → Ingest → Intent Router → Tracking / Knowledge → Reply Builder → Send Reply → Logs / Inbox / Escalation**

Flux événementiel :

**Shipment Status Update → Relance Engine → Cooldown Check → Send Reply → Logs / Inbox si besoin**

## 3. Blocs du système

### 3.1 WhatsApp
Point d’entrée externe des messages clients.
Le client envoie un message via WhatsApp.
WhatsApp transmet l’événement au système via webhook.

### 3.2 Ingest
Couche de réception et de normalisation.
Elle :
- reçoit le webhook
- valide le message entrant
- extrait les champs utiles
- normalise le format
- enregistre l’entrée
- applique les premiers garde-fous contre les doublons

### 3.3 Intent Router
Couche de compréhension et d’aiguillage.
Elle détecte l’intention principale du message et choisit le traitement adapté.

Intentions v1 typiques :
- tracking_lookup
- pricing_query
- departure_query
- warehouse_address
- human_handoff
- unknown

### 3.4 Tracking / Shipment Store
Source de vérité des colis.
Cette couche contient les données opérationnelles de shipment :
- tracking_id
- statut
- ETA
- origine
- destination
- balance éventuelle
- dernière mise à jour

Elle est utilisée quand l’intention du client concerne un colis spécifique.

### 3.5 Knowledge Store
Source contrôlée des informations métier générales.
Cette couche contient :
- tarifs
- départs
- adresses entrepôts
- horaires
- conditions simples

Elle est utilisée quand l’intention concerne une question FAQ métier.

### 3.6 Reply Builder
Couche de construction des réponses.
Elle :
- transforme les données métier en message lisible
- applique des templates de réponse
- ajoute les CTA utiles
- vérifie les garde-fous métier avant envoi

### 3.7 Send Reply
Couche d’envoi de la réponse vers WhatsApp.
Elle transmet le message final au client.

### 3.8 Inbox / Escalation
Couche humaine et opérationnelle.
Elle sert à :
- reprendre la main sur une conversation
- assigner un agent
- ajouter tags et notes
- traiter les cas inconnus ou sensibles

L’escalade est déclenchée si :
- le tracking est introuvable
- le tarif est inconnu
- la demande est ambiguë
- le client est frustré
- le cas nécessite une validation humaine

### 3.9 Relance Engine
Moteur des messages proactifs déclenchés par événement.
Il réagit aux changements métier importants comme :
- ARRIVED_KIN
- READY_FOR_PICKUP

Il applique :
- règles métier
- templates
- cooldown anti-spam
- journalisation

### 3.10 Logs / Audit / Exports
Couche de traçabilité.
Elle conserve :
- messages entrants
- intents détectés
- réponses envoyées
- relances
- escalades
- erreurs
- actions opérateurs

Cette couche est essentielle pour :
- débugger
- mesurer
- auditer
- préparer les exports futurs

## 4. Flux principal v1
1. Le client envoie un message sur WhatsApp.
2. Ingest reçoit et normalise l’événement.
3. Intent Router détermine l’intention.
4. Le système interroge soit Tracking, soit Knowledge.
5. Reply Builder construit une réponse contrôlée.
6. Send Reply envoie la réponse.
7. Logs enregistrent l’opération.
8. Si nécessaire, Inbox / Escalation prend le relais.

## 5. Flux de relance v1
1. Un shipment change d’état.
2. Le Relance Engine détecte l’événement.
3. Il vérifie les règles et le cooldown.
4. Il construit le message à envoyer.
5. Send Reply envoie la relance.
6. Logs enregistrent la relance.
7. En cas d’échec ou de cas sensible, Inbox peut être notifiée.

## 6. Principe d’architecture v1
L’architecture v1 doit rester :
- simple
- modulaire
- traçable
- contrôlée
- orientée règles métier
- compatible avec une escalade humaine propre

## 7. Résumé
SLAIVO CARGO v1 repose sur une chaîne simple :
- recevoir
- comprendre
- chercher
- répondre
- escalader si nécessaire
- tracer systématiquement