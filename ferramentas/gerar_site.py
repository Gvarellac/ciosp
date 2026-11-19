#!/usr/bin/env python3
"""Gera as páginas estáticas do site do CIOSP Bagé (sem JavaScript, sem estilos em linha)."""
import sys, pathlib

R = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path(__file__).resolve().parent.parent / "publico"

RADAR = '''<svg class="heroi__radar" viewBox="0 0 1200 620" aria-hidden="true" focusable="false">
<g fill="none" stroke="#9FB4BA"><circle cx="820" cy="310" r="210" stroke-opacity="0.14"/><circle cx="820" cy="310" r="300" stroke-opacity="0.09"/><circle cx="820" cy="310" r="410" stroke-opacity="0.06"/></g>
<path d="M820 10 A300 300 0 0 1 1102 207" fill="none" stroke="#C39A4E" stroke-width="2.5" stroke-linecap="round"/>
<circle cx="1102" cy="207" r="6" fill="#C39A4E"/>
</svg>'''

MENU = [("index.html", "Início"), ("o-ciosp.html", "O CIOSP"), ("observatorio.html", "Observatório"),
        ("index.html#noticias", "Notícias"), ("index.html#orientacoes", "Orientações"), ("#contato", "Contato")]


def pagina(arquivo, titulo, descricao, atual, corpo):
    itens = []
    for href, nome in MENU:
        cur = ' aria-current="page"' if href == atual else ''
        itens.append(f'<li><a href="{href}"{cur}>{nome}</a></li>')
    menu = "\n".join(itens)
    html = f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo}</title>
<meta name="description" content="{descricao}">
<meta name="theme-color" content="#0B2A33">
<meta name="referrer" content="strict-origin-when-cross-origin">
<meta property="og:title" content="{titulo}">
<meta property="og:description" content="{descricao}">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<link rel="icon" href="favicon.ico" sizes="48x48">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="preload" href="assets/fonts/barlow-condensed-700.woff" as="font" type="font/woff" crossorigin>
<link rel="preload" href="assets/fonts/inter-400.woff" as="font" type="font/woff" crossorigin>
<link rel="stylesheet" href="assets/css/site.css">
</head>
<body>
<a class="pular" href="#conteudo">Pular para o conteúdo</a>

<div class="faixa-topo">
<div class="container">
<span>Prefeitura Municipal de Bagé · Secretaria de Segurança e Mobilidade Urbana</span>
<span>Emergência: <a href="tel:190"><strong>190</strong></a> Brigada Militar · <a href="tel:193"><strong>193</strong></a> Bombeiros</span>
</div>
</div>

<header class="cabecalho">
<div class="container">
<a class="marca" href="index.html">
<img src="assets/img/escudo-ciosp-pequeno.webp" width="46" height="56" alt="">
<span class="marca__nome"><span class="marca__sigla">CIOSP</span><span class="marca__local">BAGÉ - RS</span></span>
<span class="sr-only">Página inicial do CIOSP Bagé</span>
</a>
<nav class="menu" aria-label="Principal">
<ul>
{menu}
</ul>
</nav>
<a class="botao botao--escuro" href="mailto:ciosp@bage.rs.gov.br">Fale conosco</a>
</div>
</header>

<main id="conteudo">
{corpo}
</main>

