# Spec — Shipment Model v1

## 1. Objectif
Ce document définit le modèle standard `Shipment` utilisé par SLAIVO CARGO v1.

Le modèle v1 doit être suffisamment simple pour fonctionner avec une agence pilote, tout en étant assez structuré pour supporter tracking, relances et inbox.

## 2. Nom du modèle
`Shipment`

## 3. Champs principaux
- `shipment_id` : string, identifiant interne unique
- `tracking_id` : string, identifiant communiqué au client
- `client_name` : string
- `client_phone` : string
- `origin` : string
- `destination` : string
- `cargo_type` : enum (`air`, `sea`, `road`, `unknown`)
- `status` : enum de la machine de statut v1
- `last_update_at` : datetime UTC
- `eta` : datetime UTC nullable
- `fees_due` : decimal nullable
- `fees_paid` : decimal nullable
- `balance` : decimal nullable
- `currency` : string nullable
- `notes_internal` : text nullable
- `created_at` : datetime UTC
- `updated_at` : datetime UTC

## 4. Champs obligatoires v1
Les champs obligatoires minimums sont :
- `shipment_id`
- `tracking_id`
- `client_phone`
- `status`
- `last_update_at`
- `created_at`
- `updated_at`

## 5. Règles métier v1
- `tracking_id` doit être unique par agence
- `client_phone` doit être normalisé
- `status` doit appartenir à la liste officielle v1
- `last_update_at` doit changer quand le statut change
- `balance` peut être dérivé de `fees_due - fees_paid` si les deux sont connus
- `notes_internal` n’est jamais exposé au client

## 6. Règles d’exposition client
Les champs potentiellement visibles côté client sont :
- `tracking_id`
- `origin`
- `destination`
- `status`
- `eta`
- `balance` si la politique agence l’autorise

Les champs non exposés par défaut sont :
- `shipment_id`
- `notes_internal`
- toute donnée interne opérateur

## 7. But du modèle v1
Le modèle shipment v1 doit permettre :
- lookup tracking
- affichage statut
- affichage ETA si disponible
- déclenchement de relances
- travail opérateur via inbox