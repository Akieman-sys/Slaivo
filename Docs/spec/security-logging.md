# Spec — Security & Logging v1

## 1. Objectif
Ce document définit les règles minimales de sécurité et de journalisation pour SLAIVO CARGO v1.

Le but est de construire un système traçable sans exposer inutilement les secrets ou les données sensibles.

## 2. Principes généraux
- logguer ce qui aide à comprendre
- ne jamais logguer les secrets en clair
- limiter les données sensibles exposées
- permettre l’audit des actions importantes
- séparer logs techniques et données métier sensibles quand possible

## 3. Ce qui doit être loggué
Le système doit journaliser au minimum :
- réception d’un message entrant
- normalisation du message
- intent détecté
- lookup tracking ou knowledge
- réponse envoyée ou échec d’envoi
- relance déclenchée ou annulée
- escalade vers inbox
- actions opérateur importantes
- erreurs système

## 4. Ce qui ne doit jamais être loggué en clair
Interdictions absolues :
- tokens API
- clés secrètes
- mots de passe
- secrets d’environnement
- credentials de base de données

Ces valeurs doivent être redacted ou absentes des logs.

## 5. Données client et minimisation
Règles v1 :
- éviter de dupliquer inutilement les données personnelles
- ne logguer que le nécessaire au débogage et à l’audit
- masquer partiellement certaines données si possible dans les vues larges

## 6. Payloads bruts
Les payloads bruts externes peuvent être conservés pour audit et débogage, mais :
- l’accès doit être limité
- leur référence doit être distincte des logs applicatifs
- ils ne doivent pas être affichés largement sans contrôle

## 7. Audit opérateur
Les actions humaines suivantes doivent être auditables :
- assignation
- ajout de note
- changement de tag
- réponse manuelle
- changement de statut effectué par un opérateur si ce cas existe

## 8. Principe de sécurité v1
SLAIVO CARGO v1 privilégie :
- simplicité
- prudence
- traçabilité
- minimisation des secrets exposés