<footer class="rodape" id="contato">
<div class="container">
<div class="rodape__blocos">
<div class="rodape__marca">
<img src="assets/img/escudo-ciosp-pequeno.webp" width="56" height="69" alt="">
<div><span class="rodape__sigla">CIOSP</span><small>Centro Integrado de Operações<br>de Segurança Pública · Bagé - RS</small></div>
</div>
<address class="rodape__contato">
<strong>Contato</strong>
<span>Av. Gen. Osório, 998 - Centro<br>Bagé - RS, 96400-100</span>
<a href="mailto:ciosp@bage.rs.gov.br">ciosp@bage.rs.gov.br</a>
</address>
<div class="rodape__ssm">
<img src="assets/img/brasao-bage.webp" width="54" height="62" alt="Brasão do Município de Bagé">
<span class="rodape__divisor" aria-hidden="true"></span>
<div><b>SSM</b><small>Secretaria de Segurança<br>e Mobilidade Urbana</small></div>
</div>
</div>
<div class="rodape__base">
<span>© 2026 Prefeitura Municipal de Bagé · <a href="privacidade.html">Aviso de privacidade</a></span>
<span>Este site não recebe ocorrências · Emergência 190 · 193 · 199 · 153 · 118</span>
</div>
</div>
</footer>
</body>
</html>
'''
    (R / arquivo).write_text(html, encoding="utf-8")


EMERG = [("190", "Brigada<br>Militar"), ("193", "Corpo de<br>Bombeiros"), ("199", "Defesa<br>Civil"),
         ("153", "Guarda Civil<br>Municipal"), ("118", "Segurança<br>Viária")]
faixa_emerg = "\n".join(
    f'<a class="emergencia" href="tel:{n}"><span class="emergencia__numero">{n}</span><span class="emergencia__nome">{t}</span></a>'
    for n, t in EMERG)

P1 = ("O Centro Integrado de Operações de Segurança Pública de Bagé — CIOSP é uma iniciativa da Prefeitura Municipal, por meio da "
      "Secretaria de Segurança e Mobilidade Urbana, voltada à modernização da segurança pública e à proteção da população. Sua proposta "
      "é integrar tecnologia, informação e cooperação entre instituições para apoiar a prevenção de ocorrências e tornar mais ágil e "
      "coordenado o atendimento às demandas do município.")
P2 = ("O projeto reúne videomonitoramento urbano, cercamento eletrônico e ferramentas de análise de informações para auxiliar na "
      "proteção dos espaços públicos, na segurança viária e no acompanhamento de situações de emergência. A integração entre os órgãos "
      "de segurança, fiscalização, socorro e defesa civil permitirá ampliar a compreensão do que acontece na cidade e apoiar decisões "
      "com base em informações compartilhadas.")
P3 = ("Mais do que uma central de câmeras, o CIOSP foi concebido como um espaço de atuação conjunta, planejamento e inteligência. "
      "Seu compromisso é contribuir para uma Bagé mais segura, com respeito à privacidade, uso responsável dos dados e atenção "
      "permanente à vida e ao bem-estar de quem vive, trabalha e circula pelo município.")

ICONES = {
    "celular": '<rect x="6" y="2.5" width="12" height="19" rx="2"/><path d="M11 18h2"/>',
    "carro": '<path d="M5 17h14l-1.5-6h-11z"/><circle cx="8" cy="19" r="1.6"/><circle cx="16" cy="19" r="1.6"/><path d="M8 11l1-4h6l1 4"/>',
    "nuvem": '<path d="M7 16a4 4 0 0 1 .5-8A5 5 0 0 1 17 8.5a3.5 3.5 0 0 1 0 7.5z"/><path d="M11 18l-1.5 3M15 18l-1.5 3"/>',
    "casa": '<path d="M4 11l8-7 8 7v9H4z"/><path d="M10 20v-5h4v5"/>',
}
ORIENT = [("celular", "Golpes e fraudes", "Como reconhecer golpes por telefone e internet."),
          ("carro", "Trânsito e interdições", "Bloqueios, desvios e eventos na cidade."),
          ("nuvem", "Alertas climáticos", "Avisos de chuva forte, vento e frio."),
          ("casa", "Segurança em casa", "Cuidados para viagens e no dia a dia.")]
orient = "\n".join(
    f'<li class="orientacao"><svg viewBox="0 0 24 24" fill="none" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">{ICONES[i]}</svg><h3>{t}</h3><p>{d}</p></li>'
    for i, t, d in ORIENT)
noticias = "\n".join(
    f'<li class="noticia"><div class="noticia__foto">[FOTO]</div><div class="noticia__texto"><span class="noticia__meta">[DD.MM.AAAA] · {c}</span><span class="noticia__titulo">[Título da notícia em até duas linhas]</span></div></li>'
    for c in ["OPERAÇÕES", "PREVENÇÃO", "INSTITUCIONAL"])

INICIO = f'''<section class="heroi" aria-labelledby="titulo-inicio">
{RADAR}
<div class="container heroi__conteudo">
<div class="heroi__texto">
<span class="etiqueta etiqueta--clara">Prefeitura de Bagé · SSM</span>
<h1 id="titulo-inicio">Centro Integrado de Operações de Segurança Pública</h1>
<p class="heroi__lead">Monitoramento, integração entre as forças de segurança e informação confiável para a população de Bagé.</p>
<div class="heroi__acoes">
<a class="botao botao--dourado" href="#noticias">Últimas notícias</a>
<a class="botao botao--contorno-claro" href="o-ciosp.html">Conheça o CIOSP</a>
</div>
</div>
<div class="heroi__escudo"><img src="assets/img/escudo-ciosp.webp" width="300" height="367" alt="Escudo do CIOSP Bagé"></div>
</div>
</section>

