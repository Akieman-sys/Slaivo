# Escalation Policy v1 — SLAIVO CARGO

## 1. Objectif
Ce document définit la politique d’escalade de SLAIVO CARGO v1.

Le but est de transférer proprement vers un humain les cas que le système ne doit pas traiter seul, afin de protéger la qualité de réponse, la cohérence métier et la relation client.

## 2. Principe
SLAIVO CARGO v1 doit :
- automatiser les cas simples et répétitifs
- escalader les cas ambigus, sensibles, incomplets ou risqués

L’escalade est une fonction normale du produit, pas un échec.

## 3. Cas d’escalade obligatoires v1
Le système doit escalader dans les cas suivants :

- intention inconnue ou non reconnue
- tracking introuvable
- prix inconnu ou ambigu
- cas douane ou opération spéciale nécessitant jugement humain
- données incohérentes ou contradictoires
- client frustré, agressif ou en situation sensible
- répétitions anormales ou comportement suspect
- demande explicite de parler à un humain

## 4. Cas non escaladés par défaut
Le système n’escalade pas par défaut si la réponse est simple, connue et fiable, par exemple :
- tracking trouvé
- tarif connu
- adresse connue
- départ connu
- relance standard normale
- FAQ métier contrôlée

## 5. Actions au moment de l’escalade
Quand un cas est escaladé, le système doit :
- arrêter le traitement automatique non nécessaire
- créer ou mettre à jour le signal correspondant dans l’inbox
- appliquer la priorité et le tag suggérés
- journaliser la raison
- envoyer si nécessaire un message de transition court au client

## 6. Message de transition client
Exemples de message de transition acceptables :
- "Je transmets votre demande à un agent pour vérification."
- "Je n’ai pas assez d’informations fiables pour vous répondre correctement. Un agent va prendre le relais."

Le message doit rester :
- court
- honnête
- rassurant
- non agressif

## 7. Format interne minimum d’une escalade
Une escalade v1 doit pouvoir contenir au minimum :
- `conversation_id`
- `customer_phone`
- `reason_code`
- `reason_detail`
- `related_shipment_id` nullable
- `triggered_at`
- `priority`
- `suggested_tag`

## 8. Reason codes v1
Les reason codes standards v1 sont :
- `unknown_intent`
- `tracking_not_found`
- `price_unknown`
- `customs_sensitive`
- `data_inconsistency`
- `angry_customer`
- `repetition_abuse`
- `human_requested`

## 9. Priorités v1
Les niveaux de priorité standards v1 sont :
- `low`
- `medium`
- `high`

## 10. Mapping v1 raison → tag → priorité
- `unknown_intent` → `needs_review` → `low`
- `tracking_not_found` → `tracking_issue` → `medium`
- `price_unknown` → `pricing_issue` → `medium`
- `customs_sensitive` → `customs` → `medium`
- `data_inconsistency` → `ops_issue` → `high`
- `angry_customer` → `angry_customer` → `high`
- `repetition_abuse` → `urgent` → `high`
- `human_requested` → `human_handoff` → `low`

## 11. Journalisation minimale
Toute escalade doit être traçable avec :
- horodatage
- raison
- priorité
- conversation concernée
- shipment lié si connu
- message de transition envoyé ou non

## 12. Résumé
SLAIVO CARGO v1 doit savoir reconnaître ses limites.
Quand la donnée manque, quand le risque métier est trop élevé ou quand la relation client devient sensible, le système doit passer la main proprement à un humain.