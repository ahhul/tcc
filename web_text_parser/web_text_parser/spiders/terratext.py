#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy
import os.path
import re


class LinksTerraSpider(scrapy.Spider):

    name = 'terratext'
    global_dpage = 1

    def start_requests(self):
        urls = [ 'http://womenshealthbrasil.com.br/caminhada-para-emagrecer/',
'http://womenshealthbrasil.com.br/coceira-no-anus/',
'http://womenshealthbrasil.com.br/contar-que-tenho-herpes/',
'http://womenshealthbrasil.com.br/tomar-agua-melhora-a-produtividade-no-trabalho/',
'http://womenshealthbrasil.com.br/como-diminuir-os-poros/',
'http://womenshealthbrasil.com.br/prisao-de-ventre/',
'https://www.papodemae.com.br/2019/01/29/importancia-de-ler/',
'https://www.papodemae.com.br/2019/01/29/volta-as-aulas-mochilas-muito-pesadas-podem-prejudicar-o-crescimento/',
'https://www.papodemae.com.br/2019/01/29/o-desenho-e-o-desenvolvimento-infantil/',
'https://www.papodemae.com.br/2019/01/29/volta-as-aulas-atencao-com-os-atropelamentos/',
'https://www.papodemae.com.br/2019/01/29/volta-as-aulas-dar-mesada-pode-gerar-economia/',
'http://womenshealthbrasil.com.br/segunda-sem-carne-receitas/',
'http://womenshealthbrasil.com.br/bebe-quase-morre-apos-contrair-herpes-atraves-de-beijo/',
'http://womenshealthbrasil.com.br/escapes-riviera-maya/',
'http://womenshealthbrasil.com.br/sentir-sono-depois-do-almoco/',
'http://womenshealthbrasil.com.br/ter-mais-energia-ao-longo-do-dia/',
'http://womenshealthbrasil.com.br/consumir-gorduras-faz-bem-para-a-saude/',
'http://womenshealthbrasil.com.br/quanto-tempo-dura-um-cochilo/',
'http://womenshealthbrasil.com.br/vegetais-na-vagina-para-induzir-menstruacao/',
'http://womenshealthbrasil.com.br/mudanca-de-paladar/',
'http://womenshealthbrasil.com.br/congelar-abacate/',
'http://womenshealthbrasil.com.br/treino-para-abdomen/',
'http://womenshealthbrasil.com.br/por-que-o-cerebro-congela-quando-tomamos-sorvete/',
'https://www.papodemae.com.br/2019/01/17/a-revista-autismo-voltou/',
'https://www.papodemae.com.br/2019/01/17/os-primeiros-mil-dias-de-vida-e-saude-bucal-da-gestante-e-bebe/',
'https://www.terra.com.br/vida-e-estilo/mulher/vida-de-mae/reta-final-da-gravidez-tentando-relaxar-ao-maximo,6834f5d51dd61586728db39071ac8e6bukqi5ksy.html',
'http://womenshealthbrasil.com.br/dormir-com-cachorro/',
'http://womenshealthbrasil.com.br/beneficios-da-musica/',
'http://womenshealthbrasil.com.br/unhas-de-acrilico/',
'http://womenshealthbrasil.com.br/menstruacao-livre/',
'http://womenshealthbrasil.com.br/raspagem-vaginal/',
'http://womenshealthbrasil.com.br/ponte-para-empinar-o-bumbum/',
'http://womenshealthbrasil.com.br/condicao-rara-faz-com-que-mulher-nao-consiga-ouvir-homens/',
'http://womenshealthbrasil.com.br/pegar-dst-atraves-do-beijo/',
'https://www.papodemae.com.br/2019/01/04/brinquedo-nao-tem-genero-2/',
'https://www.papodemae.com.br/2019/01/04/crianca-precisa-de-espaco-e-tempo-para-brincadeiras-momento-papo-de-mae/',
'http://womenshealthbrasil.com.br/comer-pizza-sem-prejudicar-a-dieta/',
'http://womenshealthbrasil.com.br/cancer-de-pele-tipo-de-pele/',
'http://womenshealthbrasil.com.br/sintomas-de-herpes-vaginal/',
'http://womenshealthbrasil.com.br/leticia-colin-nutricionista/',
'http://womenshealthbrasil.com.br/candidiase-pode-causar-sintomas-semelhantes-ao-alzheimer/',
'http://womenshealthbrasil.com.br/quantas-calorias-tem-uma-banana/',
'http://womenshealthbrasil.com.br/escapes-ler-um-livro/',
'http://womenshealthbrasil.com.br/leticia-colin-wh-brasil/',
'http://womenshealthbrasil.com.br/absorvente-interno-ficar-preso-dentro-de-voce/',
'http://womenshealthbrasil.com.br/como-perder-5-quilos-sem-mudar-a-dieta/',
'http://womenshealthbrasil.com.br/leite-de-amendoas-bebida-vegetal/',
'http://womenshealthbrasil.com.br/mulher-tem-olhos-colados-e-perde-os-cilios-apos-procedimento/',
'http://womenshealthbrasil.com.br/4-razoes-para-comecar-a-nadar-amanha/',
'https://www.papodemae.com.br/2019/01/04/dicas-de-seguranca-para-as-ferias-das-criancas-momento-papo-de-mae/',
'https://www.papodemae.com.br/2019/01/04/20595/',
'https://www.papodemae.com.br/2019/01/04/menino-ou-menina-muito-alem-do-sexo-de-bebe-obstetra-explica-importancia-do-ultrassom/',
'http://womenshealthbrasil.com.br/e-normal-soltar-muitos-gases/',
'http://womenshealthbrasil.com.br/pior-dormir-fome-comer-tarde-da-noite/',
'http://womenshealthbrasil.com.br/7-dicas-higienizar-calcinha/',
'http://womenshealthbrasil.com.br/quatro-mitos-sobre-o-protetor-solar/',
'http://womenshealthbrasil.com.br/atum-lata-e-saudavel/',
'http://womenshealthbrasil.com.br/3-dicas-para-criar-o-habito-de-malhar-mesmo-que-voce-tenha-zero-vontade/',
'http://womenshealthbrasil.com.br/voce-deve-ficar-enjoada-no-treino/',
'http://womenshealthbrasil.com.br/quanto-tempo-comida-pode-ficar-congelada-sem-estragar/',
'http://womenshealthbrasil.com.br/vontade-de-comer-doce-2/',
'http://womenshealthbrasil.com.br/se-sente-triste-no-natal-e-comum/',
'http://womenshealthbrasil.com.br/mulher-faz-sala-de-cirurgia-pegar-fogo-apos-soltar-gases/',
'http://womenshealthbrasil.com.br/sintomas-de-pedras-nos-rins/',
'http://womenshealthbrasil.com.br/escapes-pedra-azul/',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/o-que-e-a-microtraicao-e-quando-ela-se-transforma-em-traicao-de-verdade,5fb4bd1a3fc9bd05b6f45e19d2b14bbb3nhbyvws.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/a-mulher-que-tirou-a-peruca-e-decidiu-assumir-alopecia-nas-fotos-de-noivado,b94d8d20af366d1bb3441f1f3307127a4y1yzdq7.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/ainda-a-chamo-pelo-nome-masculino-pai-descreve-experiencia-de-ver-filho-de-16-anos-se-tornar-sua-filha,3ad407b2668ac55336e0467ae956d0c95kn1ljdw.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/a-diferenca-entre-flerte-e-assedio-sexual,9d233dbac3ca794f5bb3b74d13313501nurn41wd.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/a-partir-de-uma-peca-de-roupa-ela-despertou-uma-discussao-sobre-assedio-sexual-no-caribe,748e96120f84b3814dd0c5c5054eb6854m4oncn9.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/voce-sabia-por-que-as-mulheres-ficam-mal-humoradas-na-tpm,f681bc706a0e39f20857650d3fa82966d40jmmrq.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/100-vezes-mais-potente-que-cigarro-narguile-vira-moda-entre-jovens-brasileiros-e-acende-alerta-no-governo,d2019aa32f9eb208504da0ec1134e100ph4cb3j8.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/traiu-e-se-arrependeu-veja-o-que-fazer,a08f5860b0e8ca90a6b8c73184e3e01a2kqffwgm.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/dez-dicas-para-seduzir-com-a-roupa,536eebab3eac74f92370f5807915f3a8wq39vzf9.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/dez-coisas-que-ele-espera-de-voce-na-cama,12edb336f7e5b789ab5c8308e90b26219iasapop.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/como-rotulos-ligados-a-maternidade-afetam-a-carreira-de-lideres-politicas,7d1d4165358bf472735283358a95f39evo89qnc2.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/sempre-quis-ser-uma-sereia-o-que-leva-mulheres-a-viver-fantasia-de-personagem-mitica,d1a168b60922361183937d16311c22258pgtm1oy.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/salasocial-torturei-minha-garotinha-durante-anos-diz-mae-sobre-aceitacao-de-filho-transgenero-relato-viralizou,9cba797fc413a8223745c968bf8b9abbpyr4e5k1.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/idosa-de-91-anos-que-trocou-quimioterapia-por-viagem-dos-sonhos-morre-nos-eua,418810d93a41d0977567971b2ca77f0cm9hekr6f.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/como-vicio-em-pornografia-esta-afetando-saude-sexual-de-jovens-britanicos,4ef04bb917bed09bbea5d08e250134b5depp0ive.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/usando-fraldas-e-mamadeiras-jovem-de-21-anos-se-veste-como-bebe,6f2be4310d6d4ab6416447f7b0bfa2dbvy7bdob6.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/artista-que-ja-foi-homem-e-mulher-conta-por-que-agora-tem-genero-neutro,1027afdc681eebcf9f929e501093fc523cm89jl6.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/foto-de-victoria-beckham-gera-debate-online-e-certo-pais-beijarem-os-filhos-nos-labios,35ee14f9a460b0c363d94a3b92171a066hwtqoln.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/quando-visto-meu-jaleco-me-torno-um-sonho-possivel-para-as-criancas-da-favela-diz-estudante-negra-de-medicina,b9b457a21e1f75d055d366a4dce28dacfudwekde.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/11-coisas-que-as-mulheres-nao-aguentam-mais-ouvir-no-brasil-e-por-que,6a47bbc3ee4c0d4286583a5b65ad36eb95ftqoun.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/10-dicas-para-comemorar-o-dia-dos-namorados-sem-gastar-muito,f0a2308ff39252c67c253a991b92c14esnwouz7x.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/apenas-50-das-amizades-sao-reciprocas-aponta-pesquisa,2908de8b3fbfceaf7f977bfe0f98cdf19zjgk25d.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/paquistanesa-solteira-gera-polemica-ao-quebrar-tabu-com-relatos-de-vida-sexual-intensa,13b8eff2b780ebfd3bb913833ef4b586e8geoww1.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/psicologos-revelam-o-motivo-de-beijar-com-os-olhos-fechados,fb4f4c51a81837438141856470d8a83epmculmkw.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/estudo-mulheres-sao-atraidas-por-homens-com-tracos-obscuros,19aeae01aef2d3afea733d53228e9c145y2tqouo.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/a-saudita-negra-com-breve-de-piloto-que-se-tornou-simbolo-na-luta-por-direitos-civis,f1ad54614ececc7659e791559cf5229eiynhvye3.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/imagens-de-objetos-nos-olhos-fazem-sucesso-no-instagram,c6367a46986de8013596f7f388f35d51unhb4jts.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/campanha-de-moda-usa-corpo-de-mulheres-nuas-e-causa-polemica,a770cc7a10fa5f811968a73b54ca244a2tnv9e7v.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/famosas-aparecem-machucadas-em-campanha-sobre-violencia,3df7419f8bd957933b56fdf309b884abrpzt8lte.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/meg-ryan-abraca-envelhecimento-amo-minha-idade,8530a5585735b4f80d1435557986fd03xl5rh8pp.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/pornografia-artista-afirma-que-lagrimas-podem-excitar,ef594701c67aadee53aa23e247bba9bbzwan6ja6.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/emma-watson-e-outras-famosas-abrem-guarda-roupa-para-ajudar-mulheres,71a3f8e2da23d61c4f60ec17dd0cbb9c1v2300t3.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/cantora-trollada-por-gordura-durante-gravidez-enfrenta-abusador-online-em-programa,da71d4ed29a1a0bdbbad04e4e5245c8992eqglls.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/americana-posta-foto-de-autopsias-no-instagram,8848ae06a7de1cb4564dbffc9109ceb36ggrn99t.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/mulheres-conversam-sobre-masturbacao,8241990b96570aa8266dff6dd379c9ecbvi3z0z3.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/despechada-portal-colombiano-faz-sucesso-com-mulheres-desprezadas,40d3178c142f56c5f805cf39a00865e5xr7sqc9k.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/modelo-sofre-por-ter-as-pernas-mais-longas-da-america,e42589ffaec65da02d2a436b2dbbf6290xgzdhfo.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/casal-encurta-distancia-no-globo-atraves-de-fotografias,c93bfc8431b046df31e5d8c18187c127xsvmqe4x.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/facebook-testa-ferramenta-para-evitar-saia-justa-apos-fim-de-relacionamento,1c3905270a8071f2830c8306897476d3lla1wdj0.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/modelo-diz-que-editar-fotos-para-redes-sociais-e-estupido,cc65c79aa6cde59494b2ca60778fe2ddpgl71os1.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/psicologa-explica-como-melhorar-a-autoestima,13e3ffba70791741b2a521d86cea295fvfjrizcy.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/teste-que-tipo-de-mulher-e-voce-no-relacionamento,d48ad80491e4745c31b409b0a5eaea7809uahb1u.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/primeiroassedio-maioria-de-participantes-de-campanha-sofreu-1-abuso-entre-9-e-10-anos,611cdadfd3a69225b31c9aa4cb074be7ist4e4s9.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/blogueira-abandona-instagram-e-luta-contra-redes-sociais,d9dd83c48a075933f84f27d466553a86vk5qjkha.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/assedio-video-flagra-reacao-de-homens-ao-encontrarem-mulher-bebada,7c574c267ef6d15d23089884ec72e6f17q8ph5f2.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/como-o-facebook-sabe-sobre-seus-encontros-no-tinder,bc2a185c5507421af3a9dd161f693346t4dho8n7.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/voce-contaria-a-apple-toda-vez-que-faz-sexo,af19b1437fb63a606999a17e8adf03fes6l3cf83.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/jovem-cria-peticao-contra-app-yik-yak-apos-tentativa-de-suicidio,2a7d0ab1cc2951b28168cd8c0315c132dctvj9ne.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/estresse-causado-por-divorcio-aumenta-risco-de-doencas,53963bbec4b7c47032e496d3f696abebm05fRCRD.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/nudes-criancas-de-8-anos-estariam-trocando-fotos-pelo-celular,7a71e5401dd95113097a29e6d50b51fai69zRCRD.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/mulher-abandona-seus-caes-quando-deixam-de-ser-filhotes,5cd623e050cbcf2d74fd24f676100d45v204RCRD.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/10-coisas-que-acontecem-ao-reencontrar-amigos-da-faculdade,ed216b1d9132545a14ebc13bbf63ea2a0zimRCRD.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/eua-jovem-pede-namorada-em-casamento-mas-derruba-anel-no-mar,731d29eba2c8e7c18bcb260261a47c12m78iRCRD.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/faca-o-teste-e-descubra-qual-o-seu-tipo-de-personalidade,ec6c1f6009b3fce1ab30eaa162b2a05bxh0pRCRD.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/chorar-ajuda-na-sensacao-de-bem-estar-sugere-estudo,b523d523acc0662f204150d37ec3f7b42jzvRCRD.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/o-que-sua-selfie-diz-sobre-sua-personalidade-faca-o-teste,2fad7a59d6ad02db77e6994e75a6e4b2q3kbRCRD.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/falta-de-concentracao-causa-pode-ser-uso-do-smartphone,7eaf176eb0a4b8be7d4121521ca8a3f2ys5fRCRD.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/dor-de-cotovelo-e-mais-forte-mas-mais-curta-para-mulheres-diz-pesquisa,d43e008215846ac71f687c3e0af3357c23h8RCRD.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/quao-distante-voce-esta-do-seu-destino-faca-o-teste,75b76c33267757c1392c43b83b67a79doij7RCRD.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/selfie-no-provador-numero-de-curtidas-ajuda-a-comprar-roupa,276f327ac0cbc9d5e4d3382f0c81b2342bj1RCRD.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/manipulacao-emocional-veja-se-seu-parceiro-e-um-destes-casos,682976f90e411fada9b780b1c44675cdl4boRCRD.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/voce-pratica-a-sororidade-com-outras-mulheres-faca-o-teste,cabf986f277551f037def5b6c2a42d70fd6cRCRD.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/minhocao-recebe-nova-edicao-de-feira-gastronomica-em-sp,9c26e541fe81140c59c00a2bf8f0639e1bdaRCRD.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/festival-de-sopas-do-ceagesp-volta-com-sopa-detox,f4bc9229e9a611132c70acf1ae1f782cc74dRCRD.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/elisa-do-masterchef-reclama-nao-ganhei-por-ser-bonita,adeebcdad53ec410VgnVCM10000098cceb0aRCRD.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/francesa-sucede-brasileira-como-melhor-chef-mulher-do-mundo,aad4c1a7111ec410VgnCLD200000b1bf46d0RCRD.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/brasil-na-cabeca-5-top-drinques-com-ingredientes-nacionais,08598459e1b9c410VgnVCM20000099cceb0aRCRD.html',
'https://www.terra.com.br/vida-e-estilo/mulher/comportamento/sp-restaurante-de-jamie-oliver-tem-massas-a-partir-de-r-19,d0f7c9afe709c410VgnVCM20000099cceb0aRCRD.html',
]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        man = re.compile('homem')
        woman = re.compile('mulher')

        if re.findall("vida-e-estilo/mulher", response.url):
            name_subject = 'mulher_text_' + str(self.global_dpage)
            save_path = 'extracted_texts/terra_mulher'
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
            save_path = 'extracted_texts/terra_mulher'
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
            save_path = 'extracted_texts/terra_mulher'
            file_name = os.path.join(save_path, name_subject)

            title = response.xpath('//div[@class="content-left-wrap"]/h2/text()').extract()[0]
            sentences = response.xpath('//div[@class="content-left-wrap"]/p/text()').extract()

            with open(file_name, 'a') as f:
                f.write('titulo: ' + str(title) + '\n')
                for s in sentences:
                    f.write(str(s))


        if re.findall("vida-e-estilo/homem", response.url):
            name_subject = 'homem_text_' + str(self.global_dpage)
            save_path = 'extracted_texts/terra_homem'
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
            save_path = 'extracted_texts/terra_homem'
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

