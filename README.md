# ComputorV1 🧮

Un solver d'équations polynomiales du second degré en Python. Parce que résoudre des équations à la main, c'est so 2024.

## Qu'est-ce que ça fait ?

Ce programme résout des équations polynomiales comme :
- `5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0`
- `X^2 - 5*X + 6 = 0`
- `2*X^2 + 3*X = X^2 + 1`

Il affiche :
1. **L'équation réduite** sous forme `ax² + bx + c = 0`
2. **Le degré** du polynôme
3. **Les solutions** (réelles ou complexes)
---
## Installation

```bash
git clone https://github.com/tonpseudo/computorv1.git
cd computorv1
python3 computerv1.py "ton_equation_ici"
```
---
## Utilisation

### Équation du second degré classique
python3 computerv1.py "X^2 - 5*X + 6 = 0"

### Avec des décimaux
python3 computerv1.py "2.5*X^2 - 3.7*X + 1.2 = 0"

### Équation avec termes des deux côtés
python3 computerv1.py "5*X^2 + 3*X = 2*X^2 + 1"


---
## Exemples de sorties
Équation réduite: -9.3*X^2 + 4*X + 4 = 0
Degré du polynôme: 2

Le discriminant est positif, l'équation a deux solutions réelles:
X₁ = 0.846
X₂ = -0.417


