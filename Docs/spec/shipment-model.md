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


# Spec — Shipment Model v1 Contenu enrichi

## 1. Objectif
Ce document définit le modèle standard `Shipment` utilisé par SLAIVO CARGO v1.

Le modèle Shipment est l’objet métier central du système. Il doit permettre le tracking client, les relances automatiques, la consultation opérateur dans l’inbox, et la préparation des futures preuves et exports.

## 2. Principes de design
Le modèle Shipment v1 doit être :
- simple
- stable
- compatible terrain
- suffisant pour le tracking
- compatible avec des données parfois incomplètes
- strict sur les champs les plus critiques

## 3. Nom du modèle
`Shipment`

## 4. Champs du modèle

### 4.1 Identité
- `shipment_id` : string, identifiant interne unique, obligatoire
- `tracking_id` : string, identifiant communiqué au client, obligatoire

### 4.2 Client
- `client_name` : string nullable
- `client_phone` : string, obligatoire

### 4.3 Trajet
- `origin` : string nullable
- `destination` : string nullable
- `cargo_type` : enum (`air`, `sea`, `road`, `unknown`), nullable logique autorisée via `unknown`

### 4.4 État opérationnel
- `status` : enum officiel v1, obligatoire
- `last_update_at` : datetime UTC, obligatoire
- `eta` : datetime UTC nullable

### 4.5 Montants
- `fees_due` : decimal nullable
- `fees_paid` : decimal nullable
- `balance` : decimal nullable
- `currency` : string nullable

### 4.6 Interne / audit
- `notes_internal` : text nullable
- `created_at` : datetime UTC, obligatoire
- `updated_at` : datetime UTC, obligatoire

## 5. Champs obligatoires minimums v1
Les champs obligatoires minimums sont :
- `shipment_id`
- `tracking_id`
- `client_phone`
- `status`
- `last_update_at`
- `created_at`
- `updated_at`

## 6. Règles métier v1
- `shipment_id` doit être unique en interne
- `tracking_id` doit être unique par agence
- `client_phone` doit être normalisé
- `status` doit appartenir à la liste officielle des statuts v1
- `last_update_at` doit être mis à jour lors d’un changement de statut
- `notes_internal` n’est jamais exposé au client
- `eta` ne doit pas être inventée si elle est inconnue
- `balance` peut être dérivé de `fees_due - fees_paid` si les deux valeurs existent
- si `fees_due` et `fees_paid` sont connus, `balance` doit rester cohérent avec ces champs

## 7. Champs exposables côté client
Les champs potentiellement visibles côté client sont :
- `tracking_id`
- `origin`
- `destination`
- `status`
- `eta`
- `balance`
- `currency`

L’exposition de `balance` dépend de la politique de l’agence.

## 8. Champs strictement internes
Les champs suivants ne sont pas exposés au client :
- `shipment_id`
- `notes_internal`
- `created_at`
- `updated_at`

## 9. Rôle du modèle Shipment v1
Le modèle Shipment v1 doit suffire pour :
- lookup tracking
- affichage du statut
- affichage d’une ETA si disponible
- déclenchement de relances automatiques
- reprise opérateur dans l’inbox
- support de base aux exports futurs

## 10. Principe de prudence métier
Quand une donnée n’est pas connue, le système doit préférer :
- valeur absente
plutôt que
- valeur inventée

Cela s’applique particulièrement à :
- `eta`
- `fees_due`
- `fees_paid`
- `balance`
- `origin`
- `destination`