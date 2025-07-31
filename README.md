# BuyPeer
Plataforma de E-commerce

## 📋 Sobre o Projeto

BuyPeer é uma plataforma completa de e-commerce desenvolvida em Laravel com Vue.js, oferecendo uma solução robusta para lojas online com recursos avançados de gestão, pagamentos e experiência do usuário.

## ✨ Funcionalidades Principais

### 🛍️ Frontend (Loja)
- **Catálogo de Produtos**: Navegação por categorias e marcas
- **Sistema de Busca**: Busca avançada com filtros
- **Carrinho de Compras**: Gestão de produtos e quantidades
- **Checkout Completo**: Processo de compra otimizado
- **Sistema de Pagamentos**: Integração com múltiplas gateways
- **Área do Cliente**: Histórico de pedidos, endereços, favoritos
- **Sistema de Avaliações**: Reviews de produtos
- **Promoções e Cupons**: Descontos e ofertas especiais
- **Responsivo**: Interface adaptável para mobile e desktop

### 🎛️ Backend (Administração)
- **Dashboard Completo**: Métricas e relatórios em tempo real
- **Gestão de Produtos**: CRUD completo com variações
- **Gestão de Pedidos**: Acompanhamento e atualização de status
- **Gestão de Clientes**: Cadastro e histórico de compras
- **Sistema de Estoque**: Controle de inventário
- **Relatórios Avançados**: Vendas, produtos, clientes
- **Configurações**: Personalização da loja
- **Multi-idioma**: Suporte a múltiplos idiomas
- **PWA**: Progressive Web App

### 💳 Sistema de Pagamentos
- **Stripe**: Pagamentos internacionais
- **Razorpay**: Gateway indiano
- **Cashfree**: Pagamentos locais
- **Pagamento em Dinheiro**: Para retirada local
- **Múltiplas Moedas**: Suporte a diferentes moedas

## 🚀 Instalação e Configuração

### Pré-requisitos

- **PHP**: 8.1 ou superior
- **Composer**: 2.0 ou superior
- **Node.js**: 16.0 ou superior
- **MySQL**: 8.0 ou superior
- **Nginx/Apache**: Servidor web
- **SSL**: Certificado SSL (recomendado)

### 📦 Instalação Local

1. **Clone o repositório**
```bash
git clone https://github.com/Guimp-Code/BuyPeer.git
cd BuyPeer
```

2. **Instale as dependências PHP**
```bash
composer install
```

3. **Instale as dependências Node.js**
```bash
npm install
```

4. **Configure o arquivo de ambiente**
```bash
cp .env.example .env
php artisan key:generate
```

5. **Configure o banco de dados no .env**
```env
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=buypeer
DB_USERNAME=seu_usuario
DB_PASSWORD=sua_senha
```

6. **Execute as migrações**
```bash
php artisan migrate
```

7. **Execute os seeders**
```bash
php artisan db:seed
```

8. **Compile os assets**
```bash
npm run dev
```

9. **Configure o servidor web**
```bash
php artisan serve
```

### 🌐 Deploy no VPS

#### 1. Preparação do Servidor

**Sistema Operacional**: Ubuntu 20.04/22.04 LTS

**Atualize o sistema**:
```bash
sudo apt update && sudo apt upgrade -y
```

**Instale o LEMP Stack**:
```bash
# Nginx
sudo apt install nginx -y

# MySQL
sudo apt install mysql-server -y

# PHP 8.1
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:ondrej/php -y
sudo apt update
sudo apt install php8.1-fpm php8.1-mysql php8.1-xml php8.1-curl php8.1-mbstring php8.1-zip php8.1-gd php8.1-bcmath php8.1-intl php8.1-soap php8.1-redis -y

# Composer
curl -sS https://getcomposer.org/installer | php
sudo mv composer.phar /usr/local/bin/composer

# Node.js
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs
```

#### 2. Configuração do MySQL

