# Migration vers Karned Agency

Le dépôt historique `_sample` est renommé `arclith-reference` puis transféré
vers `karned-agency`. Le nouveau nom reflète son rôle réel : implémentation de
référence, laboratoire d'intégration et validation du framework avant release.

Le package Python `arclith_sample` est volontairement conservé afin de ne pas
mélanger ce changement d'identité avec une refonte de tous les imports. Les
liens, scripts CI et guides utilisent désormais `karned-agency/arclith`,
`karned-agency/arclith-reference` et `https://arclith.karned.bzh/`.