<section class="container flutuante" aria-labelledby="titulo-emergencia">
<h2 class="sr-only" id="titulo-emergencia">Telefones de emergência</h2>
<div class="cartao-flutuante">
{faixa_emerg}
<p class="emergencia__aviso">Este site não recebe ocorrências. Em caso de emergência, ligue para um dos números ao lado.</p>
</div>
</section>

<section class="container secao" aria-labelledby="titulo-sobre">
<div class="sobre-resumo">
<span class="etiqueta">O CIOSP</span>
<h2 class="h2-grande" id="titulo-sobre">Tecnologia e integração a serviço da vida</h2>
<div class="texto-corrido"><p>{P1}</p></div>
<a class="botao botao--escuro" href="o-ciosp.html">Conheça o CIOSP e as instituições integradas →</a>
</div>
</section>

<section class="container secao" id="noticias" aria-labelledby="titulo-noticias">
<div class="secao__cabeca"><div><span class="etiqueta">Notícias</span><h2 class="h2-grande" id="titulo-noticias">Últimas do CIOSP</h2></div></div>
<ul class="grade-3">
{noticias}
</ul>
</section>

<section class="container secao secao--ultima" id="orientacoes" aria-labelledby="titulo-orientacoes">
<div class="secao__cabeca"><div><span class="etiqueta">Orientações</span><h2 class="h2-grande" id="titulo-orientacoes">Como se proteger</h2></div></div>
<ul class="grade-4">
{orient}
</ul>
</section>

<section class="numeros" aria-labelledby="titulo-numeros">
<div class="container">
<div class="secao__cabeca"><div><span class="etiqueta etiqueta--clara">Transparência</span><h2 id="titulo-numeros">CIOSP em números · [mês/ano]</h2></div>
<a href="observatorio.html">Ver o Observatório da Criminalidade →</a></div>
<ul class="grade-numeros">
<li class="numero"><span class="numero__valor">[000]</span><span class="numero__rotulo">ocorrências atendidas</span></li>
<li class="numero"><span class="numero__valor">[000]</span><span class="numero__rotulo">câmeras em operação</span></li>
<li class="numero"><span class="numero__valor">[000]</span><span class="numero__rotulo">veículos recuperados</span></li>
<li class="numero"><span class="numero__valor">[000]</span><span class="numero__rotulo">[outro indicador]</span></li>
</ul>
</div>
</section>

