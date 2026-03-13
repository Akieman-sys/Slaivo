# Product Additions — SLAIVO CARGO

## 1. Base de connaissance agence configurable
Chaque agence doit pouvoir configurer ses propres contenus métier dans le système, au lieu de dépendre uniquement d’un message WhatsApp Business long et générique.

Le système doit permettre à l’agence de définir au minimum :

- un message d’accueil / de présentation
- des informations tarifs
- des informations adresses d’entrepôt
- des informations départs
- des consignes d’expédition
- des informations de paiement
- des contacts utiles
- les informations à demander au client lorsqu’il veut utiliser le service

## 2. Découpage en blocs intelligents
Le système ne doit pas seulement envoyer un gros bloc de texte identique à chaque nouveau client.

Le contenu agence doit être découpé en blocs réutilisables, par exemple :
- welcome_message
- pricing_info
- warehouse_addresses
- departure_info
- shipping_instructions
- payment_info
- contact_info
- intake_requirements

Le moteur de réponse doit ensuite choisir les bons blocs selon le contexte de la conversation.

## 3. Valeur produit
Aujourd’hui, beaucoup d’agences utilisent un long message WhatsApp Business pour répondre aux nouveaux clients.

SLAIVO CARGO doit transformer cette pratique artisanale en système plus puissant :
- réponses plus intelligentes
- contenu configurable
- meilleure réutilisation
- meilleure expérience client
- moins de copier/coller manuel
- logique liée à l’intention client
- possibilité de reprise humaine propre

## 4. Intake configurable par agence
Quand un client veut utiliser le service, le système doit pouvoir lancer une collecte d’informations.

Chaque agence doit pouvoir paramétrer les informations qu’elle souhaite demander, par exemple :
- nom complet
- numéro WhatsApp
- destination
- type de marchandise
- poids approximatif
- type cargo
- note libre
- autre champ métier spécifique

Chaque champ doit pouvoir être :
- activé ou désactivé
- obligatoire ou optionnel

## 5. Distinction métier à respecter
Le système doit distinguer clairement :
- la conversation
- l’intake request / demande de service
- le shipment

Un client qui veut utiliser le service n’est pas automatiquement un shipment.

## 6. Conversion intake → shipment
Quand l’agence considère qu’un client ou une demande devient un vrai dossier opérationnel, elle doit pouvoir convertir cette demande en shipment.

Au moment de la conversion, l’agence complète les informations restantes nécessaires au shipment, par exemple :
- tracking_id
- statut initial
- origine
- destination finale
- cargo_type
- balance éventuelle
- notes internes

## 7. Principe produit
SLAIVO CARGO ne doit pas seulement être un système de réponses automatiques.

Il doit aussi devenir :
- une base de connaissance configurable par agence
- un système de conversation
- un intake assistant
- un outil de conversion de demande en shipment
- une inbox de reprise humaine