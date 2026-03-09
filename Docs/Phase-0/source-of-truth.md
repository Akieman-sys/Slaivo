# Source of Truth v1 — SLAIVO CARGO

## 1. Décision ferme v1
La source de vérité officielle de SLAIVO CARGO v1 est :

**PostgreSQL**

En v1, PostgreSQL est hébergé et opéré via **Supabase**.

Cela signifie que :
- le modèle logique officiel est PostgreSQL
- Supabase est le provider managé de cette base
- Supabase n’est pas une source de vérité séparée
- toutes les données métier officielles utilisées par le système sont lues depuis cette base PostgreSQL

## 2. Pourquoi cette décision
Cette décision est prise car SLAIVO CARGO v1 n’est pas seulement une FAQ.

Le produit repose déjà sur :
- un modèle Shipment structuré
- des statuts contrôlés
- des relances automatiques
- une inbox opérateur
- de la traçabilité
- des règles de cohérence
- des recherches fiables par tracking_id

Ces besoins correspondent mieux à une base relationnelle stricte qu’à un tableur ou à une source semi-structurée.

## 3. Pourquoi Supabase en v1
Supabase est retenu comme manière d’opérer PostgreSQL en v1 pour les raisons suivantes :
- lancement plus rapide
- base PostgreSQL managée
- bonne expérience développeur
- import de données plus simple
- logs et outils utiles pour un MVP
- moins de charge infra au début

Le choix de Supabase permet donc d’avoir la rigueur de PostgreSQL sans ralentir exagérément l’exécution du MVP.

## 4. Ce que PostgreSQL protège
PostgreSQL protège en v1 :
- la cohérence des statuts
- l’unicité des identifiants
- la stabilité du modèle Shipment
- la qualité des données
- la capacité de requête
- la fiabilité des relances
- la base de l’inbox, des conversations et de l’audit
- l’évolution future du produit

## 5. Ce que Supabase est et n’est pas
Supabase est :
- le provider managé de notre PostgreSQL v1
- un accélérateur d’exécution
- une couche pratique pour opérer la base

Supabase n’est pas :
- une deuxième vérité
- un remplacement de notre logique métier
- une excuse pour mélanger les responsabilités du système

Le produit SLAIVO CARGO garde son propre design métier, ses propres contrats et ses propres règles.  
Supabase héberge et facilite l’opération de la base officielle.

## 6. Systèmes explicitement non retenus comme vérité principale
Les systèmes suivants ne sont pas la source de vérité officielle v1 :
- Google Sheets
- Airtable
- fichiers CSV
- exports Excel
- notes WhatsApp opérateurs

Ces sources peuvent servir d’entrée, d’import ou de support temporaire, mais pas de vérité principale du système.

## 7. Stratégie d’alimentation des données v1
En v1, les données peuvent entrer dans SLAIVO CARGO par :
- import CSV
- saisie via interface interne
- import contrôlé depuis un fichier préparé par l’agence
- plus tard, éventuellement, import depuis Google Sheets

Principe :
les données peuvent venir d’ailleurs, mais elles doivent être intégrées dans PostgreSQL avant d’être utilisées comme vérité officielle.

## 8. Règle d’or
Le système ne doit jamais répondre au client depuis une source externe non contrôlée si cette source n’a pas été intégrée dans la base officielle PostgreSQL.

Autrement dit :
- les données peuvent naître ailleurs
- la vérité officielle vit dans PostgreSQL
- les réponses produit doivent être basées sur PostgreSQL

## 9. Avantages produit et techniques
Ce choix permet :
- une meilleure fiabilité du tracking
- des relances plus sûres
- une meilleure base pour l’inbox
- une meilleure cohérence métier
- une meilleure évolutivité produit
- une réduction du chaos de données
- un lancement plus rapide grâce à Supabase

## 10. Coût accepté
Ce choix demande plus de rigueur initiale qu’un simple tableur.

Ce coût est accepté car :
- il réduit les migrations futures
- il réduit la dette produit
- il protège mieux la qualité métier
- il correspond mieux à la nature réelle de SLAIVO CARGO

## 11. Résumé
SLAIVO CARGO v1 choisit PostgreSQL comme cœur de vérité métier, opéré via Supabase.

Les fichiers, tableurs ou imports externes peuvent alimenter le système, mais la lecture officielle des données utilisées pour :
- le tracking
- les réponses client
- les relances
- l’inbox
- l’audit

se fait uniquement depuis PostgreSQL.