<section class="container secao secao--ultima" aria-labelledby="titulo-canais">
<div class="canais">
<div><h2 id="titulo-canais">Acompanhe o CIOSP</h2><p>Alertas e orientações direto no seu celular.</p></div>
<ul class="canais__lista">
<li class="canal">[Instagram]</li><li class="canal">[Facebook]</li><li class="canal">[Canal do WhatsApp]</li><li class="canal">[YouTube]</li>
</ul>
</div>
</section>'''

INST = [("prefeitura-bage", "Prefeitura Municipal de Bagé"), ("ggi-m", "Gabinete de Gestão Integrada Municipal · GGI-M"),
        ("guarda-civil-municipal", "Guarda Civil Municipal"), ("seguranca-viaria", "Segurança Viária · Agentes de Trânsito"),
        ("consepro-bage", "Consepro Bagé"), ("policia-federal", "Polícia Federal"),
        ("policia-rodoviaria-federal", "Polícia Rodoviária Federal"), ("policia-civil-rs", "Polícia Civil RS"),
        ("brigada-militar", "Brigada Militar"), ("policia-penal-rs", "Polícia Penal RS"),
        ("bombeiros-rs", "Corpo de Bombeiros Militar"), ("defesa-civil", "Defesa Civil"),
        ("samu-192", "SAMU 192"), ("mprs", "Ministério Público do RS")]
# Texto de cada janela: (quem é, papel na integração). Validar com cada instituição antes do lançamento.
INST_TEXTO = {
    "prefeitura-bage": ("Bagé, fundada em 1811, é a responsável pelo CIOSP por meio da Secretaria de Segurança e Mobilidade Urbana.",
                        "Coordena o centro, oferece a estrutura de videomonitoramento e aproxima as instituições para que trabalhem juntas em favor da população."),
    "ggi-m": ("O Gabinete de Gestão Integrada Municipal é o espaço onde os órgãos de segurança de Bagé se reúnem para planejar ações conjuntas.",
              "É no GGI-M que as prioridades são definidas em conjunto e transformadas em ações coordenadas no CIOSP."),
    "guarda-civil-municipal": ("Força de segurança do município, regida pelo Estatuto Geral das Guardas Municipais (Lei nº 13.022/2014). Protege bens, serviços e espaços públicos e faz patrulhamento preventivo.",
                               "Acompanha as imagens do centro e chega rápido aos locais onde a presença preventiva faz diferença. Atendimento pelo 153."),
    "seguranca-viaria": ("Os Agentes de Trânsito e Transportes fiscalizam, organizam e educam para o trânsito no município, conforme o Código de Trânsito Brasileiro.",
                         "Usa o monitoramento para agir em acidentes, bloqueios e grandes eventos, deixando o trânsito mais seguro e fluido. Atendimento pelo 118."),
    "consepro-bage": ("O Conselho Comunitário Pró-Segurança Pública é uma entidade da sociedade civil que apoia as forças de segurança e aproxima a comunidade do tema.",
                      "Leva ao CIOSP a voz dos moradores e ajuda a fortalecer a parceria entre a população e as instituições."),
    "policia-federal": ("Polícia judiciária da União, responsável por investigar crimes federais e atuar no controle de fronteiras e imigração.",
                        "Soma conhecimento e informações às ações integradas, em especial nas questões ligadas à fronteira e aos crimes federais."),
    "policia-rodoviaria-federal": ("Responsável pelo patrulhamento e pela fiscalização das rodovias federais.",
                                   "Integra as informações das rodovias que cortam o município às ações do centro."),
    "policia-civil-rs": ("Polícia judiciária do Estado: registra ocorrências, investiga crimes e conduz os inquéritos policiais.",
                         "Informações e imagens obtidas de forma integrada ajudam a esclarecer crimes com mais agilidade."),
    "brigada-militar": ("Polícia militar do Rio Grande do Sul, criada em 1837, responsável pelo policiamento ostensivo e pela preservação da ordem pública.",
                        "Recebe apoio do monitoramento para orientar o policiamento e agilizar o atendimento das ocorrências. Emergência: 190."),
    "policia-penal-rs": ("Responsável pela segurança dos estabelecimentos prisionais do Estado.",
                         "Compartilha informações que contribuem para a prevenção de crimes e para a segurança de toda a comunidade."),
    "bombeiros-rs": ("O Corpo de Bombeiros Militar atua na prevenção e no combate a incêndios, em salvamentos e no atendimento a emergências.",
                     "As imagens e a comunicação integrada ajudam a localizar ocorrências e a planejar a resposta. Emergência: 193."),
    "defesa-civil": ("Atua na prevenção, na preparação e na resposta a desastres, conforme o Sistema Nacional de Proteção e Defesa Civil (Lei nº 12.608/2012).",
                     "Acompanha situações de risco, como temporais e cheias, e emite alertas à população com apoio do centro. Atendimento pelo 199."),
    "samu-192": ("O Serviço de Atendimento Móvel de Urgência presta atendimento pré-hospitalar pelo SUS, acionado gratuitamente pelo 192.",
                 "A integração com as demais forças agiliza o socorro às vítimas e o acesso aos locais de atendimento."),
    "mprs": ("O Ministério Público do Rio Grande do Sul defende a ordem jurídica, o regime democrático e os interesses da sociedade, e exerce o controle externo da atividade policial.",
             "Acompanha a atuação integrada, contribuindo para que ela respeite a lei, a privacidade e os direitos de todos."),
}


def janela(a, n):
    quem, integra = INST_TEXTO[a]
    return (f'<li><button class="inst" type="button" popovertarget="inst-{a}">'
            f'<img src="assets/img/instituicoes/{a}.webp" width="120" height="120" alt="" loading="lazy">'
            f'<span>{n}</span><span class="sr-only">: saiba mais</span></button>'
            f'<div class="inst-pop" id="inst-{a}" popover role="dialog" aria-labelledby="inst-{a}-t">'
            f'<button class="inst-pop__fechar" type="button" popovertarget="inst-{a}" popovertargetaction="hide">'
            f'<span aria-hidden="true">×</span><span class="sr-only">Fechar</span></button>'
            f'<div class="inst-pop__topo"><img src="assets/img/instituicoes/{a}.webp" width="96" height="96" alt="" loading="lazy">'
            f'<h3 id="inst-{a}-t">{n}</h3></div>'
            f'<p>{quem}</p>'
            f'<h4>Na integração do CIOSP</h4><p>{integra}</p>'
            f'</div></li>')


mosaico = "\n".join(janela(a, n) for a, n in INST)
PILARES = [("Videomonitoramento urbano", "Câmeras em pontos estratégicos para proteger os espaços públicos."),
           ("Cercamento eletrônico", "Apoio ao acompanhamento de veículos e à segurança viária."),
           ("Análise de informações", "Dados compartilhados para apoiar decisões e prevenção."),
           ("Atuação integrada", "Segurança, fiscalização, socorro e defesa civil no mesmo espaço.")]
pil = "\n".join(f'<li><div><strong>{t}</strong><span>{d}</span></div></li>' for t, d in PILARES)

OCIOSP = f'''<section class="heroi heroi--interna" aria-labelledby="titulo-ciosp">
{RADAR}
<div class="container heroi__conteudo">
<nav class="trilha" aria-label="Você está em"><a href="index.html">Início</a> <span aria-hidden="true">›</span> O CIOSP</nav>
<div class="heroi__texto">
<span class="etiqueta etiqueta--clara">CIOSP Bagé</span>
<h1 id="titulo-ciosp">Tecnologia e integração a serviço da vida</h1>
</div>
</div>
</section>

