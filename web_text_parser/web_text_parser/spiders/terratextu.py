#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy
import os.path
import re


class LinksTerraUnissexSpider(scrapy.Spider):

    name = 'terratextu'
    global_dpage = 1

    def start_requests(self):
        urls = [ 'https://www.terra.com.br/vida-e-estilo/culinaria/guia-da-cozinha/doce-napolitano,cf471c90f588eacc346a15dd6a085c44if9uz86m.html',
'https://www.terra.com.br/vida-e-estilo/culinaria/videos/como-fazer-um-vegeta-negroni,8830113.html',
'https://aparecidaliberato.com.br/datas-especiais/2019-ano-novo-chines-o-ano-do-porco/',
'https://www.terra.com.br/vida-e-estilo/moda/elas-no-tapete-vermelho/anitta-grava-clipe-de-bola-rebola-com-adesivo-de-mamilo,c78c9876d43c29a6539bca8f482f5817tmive151.html',
'https://www.terra.com.br/vida-e-estilo/turismo/tumba-de-tutancamon-e-reaberta-apos-uma-decada-de-reparos,066bddb6bbca0d533880ba54d11cd6dbyykwqww4.html',
'https://www.terra.com.br/diversao/gente/purepeople/conheca-o-tratamento-de-juliana-paes-para-fazer-o-abdomen-colar-ate-o-carnaval,cf588813a9fb6740c5db797689438c56g90ikcxa.html',
'https://www.terra.com.br/vida-e-estilo/culinaria/guia-da-cozinha/flan-de-doce-de-leite,1e1fdc0b99dd77588fe4325c11c5587adgvxo3fy.html',
'https://www.terra.com.br/vida-e-estilo/culinaria/guia-da-cozinha/tranca-doce,b208b9df9536dcf4ffee607fe80f83e64pvtwmhb.html',
'https://www.revistamenu.com.br/2019/02/01/gastronomia-brasileira-mobilizada-em-prol-das-vitimas-de-brumadinho/',
'https://chickenorpasta.com.br/2019/fru-to-a-revolucao-comeca-e-termina-pela-boca/',
'https://www.terra.com.br/vida-e-estilo/moda/elas-no-tapete-vermelho/de-cleo-a-hickmann-qual-famosa-ficou-mais-estilosa-de-neon,ccaf0445457943b4ad921ac4c4ddc633al7nkd86.html',
'https://www.terra.com.br/vida-e-estilo/culinaria/guia-da-cozinha/arroz-de-forno-com-legumes,4538f61bd9130675101880516c4e6b85cjxhyjqu.html',
'https://www.terra.com.br/vida-e-estilo/culinaria/guia-da-cozinha/paozinho-de-creme,77bcd652442b8f34971fcf09f8f37370j3xt3vky.html',
'https://www.terra.com.br/vida-e-estilo/culinaria/guia-da-cozinha/lanchinho-de-pao-de-queijo-recheado,95141038ffdb5039a12f97fd731398cax8siidcr.html',
'https://www.terra.com.br/vida-e-estilo/culinaria/guia-da-cozinha/torta-pao-de-queijo,a4c8b1daca24d080f2fd64fe7e7c953ct7dp1yjt.html',
'https://www.terra.com.br/vida-e-estilo/culinaria/tudogostoso/linguica-de-soja-vegana-como-fazer,da014b7407083ddf87f6ce8eeb5d459d7cnzispc.html',
'https://www.areah.com.br/vibe/comportamento/materia/76474/1/pagina_1/15-sinais-de-que-voce-e-narcisista.aspx',
'https://www.terra.com.br/vida-e-estilo/horoscopo/astrologia/astrologia-o-que-o-ceu-do-mes-mostra-para-fevereiro,fdb5eb42350157d5509b7c8b4b19a89b2nqz1k6u.html',
'http://blogdamimis.com.br/2019/02/01/remedios-caseiros-para-sinusite/',
'https://chickenorpasta.com.br/2019/podcast-jogo-do-cop-10-tendencias-no-viagens-2019/',
'https://www.revistamenu.com.br/2019/02/01/hotel-fasano-punta-del-leste-recebe-henrique-fogaca-para-tarde-de-assados/',
'https://thesummerhunter.com/julio-secchin-musica-carnaval-rio-de-janeiro/',
'https://www.terra.com.br/vida-e-estilo/saude/tapioca-e-mocinha-ou-vila-da-dieta,a1853dfee638e5eda1066453860c956ataphb7ge.html',
'https://www.terra.com.br/vida-e-estilo/saude/neofobia-alimentar-dicas-para-superar-o-problema,3d4fd64e7b90c26bb8cc64f6577b23dcafpxy9zg.html',
'https://fortissima.com.br/2019/02/01/curtinho-moderno-especialistas-dao-dicas-para-cuidar-do-cabelo-pixie-14834162/?utm_source=terra&utm_medium=homepageTerra&utm_campaign=feedterra',
'https://www.terra.com.br/vida-e-estilo/saude/risco-de-difteria-no-pais-aumenta-e-saude-solicita-envio-de-tratamentos,f6a59e45772bece041a7a50f052c383ebhn949or.html',
'https://www.selecoes.com.br/economia/10-cursos-online-gratuitos/?origem=terra',
'https://www.selecoes.com.br/superdicas/6-usos-inusitados-para-a-farinha-de-trigo/?origem=terra',
'https://www.revistamenu.com.br/2019/01/31/festa-da-uva-de-jundiai-oferece-vivencia-na-fabricacao-de-vinhos/',
'https://awebic.com/alma/coragem/',
'https://www.terra.com.br/vida-e-estilo/saude/resistencia-a-acao-contra-dengue-leva-a-denuncias-por-crime-no-interior-de-sp,e252749824f554d5f351a69a0708c0f452c3fkem.html',
'https://www.selecoes.com.br/saude/cirurgia-bariatrica-indicacao-e-riscos/?origem=terra',
'http://womenshealthbrasil.com.br/caminhada-para-emagrecer/',
'https://www.terra.com.br/vida-e-estilo/minha-vida/washington-declara-estado-de-emergencia-devido-a-surto-de-sarampo,0e188a8680689c2eaa35d11cc90feaf43lc4ogs6.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/marido-da-cantora-americana-pink-ensina-filha-de-7-anos-a-atirar-com-arma-de-fogo,82e9d4b1b13fdf689cc42d38a407264bwmu9j5y3.html',
'https://www.terra.com.br/vida-e-estilo/minha-vida/o-que-dar-para-meu-bebe-comer-cartilha-da-dicas-ate-2-anos,4c632aa8c2e8dbbf0c512bd523577923e19fal1t.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/outback-lanca-tres-opcoes-de-lanches-vegetarianos-em-todo-o-brasil,7405c7cb9b39a340bd03610dd40ab86f8b7zntaq.html',
'https://www.terra.com.br/vida-e-estilo/culinaria/guia-da-cozinha/mousse-de-pessego-manga-e-maracuja,8566938a5f8a22d028ad74dc8e7ead095jps50el.html',
'https://www.terra.com.br/vida-e-estilo/saude/bem-estar/sport-life/excesso-de-proteinas-e-um-potencial-risco-para-os-rins-entenda,dc53b56c4312aa7d32f945392f4c3b9brge6oaqn.html',
'https://chickenorpasta.com.br/2019/eataly-monta-um-beer-garden-junto-com-a-colorado-e-a-wals/',
'https://www.areah.com.br/vibe/comportamento/materia/202111/1/pagina_1/6-principais-motivos-pelas-quais-as-mulheres-fingem-orgasmo.aspx',
'https://www.terra.com.br/vida-e-estilo/culinaria/guia-da-cozinha/receitas-sem-gluten-saudavel-sem-deixar-o-sabor-de-lado,c597266da53276322242877b7102794b90wrqulx.html',
'https://www.terra.com.br/vida-e-estilo/saude/bem-estar/oleo-de-melaleuca-veja-os-beneficios-para-beleza-e-saude,2bd774b9ee199883d6b9a1e5e428bea8otwart3s.html',
'https://www.terra.com.br/vida-e-estilo/saude/bem-estar/sport-life/6-motivos-para-sair-do-sofa-e-comecar-a-treinar-hoje-mesmo,a2ab0b74f43d12b04a13548553f520ads3dpzv80.html',
'https://www.areah.com.br/vip/viagem/materia/198505/1/pagina_1/7-destinos-gastronomicos-para-casais.aspx',
'https://www.terra.com.br/vida-e-estilo/casa-e-decoracao/viva-decora/divisorias-com-cobogo-faca-voce-mesmo,3a0c1f3006dde145afc65d2b53648c63vfderpfr.html',
'https://www.terra.com.br/vida-e-estilo/casa-e-decoracao/viva-decora/piso-ceramico-conheca-os-tipos-e-saiba-escolher-50-modelos,92ba103f0f852af4089d95c1ad309d6d6cxr923l.html',
'https://www.terra.com.br/vida-e-estilo/casa-e-decoracao/viva-decora/bolo-de-casamento-simples-saiba-como-escolher-67-modelos-lindos,72b546df8cf524a6a2bb1d8dbca4857a9hs72tbs.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/documentario-acompanha-viagem-de-moto-de-claude-troisgros-pelo-brasil,8591a5f5dfe74013eef1789a90587fd2jnhy65z5.html',
'https://www.terra.com.br/vida-e-estilo/culinaria/tudogostoso/como-fazer-casquinha-de-sorvete-confira-as-dicas-e-2-receitas,2dd4f2c1c2e5d13033ce60f1a6172ccd4q7nrje0.html',
'http://womenshealthbrasil.com.br/coceira-no-anus/',
'https://www.terra.com.br/vida-e-estilo/casa-e-decoracao/viva-decora/mini-jardim-50-modelos-criativos-de-terrarios-para-voce-se-inspirar,124bcdd45e593d18771d3e78956b9a6c2fr0gu7a.html',
'https://www.areah.com.br/vibe/entretenimento/materia/201724/1/pagina_1/12-mortes-mais-marcantes-de-game-of-thrones.aspx',
'https://www.terra.com.br/vida-e-estilo/comportamento/sobe-para-57-o-numero-de-animais-resgatados-em-brumadinho-mg,fa39b40acdc1f1ba867538c3071b3c15rdqxsiet.html',
'https://www.terra.com.br/vida-e-estilo/minha-vida/surto-de-hantavirus-ja-matou-11-pessoas-na-argentina-diz-oms,68fdfa34365ab0fff941f753e99dd48dj6chunti.html',
'https://www.selecoes.com.br/humor/truques-e-humor-com-gabriel-louchard-no-dia-do-magico/?origem=terra',
'https://www.areah.com.br/vip/estilo/materia/170578/1/pagina_1/o-terno-ideal-para-cada-corpo.aspx',
'https://www.terra.com.br/vida-e-estilo/moda/elas-no-tapete-vermelho/larissa-manoela-veste-jeans-e-neon-para-comemorar-18-anos,b4051a131d4ba165c94b791842c8778486dmuia2.html',
'https://www.terra.com.br/vida-e-estilo/culinaria/guia-da-cozinha/paozinho-integral-com-maca-e-canela,867d9bc2082920de518bdae251ea60b34rzjj7e1.html',
'https://www.terra.com.br/vida-e-estilo/culinaria/guia-da-cozinha/pave-de-danoninho,9989f3f850360e7edb70240034861cb7s674c88u.html',
'https://www.terra.com.br/vida-e-estilo/culinaria/guia-da-cozinha/bolo-de-chocolate-sem-gluten-e-sem-lactose,cb7d8d5af09967be2bdbd2267ac3fdff3ekh6ayu.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/rotulo-de-cerveja-tera-ilustracao-de-cao-que-foi-morto-no-carrefour-renda-ira-para-ongs,bdce842defe371f2c28498e0d9cb1473vs8ua6eu.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/bebe-rouba-a-cena-em-ensaio-de-casamento-dos-pais-ao-tentar-mamar,30a1d73e44039ffbbc862c01ec5425a30yjgiejm.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/marido-da-cantora-americana-pink-ensina-filha-de-7-anos-a-atirar-com-arma-de-fogo,82e9d4b1b13fdf689cc42d38a407264bwmu9j5y3.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/outback-lanca-tres-opcoes-de-lanches-vegetarianos-em-todo-o-brasil,7405c7cb9b39a340bd03610dd40ab86f8b7zntaq.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/documentario-acompanha-viagem-de-moto-de-claude-troisgros-pelo-brasil,8591a5f5dfe74013eef1789a90587fd2jnhy65z5.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/sobe-para-57-o-numero-de-animais-resgatados-em-brumadinho-mg,fa39b40acdc1f1ba867538c3071b3c15rdqxsiet.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/rotulo-de-cerveja-tera-ilustracao-de-cao-que-foi-morto-no-carrefour-renda-ira-para-ongs,bdce842defe371f2c28498e0d9cb1473vs8ua6eu.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/bebe-rouba-a-cena-em-ensaio-de-casamento-dos-pais-ao-tentar-mamar,30a1d73e44039ffbbc862c01ec5425a30yjgiejm.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/sp-ganhara-casa-cheetos-com-exposicao-de-tazos-e-menu-especial,2ce95fee4446fd90583b2bfb03d007d74jjyeo7c.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/marvel-autoriza-que-fa-em-estado-terminal-assista-vingadores-4-antes-da-estreia,4a91a347c23e3f2d201dc457a77efb74l9vt4n2i.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/menino-de-5-anos-comemora-fim-do-tratamento-do-cancer-dancando-michael-jackson-assista,e83eba5288bde82cc7d9b8591bc5228awu76qzip.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/eutanasia-com-tiros-em-animais-em-brumadinho-foi-tecnica-diz-conselho-veterinario,8e9517d4dd600a732a8c5a1c755db570jbi8vflj.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/narizinho-de-monteiro-lobato-ganha-ilustracoes-de-mauricio-de-sousa-em-novo-livro,b921ac8d268fe6ba4723ea1421f3a603k6bsm2pj.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/conheca-a-cadela-que-vai-buscar-pao-sozinha-na-padaria,b12b79f6a7568b7fa5567b564834051evcwyzg44.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/dar-leite-para-cachorro-pode-causar-problemas-intestinais-e-no-pancreas,5db557f97c82bbc93417afb16f7200f3yssbvg5e.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/homem-diz-que-apoio-emocional-de-jacare-o-ajudou-durante-depressao,b792d52b3012feeb36b3d887341a39621tdp1e33.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/cachorro-que-nasceu-com-as-patas-viradas-para-cima-passa-por-cirurgia-para-andar,72777e4a71f68dbaa874d91aececd70frv0q2i7b.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/animais-domesticos-poderao-ser-transportados-no-metro-de-sao-paulo,3c68dc8cf46067c528a8e1d0f28e88eatpcvhv4x.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/conheca-cinco-lendas-urbanas-horripilantes-de-sao-paulo,294e41d1e9edd83fb5d379dbf935d299vo0zj5rw.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/conheca-os-shoppings-e-outros-lugares-mais-visitados-em-sao-paulo,0388633af2a294d78a152c552495cef0rkaph469.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/conheca-aplicativos-que-te-ajudam-a-cumprir-metas-e-objetivos,2d89cfd2aabfab47a8b59044ed0b62ae7znkg4p0.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/viagem-de-ferias-com-bebe-necessita-de-planejamento-antecipado,eec08265ba52a2f15c247bd1a2dc9da0s9ne2cg2.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/dia-mais-triste-do-ano-e-nesta-segunda-feira-diz-pesquisas,8c3d8645a8cafd258ab0bf512cf35a7a998ngjto.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/aos-113-anos-de-idade-morre-homem-mais-velho-do-mundo-no-japao,56391c736871fcde4e007a3e3398f4f54qwzp1rq.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/miss-rio-de-janeiro-tera-primeira-candidata-transexual-em-2019,0fbfb3529284a24cf298330fe6d164ddibzfatzn.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/serie-you-exposicao-da-vida-pessoal-na-internet-alimenta-desejo-de-stalkear,0df746c8c143d3fc2212b1948710620ev03wl3iu.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/resiliencia-deve-levar-em-consideracao-o-tipo-de-trauma-sofrido,a34e8a0a231e4ab0579793f910d76716i8q1jysx.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/viaje-mas-nao-deixe-seu-pet-sozinho-saiba-por-que,4789be9a5f176783f5efd10b449ec0c5lewc9wln.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/por-que-fazer-fofoca-nem-sempre-e-sempre-e-algo-ruim,4e67bf0aa90a5c54bcbf1273512257acwvp2auz4.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/jovem-se-envolve-em-acidente-ao-fazer-desafio-de-bird-box-nos-eua,8cf5b3df49dc058283c6c7343c8a49bekii34bns.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/shopping-distribuira-canudos-reutilizaveis-para-clientes-nesta-sexta,0f6b6c2108efb4ff58c2cbb29c6c3dc2tus3m7kb.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/loja-de-noivas-coloca-manequim-em-cadeira-de-rodas-na-inglaterra,cad1fb23d07e12d50d92c2eda9a5161au3tigbvo.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/filhotes-de-tigre-branco-em-zoologico-no-brasil-sao-mostrados-ao-publico,d59abf9ec008fbf9da7a7d5aff025338dxnxk2zq.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/aos-nove-anos-brasileiro-faz-vaquinha-online-para-estudar-bale-no-bolshoi,0f484f3ea686c819fa40472a520443cfe06l67tb.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/indonesia-censura-cena-de-beijo-de-aquaman-segundo-fas-do-filme,3b675fde623505aedf246c00387144c7bmsy53mx.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/os-nomes-de-cachorros-mais-comuns-em-2018-foram-thor-e-mel,0ad0c48c6e2fd0e9cde0f58ff952cd4b2lk6jd73.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/menina-da-agua-que-virou-meme-estrela-campanha-publicitaria,7d6cb2e1cbc2a935b73fb2b74320ee6aa49pqm87.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/casal-de-idosos-joga-mario-kart-diariamente-para-ver-quem-fara-cha,c2e79de83192d3ea25bde6feddf3bfe16s82v5w7.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/pais-de-alunos-promovem-troca-de-material-usado-para-volta-as-aulas,2362725a0bd755c144de0dfba1bcc7687cv49i8v.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/projeto-do-sesc-mostra-musica-instrumental-em-estilos-como-rock-percussao-e-eletronica,9045124ac846fa19a2db71bb5f71d4a3h9knxrpj.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/internautas-compartilham-desafio-bird-box-e-netflix-se-pronuncia,718a23dcb8309d23536ccca707e4a32dhwn19iqf.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/cachorros-aguardam-por-morador-de-rua-que-foi-internado-em-hospital-no-parana,389d534eed8bb279d1e544af24d0d92cyplowb7r.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/mp-quer-que-google-derrube-conteudo-de-youtubers-mirins-sobre-brinquedos,a47162056d9ac5952be58526c88fbc03jx07nk7c.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/vizinho-aciona-policia-apos-ouvir-ameacas-de-morte-contra-aranha,acff46485fb54a193ba5c754825d3a22ruq8366i.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/cadela-morre-apos-queima-de-fogos-no-rio-de-janeiro,8e5816da7f35f92e0c2d08a907983353x3fwdf3u.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/volta-as-aulas-aos-90-anos-os-idosos-brasileiros-que-decidiram-ir-a-faculdade,96ac4ac4c9a971dfa3611ccbe84f9a4dq3sc05ad.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/mulher-relata-que-policial-pagou-lanche-para-menino-que-fazia-malabares-na-rua,42f8ec17630f34bffedfc4973d8b62377hyuc9dc.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/cinco-dicas-para-conseguir-cumprir-resolucoes-de-ano-novo,aa24f88c74e9692b3a2d4d4ab9b1f4c641ejy16d.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/a-historia-do-gay-solteiro-que-adotou-bebe-com-sindrome-de-down-rejeitado-por-20-familias,ac2443180e1b970a67838b3822f89f91vn9p3lqt.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/caixa-de-supermercado-paga-conta-de-cliente-que-nao-tinha-dinheiro,0a158a7ceb78aa0eef4e7e13888b0196o7u2vwuy.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/homem-manda-matar-cachorros-apos-divorcio-mas-pets-sao-resgatados-por-ong,278ccbb8602d47c28ac32113062e8631qmhdnpkb.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/enzo-gabriel-e-o-nome-mais-registrado-no-brasil-em-2018,2b313576f9b6a2d7c8f3a88699b8b442xlf28a6w.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/conheca-finn-o-boi-de-estimacao-que-vive-dentro-de-casa-com-dois-cachorros,92b726b886e6dbd55336ad4a9b0173ad7ff6smxg.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/cadela-ganha-filhote-de-presente-e-emociona-internautas-assista,850db6aa06bea4ddf06671a79bfcde060kqb9q2h.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/1-natal-em-casa-a-historia-da-familia-que-adotou6-irmaos-de-uma-so-vez-e-agora-tem-22-filhos,b176210fa156038fd34e4015d6654af9ssnr9lip.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/indianos-usam-whatsapp-para-salvar-tradicoes,28dda78d1fcee7a0c68c861b204069ea1fgo98uu.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/como-sobreviver-ao-jantar-com-a-familia-no-natal-pos-eleicoes-as-dicas-de-um-especialista-em-resolucao-de-conflitos,8b2081549b4ab575714dea8f71a71dabomq4dd2o.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/saiba-como-reduzir-o-estresse-dos-pets-em-datas-festivas,d2b381c694c9e90800ad2563bfca3849h49yi0es.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/brincadeiras-off-line-durante-as-ferias-pais-buscam-alternativas-para-tirar-criancas-dos-eletronico,f2acdc698b3691b5e1d770e2690bf2108cdwil61.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/filha-interpreta-letras-de-musicas-para-pai-surdo-durante-show,157b885d8e8ccfb14ae12dcaa478e9b606htldip.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/bicho-preguica-resgatado-no-rio-de-janeiro-faz-sucesso-em-rede-social,5a208f9a7d10014ed3963a27f13340e6qrsgkzfb.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/assistente-do-google-sugere-atos-de-gentileza-para-usuarios,69f27d6f3410a50393df758ae3491a2500ks5zrt.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/mulher-da-a-luz-durante-voo-com-ajuda-do-marido-e-da-tripulacao,c3495ab9f804ed9333f338cca26a9761c6mqszmz.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/como-transportar-animais-de-estimacao-em-seguranca-durante-passeios-e-viagens,3cac23335b30cbf85e8a6b75a52334behhhgz2uq.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/mulher-faz-decoracao-natalina-com-dragoes-e-vizinhos-associam-a-culto-demoniaco,b187b8ae47fc5bd7ed7274d651160c98ebjhdgvb.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/presentear-com-animais-de-estimacao-pode-ser-uma-boa-opcao,ac6b3463582610495b46df36b34cde329q088i62.html',
'https://www.terra.com.br/vida-e-estilo/comportamento/tata-werneck-e-paolla-oliveira-denunciam-morte-de-cadela-a-pauladas-no-rio-de-janeiro,5f3d46243f84e0b6730a8d8a1d15f56dgaehhm4c.html',
'',
]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        if re.findall("vida-e-estilo/mulher", response.url):
            name_subject = 'mulher_text_' + str(self.global_dpage)
            save_path = 'extracted_texts/terra_unissex_clean'
            file_name = os.path.join(save_path, name_subject)

            title = \
                response.xpath('//h1[@class="entry-title"]/text()').extract()
            sentences = response.xpath('//p/text()').extract()

            with open(file_name, 'a') as f:
                f.write('titulo: ' + str(title) + '\n')
                if response.xpath('//div[@class="subtitle subtitle--M"]/h2/text()'
                                  ):
                    subtitle = \
                        response.xpath('//div[@class="subtitle subtitle--M"]/h2/text()'
                            ).extract()[0]
                    f.write('subtitulo: ' + str(subtitle) + '\n')
                for s in sentences:
                    f.write(str(s))

        if re.findall('womenshealthbrasil', response.url):
            name_subject = 'mulher_text_' + str(self.global_dpage)
            save_path = 'extracted_texts/terra_unissex_clean'
            file_name = os.path.join(save_path, name_subject)

            title = \
                response.xpath('//h1[@class="entry-title"]/text()').extract()[0]

            sentences = response.xpath('//div[@class="td-post-content"]/p/text()').extract()

            with open(file_name, 'a') as f:
                f.write('titulo: ' + str(title) + '\n')
                for s in sentences:
                    f.write(str(s))

        if re.findall('papodemae', response.url):
            name_subject = 'mulher_text_' + str(self.global_dpage)
            save_path = 'extracted_texts/terra_unissex_clean'
            file_name = os.path.join(save_path, name_subject)

            title = response.xpath('//div[@class="content-left-wrap"]/h2/text()').extract()[0]
            sentences = response.xpath('//div[@class="content-left-wrap"]/p/text()').extract()

            with open(file_name, 'a') as f:
                f.write('titulo: ' + str(title) + '\n')
                for s in sentences:
                    f.write(str(s))


        if re.findall("vida-e-estilo/homem", response.url):
            name_subject = 'homem_text_' + str(self.global_dpage)
            save_path = 'extracted_texts/terra_unissex_clean'
            file_name = os.path.join(save_path, name_subject)

            title = \
                response.xpath('//div[@class="title headline"]/h1/text()'
                               ).extract()[0]
            sentences = response.xpath('//p/text()').extract()

            with open(file_name, 'a') as f:
                f.write('titulo: ' + str(title) + '\n')
                if response.xpath('//div[@class="subtitle subtitle--M"]/h2/text()'
                                  ):
                    subtitle = \
                        response.xpath('//div[@class="subtitle subtitle--M"]/h2/text()'
                            ).extract()[0]
                    f.write('subtitulo: ' + str(subtitle) + '\n')
                for s in sentences:
                    f.write(str(s))

        if re.findall('areah', response.url):
            name_subject = 'homem_text_' + str(self.global_dpage)
            save_path = 'extracted_texts/terra_unissex_clean'
            file_name = os.path.join(save_path, name_subject)

            title = response.xpath('//h1[@itemprop="name"]/text()'
                                   ).extract()[0]

            sentences = \
                response.xpath('//div[@class="content-main sa_incontent"]/div/text()'
                               ).extract()

            with open(file_name, 'a') as f:
                f.write('titulo: ' + str(title) + '\n')
                if response.xpath('//div[@class="col_descricao"]/h2/text()'
                                  ):
                    subtitle = \
                        response.xpath('//div[@class="col_descricao"]/h2/text()'
                            ).extract()[0]
                    f.write('subtitulo: ' + str(subtitle) + '\n')
                for s in sentences:
                    f.write(str(s))


        regexdig = re.compile(r"D=\d+")
        self.global_dpage += 1
        sr_str = 'D=' + str(self.global_dpage)
        next_page = re.sub(regexdig, sr_str, response.url)
        self.log('\n' + str(next_page))
        self.log('''''' + str(self.global_dpage) + '''''')
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
