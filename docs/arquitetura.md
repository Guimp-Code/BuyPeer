# FILE: docs/arquitetura.md
## Padrão Arquitetural
- **MVC + Service Layer** (Controllers finos + Services).
- **API RESTful** separada do front SPA.
- **Repositories** e **DTOs** para isolar data layer.

## Estrutura de Pastas Recomendada
app/
├── Actions/
├── Http/
│ ├── Controllers/
│ └── Requests/
├── Models/
├── Services/
├── Repositories/
├── DTOs/
└── Policies/
resources/js/
├── components/
├── pages/
├── router/
└── store/

markdown
Copiar
Editar

## Convenções
- **PHP**: PSR-12.
- **Git**: `main`, `develop`, `feat/*`, `fix/*`.
- **Commits**: Conventional Commits.

## CI/CD
GitHub Actions  
1. `composer install`, `npm ci`, testes  
2. Build Vite  
3. Deploy via SSH-RSYNC + secrets
markdown
Copiar
Editar