<section class="container secao" aria-label="Apresentação">
<div class="duas-colunas">
<div class="texto-corrido"><p>{P1}</p><p>{P2}</p><p>{P3}</p></div>
<aside class="quadro-escuro" aria-labelledby="titulo-reune"><h2 id="titulo-reune">O que o CIOSP reúne</h2><ul class="pilares">
{pil}
</ul></aside>
</div>
</section>

<section class="container secao secao--ultima" aria-labelledby="titulo-instituicoes">
<div class="titulo-secao"><h2 id="titulo-instituicoes">Instituições integradas</h2></div>
<p class="mosaico__dica">Toque em uma instituição para conhecer o seu papel na integração.</p>
<ul class="mosaico">
{mosaico}
</ul>
<a class="voltar" href="index.html">← Voltar para a página inicial</a>
</section>'''

IND = ["Homicídio doloso", "Latrocínio", "Feminicídio", "Roubos", "Furtos", "Roubo de veículos", "Furto de veículos",
       "Estelionato", "Tráfico de entorpecentes", "Delitos com armas e munições"]
cards = "\n".join(
    f'<li class="indicador"><span class="indicador__nome">{n}</span><span class="indicador__valor">[000]</span><span class="indicador__variacao">[± 0%] em relação ao mesmo período de [ano anterior]</span></li>'
    for n in IND)
barras = "".join("<span></span>" for _ in range(12))
meses = "".join(f"<span>{m}</span>" for m in "Jan Fev Mar Abr Mai Jun Jul Ago Set Out Nov Dez".split())
bairros = "\n".join(
    f'<li><span class="bairros__nome">[Bairro {i}]</span><span class="bairros__barra"><i></i></span><span class="bairros__valor">[000]</span></li>'
    for i in range(1, 7))


def painel(t, itens):
    li = "".join(f"<li><span>{x}</span><strong>[000]</strong></li>" for x in itens)
    return f'<section class="painel" aria-label="{t}"><h3>{t}</h3><ul>{li}</ul></section>'


paineis = "\n".join([painel("Trânsito", ["Acidentes", "Feridos", "Autuações", "Operações de fiscalização"]),
                     painel("SAMU", ["Atendimentos realizados", "Tempo médio de resposta"]),
                     painel("Defesa Civil", ["Ocorrências", "Alertas emitidos", "Famílias atendidas"])])

OBS = f'''<section class="heroi heroi--interna heroi--com-filtro" aria-labelledby="titulo-obs">
{RADAR}
<div class="container heroi__conteudo">
<nav class="trilha" aria-label="Você está em"><a href="index.html">Início</a> <span aria-hidden="true">›</span> Observatório</nav>
<div class="heroi__texto">
<span class="etiqueta etiqueta--clara">Observatório</span>
<h1 id="titulo-obs">Observatório da Criminalidade de Bagé</h1>
<p class="heroi__lead">Indicadores de segurança pública do município, sempre com fonte, período e data de atualização, para que a população acompanhe a realidade de Bagé.</p>
</div>
</div>
</section>

