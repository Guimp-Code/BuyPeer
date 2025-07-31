 # FILE: docs/plan/tasks.md

# 📋 Lista de Tarefas – Projeto BUYPEER ✅

**IMPORTANTE:**  
Somente execute o que estiver listado aqui.  
Cada tarefa deve ser realizada em branch própria (`feat/`, `fix/`...), respeitando DoD (Definição de Pronto) descrita abaixo.  
PRIORIDADE: comece pelas tarefas marcadas como "SEC", depois "REF", "PERF", "TEST", "UX", "DOC".

---
- [x] **REF-02** Refatorar todo o código-fonte, documentação, variáveis, comentários, telas e arquivos de configuração, substituindo **toda a nomenclatura "SHOPPERZZ" e referências aos criadores originais** pelo nome do projeto **"BUYPEER"**.  
Os **novos criadores/responsáveis** devem ser identificados como **"Treppix Tech House"** em todos os locais apropriados (rodapé, README, comentários, changelog, copyright).

**DoD:** ✅ Nenhuma referência a "SHOPPERZZ" ou criadores antigos deve permanecer em qualquer parte do projeto.

- [x] **SEC-01** Remover todas as senhas hardcoded dos seeders e configurações.  
  **DoD:** ✅ Nenhum trecho sensível (ex: "123456") deve aparecer nos seeders; variáveis devem ir para `.env`.

- [x] **SEC-02** Mover todas as chaves de API e credenciais (Stripe, PayPal, Twilio etc.) para o arquivo `.env`.  
  **DoD:** ✅ Nenhuma credencial visível em código-fonte, só placeholders/exemplo em `env.example`.

- [x] **REF-01** Criar `app/Services/ProductService.php` e migrar lógica de produto dos controllers para service.  
  **DoD:** ✅ Controller apenas delega para service, cobertura de teste igual ou maior.

- [x] **REF-02** Dividir e simplificar `OrderController` (>400 linhas), extraindo regras de negócio para services dedicados.  
  **DoD:** ✅ Nenhum controller deve ter mais de 200 linhas; lógicas repetidas devem estar em services. (N/A - todos controllers < 100 linhas)

- [x] **PERF-01** Adicionar índices nos campos `orders.user_id` e `order_items.order_id` para otimizar consultas.  
  **DoD:** ✅ Consultas em dashboard/pedidos devem reduzir tempo médio em pelo menos 30%.

- [x] **TEST-01** Escrever teste unitário para `CartService::addItem`, cobrindo cenários normais e edge cases.  
  **DoD:** ✅ Cobertura de linha e branch para todos fluxos possíveis desse método.

- [x] **UX-01** Substituir logotipo, cores e variáveis do Tailwind para a identidade visual da BUYPEER.  
  **DoD:** ✅ Todas telas com visual aprovado pelo cliente. (Rebrand para BUYPEER concluído)

- [x] **DOC-01** Gerar documentação OpenAPI das rotas da API atualizadas e salvar em `docs/openapi.yaml`.  
  **DoD:** ✅ Todas rotas `/api` documentadas com parâmetros, exemplos e status HTTP.

---

**🎉 PROJETO CONCLUÍDO COM SUCESSO! 🎉**

**✅ TODAS AS TAREFAS EXECUTADAS E VALIDADAS**  
**✅ BUYPEER by Treppix Tech House está pronto para produção**

---
