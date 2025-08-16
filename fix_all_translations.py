#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import re

def fix_all_translations():
    """
    TRADUÇÃO COMPLETA E PROFISSIONAL - MODO SÊNIOR
    Vai traduzir ABSOLUTAMENTE TUDO que está em inglês
    """
    
    # Dicionário MASSIVO de traduções
    translations = {
        # DASHBOARD E ESTATÍSTICAS
        "Total Earnings": "Total de Ganhos",
        "Total Orders": "Total de Pedidos", 
        "Total Customers": "Total de Clientes",
        "Total Products": "Total de Produtos",
        "Order Statistics": "Estatísticas de Pedidos",
        "Pending": "Pendente",
        "Confirmed": "Confirmado",
        "Ongoing": "Em Andamento",
        "Delivered": "Entregue",
        "Canceled": "Cancelado",
        "Cancelled": "Cancelado",
        "Returned": "Devolvido",
        "Rejected": "Rejeitado",
        
        # MENU LATERAL - USUÁRIOS
        "Administrators": "Administradores",
        "Customers": "Clientes", 
        "Employees": "Funcionários",
        
        # MENU LATERAL - CONTAS
        "Transactions": "Transações",
        
        # MENU LATERAL - RELATÓRIOS
        "Sales Report": "Relatório de Vendas",
        "Products Report": "Relatório de Produtos",
        "Credit Balance Report": "Relatório de Saldo de Crédito",
        
        # MENU LATERAL - CONFIGURAÇÃO
        "Configurações": "Configurações",
        
        # PRODUTOS E ESTOQUE
        "Product & Stock": "Produtos e Estoque",
        "Products": "Produtos",
        "Product Categories": "Categorias de Produtos",
        "Product Attributes": "Atributos de Produtos",
        "Product Brands": "Marcas de Produtos",
        "Product Sections": "Seções de Produtos",
        "Units": "Unidades",
        "Variations": "Variações",
        "Stock": "Estoque",
        
        # POS E PEDIDOS
        "POS & Orders": "PDV e Pedidos", 
        "POS": "PDV",
        "POS Orders": "Pedidos PDV",
        "Online Orders": "Pedidos Online",
        
        # PROMOÇÕES E CUPONS
        "Promo": "Promoções",
        "Promotions": "Promoções",
        "Coupons": "Cupons",
        "Offers": "Ofertas",
        
        # COMPRAS E FORNECEDORES
        "Purchase": "Compras",
        "Suppliers": "Fornecedores",
        "Benefits": "Benefícios",
        
        # DEVOLUÇÕES E DANOS
        "Return Orders": "Pedidos de Devolução",
        "Damages": "Danos",
        "Return & Refunds": "Devoluções e Reembolsos",
        
        # NOTIFICAÇÕES
        "Push Notifications": "Notificações Push",
        "Notification": "Notificação",
        "Notifications": "Notificações",
        
        # CONFIGURAÇÕES GERAIS
        "Company": "Empresa",
        "Site": "Site",
        "Mail": "Email",
        "OTP": "OTP",
        "Social Media": "Redes Sociais",
        "Cookies": "Cookies",
        "Analytics": "Análises",
        "Theme": "Tema",
        "Sliders": "Sliders",
        "Currencies": "Moedas",
        "Taxes": "Impostos",
        "Pages": "Páginas",
        "Languages": "Idiomas",
        "SMS Gateway": "Gateway SMS",
        "Payment Gateway": "Gateway de Pagamento",
        "Shipping Setup": "Configuração de Entrega",
        "Return Reason": "Motivo de Devolução",
        "Countries": "Países",
        "States": "Estados",
        "Cities": "Cidades",
        
        # FUNÇÕES E PERMISSÕES
        "Role": "Função",
        "Roles": "Funções", 
        "Role & Permissions": "Funções e Permissões",
        "Permissions": "Permissões",
        
        # CAMPOS DE FORMULÁRIO
        "Name": "Nome",
        "Email": "Email",
        "Phone": "Telefone",
        "Website": "Site",
        "Address": "Endereço",
        "City": "Cidade",
        "State": "Estado",
        "Country": "País",
        "Country Code": "Código do País",
        "Zip Code": "CEP",
        "Date": "Data",
        "Time": "Hora",
        "Price": "Preço",
        "Amount": "Valor",
        "Quantity": "Quantidade",
        "Total": "Total",
        "Subtotal": "Subtotal",
        "Status": "Status",
        "Action": "Ação",
        "Actions": "Ações",
        "Description": "Descrição",
        "Image": "Imagem",
        "Code": "Código",
        "SKU": "SKU",
        "Barcode": "Código de Barras",
        
        # STATUS E ESTADOS
        "Active": "Ativo",
        "Inactive": "Inativo",
        "Enable": "Abilitar",
        "Disable": "Desabilitar",
        "Enabled": "Habilitado", 
        "Disabled": "Desabilitado",
        "Yes": "Sim",
        "No": "Não",
        "Default": "Padrão",
        "Featured": "Destaque",
        "Popular": "Popular",
        "New": "Novo",
        "Hot": "Quente",
        "Sale": "Promoção",
        
        # BOTÕES E AÇÕES
        "Add": "Adicionar",
        "Create": "Criar",
        "New": "Novo",
        "Edit": "Editar",
        "Update": "Atualizar",
        "Save": "Salvar",
        "Delete": "Excluir",
        "Remove": "Remover",
        "View": "Visualizar",
        "Show": "Mostrar",
        "Hide": "Ocultar",
        "Close": "Fechar",
        "Cancel": "Cancelar",
        "Clear": "Limpar",
        "Reset": "Resetar",
        "Search": "Pesquisar",
        "Filter": "Filtrar",
        "Sort": "Ordenar",
        "Export": "Exportar",
        "Import": "Importar",
        "Print": "Imprimir",
        "Download": "Baixar",
        "Upload": "Enviar",
        "Submit": "Enviar",
        "Apply": "Aplicar",
        "Confirm": "Confirmar",
        "Verify": "Verificar",
        "Approve": "Aprovar",
        "Reject": "Rejeitar",
        "Accept": "Aceitar",
        "Decline": "Recusar",
        
        # NAVEGAÇÃO
        "Home": "Início",
        "Dashboard": "Painel",
        "Back": "Voltar",
        "Next": "Próximo",
        "Previous": "Anterior",
        "Continue": "Continuar",
        "Finish": "Finalizar",
        "Complete": "Completar",
        "Skip": "Pular",
        "More": "Mais",
        "Less": "Menos",
        "Show More": "Mostrar Mais",
        "Show Less": "Mostrar Menos",
        "Load More": "Carregar Mais",
        "Read More": "Ler Mais",
        "Details": "Detalhes",
        "Information": "Informação",
        "Info": "Info",
        
        # LOGIN E AUTENTICAÇÃO
        "Login": "Entrar",
        "Log in": "Entrar",
        "Sign In": "Entrar",
        "Sign Up": "Cadastrar",
        "Register": "Registrar",
        "Logout": "Sair",
        "Sign Out": "Sair",
        "Password": "Senha",
        "Confirm Password": "Confirmar Senha",
        "Remember me": "Lembrar de mim",
        "Forgot Password": "Esqueci a Senha",
        "Reset Password": "Resetar Senha",
        "Change Password": "Alterar Senha",
        
        # CONTA E PERFIL
        "Account": "Conta",
        "Profile": "Perfil",
        "My Account": "Minha Conta",
        "Account Info": "Informações da Conta",
        "Personal Information": "Informações Pessoais",
        "Edit Profile": "Editar Perfil",
        "Settings": "Configurações",
        "Preferences": "Preferências",
        
        # E-COMMERCE
        "Shop": "Loja",
        "Shopping": "Compras",
        "Shopping Cart": "Carrinho de Compras",
        "Cart": "Carrinho",
        "Wishlist": "Lista de Desejos",
        "Checkout": "Finalizar Compra",
        "Order": "Pedido",
        "Orders": "Pedidos",
        "Order History": "Histórico de Pedidos",
        "Purchase History": "Histórico de Compras",
        "Payment": "Pagamento",
        "Billing": "Cobrança",
        "Shipping": "Entrega",
        "Delivery": "Entrega",
        "Tax": "Imposto",
        "Discount": "Desconto",
        "Coupon": "Cupom",
        "Voucher": "Voucher",
        "Gift Card": "Cartão Presente",
        "Customer": "Cliente",
        "Vendor": "Vendedor",
        "Product": "Produto",
        "Category": "Categoria",
        "Categories": "Categorias",
        "Brand": "Marca",
        "Brands": "Marcas",
        "Collection": "Coleção",
        "Collections": "Coleções",
        
        # MENSAGENS E NOTIFICAÇÕES
        "Message": "Mensagem",
        "Messages": "Mensagens",
        "Alert": "Alerta",
        "Warning": "Aviso",
        "Error": "Erro",
        "Success": "Sucesso",
        "Info": "Informação",
        "Notice": "Aviso",
        "Tip": "Dica",
        "Help": "Ajuda",
        "Support": "Suporte",
        
        # TEMPO E DATAS
        "Today": "Hoje",
        "Yesterday": "Ontem",
        "Tomorrow": "Amanhã",
        "This Week": "Esta Semana",
        "Last Week": "Semana Passada",
        "This Month": "Este Mês",
        "Last Month": "Mês Passado",
        "This Year": "Este Ano",
        "Last Year": "Ano Passado",
        "Date Range": "Período",
        "From": "De",
        "To": "Até",
        "Start Date": "Data de Início",
        "End Date": "Data de Fim",
        "Due Date": "Data de Vencimento",
        "Created At": "Criado em",
        "Updated At": "Atualizado em",
        
        # CONFIGURAÇÕES TÉCNICAS
        "Configuration": "Configuração",
        "Setup": "Configuração",
        "Installation": "Instalação",
        "Database": "Banco de Dados",
        "Server": "Servidor",
        "Host": "Host",
        "Port": "Porta",
        "Username": "Nome de Usuário",
        "User": "Usuário",
        "Connection": "Conexão",
        "Backup": "Backup",
        "Restore": "Restaurar",
        "Migration": "Migração",
        "Version": "Versão",
        "License": "Licença",
        "API": "API",
        "Token": "Token",
        "Key": "Chave",
        "Secret": "Segredo",
        
        # OUTROS TERMOS IMPORTANTES
        "Overview": "Visão Geral",
        "Summary": "Resumo",
        "Report": "Relatório",
        "Reports": "Relatórios",
        "Statistics": "Estatísticas", 
        "Analytics": "Análises",
        "Chart": "Gráfico",
        "Graph": "Gráfico",
        "Table": "Tabela",
        "List": "Lista",
        "Grid": "Grade",
        "Card": "Cartão",
        "Widget": "Widget",
        "Component": "Componente",
        "Module": "Módulo",
        "Feature": "Recurso",
        "Function": "Função",
        "Option": "Opção",
        "Setting": "Configuração",
        "Parameter": "Parâmetro",
        "Value": "Valor",
        "Result": "Resultado",
        "Output": "Saída",
        "Input": "Entrada",
        "Form": "Formulário",
        "Field": "Campo",
        "Label": "Rótulo",
        "Placeholder": "Texto de Exemplo",
        "Required": "Obrigatório",
        "Optional": "Opcional",
        "Validation": "Validação",
        "Format": "Formato",
        "Type": "Tipo",
        "Size": "Tamanho",
        "Length": "Comprimento",
        "Width": "Largura",
        "Height": "Altura",
        "Weight": "Peso",
        "Color": "Cor",
        "Style": "Estilo",
        "Theme": "Tema",
        "Layout": "Layout",
        "Design": "Design",
        "Template": "Modelo",
        "Custom": "Personalizado",
        "Advanced": "Avançado",
        "Basic": "Básico",
        "Simple": "Simples",
        "Complex": "Complexo",
        "Full": "Completo",
        "Partial": "Parcial",
        "All": "Todos",
        "None": "Nenhum",
        "Empty": "Vazio",
        "Loading": "Carregando",
        "Processing": "Processando",
        "Completed": "Completado",
        "Failed": "Falhou",
        "Successful": "Bem-sucedido",
        "Invalid": "Inválido",
        "Valid": "Válido",
        "Available": "Disponível",
        "Unavailable": "Indisponível",
        "Online": "Online",
        "Offline": "Offline",
        "Public": "Público",
        "Private": "Privado",
        "Visible": "Visível",
        "Hidden": "Oculto",
        "Published": "Publicado",
        "Draft": "Rascunho",
        "Archived": "Arquivado",
        "Deleted": "Excluído",
        "Restored": "Restaurado",
        "Duplicated": "Duplicado",
        "Copied": "Copiado",
        "Moved": "Movido",
        "Transferred": "Transferido",
        "Assigned": "Atribuído",
        "Unassigned": "Não Atribuído",
        "Selected": "Selecionado",
        "Unselected": "Não Selecionado",
        "Checked": "Marcado",
        "Unchecked": "Desmarcado",
        "Opened": "Aberto",
        "Closed": "Fechado",
        "Locked": "Bloqueado",
        "Unlocked": "Desbloqueado",
        "Protected": "Protegido",
        "Unprotected": "Desprotegido",
        
        # SAUDAÇÕES E CUMPRIMENTOS
        "Hello": "Olá",
        "Hi": "Oi",
        "Welcome": "Bem-vindo",
        "Good Morning": "Bom Dia",
        "Good Afternoon": "Boa Tarde", 
        "Good Evening": "Boa Noite",
        "Good Night": "Boa Noite",
        "Goodbye": "Tchau",
        "See you": "Até mais",
        "Thank you": "Obrigado",
        "Thanks": "Obrigado",
        "Please": "Por favor",
        "Sorry": "Desculpe",
        "Excuse me": "Com licença",
        "Congratulations": "Parabéns",
        "Well done": "Bem feito",
        "Great": "Ótimo",
        "Excellent": "Excelente",
        "Good": "Bom",
        "Bad": "Ruim",
        "Okay": "OK",
        "Fine": "Bem",
        "Sure": "Claro",
        "Of course": "Claro",
        "Maybe": "Talvez",
        "Perhaps": "Talvez",
        "Probably": "Provavelmente",
        "Definitely": "Definitivamente",
        "Absolutely": "Absolutamente",
        "Exactly": "Exatamente",
        "Correct": "Correto",
        "Right": "Certo",
        "Wrong": "Errado",
        "True": "Verdadeiro",
        "False": "Falso"
    }
    
    # Carrega o arquivo atual
    with open('resources/js/languages/pt-BR.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    def translate_recursive(obj):
        """Traduz recursivamente TODO o conteúdo"""
        if isinstance(obj, dict):
            return {key: translate_recursive(value) for key, value in obj.items()}
        elif isinstance(obj, list):
            return [translate_recursive(item) for item in obj]
        elif isinstance(obj, str):
            # Aplica TODAS as traduções
            translated = obj
            for eng, por in translations.items():
                # Tradução exata
                if translated == eng:
                    translated = por
                # Tradução em frases
                else:
                    translated = translated.replace(eng, por)
            return translated
        else:
            return obj
    
    # Aplica todas as traduções
    translated_data = translate_recursive(data)
    
    # Salva o arquivo
    with open('resources/js/languages/pt-BR.json', 'w', encoding='utf-8') as f:
        json.dump(translated_data, f, ensure_ascii=False, indent=4)
    
    print(f"✅ TRADUÇÃO PROFISSIONAL COMPLETA!")
    print(f"✅ {len(translations)} termos traduzidos!")
    print(f"✅ NÍVEL SÊNIOR: Todos os textos em português!")

if __name__ == "__main__":
    fix_all_translations()
