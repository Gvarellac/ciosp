# Site do CIOSP Bagé — pacote de publicação

Versão de homologação · novembro de 2026

Site institucional estático do Centro Integrado de Operações de Segurança Pública de Bagé, com três páginas (Início, O CIOSP e Observatório da Criminalidade), aviso de privacidade e página de erro. O visual segue o Manual da marca CIOSP v1.1.

## O que tem no pacote

| Pasta / arquivo | Para que serve |
| --- | --- |
| `publico/` | **Somente esta pasta vai para o ar.** Páginas, estilos, fontes e imagens. |
| `publico/.htaccess` | Regras de segurança para servidor **Apache**. |
| `publico/_headers` | Regras de segurança para **Cloudflare Pages** ou **Netlify**. |
| `servidor/` | Configuração para servidor **Nginx** (`nginx.conf`, `seguranca.conf`, `comum.conf`). |
| `Dockerfile` | Imagem pronta para hospedagens com container (Railway, Render etc.). |
| `ferramentas/gerar_site.py` | Script que gera as páginas a partir dos textos (opcional, para manutenção). |

## Como o site foi protegido

O jeito mais seguro de ter um site é não ter nada para invadir. Por isso:

- **Site estático:** não tem banco de dados, login, painel administrativo, formulário nem programa rodando no servidor.
- **Zero JavaScript:** nenhuma página executa scripts, nem próprios nem de terceiros.
- **Sem serviços externos:** fontes, imagens e estilos ficam no próprio servidor. Não há Google Fonts, analytics, pixels, cookies nem rastreadores, e nenhum dado do visitante vai para terceiros.
- **Política de segurança de conteúdo (CSP) estrita:** o navegador só aceita arquivos do próprio site e bloqueia scripts, frames e envio de formulários. Isso impede injeção de código (XSS) mesmo que alguém consiga alterar um texto.
- **Proteção contra clickjacking:** o site não pode ser carregado dentro de outro site.
- **HTTPS obrigatório:** redirecionamento automático e HSTS de 1 ano.
- **Só leitura:** o servidor recusa qualquer método além de GET e HEAD.
- **Arquivos ocultos e de configuração bloqueados**, listagem de pastas desligada e versão do servidor escondida.
- **Imagens regravadas:** todas sem metadados.
- **`/.well-known/security.txt`:** canal para relatar falhas de segurança.

## Como publicar

Antes de tudo, recomendamos publicar num **subdomínio próprio**, por exemplo `ciosp.bage.rs.gov.br`. Isso isola o site dos outros sistemas da Prefeitura.

### Opção A — Servidor da Prefeitura com Nginx
1. Copie o conteúdo de `publico/` para a pasta do site, por exemplo `/var/www/ciosp`.
2. Copie `servidor/seguranca.conf` para `/etc/nginx/snippets/ciosp-seguranca.conf` e `servidor/comum.conf` para `/etc/nginx/snippets/ciosp-comum.conf`.
3. Use `servidor/nginx.conf` como bloco do site e ajuste as linhas marcadas com `[ajustar]`.
4. Emita o certificado HTTPS (Let's Encrypt/certbot, gratuito).
5. Rode `nginx -t` para testar a configuração e depois `systemctl reload nginx`.

### Opção B — Servidor da Prefeitura com Apache
1. Copie o conteúdo de `publico/` para a pasta do site, **incluindo** os arquivos ocultos `.htaccess` e `.well-known/`.
2. Habilite `mod_headers` e `mod_rewrite` e permita `.htaccess` na pasta (`AllowOverride All`).
3. Configure o HTTPS.

### Opção C — Cloudflare Pages ou Netlify
Publique a pasta `publico/`. O arquivo `_headers` já aplica as regras de segurança.

### Opção D — Container (Railway e similares)
Use o `Dockerfile` da raiz do pacote. O site responde na porta **8080**. O HTTPS fica a cargo da plataforma.

### Conferir depois de publicar
- https://securityheaders.com: a nota esperada é **A** ou **A+**.
- https://www.ssllabs.com/ssltest: a nota esperada é **A**.
- Abrir as páginas no celular e no computador.

## Antes do lançamento oficial

1. **Preencher os campos entre colchetes.** Os números (`[000]`), as notícias, as fotos, os links das redes sociais, a fonte e a metodologia do Observatório e o contato do encarregado de dados (DPO) estão marcados assim. Para achar todos: `grep -n "\[" publico/*.html`.
2. **Números do Observatório:** publicar somente dados aprovados pela coordenação, sempre com fonte e período.
3. **`publico/robots.txt`:** hoje ele bloqueia os buscadores (modo homologação). No lançamento, troque por `Allow: /`.
4. **`security.txt`:** renovar a data `Expires` antes de novembro de 2027.
5. **Botões de download do Observatório:** quando houver os arquivos, trocar o texto entre colchetes por um link para o arquivo dentro de `publico/`.

## Manutenção

- **Atualizar textos:** edite os arquivos `.html` em `publico/`. Não use atributos `style="..."` nem `<script>`, porque a política de segurança vai bloqueá-los. Todo visual fica em `publico/assets/css/site.css`.
- **Alternativa:** os textos também estão em `ferramentas/gerar_site.py`. Depois de editar, rode `python3 ferramentas/gerar_site.py` para regerar as páginas.
- **Fotos de notícias:** use formato WebP ou JPG, com até 1600 px de largura. Não mostre rostos de presos, vítimas, crianças ou adolescentes, placas de veículos, telas de monitoramento nem posição de câmeras (Manual da marca, prancha 14).
- **Se um dia houver painel com login**, isso muda o nível de risco: será preciso autenticação em dois fatores, atualizações frequentes e revisão da política de segurança.

## Licenças

As fontes Barlow Condensed e Inter estão sob a licença SIL Open Font License 1.1, de uso livre (`publico/assets/fonts/`). As logomarcas das instituições pertencem a cada órgão e são usadas para identificar a parceria no CIOSP.
