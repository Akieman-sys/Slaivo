# SLO internes v1 — SLAIVO CARGO

## 1. Objectif
Ce document définit les objectifs internes minimums de qualité, fiabilité et sécurité pour SLAIVO CARGO v1.

Ces SLO ne sont pas encore des promesses contractuelles client. Ils servent de discipline interne pour construire un produit sérieux, mesurable et contrôlable.

## 2. Principes
Les SLO v1 doivent protéger en priorité :
- l’expérience client sur WhatsApp
- la cohérence des réponses
- la sécurité des secrets
- la fiabilité métier
- la prévention du spam ou des boucles

## 3. SLO v1

### 3.1 Temps de réponse WhatsApp
Objectif :
- p95 du temps de réponse < 30 secondes

Interprétation :
- au moins 95 % des réponses doivent être envoyées en moins de 30 secondes

Pourquoi :
- WhatsApp est un canal conversationnel
- une réponse trop lente dégrade fortement l’expérience perçue

### 3.2 Zéro double réponse
Objectif :
- zéro double réponse automatique sur un même message client

Interprétation :
- un même message entrant ne doit pas produire plusieurs réponses automatiques

Pourquoi :
- les doublons créent de la confusion
- ils peuvent être causés par des retries, des webhooks dupliqués ou un traitement non idempotent

### 3.3 Aucune invention de prix
Objectif :
- le système ne doit jamais inventer un tarif ou une information commerciale inconnue

Interprétation :
- si le tarif n’est pas connu, ambigu, manquant ou expiré, le système doit demander une précision ou escalader vers un humain

Pourquoi :
- un faux prix peut provoquer une perte de confiance, un conflit commercial ou une erreur opérationnelle

### 3.4 Cooldown anti-spam
Objectif :
- le système doit appliquer des garde-fous de fréquence et de répétition des messages

Interprétation :
- pas de répétition excessive d’un même message ou d’une même relance dans une fenêtre courte
- application d’un cooldown par téléphone client et par intent lorsque nécessaire

Pourquoi :
- éviter le spam
- éviter les boucles automatiques
- protéger l’expérience client et la réputation du numéro WhatsApp

### 3.5 Secrets jamais loggés en clair
Objectif :
- aucun token, secret, mot de passe ou clé API ne doit être loggé en clair

Interprétation :
- les logs doivent masquer ou redacter toute information sensible

Pourquoi :
- les logs sont souvent largement accessibles ou conservés
- une fuite dans les logs augmente fortement le risque de compromission

## 4. Résumé
SLAIVO CARGO v1 doit être :
- suffisamment rapide
- cohérent
- prudent sur les réponses métier
- non spammy
- sûr dans sa gestion des secrets

Ces SLO constituent le minimum de qualité interne à respecter dès le MVP.