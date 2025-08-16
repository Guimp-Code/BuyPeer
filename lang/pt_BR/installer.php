<?php


return [
    'title'       => 'Instalador BUYPEER',
    'next'        => 'Próxima Etapa',
    'welcome'     => [
        'templateTitle' => 'Bem-vindo',
        'title'         => 'Instalador BUYPEER',
        'message'       => 'Assistente de Instalação e Configuração Fácil.',
        'next'          => 'Verificar Requisitos',
    ],
    'requirement' => [
        'templateTitle' => 'Etapa 1 | Requisitos do Servidor',
        'title'         => 'Requisitos do Servidor',
        'next'          => 'Verificar Permissões',
        'version'       => 'versão',
        'required'      => 'necessário'
    ],
    'permission'  => [
        'templateTitle'       => 'Etapa 2 | Permissões',
        'title'               => 'Permissões',
        'next'                => 'Configuração do Site',
        'permission_checking' => 'Verificação de Permissões'
    ],
    'license' => [
        'templateTitle'       => 'Etapa 3 | Licença',
        'title'               => 'Configuração de Licença',
        'next'                => 'Configuração do Site',
        'active_process'      => 'Processo de Ativação',
        'label'               => [
            'license_code' => 'Código de Licença'
        ]
    ],
    'site'        => [
        'templateTitle' => 'Etapa 3 | Configuração do Site',
        'title'         => 'Configuração do Site',
        'next'          => 'Configuração do Banco de Dados',
        'label'         => [
            'app_name' => 'Nome da Aplicação',
            'app_url'  => 'URL da Aplicação',
        ]
    ],
    'database'    => [
        'templateTitle'            => 'Etapa 4 | Configuração do Banco de Dados',
        'title'                    => 'Configuração do Banco de Dados',
        'next'                     => 'Configuração Final',
        'fail_message'             => 'Não foi possível conectar ao banco de dados.',
        'fail_mysql_version'       => 'Use a versão 8.0 ou posterior do MySQL.',
        'fail_mariadb_version'     => 'Use a versão 10.2 ou posterior do MariaDB.',
        'fail_postgresql_version'  => 'Use a versão 9.4 ou posterior do PostgreSQL.',
        'fail_sqlserver_version'   => 'Use a versão 2008 ou posterior do SQL Server.',
        'fail_singlestore_version' => 'Use a versão 8.1 ou posterior do SingleStore.',
        'label'                    => [
            'database_connection' => 'Conexão do Banco de Dados',
            'database_host'       => 'Host do Banco de Dados',
            'database_port'       => 'Porta do Banco de Dados',
            'database_name'       => 'Nome do Banco de Dados',
            'database_username'   => 'Usuário do Banco de Dados',
            'database_password'   => 'Senha do Banco de Dados',
        ]
    ],
    'final'       => [
        'templateTitle'   => 'Etapa 6 | Configuração Final',
        'title'           => 'Configuração Final',
        'success_message' => 'Aplicação foi instalada com sucesso.',
        'login_info'      => 'Informações de Login',
        'email'           => 'Email',
        'password'        => 'Senha',
        'email_info'      => 'admin@example.com',
        'password_info'   => 'Use sua própria senha segura',
        'next'            => 'Finalizar',
    ],
    'installed'   => [
            'success_log_message' => 'Instalador BUYPEER instalado com sucesso em ',
    'update_log_message'  => 'Instalador BUYPEER atualizado com sucesso em ',
    ],
];
