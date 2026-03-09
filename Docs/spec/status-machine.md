# Spec — Status Machine v1

## 1. Objectif
Ce document définit la machine de statut officielle des shipments pour SLAIVO CARGO v1.

Le but est de standardiser le cycle de vie d’un colis et de limiter les transitions incohérentes.

## 2. Liste officielle des statuts v1
Les statuts standards v1 sont :

- `RECEIVED`
- `DEPARTED`
- `IN_TRANSIT`
- `ARRIVED`
- `IN_CUSTOMS`
- `CLEARED`
- `ARRIVED_KIN`
- `READY_FOR_PICKUP`
- `DELIVERED`
- `ISSUE`

## 3. Signification des statuts
- `RECEIVED` : colis reçu ou enregistré initialement
- `DEPARTED` : départ confirmé
- `IN_TRANSIT` : en cours de transport
- `ARRIVED` : arrivé au hub ou point intermédiaire important
- `IN_CUSTOMS` : en attente ou en traitement douane
- `CLEARED` : dédouanement terminé
- `ARRIVED_KIN` : arrivé à Kinshasa
- `READY_FOR_PICKUP` : disponible pour retrait
- `DELIVERED` : remis au client
- `ISSUE` : incident, blocage ou anomalie

## 4. Transitions autorisées v1
Transitions normales autorisées :

- `RECEIVED -> DEPARTED`
- `DEPARTED -> IN_TRANSIT`
- `IN_TRANSIT -> ARRIVED`
- `ARRIVED -> IN_CUSTOMS`
- `IN_CUSTOMS -> CLEARED`
- `CLEARED -> ARRIVED_KIN`
- `ARRIVED_KIN -> READY_FOR_PICKUP`
- `READY_FOR_PICKUP -> DELIVERED`

Transitions exceptionnelles autorisées :
- tout statut opérationnel peut aller vers `ISSUE`
- `ISSUE -> IN_TRANSIT`
- `ISSUE -> IN_CUSTOMS`
- `ISSUE -> ARRIVED_KIN`
- `ISSUE -> READY_FOR_PICKUP`

## 5. Transitions interdites v1
Exemples de transitions interdites :
- `RECEIVED -> DELIVERED`
- `DEPARTED -> READY_FOR_PICKUP`
- `DELIVERED -> IN_TRANSIT`
- `READY_FOR_PICKUP -> RECEIVED`

## 6. Règles v1
- un shipment ne doit avoir qu’un seul statut courant
- chaque changement de statut doit être horodaté
- les transitions doivent être validées côté backend
- les transitions interdites doivent être rejetées ou signalées
- `ISSUE` n’efface pas l’historique, c’est un état courant temporaire de blocage

## 7. Usage produit
La machine de statut v1 est utilisée pour :
- le tracking client
- les relances automatiques
- la timeline dossier
- la cohérence des opérations