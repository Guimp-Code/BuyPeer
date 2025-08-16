 # FILE: docs/README-GERADO.md
## Toriba E-commerce – Planejamento

Documentação de planejamento localizada em **docs/**.

### Como Iniciar
```bash
git clone git@github.com:toriba/toriba-shop.git
cp docs/env.example .env
composer install && npm ci
php artisan key:generate
php artisan migrate --seed
npm run dev


Arquivos de Planejamento
docs/contexto.md

docs/arquitetura.md

docs/plan.md

docs/plan/tasks.md

docs/tests/estrategia.md

docs/prompts/regras_agentes.md

docs/env.example