```bash
sudo mysql_secure_installation
```

**Crie o banco de dados**:
```sql
CREATE DATABASE buypeer;
CREATE USER 'buypeer_user'@'localhost' IDENTIFIED BY 'sua_senha_forte';
GRANT ALL PRIVILEGES ON buypeer.* TO 'buypeer_user'@'localhost';
FLUSH PRIVILEGES;
```

#### 3. Deploy da Aplicação

**Clone o projeto**:
```bash
cd /var/www
sudo git clone https://github.com/Guimp-Code/BuyPeer.git
sudo chown -R www-data:www-data BuyPeer
cd BuyPeer
```

**Configure as permissões**:
```bash
sudo chmod -R 755 storage bootstrap/cache
sudo chown -R www-data:www-data storage bootstrap/cache
```

**Instale as dependências**:
```bash
composer install --optimize-autoloader --no-dev
npm install
npm run production
```

**Configure o .env**:
```bash
cp .env.example .env
php artisan key:generate
```

**Configure o arquivo .env para produção**:
```env
APP_ENV=production
APP_DEBUG=false
APP_URL=https://seudominio.com

DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=buypeer
DB_USERNAME=buypeer_user
DB_PASSWORD=sua_senha_forte

CACHE_DRIVER=redis
SESSION_DRIVER=redis
QUEUE_CONNECTION=redis

REDIS_HOST=127.0.0.1
REDIS_PASSWORD=null
REDIS_PORT=6379
```

**Execute as migrações**:
```bash
php artisan migrate --force
php artisan db:seed --force
```

**Configure o cache**:
```bash
php artisan config:cache
php artisan route:cache
php artisan view:cache
```

#### 4. Configuração do Nginx

**Crie o arquivo de configuração**:
```bash
sudo nano /etc/nginx/sites-available/buypeer
```

**Adicione a configuração**:
```nginx
server {
    listen 80;
    server_name seudominio.com www.seudominio.com;
    root /var/www/BuyPeer/public;

    add_header X-Frame-Options "SAMEORIGIN";
    add_header X-Content-Type-Options "nosniff";

    index index.php;

    charset utf-8;

    location / {
        try_files $uri $uri/ /index.php?$query_string;
    }

    location = /favicon.ico { access_log off; log_not_found off; }
    location = /robots.txt  { access_log off; log_not_found off; }

    error_page 404 /index.php;

    location ~ \.php$ {
        fastcgi_pass unix:/var/run/php/php8.1-fpm.sock;
        fastcgi_param SCRIPT_FILENAME $realpath_root$fastcgi_script_name;
        include fastcgi_params;
    }

    location ~ /\.(?!well-known).* {
        deny all;
    }
}
```