<section class="container flutuante" aria-labelledby="titulo-filtros">
<h2 class="sr-only" id="titulo-filtros">Período e fonte dos dados</h2>
<div class="cartao-flutuante filtros">
<label>Mês<select disabled><option>[Mês]</option></select></label>
<label>Ano<select disabled><option>[Ano]</option></select></label>
<div class="filtros__fonte">
<span><strong>Fonte:</strong> [SSP-RS · Indicadores criminais por município]</span>
<span>Atualizado em [dd/mm/aaaa] · Período: [mês/ano a mês/ano]</span>
</div>
</div>
</section>

<section class="container secao" aria-labelledby="titulo-ind">
<div class="titulo-secao"><h2 id="titulo-ind">Indicadores criminais</h2></div>
<ul class="indicadores">
{cards}
</ul>
</section>

<section class="container secao" aria-label="Gráficos">
<div class="graficos">
<figure class="grafico grafico--largo">
<figcaption><strong>Evolução mensal</strong><span>[Indicador] · [ano]</span></figcaption>
<div class="barras" aria-hidden="true">{barras}</div>
<div class="meses" aria-hidden="true">{meses}</div>
<p class="grafico__nota">Ilustração do formato do gráfico. Ainda sem dados.</p>
</figure>
<figure class="grafico grafico--estreito">
<figcaption><strong>Ocorrências por bairro</strong><span>Dados agregados, sem endereços nem pessoas</span></figcaption>
<ul class="bairros">
{bairros}
</ul>
</figure>
</div>
</section>

<section class="container secao" aria-labelledby="titulo-paineis">
<div class="titulo-secao"><h2 id="titulo-paineis">Outros painéis</h2></div>
<div class="paineis">
{paineis}
</div>
</section>

