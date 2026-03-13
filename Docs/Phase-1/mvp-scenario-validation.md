# MVP Scenario Validation — SLAIVO CARGO

## Objectif
Valider les scénarios v1 les plus importants de bout en bout.

---

## Scénario 1 — Tracking self-serve
### Entrée
Client envoie : `TRACK 92818`

### Attendu
- intent = `tracking_lookup`
- tracking_id extrait
- shipment trouvé
- reply tracking construite
- pas d’escalade

### Observé
- [ ] validé

### Notes
-

---

## Scénario 2 — Tarifs
### Entrée
Client envoie : `Tarifs Dubai-Kin ?`

### Attendu
- intent = `pricing_query`
- knowledge item pricing trouvé
- reply knowledge construite
- pas d’escalade

### Observé
- [ ] validé

### Notes
-

---

## Scénario 3 — Adresse entrepôt
### Entrée
Client envoie : `Adresse entrepôt ?`

### Attendu
- intent = `warehouse_address`
- knowledge item address trouvé
- reply knowledge construite
- pas d’escalade

### Observé
- [ ] validé

### Notes
-

---

## Scénario 4 — Relance ARRIVED_KIN
### Entrée
Déclenchement événementiel sur shipment `92818`

### Attendu
- event_notification créée
- message outbound créé
- second déclenchement bloqué par cooldown

### Observé
- [ ] validé

### Notes
-

---

## Scénario 5 — Cas sensible / escalade humaine
### Entrée
Client envoie un message difficile / non reconnu / sensible

### Attendu
- intent = unknown ou cas sensible
- should_escalate = true
- conversation visible dans inbox
- agent peut reprendre et créer une réponse humaine

### Observé
- [ ] validé

### Notes