**Ative o site**:
```bash
sudo ln -s /etc/nginx/sites-available/buypeer /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

#### 5. Configuração do SSL (Let's Encrypt)

**Instale o Certbot**:
```bash
sudo apt install certbot python3-certbot-nginx -y
```

**Obtenha o certificado SSL**:
```bash
sudo certbot --nginx -d seudominio.com -d www.seudominio.com
```

#### 6. Configuração do Redis (Opcional)

**Instale o Redis**:
```bash
sudo apt install redis-server -y
sudo systemctl enable redis-server
```

#### 7. Configuração do Supervisor (Para Filas)

**Instale o Supervisor**:
```bash
sudo apt install supervisor -y
```

**Crie o arquivo de configuração**:
```bash
sudo nano /etc/supervisor/conf.d/buypeer-worker.conf
```

**Adicione a configuração**:
```ini
[program:buypeer-worker]
process_name=%(program_name)s_%(process_num)02d
command=php /var/www/BuyPeer/artisan queue:work redis --sleep=3 --tries=3 --max-time=3600
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true
user=www-data
numprocs=2
redirect_stderr=true
stdout_logfile=/var/www/BuyPeer/storage/logs/worker.log
stopwaitsecs=3600
```

**Ative o supervisor**:
```bash
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start buypeer-worker:*
```

### 🔧 Configurações Iniciais

#### 1. Acesso ao Painel Administrativo

Após a instalação, acesse:
```
https://seudominio.com/admin
```

**Credenciais padrão**:
- **Email**: admin@buypeer.com
- **Senha**: 12345678

#### 2. Configurações Essenciais

**No painel administrativo, configure**:

1. **Informações da Empresa**
   - Nome da loja
   - Endereço
   - Telefone
   - Email

2. **Configurações de Pagamento**
   - Ative os gateways desejados
   - Configure as chaves de API
   - Teste as integrações

3. **Configurações de Email**
   - SMTP para notificações
   - Templates de email

4. **Configurações de Frete**
   - Áreas de entrega
   - Taxas de frete
   - Métodos de entrega

5. **Produtos e Categorias**
   - Crie categorias principais
   - Adicione produtos de exemplo
   - Configure variações

#### 3. Otimizações de Performance

**Configure o cache**:
```bash
php artisan config:cache
php artisan route:cache
php artisan view:cache
```

**Configure o cron para tarefas agendadas**:
```bash
crontab -e
```

**Adicione a linha**:
```cron
* * * * * cd /var/www/BuyPeer && php artisan schedule:run >> /dev/null 2>&1
```

### 🔒 Segurança

#### Recomendações de Segurança

1. **Firewall**:
```bash
sudo ufw enable
sudo ufw allow ssh
sudo ufw allow 'Nginx Full'
```

2. **Atualizações regulares**:
```bash
sudo apt update && sudo apt upgrade -y
```

3. **Backup automático**:
```bash
# Crie um script de backup
sudo nano /usr/local/bin/backup-buypeer.sh
```

**Conteúdo do script**:
```bash
#!/bin/bash
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/backup/buypeer"
mkdir -p $BACKUP_DIR

# Backup do banco
mysqldump -u buypeer_user -p buypeer > $BACKUP_DIR/database_$DATE.sql

# Backup dos arquivos
tar -czf $BACKUP_DIR/files_$DATE.tar.gz /var/www/BuyPeer

# Manter apenas os últimos 7 backups
find $BACKUP_DIR -name "*.sql" -mtime +7 -delete
find $BACKUP_DIR -name "*.tar.gz" -mtime +7 -delete
```

**Torne executável e agende**:
```bash
sudo chmod +x /usr/local/bin/backup-buypeer.sh
sudo crontab -e
# Adicione: 0 2 * * * /usr/local/bin/backup-buypeer.sh
```

### 📊 Monitoramento

#### Logs Importantes

- **Laravel logs**: `/var/www/BuyPeer/storage/logs/laravel.log`
- **Nginx logs**: `/var/log/nginx/access.log` e `/var/log/nginx/error.log`
- **PHP-FPM logs**: `/var/log/php8.1-fpm.log`

#### Comandos Úteis

```bash
# Verificar status dos serviços
sudo systemctl status nginx php8.1-fpm mysql redis-server

# Verificar logs em tempo real
sudo tail -f /var/www/BuyPeer/storage/logs/laravel.log

# Limpar cache
php artisan cache:clear
php artisan config:clear
php artisan route:clear
php artisan view:clear

# Verificar permissões
sudo chown -R www-data:www-data /var/www/BuyPeer
sudo chmod -R 755 /var/www/BuyPeer/storage
```

### 🆘 Suporte

Para suporte técnico ou dúvidas sobre o projeto:

- **Issues**: [GitHub Issues](https://github.com/Guimp-Code/BuyPeer/issues)
- **Documentação**: Consulte a documentação do Laravel
- **Comunidade**: Stack Overflow com tag `laravel`

### 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

---

**Desenvolvido com ❤️ pela equipe BuyPeer**
