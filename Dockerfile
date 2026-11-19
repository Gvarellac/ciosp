# CIOSP Bagé — imagem para hospedagens com container (Railway, Render, Fly etc.)
# Nginx sem privilégios de root, servindo apenas a pasta "publico" (só leitura).
FROM nginxinc/nginx-unprivileged:1.27-alpine
COPY --chown=root:root servidor/docker-nginx.conf /etc/nginx/conf.d/default.conf
COPY --chown=root:root servidor/seguranca.conf /etc/nginx/snippets/ciosp-seguranca.conf
COPY --chown=root:root servidor/comum.conf /etc/nginx/snippets/ciosp-comum.conf
COPY --chown=root:root publico/ /usr/share/nginx/html/
EXPOSE 8080
USER 101
