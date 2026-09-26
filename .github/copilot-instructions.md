# arclith-reference — Copilot Instructions

Sandbox R&D uniquement. Sert à tester et faire evoluer `arclith` avant publication PyPI. **Ne jamais deployer.**

## Regles specifiques a ce repo

- R&D uniquement — zero code de production ici.
- Toujours utiliser `arclith` en mode editable depuis `../arclith` pour tester les changements locaux.
- Ne pas ajouter de logique metier persistante — c est un terrain d experimentation.
- Lire `../arclith/AGENTS.md` avant de modifier quoi que ce soit ici.
- **HTTP Status Codes** : toujours declarer explicitement `status_code` et `responses` dans FastAPI. Voir `docs/http-conventions.md`.
