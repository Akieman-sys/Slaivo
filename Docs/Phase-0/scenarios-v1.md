# Scénarios v1 — SLAIVO CARGO

## 1. Objectif
Ce document décrit les scénarios concrets minimums de SLAIVO CARGO v1.

Le but est de vérifier que le produit, les données, les règles métier et les garde-fous sont cohérents à travers des cas réels simples.

---

## 2. Scénario 1 — Tracking self-serve

### Contexte
Le client veut connaître l’état de son colis.

### Déclencheur
Message client :
`TRACK 92818`

### Intention attendue
`tracking_lookup`

### Ce que fait le système
1. Reçoit le message via WhatsApp webhook
2. Normalise le message entrant
3. Détecte l’intention `tracking_lookup`
4. Extrait le tracking_id `92818`
5. Interroge la source de vérité PostgreSQL
6. Trouve le shipment correspondant
7. Construit une réponse client
8. Envoie la réponse
9. Journalise l’opération

### Données lues
- `tracking_id`
- `status`
- `eta`
- `balance` si politique agence autorisée
- `last_update_at`

### Réponse attendue
Exemple :
`Votre colis 92818 est actuellement ARRIVED_KIN. ETA : non applicable. Prochaine étape : récupération. Si vous voulez, je peux vous mettre en relation avec un agent.`

### Règles appliquées
- une seule réponse automatique pour ce message entrant
- pas d’invention de données manquantes
- réponse courte et compréhensible
- logs obligatoires

### Cas d’échec
Si le tracking est introuvable :
- ne pas inventer
- escalader avec reason code `tracking_not_found`
- envoyer un message de transition court

### Logs minimums
- message entrant
- intent détecté
- tracking_id extrait
- résultat lookup
- réponse envoyée ou escalade

---

## 3. Scénario 2 — Question tarif

### Contexte
Le client demande un tarif cargo.

### Déclencheur
Message client :
`Tarifs Dubai-Kin ?`

### Intention attendue
`pricing_query`

### Ce que fait le système
1. Reçoit le message
2. Normalise le contenu
3. Détecte `pricing_query`
4. Cherche l’information tarifaire dans le Knowledge Store
5. Vérifie que le tarif est suffisamment clair pour être communiqué
6. Construit une réponse courte
7. Envoie la réponse
8. Journalise l’opération

### Données lues
- destination
- route concernée
- grille tarifaire active
- conditions simples si disponibles

### Réponse attendue
Exemple :
`Les tarifs Dubai → Kinshasa dépendent du type d’envoi et du poids. Pour cette semaine, la grille disponible commence à partir de X. Si vous me donnez le poids ou le type de cargo, je peux affiner ou vous orienter vers un agent.`

### Règles appliquées
- ne jamais inventer un prix
- si ambigu, demander une précision ou escalader
- garder la réponse courte
- éviter un faux engagement commercial

### Cas d’échec
Si aucun tarif fiable n’est disponible :
- escalade `price_unknown`
- message client de transition

### Logs minimums
- message entrant
- intent détecté
- lookup knowledge
- réponse ou escalade

---

## 4. Scénario 3 — Adresse entrepôt

### Contexte
Le client veut l’adresse d’un entrepôt.

### Déclencheur
Message client :
`Adresse entrepôt Dubai ?`

### Intention attendue
`warehouse_address`

### Ce que fait le système
1. Reçoit et normalise le message
2. Détecte l’intention `warehouse_address`
3. Cherche l’adresse et les horaires dans le Knowledge Store
4. Construit une réponse claire
5. Ajoute un CTA vers agent si nécessaire
6. Envoie la réponse
7. Journalise l’opération

### Données lues
- adresse entrepôt
- horaires
- informations de contact disponibles

### Réponse attendue
Exemple :
`Voici l’adresse de l’entrepôt Dubai : [adresse]. Horaires : [horaires]. Si vous avez besoin d’une confirmation ou d’un contact direct, je peux vous orienter vers un agent.`

### Règles appliquées
- réponse claire et compacte
- pas d’information inventée
- CTA agent possible

### Cas d’échec
Si l’adresse n’est pas fiable ou manque :
- escalade
- message de transition

### Logs minimums
- message entrant
- intent détecté
- lookup knowledge
- réponse envoyée ou escalade

---

## 5. Scénario 4 — Relance automatique ARRIVED_KIN

### Contexte
Le statut d’un shipment passe à `ARRIVED_KIN`.

### Déclencheur
Événement métier :
`status_changed -> ARRIVED_KIN`

### Intention système attendue
Relance événementielle `ARRIVED_KIN`

### Ce que fait le système
1. Détecte le changement de statut
2. Vérifie que le shipment est valide
3. Vérifie la présence du téléphone client
4. Vérifie le cooldown `shipment_id + ARRIVED_KIN`
5. Construit le message de relance
6. Inclut la prochaine étape
7. Inclut la balance si politique agence autorisée et donnée fiable
8. Envoie la relance
9. Journalise l’opération

### Données lues
- `shipment_id`
- `client_phone`
- `status`
- `balance`
- `currency`
- règles de cooldown

### Réponse attendue
Exemple :
`Bonjour, votre colis 92818 est arrivé à Kinshasa. Prochaine étape : récupération selon les instructions de l’agence. Solde restant : X [currency] si applicable. Si besoin, un agent peut vous assister.`

### Règles appliquées
- pas plus d’une relance automatique ARRIVED_KIN dans 24h pour le même shipment
- pas d’invention de balance
- journalisation obligatoire
- possibilité de transfert à l’inbox si anomalie

### Cas d’échec
Pas de relance automatique si :
- numéro absent ou invalide
- cooldown actif
- shipment incohérent
- blocage manuel

### Logs minimums
- événement détecté
- contrôle cooldown
- message envoyé ou annulé
- raison d’annulation si applicable

---

## 6. Scénario 5 — Client énervé / escalade

### Contexte
Le client exprime colère, frustration ou accusation.

### Déclencheur
Message client :
`Ça fait trop longtemps, vous m’avez dit autre chose avant, votre service est nul.`

### Intention attendue
Signal relationnel sensible, avec escalade

### Ce que fait le système
1. Reçoit le message
2. Le normalise
3. Détecte un cas sensible / frustration client
4. N’essaie pas de résoudre automatiquement le fond du dossier
5. Crée une escalade vers l’inbox
6. Applique reason code `angry_customer`
7. Applique priorité `high`
8. Ajoute le tag `angry_customer`
9. Envoie un message de transition apaisant
10. Journalise l’escalade

### Réponse attendue
Exemple :
`Je comprends votre inquiétude. Je transmets votre demande à un agent pour vérification rapide.`

### Règles appliquées
- ne pas argumenter automatiquement
- ne pas contredire le client
- ne pas inventer une justification
- priorité haute
- arrêt du traitement automatique non nécessaire

### Cas d’échec
Aucun fallback automatique long.
Le bon comportement est l’escalade humaine.

### Logs minimums
- message entrant
- détection de sensibilité
- reason code
- priorité
- tag
- message de transition envoyé

---

## 7. Résumé
Les scénarios v1 minimums de SLAIVO CARGO couvrent :
- tracking self-serve
- FAQ tarif
- FAQ adresse
- relance événementielle
- escalade relationnelle

Ils servent de pont entre le cadrage Phase 0 et la construction du MVP Phase 1.