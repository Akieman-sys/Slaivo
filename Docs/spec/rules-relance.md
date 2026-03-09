# Spec — Rules Relance v1

## 1. Objectif
Ce document définit les règles de relance automatique pour SLAIVO CARGO v1.

Le but est d’envoyer les bons messages au bon moment, sans spam et sans contradictions.

## 2. Événements supportés v1
Les relances automatiques v1 sont déclenchées au minimum par :
- `ARRIVED_KIN`
- `READY_FOR_PICKUP`

## 3. Pré-conditions générales
Une relance automatique ne doit être envoyée que si :
- le shipment existe
- le téléphone client est disponible
- le statut courant correspond bien à l’événement
- aucun blocage manuel n’empêche l’envoi
- le cooldown autorise l’envoi

## 4. Relance ARRIVED_KIN
### Déclencheur
Quand un shipment passe à `ARRIVED_KIN`

### Objectif
Informer le client que son colis est arrivé à Kinshasa et lui indiquer la prochaine étape.

### Contenu attendu
Le message peut inclure :
- confirmation d’arrivée
- consigne de prochaine étape
- balance si applicable selon politique agence
- proposition de contact agent

### Cooldown recommandé
- pas plus d’une relance ARRIVED_KIN automatique dans une fenêtre de 24h pour le même shipment

## 5. Relance READY_FOR_PICKUP
### Déclencheur
Quand un shipment passe à `READY_FOR_PICKUP`

### Objectif
Inviter le client à venir récupérer son colis.

### Contenu attendu
Le message peut inclure :
- confirmation de disponibilité
- horaires ou lieu de retrait
- rappel du solde si applicable
- CTA vers agent

### Cooldown recommandé
- une relance initiale à l’entrée du statut
- puis au maximum une relance de rappel dans les 24h si aucune action n’est constatée

## 6. Cas de non-envoi
Aucune relance ne doit être envoyée si :
- le numéro client est absent ou invalide
- le shipment est dans un état incohérent
- un agent a posé un blocage manuel
- le cooldown interdit l’envoi
- le dossier est marqué sensible

## 7. Journalisation obligatoire
Chaque relance doit être tracée avec :
- shipment concerné
- type de relance
- horodatage
- statut d’envoi
- template utilisé
- raison du non-envoi si relance annulée

## 8. Principe v1
Les relances v1 doivent être :
- utiles
- limitées
- traçables
- compatibles avec une reprise humaine