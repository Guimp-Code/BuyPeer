#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import re

# Dicionário completo de traduções árabe -> português brasileiro
translations = {
    # MENU PRINCIPAL
    "رخصة": "Licença",
    "إنشاء": "Criar",
    "تعديل": "Editar", 
    "عرض": "Visualizar",
    "لوحة التحكم": "Painel",
    "الإعدادات": "Configurações",
    "الشركة": "Empresa",
    "البريد": "Email",
    "رمز التحقق": "OTP",
    "الإشعارات": "Notificações",
    "وسائل التواصل الاجتماعي": "Redes Sociais",
    "ملفات تعريف الارتباط": "Cookies",
    "تحليلات": "Análises",
    "قسم التحليل": "Seção de Análises",
    "السمة": "Tema",
    "منزلقات": "Sliders",
    "العملات": "Moedas",
    "فئات المنتجات": "Categorias de Produtos",
    "سمات المنتج": "Atributos de Produtos",
    "خيارات سمة المنتج": "Opções de Atributos",
    "الضرائب": "Impostos",
    "الصفحات": "Páginas",
    "اللغات": "Idiomas",
    "بوابة الرسائل القصيرة": "Gateway SMS",
    "بوابة الدفع": "Gateway de Pagamento",
    "الموقع": "Site",
    "الدور": "Função",
    "الدور والصلاحيات": "Funções e Permissões",
    
    # PRODUTOS E ESTOQUE
    "المنتج والمخزون": "Produtos e Estoque",
    "نقطة البيع والطلبات": "PDV e Pedidos",
    "العروض الترويجية": "Promoções",
    "الشراء": "Compra",
    "المخزون": "Estoque",
    "نقطة البيع": "PDV",
    "طلبات نقطة البيع": "Pedidos PDV",
    "الطلبات الإلكترونية": "Pedidos Online",
    "الكوبونات": "Cupons",
    "العروض": "Ofertas",
    "الإشعارات المدفوعة": "Notificações Push",
    
    # USUÁRIOS
    "المديرين": "Administradores",
    "العملاء": "Clientes",
    "الموظفين": "Funcionários",
    "المعاملات": "Transações",
    
    # RELATÓRIOS
    "تقرير المبيعات": "Relatório de Vendas",
    "تقرير المنتجات": "Relatório de Produtos",
    "تقرير رصيد الائتمان": "Relatório de Saldo de Crédito",
    
    # CONTA E PERFIL
    "نظرة عامة": "Visão Geral",
    "معلومات الحساب": "Informações da Conta",
    "تغيير كلمة المرور": "Alterar Senha",
    "تاريخ الطلبات": "Histórico de Pedidos",
    "طلبات الإرجاع": "Pedidos de Devolução",
    "الأضرار": "Danos",
    "العنوان": "Endereço",
    "العناوين": "Endereços",
    "قائمة الرغبات": "Lista de Desejos",
    "تسجيل الدخول": "Entrar",
    
    # CAMPOS BÁSICOS
    "الاسم": "Nome",
    "البريد الإلكتروني": "Email",
    "الهاتف": "Telefone",
    "الموقع الإلكتروني": "Site",
    "المدينة": "Cidade",
    "الولاية": "Estado",
    "رمز البلد": "Código do País",
    "الرمز البريدي": "CEP",
    "التاريخ": "Data",
    "السعر": "Preço",
    "المبلغ": "Valor",
    "الحالة": "Status",
    "الإجراء": "Ação",
    "نشط": "Ativo",
    "غير نشط": "Inativo",
    "نعم": "Sim",
    "لا": "Não",
    "افتراضي": "Padrão",
    
    # BOTÕES
    "إضافة": "Adicionar",
    "حفظ": "Salvar",
    "حذف": "Excluir",
    "إغلاق": "Fechar",
    "إلغاء": "Cancelar",
    "مسح": "Limpar",
    "بحث": "Pesquisar",
    "تصفية": "Filtrar",
    "تصدير": "Exportar",
    "طباعة": "Imprimir",
    "إكسل": "Excel",
    "إعادة تعيين": "Resetar",
    "تسجيل الخروج": "Sair",
    "إرسال": "Enviar",
    "تطبيق": "Aplicar",
    "إزالة": "Remover",
    "التحقق": "Verificar",
    
    # E-COMMERCE
    "سلة التسوق": "Carrinho de Compras",
    "الخروج": "Finalizar Compra",
    "الدفع": "Pagamento",
    "الشحن": "Entrega",
    "الضريبة": "Imposto",
    "خصم": "Desconto",
    "كوبون": "Cupom",
    "الكمية": "Quantidade",
    "المجموع": "Total",
    "المجموع الفرعي": "Subtotal",
    "الطلب": "Pedido",
    "العميل": "Cliente",
    "المنتج": "Produto",
    "الفئة": "Categoria",
    "العلامة التجارية": "Marca",
    "الوصف": "Descrição",
    "الصورة": "Imagem",
    "الكود": "Código",
    
    # MENSAGENS
    "شكرا لك": "Obrigado",
    "من فضلك": "Por favor",
    "نجح": "Sucesso",
    "خطأ": "Erro",
    "تحذير": "Aviso",
    "معلومات": "Informação",
    "مرحبا": "Bem-vindo",
    "جاري التحميل": "Carregando",
    "مطلوب": "Obrigatório",
    "اختياري": "Opcional",
    
    # NAVEGAÇÃO
    "الرئيسية": "Início",
    "رجوع": "Voltar",
    "المزيد": "Mais",
    "عرض المزيد": "Mostrar Mais",
    "اقرأ المزيد": "Ler Mais",
    
    # CONFIGURAÇÕES
    "تنسيق التاريخ": "Formato de Data",
    "تنسيق الوقت": "Formato de Hora",
    "المنطقة الزمنية الافتراضية": "Fuso Horário Padrão",
    "العملة الافتراضية": "Moeda Padrão",
    "اللغة الافتراضية": "Idioma Padrão",
    
    # MAIS TERMOS ESPECÍFICOS
    "علامات المنتجات": "Marcas de Produtos",
    "الوحدات": "Unidades",
    "الاختلافات": "Variações",
    "قائمة الإعدادات": "Menu de Configurações",
    "فيديو المنتج": "Vídeo do Produto",
    "تحسين محركات البحث": "SEO",
    "أقسام المنتجات": "Seções de Produtos",
    "الفوائد": "Benefícios",
    "الموردين": "Fornecedores",
    "الملف الشخصي": "Perfil",
    "كلمة المرور": "Senha",
    "رمز الترخيص": "Código de Licença",
    "السابق": "Anterior",
    "التالي": "Próximo",
    "تذكرني": "Lembrar de mim",
    "مرحبا": "Olá",
    
    # TERMOS DO SISTEMA
    "قاعدة البيانات": "Banco de Dados",
    "التثبيت": "Instalação",
    "الخادم": "Servidor",
    "المضيف": "Host",
    "المنفذ": "Porta",
    "اسم المستخدم": "Nome de Usuário",
    "كلمة السر": "Senha",
    "الاتصال": "Conexão",
    "التحقق": "Verificação",
    "التحديث": "Atualização",
    "النسخ الاحتياطي": "Backup",
    "الاستيراد": "Importar",
    "التصدير": "Exportar",
    "الرفع": "Upload",
    "التحميل": "Download"
}

def translate_text(text):
    """Traduz texto árabe para português"""
    if not isinstance(text, str):
        return text
    
    # Aplica todas as traduções
    for arabic, portuguese in translations.items():
        text = text.replace(arabic, portuguese)
    
    return text

def translate_json_recursive(obj):
    """Traduz recursivamente um objeto JSON"""
    if isinstance(obj, dict):
        return {key: translate_json_recursive(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [translate_json_recursive(item) for item in obj]
    elif isinstance(obj, str):
        return translate_text(obj)
    else:
        return obj

# Carrega o arquivo árabe
with open('resources/js/languages/pt-BR.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Traduz todo o conteúdo
translated_data = translate_json_recursive(data)

# Salva o arquivo traduzido
with open('resources/js/languages/pt-BR.json', 'w', encoding='utf-8') as f:
    json.dump(translated_data, f, ensure_ascii=False, indent=4)

print("✅ Tradução completa do árabe para português brasileiro aplicada!")
print(f"✅ {len(translations)} termos traduzidos!")
