# Exit Criteria — Phase 0 — SLAIVO CARGO

## 1. Objectif
Ce document définit les conditions minimales à remplir pour considérer la Phase 0 comme terminée.

La Phase 0 n’est pas validée parce que l’équipe “se sent prête”.
Elle est validée lorsque les éléments critiques de cadrage, de design métier et de limites v1 sont explicitement décidés.

## 2. Critères de sortie obligatoires

### 2.1 ICP v1 défini
L’équipe doit pouvoir expliquer clairement :
- quel type d’agence est ciblé
- qui décide l’achat
- qui utilise le produit
- quelles douleurs principales sont visées

Référence :
- `docs/phase0/icp.md`

### 2.2 Wedge v1 défini
L’équipe doit pouvoir résumer en une phrase la porte d’entrée commerciale et produit de SLAIVO CARGO v1.

Référence :
- `docs/phase0/wedge.md`

### 2.3 Scope v1 figé
L’équipe doit avoir explicitement décidé :
- ce qui est dans la v1
- ce qui est hors scope v1
- pourquoi certains éléments sont refusés

Référence :
- `docs/phase0/scope.md`

### 2.4 SLO internes v1 définis
Les objectifs minimums de qualité, cohérence et sécurité doivent être écrits.

Référence :
- `docs/phase0/slo-v1.md`

### 2.5 Architecture 1 page disponible
L’équipe doit pouvoir raconter simplement le trajet d’un message entrant et d’un événement de relance.

Référence :
- `docs/phase0/architecture.md`

### 2.6 Contrats principaux définis
Les contrats minimums suivants doivent exister :
- messages WhatsApp
- modèle Shipment
- machine de statuts
- règles de relance
- actions inbox
- sécurité & logging

Références :
- `docs/spec/whatsapp-messages.md`
- `docs/spec/shipment-model.md`
- `docs/spec/status-machine.md`
- `docs/spec/rules-relance.md`
- `docs/spec/inbox-actions.md`
- `docs/spec/security-logging.md`

### 2.7 Modèle Shipment v1 figé
Le modèle Shipment v1 doit être suffisamment clair pour permettre le tracking, les relances et la consultation opérateur.

Référence :
- `docs/spec/shipment-model.md`

### 2.8 Source de vérité décidée
L’équipe doit avoir décidé où vit la vérité officielle du système et comment les données externes y entrent.

Référence :
- `docs/phase0/source-of-truth.md`

### 2.9 Politique anti-spam / cooldown définie
Le système doit avoir des garde-fous explicites contre répétitions, doublons, rafales et boucles.

Référence :
- `docs/phase0/anti-spam-cooldown.md`

### 2.10 Politique d’escalade définie
L’équipe doit avoir formalisé :
- quand le bot passe la main
- comment il le fait
- quelles raisons et priorités existent

Référence :
- `docs/phase0/escalation.md`

### 2.11 GAPS prioritaires identifiés
Les principaux trous de connaissance v1 doivent être écrits, avec risques, méthode de validation et livrables attendus.

Référence :
- `docs/phase0/gaps.md`

### 2.12 Scénarios v1 minimums disponibles
Au moins 3 scénarios v1 doivent exister et être racontables de bout en bout, par exemple :
- tracking lookup
- tarifs
- adresse entrepôt
- relance ARRIVED_KIN
- client énervé avec escalade

Ces scénarios peuvent être regroupés dans un document dédié ou dans une section Phase 0.

## 3. Test de validation final
La Phase 0 est considérée comme terminée si l’équipe peut répondre clairement, sans improvisation, aux questions suivantes :
- qui paie ?
- quelle est la wedge v1 ?
- que fait exactement la v1 ?
- que refuse la v1 ?
- à quoi ressemble un shipment ?
- quels statuts sont autorisés ?
- depuis où lit-on la vérité officielle ?
- comment un message traverse-t-il le système ?
- quand le bot se tait-il ?
- quels sont les grands GAPS restants ?

## 4. Résumé
La Phase 0 est finie quand le flou principal a été réduit à un niveau suffisamment bas pour lancer un MVP v1 sans confusion majeure sur :
- le client
- la promesse
- le périmètre
- le modèle métier
- l’architecture
- les garde-fous
- les inconnues restantes