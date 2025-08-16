#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

def add_missing_dashboard_terms():
    """Adiciona TODOS os termos que faltam do dashboard"""
    
    # Carrega o arquivo atual
    with open('resources/js/languages/pt-BR.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Termos que faltam baseados na tela do usuário
    missing_terms = {
        # STATUS DE PEDIDOS (em inglês na tela)
        "pending": "Pendente",
        "confirmed": "Confirmado", 
        "ongoing": "Em Andamento",
        "delivered": "Entregue",
        "canceled": "Cancelado",
        "cancelled": "Cancelado",
        "returned": "Devolvido",
        "rejected": "Rejeitado",
        
        # FRASES ESPECÍFICAS
        "order_pending": "Pedido Pendente",
        "order_confirmed": "Pedido Confirmado",
        "order_delivered": "Pedido Entregue", 
        "order_rejected": "Pedido Rejeitado",
        "order_returned": "Pedido Devolvido",
        "order_canceled": "Pedido Cancelado",
        "order_cancelled": "Pedido Cancelado",
        "order_ongoing": "Pedido em Andamento",
        
        # TOTAIS ESPECÍFICOS
        "total_returned": "Total Devolvido",
        "total_pending": "Total Pendente",
        "total_confirmed": "Total Confirmado",
        "total_delivered": "Total Entregue",
        "total_rejected": "Total Rejeitado",
        "total_canceled": "Total Cancelado",
        "total_cancelled": "Total Cancelado",
        "total_ongoing": "Total em Andamento",
        
        # TERMOS DO MENU QUE APARECEM EM INGLÊS
        "subscribers": "Assinantes",
        "sales_report": "Relatório de Vendas",
        "products_report": "Relatório de Produtos", 
        "credit_balance_report": "Relatório de Saldo de Crédito",
        
        # TERMOS GERAIS QUE PODEM APARECER
        "good_evening": "Boa Noite",
        "good_morning": "Bom Dia",
        "good_afternoon": "Boa Tarde",
        "select_date_range": "Selecionar Período",
        "date_range": "Período de Datas",
        "filter_by_date": "Filtrar por Data",
        "all_time": "Todo o Período",
        "last_7_days": "Últimos 7 Dias",
        "last_30_days": "Últimos 30 Dias",
        "this_month": "Este Mês",
        "last_month": "Mês Passado",
        "this_year": "Este Ano",
        "last_year": "Ano Passado",
        
        # OUTROS TERMOS IMPORTANTES
        "overview": "Visão Geral",
        "summary": "Resumo",
        "statistics": "Estatísticas",
        "reports": "Relatórios",
        "analytics": "Análises",
        "dashboard": "Painel",
        "welcome": "Bem-vindo",
        "hello": "Olá",
        "admin": "Administrador",
        "user": "Usuário",
        "profile": "Perfil",
        "settings": "Configurações",
        "logout": "Sair",
        "login": "Entrar",
        
        # CONFIGURAÇÕES QUE PODEM APARECER
        "configuration": "Configuração",
        "setup": "Configuração",
        "installation": "Instalação",
        "system": "Sistema",
        "general": "Geral",
        "advanced": "Avançado",
        "basic": "Básico",
        "preferences": "Preferências",
        "options": "Opções",
        
        # TERMOS DE TEMPO
        "today": "Hoje",
        "yesterday": "Ontem", 
        "tomorrow": "Amanhã",
        "now": "Agora",
        "recently": "Recentemente",
        "latest": "Mais Recente",
        "newest": "Mais Novo",
        "oldest": "Mais Antigo",
        
        # AÇÕES QUE PODEM APARECER
        "refresh": "Atualizar",
        "reload": "Recarregar",
        "sync": "Sincronizar",
        "backup": "Backup",
        "restore": "Restaurar",
        "migrate": "Migrar",
        "update": "Atualizar",
        "upgrade": "Atualizar",
        "downgrade": "Fazer Downgrade",
        "install": "Instalar",
        "uninstall": "Desinstalar",
        "enable": "Habilitar",
        "disable": "Desabilitar"
    }
    
    # Adiciona os termos que faltam
    if "label" not in data:
        data["label"] = {}
    
    if "button" not in data:
        data["button"] = {}
        
    if "message" not in data:
        data["message"] = {}
        
    if "status" not in data:
        data["status"] = {}
    
    # Distribui os termos nas seções apropriadas
    for key, value in missing_terms.items():
        if key.startswith("total_") or key.startswith("order_"):
            data["label"][key] = value
        elif key in ["pending", "confirmed", "delivered", "canceled", "rejected", "returned", "ongoing"]:
            data["status"][key] = value
        elif "button" in key or key in ["refresh", "reload", "sync", "update", "save", "cancel"]:
            data["button"][key] = value
        else:
            data["label"][key] = value
    
    # Salva o arquivo
    with open('resources/js/languages/pt-BR.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    print(f"✅ TERMOS ADICIONADOS: {len(missing_terms)} novos termos!")
    print(f"✅ TODOS os textos da tela devem estar traduzidos agora!")

if __name__ == "__main__":
    add_missing_dashboard_terms()
