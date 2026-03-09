# Spec — WhatsApp Messages v1

## 1. Objectif
Ce document définit le format interne normalisé des messages WhatsApp entrants et sortants dans SLAIVO CARGO v1.

Le but est de ne pas propager directement partout le format brut du provider WhatsApp.

## 2. Principes
- un message entrant brut doit être normalisé
- les champs minimums doivent être stables
- le système doit pouvoir tracer chaque message
- les IDs externes et internes doivent être distingués

## 3. Message entrant normalisé

### 3.1 Nom du modèle
`InboundWhatsAppMessage`

### 3.2 Champs
- `internal_message_id` : string, identifiant interne unique
- `provider_message_id` : string, identifiant message côté provider WhatsApp
- `conversation_id` : string, identifiant logique de conversation
- `from_phone` : string, téléphone client normalisé
- `to_phone` : string, numéro WhatsApp de l’agence
- `text_body` : string, texte brut du message
- `message_type` : enum (`text`, `image`, `document`, `interactive`, `unknown`)
- `received_at` : datetime UTC
- `raw_payload_ref` : string, référence vers le payload brut stocké
- `dedupe_key` : string, clé anti-duplication
- `source_channel` : string, valeur fixe `whatsapp`
- `is_from_customer` : boolean

## 4. Règles v1 message entrant
- `internal_message_id` est généré par notre système
- `provider_message_id` doit être conservé s’il existe
- `from_phone` doit être normalisé
- `text_body` peut être vide pour les messages non textuels
- `raw_payload_ref` doit pointer vers une trace brute stockée
- `dedupe_key` doit permettre d’éviter un double traitement du même message

## 5. Message sortant normalisé

### 5.1 Nom du modèle
`OutboundWhatsAppMessage`

### 5.2 Champs
- `outbound_message_id` : string, identifiant interne unique
- `conversation_id` : string
- `to_phone` : string, téléphone destinataire
- `from_phone` : string, numéro de l’agence
- `reply_text` : string
- `message_type` : enum (`text`, `template`)
- `template_name` : string nullable
- `intent` : string nullable
- `trigger_type` : enum (`user_reply`, `relance_event`, `agent_reply`, `system_notice`)
- `sent_at` : datetime UTC nullable
- `status` : enum (`pending`, `sent`, `failed`)
- `cooldown_key` : string nullable
- `related_inbound_message_id` : string nullable
- `related_shipment_id` : string nullable

## 6. Règles v1 message sortant
- un message sortant doit toujours avoir un destinataire clair
- `reply_text` est obligatoire pour les messages texte simples
- `template_name` est obligatoire si `message_type=template`
- `trigger_type` doit être renseigné
- chaque envoi doit être traçable dans les logs

## 7. Champs minimums pour l’audit
Pour tout message entrant ou sortant, le système doit pouvoir retrouver :
- qui a envoyé
- à qui
- quand
- sous quel identifiant
- avec quel statut d’envoi ou de réception