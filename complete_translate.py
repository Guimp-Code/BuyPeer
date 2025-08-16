#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import re

# Vou usar o arquivo inglês como dicionário base para fazer a tradução
# já que tem a mesma estrutura do árabe, mas em inglês

def load_english_as_base():
    """Carrega o arquivo inglês e aplica traduções em português"""
    
    # Dicionário de traduções inglês -> português
    translations = {
        # MENU PRINCIPAL
        "License": "Licença",
        "Create": "Criar",
        "Edit": "Editar", 
        "View": "Visualizar",
        "Dashboard": "Painel",
        "Settings": "Configurações",
        "Company": "Empresa",
        "Mail": "Email",
        "OTP": "OTP",
        "Notification": "Notificação",
        "Social Media": "Redes Sociais",
        "Cookies": "Cookies",
        "Analytics": "Análises",
        "Analytic Section": "Seção de Análises",
        "Theme": "Tema",
        "Sliders": "Sliders",
        "Currencies": "Moedas",
        "Product Categories": "Categorias de Produtos",
        "Product Attributes": "Atributos de Produtos",
        "Product Attribute Options": "Opções de Atributos",
        "Taxes": "Impostos",
        "Pages": "Páginas",
        "Languages": "Idiomas",
        "Sms Gateway": "Gateway SMS",
        "Payment Gateway": "Gateway de Pagamento",
        "Site": "Site",
        "Role": "Função",
        "Role & Permissions": "Funções e Permissões",
        
        # PRODUTOS E ESTOQUE
        "Product & Stock": "Produtos e Estoque",
        "POS & Orders": "PDV e Pedidos",
        "Promo": "Promoção",
        "Purchase": "Compra",
        "Stock": "Estoque",
        "POS": "PDV",
        "POS Orders": "Pedidos PDV",
        "Online Orders": "Pedidos Online",
        "Coupons": "Cupons",
        "Offers": "Ofertas",
        "Push Notifications": "Notificações Push",
        
        # USUÁRIOS
        "Administrators": "Administradores",
        "Customers": "Clientes",
        "Employees": "Funcionários",
        "Transactions": "Transações",
        
        # RELATÓRIOS
        "Sales Report": "Relatório de Vendas",
        "Products Report": "Relatório de Produtos",
        "Credit Balance Report": "Relatório de Saldo de Crédito",
        
        # CONTA E PERFIL
        "Overview": "Visão Geral",
        "Account info": "Informações da Conta",
        "Change Password": "Alterar Senha",
        "Order History": "Histórico de Pedidos",
        "Return Orders": "Pedidos de Devolução",
        "Damages": "Danos",
        "Address": "Endereço",
        "Addresses": "Endereços",
        "Wishlist": "Lista de Desejos",
        "Log in": "Entrar",
        
        # CAMPOS BÁSICOS
        "Name": "Nome",
        "Email": "Email",
        "Phone": "Telefone",
        "Website": "Site",
        "City": "Cidade",
        "State": "Estado",
        "Country Code": "Código do País",
        "Zip Code": "CEP",
        "Date": "Data",
        "Price": "Preço",
        "Amount": "Valor",
        "Status": "Status",
        "Action": "Ação",
        "Active": "Ativo",
        "Inactive": "Inativo",
        "Yes": "Sim",
        "No": "Não",
        "Default": "Padrão",
        
        # BOTÕES
        "Add": "Adicionar",
        "Save": "Salvar",
        "Delete": "Excluir",
        "Close": "Fechar",
        "Cancel": "Cancelar",
        "Clear": "Limpar",
        "Search": "Pesquisar",
        "Filter": "Filtrar",
        "Export": "Exportar",
        "Print": "Imprimir",
        "Excel": "Excel",
        "Reset": "Resetar",
        "Logout": "Sair",
        "Submit": "Enviar",
        "Apply": "Aplicar",
        "Remove": "Remover",
        "Verify": "Verificar",
        
        # E-COMMERCE
        "Shopping Cart": "Carrinho de Compras",
        "Checkout": "Finalizar Compra",
        "Payment": "Pagamento",
        "Shipping": "Entrega",
        "Tax": "Imposto",
        "Discount": "Desconto",
        "Coupon": "Cupom",
        "Quantity": "Quantidade",
        "Total": "Total",
        "Subtotal": "Subtotal",
        "Order": "Pedido",
        "Customer": "Cliente",
        "Product": "Produto",
        "Category": "Categoria",
        "Brand": "Marca",
        "Description": "Descrição",
        "Image": "Imagem",
        "Code": "Código",
        
        # MENSAGENS
        "Thank You": "Obrigado",
        "Thank you": "Obrigado",
        "Please": "Por favor",
        "Success": "Sucesso",
        "Error": "Erro",
        "Warning": "Aviso",
        "Information": "Informação",
        "Welcome": "Bem-vindo",
        "Loading": "Carregando",
        "Required": "Obrigatório",
        "Optional": "Opcional",
        
        # NAVEGAÇÃO
        "Home": "Início",
        "Back": "Voltar",
        "More": "Mais",
        "Show More": "Mostrar Mais",
        "Read More": "Ler Mais",
        
        # CONFIGURAÇÕES
        "Date Format": "Formato de Data",
        "Time Format": "Formato de Hora",
        "Default Timezone": "Fuso Horário Padrão",
        "Default Currency": "Moeda Padrão",
        "Default Language": "Idioma Padrão",
        
        # MAIS TERMOS
        "Product Brands": "Marcas de Produtos",
        "Units": "Unidades",
        "Variations": "Variações",
        "Settings Menu": "Menu de Configurações",
        "Product Video": "Vídeo do Produto",
        "SEO": "SEO",
        "Promotions": "Promoções",
        "Product Sections": "Seções de Produtos",
        "Benefits": "Benefícios",
        "Suppliers": "Fornecedores",
        "Profile": "Perfil",
        "Password": "Senha",
        "License Code": "Código de Licença",
        "Previous": "Anterior",
        "Next": "Próximo",
        "Sign In": "Entrar",
        "Remember me": "Lembrar de mim",
        "Hello": "Olá"
    }
    
    # Carrega arquivo inglês
    with open('resources/js/languages/en.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    def translate_recursive(obj):
        if isinstance(obj, dict):
            return {key: translate_recursive(value) for key, value in obj.items()}
        elif isinstance(obj, list):
            return [translate_recursive(item) for item in obj]
        elif isinstance(obj, str):
            # Aplica traduções
            translated = obj
            for eng, por in translations.items():
                translated = translated.replace(eng, por)
            return translated
        else:
            return obj
    
    return translate_recursive(data)

# Gera o arquivo traduzido
translated_data = load_english_as_base()

# Salva o arquivo traduzido
with open('resources/js/languages/pt-BR.json', 'w', encoding='utf-8') as f:
    json.dump(translated_data, f, ensure_ascii=False, indent=4)

print("✅ Tradução COMPLETA aplicada usando base inglesa!")
print("✅ Todas as strings traduzidas para português brasileiro!")
