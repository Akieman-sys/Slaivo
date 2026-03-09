# Spec — Inbox Actions v1

## 1. Objectif
Ce document définit les actions opérateur disponibles dans l’inbox SLAIVO CARGO v1.

Le but est de permettre une reprise humaine simple, traçable et cohérente.

## 2. Entités manipulées
L’inbox v1 manipule principalement :
- conversations
- messages
- shipments liés
- tags
- notes internes
- assignations

## 3. Actions opérateur v1 autorisées
Les actions minimums autorisées sont :

- voir une conversation
- assigner une conversation à un agent
- retirer l’assignation
- ajouter un tag
- retirer un tag
- ajouter une note interne
- marquer une conversation comme escaladée
- marquer une conversation comme résolue
- répondre manuellement au client
- lier une conversation à un shipment si nécessaire

## 4. Assignation
### Règles v1
- une conversation peut être non assignée ou assignée à un agent
- l’assignation courante doit être visible
- tout changement d’assignation doit être horodaté
- l’identité de l’agent doit être auditée

## 5. Tags v1
Exemples de tags v1 :
- `urgent`
- `payment`
- `customs`
- `vip`
- `angry_customer`
- `tracking_issue`

Règles :
- les tags doivent être simples et lisibles
- les tags servent au tri opérationnel, pas à remplacer les notes détaillées

## 6. Notes internes
Règles v1 :
- les notes internes ne sont jamais visibles côté client
- chaque note doit être liée à un auteur et un horodatage
- une note peut expliquer le contexte, le risque ou la prochaine action

## 7. Réponse manuelle
Quand un agent répond manuellement :
- la réponse doit être journalisée
- l’auteur doit être identifiable
- le lien avec la conversation doit être conservé

## 8. Audit minimum
Les actions suivantes doivent être auditables :
- assignation
- changement de tag
- ajout de note
- escalade
- résolution
- réponse manuelle