<section class="container secao secao--ultima" aria-labelledby="titulo-metodo">
<div class="metodologia">
<div class="texto-corrido">
<div class="titulo-secao"><h2 id="titulo-metodo">Fontes e metodologia</h2></div>
<p>[Explicar de onde vêm os dados (por exemplo, os indicadores criminais da SSP-RS e os registros dos órgãos integrados), com que frequência são atualizados e quem os aprova antes da publicação.]</p>
<p>Os números são apresentados de forma agregada. O Observatório não divulga nomes, endereços, placas nem qualquer dado que permita identificar pessoas.</p>
</div>
<div class="metodologia__lado">
<span class="botao botao--contorno">[Baixar dados (planilha)]</span>
<span class="botao botao--contorno">[Baixar relatório (PDF)]</span>
<p class="caixa-aviso">Este site não recebe ocorrências. Em emergência, ligue <strong>190</strong> (Brigada Militar), <strong>193</strong> (Bombeiros) ou <strong>153</strong> (Guarda Civil Municipal).</p>
</div>
</div>
</section>'''

PRIV = '''<section class="container simples" aria-labelledby="titulo-priv">
<span class="etiqueta">Privacidade</span>
<h1 id="titulo-priv">Aviso de privacidade</h1>
<div class="texto-corrido">
<p>Este site é apenas informativo. Ele não tem formulários, cadastro, login nem área restrita, e não usa cookies, ferramentas de rastreamento ou publicidade.</p>
<p>O servidor que hospeda o site pode registrar dados técnicos de acesso, como endereço IP, data e hora, apenas para segurança e funcionamento, conforme a Lei Geral de Proteção de Dados (Lei nº 13.709/2018) e o Marco Civil da Internet (Lei nº 12.965/2014).</p>
<p>As informações publicadas no Observatório são agregadas e não permitem identificar pessoas.</p>
<h2>Contato</h2>
<p>Dúvidas sobre privacidade: <a href="mailto:ciosp@bage.rs.gov.br">ciosp@bage.rs.gov.br</a>. [Encarregado de dados (DPO) da Prefeitura: nome e contato]</p>
<p>Última atualização: [dd/mm/aaaa].</p>
</div>
</section>'''

ERRO = '''<section class="container simples" aria-labelledby="titulo-erro">
<span class="etiqueta">Erro 404</span>
<h1 id="titulo-erro">Página não encontrada</h1>
<p class="texto-corrido">O endereço pode ter mudado ou não existe. Em caso de emergência, ligue 190 (Brigada Militar) ou 193 (Bombeiros).</p>
<a class="botao botao--escuro" href="index.html">Ir para a página inicial</a>
</section>'''

pagina("index.html", "CIOSP Bagé · Centro Integrado de Operações de Segurança Pública",
       "Centro Integrado de Operações de Segurança Pública de Bagé: notícias, orientações, telefones de emergência e o Observatório da Criminalidade.",
       "index.html", INICIO)
pagina("o-ciosp.html", "O CIOSP · CIOSP Bagé",
       "O que é o CIOSP Bagé e quais instituições atuam de forma integrada na segurança pública do município.", "o-ciosp.html", OCIOSP)
pagina("observatorio.html", "Observatório da Criminalidade · CIOSP Bagé",
       "Indicadores de segurança pública de Bagé, com fonte, período e data de atualização.", "observatorio.html", OBS)
pagina("privacidade.html", "Aviso de privacidade · CIOSP Bagé", "Como o site do CIOSP Bagé trata dados pessoais.", "", PRIV)
pagina("404.html", "Página não encontrada · CIOSP Bagé", "Página não encontrada.", "", ERRO)
# a 404 pode ser servida em qualquer caminho: usa endereços a partir da raiz do site
e=(R/"404.html").read_text(encoding="utf-8")
for a in ['href="assets/','src="assets/','href="favicon.ico','href="index.html','href="o-ciosp.html','href="observatorio.html','href="privacidade.html']:
    e=e.replace(a,a.replace('="','="/',1))
(R/"404.html").write_text(e,encoding="utf-8")
print("ok")
