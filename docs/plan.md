 # FILE: docs/plan.md
## Cronograma Macro
| Fase | Entregáveis | Dias | Aceitação |
|------|-------------|------|-----------|
| Kick-off | Repo e `.env` ok | 2 | `php artisan migrate --seed` ok |
| Segurança | Remover hard-codes | 5 | Scan sem credenciais expostas |
| Refatoração | Controllers → Services | 10 | CI sem lint errors |
| Performance | Índices + cache | 7 | P95 < 300 ms |
| Testes | Unit + e2e base | 8 | Cobertura > 50 % |
| UX/Branding | Layout Toriba | 6 | Cliente aprova |
| Documentação | OpenAPI + README | 3 | Swagger disponível |
| Go-Live | Deploy + monitor | 3 | Zero 5xx por 48 h |

Total: **44 dias úteis**

### Dependências
- Credenciais Stripe / Twilio
- Logo e paleta oficial

### Estratégia de Testes
> Consulte **docs/tests/estrategia.md**
