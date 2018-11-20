#-*- coding: utf-8 -*-
import scrapy
import os.path
import re


class TextfolhaspSpider (scrapy.Spider):
    name = 'textfolhasp'
    #allowed_domains = ['www.folha.uol.com.br', 'www1.folha.uol.com.br']
    #start_urls = ['http://www.folha.uol.com.br/']
    handle_httpstatus_list = [302, 301]
    global_links = 1

    def login(self , response):
        data = {
            'email' : 'ludmila.silva@usp.br',
            'pass' : 'Corbomitelog2!',
        }
        yield FormRequest(url=self.login_url, formdata=data ,callback=self.parse)


    def start_requests (self):
        urls = [ 'http://www1.folha.uol.com.br/poder/eleicoes-2016/2016/08/1808438-haddad-diz-que-marta-confunde-opiniao-publica-ao-sugerir-aumento-de-velocidade.shtml',
'http://fotografia.folha.uol.com.br/galerias/42921-isto-e-nuzman#foto-598700',
'http://www1.folha.uol.com.br/paineldoleitor/2016/08/1803745-herois-brasileiros-so-sao-reconhecidos-quando-ganham-medalha-diz-leitor.shtml',
'http://www1.folha.uol.com.br/mercado/2016/08/1803581-projeto-de-teto-de-gasto-federal-enfrenta-resistencia-no-senado.shtml',
'http://www1.folha.uol.com.br/paineldoleitor/2016/08/1801443-duvidas-sobre-olimpiada-sumiram-com-inicio-dos-jogos-diz-leitor.shtml',
'http://www.agora.uol.com.br/brasil/2016/08/1797455-protestos-a-favor-e-contra-o-impeachment-voltam-as-ruas.shtml',
'http://www1.folha.uol.com.br/paineldoleitor/2016/07/1794594-leitor-compara-acao-contra-terrorismo-ao-combate-a-criminalidade-no-pais.shtml',
'http://www1.folha.uol.com.br/mercado/2016/07/1791256-governo-planeja-garantir-autonomia-do-banco-central-ainda-neste-ano.shtml',
'http://www1.folha.uol.com.br/saopaulo/hoje/2016/07/1790576-terca-tem-carlinhos-brown-opera-lady-macbeth-e-mostra-file-de-tecnologia.shtml',
'http://www1.folha.uol.com.br/poder/2016/07/1790372-outro-delator-diz-ter-dado-recurso-de-caixa-2-a-aloysio.shtml',
'http://www1.folha.uol.com.br/poder/2016/07/1789850-pedalada-no-bndes-nao-foi-crime-diz-procurador-do-ministerio-publico-federal.shtml',
'http://www1.folha.uol.com.br/paineldoleitor/2016/07/1789613-lagrimas-de-cunha-nao-o-livrarao-do-julgamento-do-povo-diz-leitor.shtml',
'http://aovivo.folha.uol.com.br/2016/06/10/4852-6-aovivo.shtml#post337250',
'http://www1.folha.uol.com.br/poder/2016/06/1778938-joaquim-barbosa-volta-a-defender-eleicoes-antecipadas.shtml',
'http://www1.folha.uol.com.br/poder/2016/06/1778127-relator-da-lava-jato-teori-e-o-ministro-com-mais-processos-ocultos.shtml',
'http://www1.folha.uol.com.br/poder/2016/05/1776026-audios-de-delator-da-lava-jato-abalam-pmdb-que-adota-cautela.shtml',
'http://www1.folha.uol.com.br/poder/2016/05/1775557-supremo-acaba-com-tramitacao-oculta-de-processos-na-corte.shtml',
'http://aovivo.folha.uol.com.br/2016/05/25/5015-2-aovivo.shtml#post347313',
'http://agoraequesaoelas.blogfolha.uol.com.br/?p=281',
'http://www1.folha.uol.com.br/poder/2016/05/1770637-novo-ministro-do-bolsa-familia-ja-criticou-coleira-politica-do-programa.shtml',
'http://aovivo.folha.uol.com.br/2016/05/11/4788-4-aovivo.shtml#post334551',
'http://www1.folha.uol.com.br/poder/2016/05/1769718-apesar-de-recuo-partidos-tentam-tirar-maranhao-do-comando-da-camara.shtml',
'http://www1.folha.uol.com.br/poder/2016/05/1769502-camara-anulou-rito-do-impeachment-mas-senado-ignorou-entenda-tudo-o-que-aconteceu-nesta-segunda.shtml',
'http://www1.folha.uol.com.br/colunas/marilizpereirajorge/2016/05/1768808-politica-e-o-nosso-esporte-favorito.shtml',
'http://fotografia.folha.uol.com.br/galerias/32089-o-segundo-mandato-de-dilma-rousseff#foto-475523',
'http://baixomanhattan.blogfolha.uol.com.br/?p=4260',
'http://www1.folha.uol.com.br/mundo/2016/04/1762164-brasilianistas-apontam-estresse-da-democracia-mas-elogiam-instituicoes.shtml',
'http://aovivo.folha.uol.com.br/2016/04/16/4714-35-aovivo.shtml#post331388',
'http://www1.folha.uol.com.br/poder/2016/04/1761560-temer-faz-acao-diplomatica-contra-golpe-em-processo-de-impeachment.shtml',
'http://www1.folha.uol.com.br/internacional/en/brazil/2016/04/1761232-to-make-pressure-ex-president-lula-launches-front-in-defense-of-democracy.shtml',
'http://www1.folha.uol.com.br/poder/2016/04/1757067-em-resposta-a-editorial-da-folha-dilma-diz-que-jamais-renunciara.shtml',
'http://www1.folha.uol.com.br/poder/2016/03/1755998-em-portugal-aecio-afirma-que-psdb-pode-apoiar-governo-temer.shtml',
'http://fotografia.folha.uol.com.br/galerias/42661-protestos-contra-nomeacao-de-lula-em-sao-paulo#foto-596113',
'http://www1.folha.uol.com.br/internacional/en/brazil/2016/03/1750957-10000-protest-in-brasilia-over-appointment-of-ex-president-lula-as-chief-of-staff.shtml',
'http://www1.folha.uol.com.br/poder/2016/03/1750808-em-ligacao-a-falcao-lula-discutiu-buscas-da-pf-antes-de-acontecerem.shtml',
'http://fotografia.folha.uol.com.br/galerias/42594-manifestacao-vista-do-alto-pelo-brasil#foto-595094',
'http://fotografia.folha.uol.com.br/galerias/42589-manifestacao-contra-o-governo-politicos#foto-594980',
'http://fotografia.folha.uol.com.br/galerias/42586-manifestacao-contra-o-governo-pelo-brasil#foto-594949',
'http://fotografia.folha.uol.com.br/galerias/42582-manifestacao-contra-o-governo-sao-paulo#foto-594929',
'http://www1.folha.uol.com.br/poder/2016/03/1746563-ato-pro-pt-lota-quadra-de-sindicato-com-mote-nao-vai-ter-golpe.shtml',
'http://www1.folha.uol.com.br/internacional/es/brasil/2016/03/1746217-senador-cita-a-rousseff-y-lula-en-su-delacion-ante-la-justicia.shtml',
'http://www1.folha.uol.com.br/poder/2016/02/1743019-movimentos-sociais-pedem-a-dilma-vetos-a-artigos-da-lei-antiterroristmo.shtml',
'http://f5.folha.uol.com.br/colunistas/renatokramer/2016/02/10000143-amaury-jr-revela-sentir-falta-do-cheiro-de-lanca-perfume-no-carnaval.shtml',
'http://www1.folha.uol.com.br/colunas/raquellandim/2016/02/1736998-a-goleada-dos-pessimistas.shtml',
'http://baixomanhattan.blogfolha.uol.com.br/?p=3790',
'http://www1.folha.uol.com.br/poder/2016/01/1734577-mantega-e-miguel-jorge-deverao-depor-em-acao-da-zelotes-na-semana-que-vem.shtml',
'http://www1.folha.uol.com.br/ciencia/2016/01/1733138-marco-legal-da-ciencia-deixa-duvida-sobre-isencao-de-bolsas-no-brasil.shtml',
'http://www1.folha.uol.com.br/mercado/2015/12/1720615-atividade-economica-inicia-4-tri-com-retracao-pior-que-a-esperada-diz-bc.shtml',
'http://www1.folha.uol.com.br/saopaulo/hoje/2015/12/1718165-ato-pro-impeachment-complica-transito-na-paulista-neste-domingo.shtml',
'http://www1.folha.uol.com.br/paineldoleitor/2015/12/1715329-leitora-critica-incoerencia-da-oposicao-sobre-o-ritmo-do-impeachment.shtml',
'http://www1.folha.uol.com.br/poder/2015/12/1714195-midia-estrangeira-repercute-abertura-de-acao-de-impeachment-de-dilma.shtml',
'http://fotografia.folha.uol.com.br/galerias/40415-repercussao-do-pedido-de-impeachment-de-dilma-rousseff#foto-571183',
'http://www1.folha.uol.com.br/mundo/2015/11/1708418-eventos-como-olimpiada-sao-imas-para-terroristas-diz-especialista.shtml',
'http://f5.folha.uol.com.br/colunistas/renatokramer/2015/11/1707898-depois-de-23-anos-no-jornalismo-mariana-godoy-comemora-sucesso-de-talk-show.shtml',
'http://www1.folha.uol.com.br/poder/2015/11/1705730-dilma-deve-recalibrar-economia-diz-haddad.shtml',
'http://www1.folha.uol.com.br/poder/2015/11/1703344-portugal-suspeita-que-lula-tenha-sido-usado-por-ex-primeiro-ministro-preso.shtml',
'http://www1.folha.uol.com.br/poder/2015/11/1701211-oficialmente-licenciado-irmao-de-palocci-da-expediente-em-estatal.shtml',
'http://www1.folha.uol.com.br/poder/2015/10/1698892-defesa-de-lobista-amigo-de-lula-pede-acesso-a-delacoes-da-lava-jato.shtml',
'http://www1.folha.uol.com.br/saopaulo/hoje/2015/10/1698389-segunda-chuvosa-tem-manifestacao-pelo-impeachment-na-paulista.shtml',
'http://www1.folha.uol.com.br/saopaulo/hoje/2015/10/1695083-segunda-tem-protesto-pelo-impeachment-no-largo-da-batata.shtml',
'http://www1.folha.uol.com.br/fsp/poder/236177-lobista-do-pmdb-diz-que-pagou-despesas-para-filho-de-lula.shtml',
'http://www1.folha.uol.com.br/poder/2015/10/1692524-stf-aprova-delacao-de-fernando-baiano.shtml',
'http://www1.folha.uol.com.br/poder/2015/10/1691649-grupos-anti-dilma-levam-boneco-de-lula-vestido-de-presidiario-ao-rio.shtml',
'http://www1.folha.uol.com.br/fsp/ilustrissima/235275-poder-moderador.shtml',
'http://www1.folha.uol.com.br/colunas/josesimao/2015/10/1688974-dilma-nem-casa-nem-vida.shtml',
'http://www1.folha.uol.com.br/fsp/ilustrada/235060-dilma-nem-casa-nem-vida.shtml',
'http://www1.folha.uol.com.br/ilustrissima/2015/09/1686423-ao-pt-o-que-e-do-pt.shtml',
'http://www1.folha.uol.com.br/fsp/ilustrissima/234472-ao-pt-o-que-e-do-pt.shtml',
'http://www1.folha.uol.com.br/internacional/en/opinion/2015/09/1681357-editorial-roussef-has-her-last-chance-to-save-her-administration.shtml',
'http://www1.folha.uol.com.br/fsp/poder/232395-fora-da-agenda-ministro-da-justica-recebe-anastasia-e-aecio.shtml',
'http://www1.folha.uol.com.br/poder/2015/09/1679138-em-compromisso-fora-da-agenda-cardozo-recebe-anastasia-e-aecio.shtml',
'http://www1.folha.uol.com.br/multimidia/videocasts/2015/08/1671941-se-eleicao-fosse-hoje-rio-nao-seria-escolhido-para-sediar-jogos-assista.shtml',
'http://www1.folha.uol.com.br/fsp/poder/229674-a-xepa-de-feira-de-renan-dilma-e-levy.shtml',
'http://www1.folha.uol.com.br/saopaulo/2015/08/1669070-sph-protesto-pelo-impeachment-de-dilma-fecha-paulista-neste-domingo.shtml',
'http://www1.folha.uol.com.br/saopaulo/2015/08/1667432-sph-quarta-tem-multa-mais-alta-para-quem-trafegar-por-faixa-de-onibus.shtml',
'http://www1.folha.uol.com.br/fsp/esporte/228509-ainda-ha-muito-o-que-fazer-afirma-dilma.shtml',
'http://www1.folha.uol.com.br/fsp/poder/227812-comissao-de-etica-descarta-infracao-de-ex-ministro-da-secom.shtml',
'http://www1.folha.uol.com.br/paineldoleitor/2015/07/1655868-apos-eleicoes-premie-grego-e-dilma-se-renderam-a-austeridade-diz-leitor.shtml',
'http://www1.folha.uol.com.br/fsp/opiniao/226150-painel-do-leitor.shtml',
'http://www1.folha.uol.com.br/colunas/josesimao/2015/07/1655228-pan-com-ovo-ouro-na-porrada.shtml',
'http://www1.folha.uol.com.br/fsp/ilustrada/226029-pan-com-ovo-ouro-na-porrada.shtml',
'http://fotografia.folha.uol.com.br/galerias/36565-imagens-do-dia#foto-528414',
'http://www1.folha.uol.com.br/fsp/poder/224999-planalto-contesta-reportagem-sobre-doleiro.shtml',
'http://classificados.folha.uol.com.br/empregos/2015/06/1647647-em-busca-de-emprego-saiba-que-setores-estao-mais-resilientes-a-crise.shtml',
'http://www1.folha.uol.com.br/poder/2015/06/1645034-stj-recebe-pedido-para-investigar-o-governador-de-mg-fernando-pimentel.shtml',
'http://fotografia.folha.uol.com.br/galerias/14674-dilma-rousseff#foto-256172',
'http://www1.folha.uol.com.br/poder/2015/06/1636294-pela-internet-mulher-de-pimentel-nega-que-empresa-fosse-fantasma.shtml',
'http://www1.folha.uol.com.br/fsp/poder/221073-pf-aponta-suspeitas-sobre-primeira-dama.shtml',
'http://www1.folha.uol.com.br/poder/2015/05/1635892-empresa-da-primeira-dama-de-mg-seria-fantasma-aponta-pf.shtml',
'http://www1.folha.uol.com.br/paineldoleitor/2015/05/1631708-leitores-demonstram-pouca-fe-em-acordos-economicos-com-china.shtml',
'http://www1.folha.uol.com.br/livrariadafolha/2015/05/1625195-veja-lista-de-livros-sobre-marketing-politico.shtml',
'http://www1.folha.uol.com.br/poder/2015/04/1618722-governo-recebeu-detalhes-sobre-lobista.shtml',
'http://www1.folha.uol.com.br/fsp/poder/216682-governo-recebeu-dados-sobre-lobista.shtml',
'http://www1.folha.uol.com.br/paineldoleitor/2015/04/1617207-prisao-de-tesoureiro-do-pt-e-mais-um-tento-do-juiz-sergio-moro-diz-leitor.shtml',
'http://www1.folha.uol.com.br/poder/2015/04/1616017-petrobras-e-sbm-querem-fugir-da-palavra-propina-diz-ex-diretor-da-empresa-holandesa.shtml',
'http://www1.folha.uol.com.br/fsp/poder/215905-petrobras-e-sbm-querem-fugir-da-palavra-propina.shtml',
'http://www1.folha.uol.com.br/fsp/poder/214405-lula-volta-a-criticar-a-conducao-do-governo.shtml',
'http://www1.folha.uol.com.br/paineldoleitor/2015/03/1609440-leitor-diz-que-cotas-para-mulheres-no-congresso-e-afronta-a-democracia.shtml',
'http://www1.folha.uol.com.br/poder/2015/03/1607975-ministro-da-comunicacao-social-deixa-governo.shtml',
'http://www1.folha.uol.com.br/internacional/en/sports/olympicgames/2015/03/1604469-rio-mayor-says-2016-olympics-will-have-bigger-legacy-than-barcelona.shtml',
'http://www1.folha.uol.com.br/fsp/poder/212043-impeachment-nao-vai-adiantar-diz-lider-pro-intervencao-militar.shtml',
'http://www1.folha.uol.com.br/poder/2015/03/1602975-vaccari-nao-tratou-de-financas-com-ex-gerente-diz-pt.shtml',
'http://www.agora.uol.com.br/brasil/2015/03/1603118-documento-reforca-suspeita-de-propina-em-campanha.shtml',
'http://www1.folha.uol.com.br/fsp/poder/211920-vaccari-nao-tratou-de-financas-com-ex-gerente-diz-pt.shtml',
'http://www1.folha.uol.com.br/paineldoleitor/2015/03/1602156-leitores-questionam-ausencia-de-aecio-neves-em-manifestacoes-do-dia-15.shtml',
'http://www1.folha.uol.com.br/paineldoleitor/2015/03/1601539-nao-e-so-a-classe-a-que-esta-insatisfeita-diz-leitor-sobre-governo.shtml',
'http://www1.folha.uol.com.br/colunas/josesimao/2015/03/1600850-ueba-panela-sobe-500.shtml',
'http://www1.folha.uol.com.br/fsp/ilustrada/211312-ueba-panela-sobe-500.shtml',
'http://www1.folha.uol.com.br/fsp/poder/210993-tabela-de-precos-provocava-briga-no-pp-dizem-delatores.shtml',
'http://www1.folha.uol.com.br/mercado/2015/03/1597353-caminhoneiros-protestam-na-rodovia-raposto-tavares-em-sao-paulo.shtml',
'http://www1.folha.uol.com.br/paineldoleitor/2015/02/1592188-leitores-questionam-patrocinio-da-guine-equatorial-a-beija-flor.shtml',
'http://f5.folha.uol.com.br/colunistas/renatokramer/2015/02/1588887-foi-amor-a-segunda-vista-diz-ex-aprendiz-e-namorada-de-roberto-justus.shtml',
'http://www1.folha.uol.com.br/livrariadafolha/2015/02/1587883-veja-lista-de-livros-sobre-marketing-politico.shtml',
'http://www1.folha.uol.com.br/poder/2015/02/1586072-psdb-tera-de-informar-em-quais-cidades-pretende-auditar-as-urnas.shtml',
'http://www1.folha.uol.com.br/fsp/poder/207181-psdb-tera-de-informar-em-quais-cidades-pretende-auditar-as-urnas.shtml',
'http://www1.folha.uol.com.br/fsp/poder/206581-com-casamento-marcado-ministra-katia-abreu-fura-a-fila-de-votacao.shtml',
'http://www1.folha.uol.com.br/poder/2015/02/1583660-suplicy-critica-dilma-em-mensagem-de-despedida-do-senado.shtml',
'http://www1.folha.uol.com.br/fsp/poder/206102-empreiteiro-inclui-ministro-de-dilma-como-testemunha.shtml',
'http://www1.folha.uol.com.br/internacional/en/brazil/2015/01/1581596-rousseff-defends-fiscal-adjustments-and-says-measures-do-not-change-campaign-promises.shtml',
'http://www1.folha.uol.com.br/poder/2015/01/1579160-vice-do-pt-faz-critica-publica-a-politica-economica-de-dilma.shtml',
'http://www1.folha.uol.com.br/fsp/poder/205152-vice-do-pt-faz-critica-publica-a-politica-economica-de-dilma.shtml',
'http://www1.folha.uol.com.br/paineldoleitor/2015/01/1578496-marco-aurelio-garcia-diz-que-dilma-nao-propos-dialogo-com-terroristas.shtml',
'http://www1.folha.uol.com.br/paineldoleitor/2015/01/1575882-e-inaceitavel-que-brasileiro-seja-executado-na-indonesia-diz-leitor.shtml',
'http://www1.folha.uol.com.br/fsp/mundo/203669-embaixador-do-brasil-vai-ao-evento.shtml',
]

        #with open ("extracted_texts/links_folhasp_michel_temer.txt", "r") as f:
        #    urls = f.readlines()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse (self, response):
        save_path = 'extracted_texts/folhasp/dilma_folha/'
        regex_url = re.compile (r'((?:[a-z\d*]+\-)+[a-z\d*]+)')
        text_url = str (response.request.url)
        name_file = re.findall(regex_url, text_url)
        self.log (name_file)
        file_name = 'text_' + name_file.pop()

        f_name = os.path.join (save_path, file_name + ".txt")

        # parser para notícias velhas
        if (response.xpath ('//div[@id="articleNew"]/text()').extract()):

            with open (f_name, 'w') as f:

                text_date = response.xpath ('//div[@id="articleDate"]/text()').re_first(r'\d{2}\/\d{2}\/\d{4}')
                text_body = response.xpath ('//div[@id="articleNew"]/p/text()').extract()
                text_title = response.xpath ('//div[@id="articleNew"]/h1/text()').extract()

                f.write ('url: '+str (text_url)+'\n')
                f.write ('title: ')
                for i in text_title:
                    f.write (i.encode('utf-8'))

                f.write ('\n')
                f.write ('date: '.encode('utf-8') + text_date.encode('utf-8') +'\n')
                self.log (text_date)
                f.write ('text: \n')
                for i in text_body:
                    f.write (i.encode('utf-8'))

        elif (response.xpath('//article[@class="news content article"]/header/h1/text()').extract()):

            with open (f_name, 'w') as f:
                text_date = response.xpath('//meta[@itemprop="datePublished"]/@content').extract()
                text_body = response.xpath('//article[@class="news content article"]/p/text()').extract()
                text_title = response.xpath('//article[@class="new content article"]/header/h1/text()').extract()

                f.write ('url: '+str (text_url)+'\n')
                f.write ('title: ')
                for i in text_title:
                    f.write (i.encode('utf-8'))

                f.write ('\n')
                f.write ('date: '.encode('utf-8') + text_date.encode('utf-8') +'\n')
                self.log (text_date)
                f.write ('text: \n')
                for i in text_body:
                    f.write (i.encode('utf-8'))


        # parser para notícias novas
        elif (response.xpath ('//div["c-news__content"]').extract()):

            with open (f_name, 'w') as f:

                # pega a data
                tag_date = response.xpath ('//time["c-more-options__published-date/datetime"]').extract_first()
                regex_date = re.compile ('\d{4}\-\d{2}\-\d{2}')
                text_date_reverse = regex_date.findall(tag_date).pop()
                text_date = text_date_reverse[8:10] + '/' + text_date_reverse[5:7] + '/' + text_date_reverse[0:4]
                # pega título e texto
                f.write ('url: '+str (text_url)+'\n')
                text_url = str (response.request.url)
                self.log(text_date)
                text_title = response.xpath ('//h1[@class="c-content-head__title"]/text()').extract()
                text_body = response.xpath ('//div[@class="c-news__body"]/p/text()').extract()
                
                text_t = text_title.pop()
                f.write ('title: ' + text_t + '\n')
                self.log(text_t)
                f.write ('date: ' + str (text_date) + '\n')
                self.log (text_date)
                f.write ('text: \n')
                for i in text_body:
                    f.write (str(i))


        self.global_paginas =+ 1

