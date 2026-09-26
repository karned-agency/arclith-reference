# Dev Mode Editable — arclith-reference

## Quand utiliser

Vous développez **simultanément** dans `arclith/` et `arclith-reference/` et
vous voulez tester les changements locaux avant leur publication sur PyPI.

## ⚠️ Règles absolues

- **Ne JAMAIS merger** vers `main` avec `[tool.uv.sources]` présent
- Ce mode est **uniquement pour les branches locales de développement**
- La CI bloque toute PR vers `main` contenant `[tool.uv.sources]` (voir [`.github/workflows/check-stable-template.yml`](../.github/workflows/check-stable-template.yml))

## Activation

### Étape 1 — Checkout une branche locale

```bash
cd /path/to/workspace/arclith-reference
git checkout -b dev/my-feature
```

### Étape 2 — Ajouter la source editable

Éditez `pyproject.toml` :

```toml
# ...existing dependencies...

[tool.uv.sources]
arclith = { path = "../arclith", editable = true }
```

### Étape 3 — Synchroniser les dépendances

```bash
uv sync
```

Arclith est maintenant résolu depuis le clone frère `../arclith` en mode
editable : tout changement du framework est immédiatement visible dans
`arclith-reference` sans réinstallation.

### Étape 4 — Tester vos changements

```bash
uv run python main.py         # MODE=api → REST :8000
MODE=mcp_http uv run python main.py  # MCP :8001
uv run pytest -v
```

## Désactivation — retour PyPI stable

### Avant de merge vers `main`

```bash
# Supprimer [tool.uv.sources] de pyproject.toml
git diff pyproject.toml  # vérifier qu'aucune trace de [tool.uv.sources]
git add pyproject.toml
git commit -m "chore: restore stable PyPI arclith"
git push origin dev/my-feature
```

La CI vérifiera automatiquement que `[tool.uv.sources]` est absent.

## Pattern alternatif — override temporaire sans commit

Si vous voulez tester localement **sans committer** la modification :

```bash
# Créer une copie locale
cp pyproject.toml pyproject.toml.bak

# Ajouter [tool.uv.sources] temporairement
# ... éditer pyproject.toml ...

uv sync
# ... tester ...

# Restaurer avant commit
mv pyproject.toml.bak pyproject.toml
git status  # pyproject.toml clean
```

Ou utiliser `git stash` :

```bash
# 1. Éditer pyproject.toml pour dev local
# 2. Tester avec uv sync / pytest
git add pyproject.toml
git stash
# 3. pyproject.toml restauré au dernier commit (PyPI stable)
git stash drop  # supprimer le stash une fois confirmé
```

## Cas d'usage typiques

### Tester une nouvelle primitive de framework

```bash
# Terminal 1 — éditer le framework
cd /path/to/workspace/arclith
# ... éditer arclith/domain/models/entity.py ...

# Terminal 2 — tester dans arclith-reference (avec editable = true)
cd /path/to/workspace/arclith-reference
uv run pytest tests/units/domain/test_models.py -v
# Les changements dans arclith/ sont immédiatement visibles
```

### Valider un adaptateur avant publication

```bash
# 1. Implémenter le nouvel adapter dans arclith/arclith/adapters/outbound/newdb/
# 2. Activer [tool.uv.sources] editable dans arclith-reference
# 3. Utiliser le nouvel adapter dans arclith-reference/config/adapters/outbound/newdb.yaml
# 4. Tester : uv run python main.py
# 5. Une fois validé, désactiver [tool.uv.sources] avant merge
```

## Vérification rapide

```bash
# Vérifier que vous êtes bien en mode PyPI stable (prêt pour main)
grep "tool.uv.sources" pyproject.toml
# → aucun résultat = ✅ stable

# Vérifier que vous êtes en mode editable local (dev seulement)
grep "tool.uv.sources" pyproject.toml
# → [tool.uv.sources] trouvé = ⚠️  ne pas merger vers main
```

## Référence CI

- **Workflow** : [`.github/workflows/check-stable-template.yml`](../.github/workflows/check-stable-template.yml)
- **Script patch CI** : [`.github/scripts/patch-framework-source.sh`](../.github/scripts/patch-framework-source.sh) — utilisé dans `pr-quality.yml` pour permettre les tests CI même avec PyPI stable (patché en Git source temporairement)

---

**Skill version** : 1.0.0  
**Dernière révision** : 2026-03-30
