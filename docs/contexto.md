# FILE: docs/contexto.md
## Visão Geral
O projeto **Toriba** consiste em customizar e aprimorar um e-commerce existente (Laravel 10 + Vue 3) para a ótica **Toriba Sunglass**.

### Problema
A Toriba precisa de uma plataforma robusta, segura e moderna para vender óculos on-line, com integrações de pagamento, logística e marketing.

### Objetivos
1. Rebatizar toda a base de código para “Toriba”.
2. Corrigir vulnerabilidades críticas e remover hard-codes.
3. Otimizar performance (queries, cache, assets).
4. Entregar todas as funcionalidades existentes 100 % operacionais.
5. Adicionar painel administrativo refinado e UX atualizada.
6. Documentar a API e criar base de testes automatizados.

### Personas / Histórias de Usuário
- **Comprador (Idoso)** – precisa de IA que o oriente a escolher lentes.
- **Gerente da Loja** – controla catálogo, estoque e pedidos.
- **Admin Toriba** – gerencia cupons, relatórios e integrações.

### Restrições
- Prazo máximo: **60 dias** para go-live.
- VPS atual (Ubuntu 22.04, 4 vCPU / 8 GB RAM).
- Manter stack PHP 8.1, MySQL 8, Vue 3.

### Requisitos Não-Funcionais
- **Segurança** OWASP Top 10 (A-rated).
- **Performance**: TTFB < 200 ms (páginas críticas).
- **Escalabilidade** futura via Docker/K8s.

### Referências
- Relatório técnico 2025-07-28.
- Clean Code, DDD, GoF Patterns.
