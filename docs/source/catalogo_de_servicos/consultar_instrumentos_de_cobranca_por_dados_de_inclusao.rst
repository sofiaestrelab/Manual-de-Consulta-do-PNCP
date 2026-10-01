Consultar Instrumentos de Cobrança por Dados de Inclusão
=======================================================

Servços de consulta dos Instrumentos de Cobrança por Dados de Inclusão.


Detalhes de Requisição
~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :width: 100%
   :widths: auto
   :header-rows: 1

   * - Endpoint
     - Método HTTP
   * - /v1/instrumentoscobranca/inclusao
     - GET

Exemplo de Payload
~~~~~~~~~~~~~~~~~~

.. code-block:: text
   :linenos:

   Não se aplica.

Exemplo Requisição (cURL)
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash
   :linenos:

   curl -X 'GET' \
     'https://pncp.gov.br/api/consulta/v1/instrumentoscobranca/inclusao?dataInicial=20260101&dataFinal=20260101&pagina=2' \
     -H 'accept: */*'

Dados de entrada
~~~~~~~~~~~~~~~~

.. note::

   Alimentar os parâmetros de consulta da requisição.

.. list-table::
   :width: 100%
   :widths: 5 25 10 15 55
   :header-rows: 1
   :class: quebra-linha-dois-ultima 

   * - Id
     - Campo
     - Tipo
     - Obrigatório
     - Descrição
   * - 1
     - dataInicial
     - string
     - Sim
     - Data inicial do período a ser consultado no formato AAAAMMDD.
   * - 2
     - dataFinal
     - string
     - Sim
     - Data final do período a ser consultado no formato AAAAMMDD.
   * - 3
     - tipoInstrumentoCobranca
     - integer (int64)
     - Não
     - Código do tipo de instrumento de cobrança.
   * - 4
     - cnpjOrgao
     - string
     - Não
     - CNPJ do órgão responsável pelo instrumento de cobrança.
   * - 5
     - pagina
     - integer (int32)
     - Sim
     - Número da página que se deseja obter os dados.
   * - 6
     - tamanhoPagina
     - integer (int32)
     - Não
     - Tamanho da página para retorno dos registros.

Dados de retorno
~~~~~~~~~~~~~~~~

.. list-table::
   :width: 100%
   :widths: 5 25 15 55
   :header-rows: 1
   :class: quebra-linha-dois-ultima 

   * - Id
     - Campo
     - Tipo
     - Descrição
   * - 1
     - data
     - Lista
     - Lista de Instrumentos de Cobrança.
   * - 1.1
     - cnpj
     - Texto
     - CNPJ do órgão responsável pelo instrumento de cobrança.
   * - 1.2
     - ano
     - Inteiro
     - Ano do contrato relacionado ao instrumento de cobrança.
   * - 1.3
     - sequencialContrato
     - Inteiro
     - Sequencial do contrato no PNCP.
   * - 1.4
     - sequencialInstrumentoCobranca
     - Inteiro
     - Sequencial do instrumento de cobrança.
   * - 1.5
     - tipoInstrumentoCobranca
     - Lista
     - Dados do tipo de instrumento de cobrança.
   * - 1.5.1
     - id
     - Inteiro
     - Código do tipo de instrumento de cobrança.
   * - 1.5.2
     - nome
     - Texto
     - Nome do tipo de instrumento de cobrança.
   * - 1.5.3
     - descricao
     - Texto
     - Descrição do tipo de instrumento de cobrança.
   * - 1.5.4
     - dataInclusao
     - Data/Hora
     - Data da inclusão do tipo de instrumento de cobrança.
   * - 1.5.5
     - dataAtualizacao
     - Data/Hora
     - Data da última atualização do tipo de instrumento de cobrança.
   * - 1.5.6
     - statusAtivo
     - Booleano
     - Indicador de status ativo do tipo de instrumento de cobrança.
   * - 1.6
     - numeroInstrumentoCobranca
     - Texto
     - Número do instrumento de cobrança.
   * - 1.7
     - dataEmissaoDocumento
     - Data
     - Data de emissão do documento.
   * - 1.8
     - observacao
     - Texto
     - Observação referente ao instrumento de cobrança.
   * - 1.9
     - chaveNFe
     - Texto
     - Chave da Nota Fiscal Eletrônica.
   * - 1.10
     - fonteNFe
     - Inteiro
     - Código da fonte da Nota Fiscal Eletrônica.
   * - 1.11
     - dataConsultaNFe
     - Data/Hora
     - Data da consulta da Nota Fiscal Eletrônica.
   * - 1.12
     - statusResponseNFe
     - Texto
     - Status da resposta da Nota Fiscal Eletrônica.
   * - 1.13
     - jsonResponseNFe
     - Texto
     - Resposta da consulta da Nota Fiscal Eletrônica em formato JSON.
   * - 1.14
     - notaFiscalEletronica
     - Lista
     - Dados da Nota Fiscal Eletrônica.
   * - 1.14.1
     - instrumentoCobrancaId
     - Inteiro
     - Identificador do instrumento de cobrança relacionado à Nota Fiscal Eletrônica.
   * - 1.14.2
     - chave
     - Texto
     - Chave da Nota Fiscal Eletrônica.
   * - 1.14.3
     - nfTransparenciaID
     - Inteiro
     - Identificador da Nota Fiscal na Transparência.
   * - 1.14.4
     - numero
     - Inteiro
     - Número da Nota Fiscal Eletrônica.
   * - 1.14.5
     - serie
     - Inteiro
     - Série da Nota Fiscal Eletrônica.
   * - 1.14.6
     - dataEmissao
     - Texto
     - Data de emissão da Nota Fiscal Eletrônica.
   * - 1.14.7
     - niEmitente
     - Texto
     - Número de identificação do emitente da Nota Fiscal Eletrônica.
   * - 1.14.8
     - nomeEmitente
     - Texto
     - Nome do emitente da Nota Fiscal Eletrônica.
   * - 1.14.9
     - nomeMunicipioEmitente
     - Texto
     - Nome do município do emitente da Nota Fiscal Eletrônica.
   * - 1.14.10
     - codigoOrgaoDestinatario
     - Texto
     - Código do órgão destinatário da Nota Fiscal Eletrônica.
   * - 1.14.11
     - nomeOrgaoDestinatario
     - Texto
     - Nome do órgão destinatário da Nota Fiscal Eletrônica.
   * - 1.14.12
     - codigoOrgaoSuperiorDestinatario
     - Texto
     - Código do órgão superior destinatário da Nota Fiscal Eletrônica.
   * - 1.14.13
     - nomeOrgaoSuperiorDestinatario
     - Texto
     - Nome do órgão superior destinatário da Nota Fiscal Eletrônica.
   * - 1.14.14
     - valorNotaFiscal
     - Texto
     - Valor da Nota Fiscal Eletrônica.
   * - 1.14.15
     - tipoEventoMaisRecente
     - Texto
     - Tipo do evento mais recente da Nota Fiscal Eletrônica.
   * - 1.14.16
     - dataTipoEventoMaisRecente
     - Texto
     - Data do evento mais recente da Nota Fiscal Eletrônica.
   * - 1.14.17
     - dataInclusao
     - Data/Hora
     - Data da inclusão da Nota Fiscal Eletrônica.
   * - 1.14.18
     - dataAtualizacao
     - Data/Hora
     - Data da última atualização da Nota Fiscal Eletrônica.
   * - 1.14.19
     - itens
     - Lista
     - Lista de itens da Nota Fiscal Eletrônica.
   * - 1.14.19.1
     - numeroItem
     - Texto
     - Número do item da Nota Fiscal Eletrônica.
   * - 1.14.19.2
     - descricaoProdutoServico
     - Texto
     - Descrição do produto ou serviço.
   * - 1.14.19.3
     - codigoNCM
     - Texto
     - Código NCM do produto ou serviço.
   * - 1.14.19.4
     - descricaoNCM
     - Texto
     - Descrição do NCM do produto ou serviço.
   * - 1.14.19.5
     - cfop
     - Texto
     - Código Fiscal de Operações e Prestações (CFOP).
   * - 1.14.19.6
     - quantidade
     - Texto
     - Quantidade do item.
   * - 1.14.19.7
     - unidade
     - Texto
     - Unidade de medida do item.
   * - 1.14.19.8
     - valorUnitario
     - Texto
     - Valor unitário do item.
   * - 1.14.19.9
     - valorTotal
     - Texto
     - Valor total do item.
   * - 1.14.20
     - eventos
     - Lista
     - Lista de eventos da Nota Fiscal Eletrônica.
   * - 1.14.20.1
     - dataEvento
     - Texto
     - Data do evento.
   * - 1.14.20.2
     - tipoEvento
     - Texto
     - Tipo do evento.
   * - 1.14.20.3
     - evento
     - Texto
     - Descrição do evento.
   * - 1.14.20.4
     - motivoEvento
     - Texto
     - Motivo do evento.
   * - 1.15
     - dataInclusao
     - Data/Hora
     - Data da inclusão do instrumento de cobrança.
   * - 1.16
     - dataAtualizacao
     - Data/Hora
     - Data da última atualização do instrumento de cobrança.
   * - 1.17
     - recuperarContratoDTO
     - Lista
     - Dados do contrato relacionado ao instrumento de cobrança.
   * - 1.17.1
     - numeroControlePncpCompra
     - Texto
     - Número de Controle PNCP da contratação.
   * - 1.17.2
     - numeroControlePncpAta
     - Texto
     - Número de Controle PNCP da Ata.
   * - 1.17.3
     - codigoPaisFornecedor
     - Texto
     - Código do país do fornecedor.
   * - 1.17.4
     - anoContrato
     - Inteiro
     - Ano do contrato.
   * - 1.17.5
     - tipoContrato
     - 
     - Dados do tipo de contrato.
   * - 1.17.5.1
     - id
     - Inteiro
     - Código do tipo de contrato.
   * - 1.17.5.2
     - nome
     - Texto
     - Nome do tipo de contrato.
   * - 1.17.6
     - numeroContratoEmpenho
     - Texto
     - Número do contrato ou empenho.
   * - 1.17.7
     - dataAssinatura
     - Data
     - Data de assinatura do contrato.
   * - 1.17.8
     - dataVigenciaInicio
     - Data
     - Data de início da vigência do contrato.
   * - 1.17.9
     - dataVigenciaFim
     - Data
     - Data de término da vigência do contrato.
   * - 1.17.10
     - niFornecedor
     - Texto
     - Número de identificação do fornecedor.
   * - 1.17.11
     - tipoPessoa
     - Texto
     - Tipo de pessoa do fornecedor.
   * - 1.17.12
     - orgaoEntidade
     - Lista
     - Dados do Órgão/Entidade.
   * - 1.17.12.1
     - cnpj
     - Texto
     - CNPJ do Órgão referente à contratação.
   * - 1.17.12.2
     - razaoSocial
     - Texto
     - Razão social do Órgão referente à contratação.
   * - 1.17.12.3
     - poderId
     - Texto
     - Código do poder a que pertence o Órgão. L - Legislativo; E - Executivo; J - Judiciário.
   * - 1.17.12.4
     - esferaId
     - Texto
     - Código da esfera a que pertence o Órgão. F - Federal; E - Estadual; M - Municipal; D - Distrital.
   * - 1.17.13
     - categoriaProcesso
     - Lista
     - Dados da categoria do processo.
   * - 1.17.13.1
     - id
     - Inteiro
     - Código da categoria do processo.
   * - 1.17.13.2
     - nome
     - Texto
     - Nome da categoria do processo.
   * - 1.17.14
     - dataPublicacaoPncp
     - Data/Hora
     - Data da publicação do contrato no PNCP.
   * - 1.17.15
     - dataAtualizacao
     - Data/Hora
     - Data da última atualização do registro do contrato.
   * - 1.17.16
     - sequencialContrato
     - Inteiro
     - Sequencial do contrato no PNCP.
   * - 1.17.17
     - unidadeOrgao
     - Lista
     - Dados da Unidade Administrativa.
   * - 1.17.17.1
     - ufNome
     - Texto
     - Nome da unidade federativa do município.
   * - 1.17.17.2
     - codigoIbge
     - Texto
     - Código IBGE do município.
   * - 1.17.17.3
     - codigoUnidade
     - Texto
     - Código da Unidade Administrativa pertencente ao Órgão.
   * - 1.17.17.4
     - nomeUnidade
     - Texto
     - Nome da Unidade Administrativa pertencente ao Órgão.
   * - 1.17.17.5
     - ufSigla
     - Texto
     - Sigla da unidade federativa do município.
   * - 1.17.17.6
     - municipioNome
     - Texto
     - Nome do município.
   * - 1.17.18
     - informacaoComplementar
     - Texto
     - Informação complementar referente ao contrato.
   * - 1.17.19
     - processo
     - Texto
     - Número do processo de contratação no sistema de origem.
   * - 1.17.20
     - unidadeSubRogada
     - Lista
     - Dados da Unidade Administrativa do Órgão subrogado.
   * - 1.17.20.1
     - ufNome
     - Texto
     - Nome da unidade federativa do município.
   * - 1.17.20.2
     - codigoIbge
     - Texto
     - Código IBGE do município.
   * - 1.17.20.3
     - codigoUnidade
     - Texto
     - Código da Unidade Administrativa pertencente ao Órgão subrogado.
   * - 1.17.20.4
     - nomeUnidade
     - Texto
     - Nome da Unidade Administrativa pertencente ao Órgão subrogado.
   * - 1.17.20.5
     - ufSigla
     - Texto
     - Sigla da unidade federativa do município.
   * - 1.17.20.6
     - municipioNome
     - Texto
     - Nome do município.
   * - 1.17.21
     - orgaoSubRogado
     - Lista
     - Dados do Órgão/Entidade subrogado.
   * - 1.17.21.1
     - cnpj
     - Texto
     - CNPJ do Órgão referente à contratação.
   * - 1.17.21.2
     - razaoSocial
     - Texto
     - Razão social do Órgão referente à contratação.
   * - 1.17.21.3
     - poderId
     - Texto
     - Código do poder a que pertence o Órgão. L - Legislativo; E - Executivo; J - Judiciário.
   * - 1.17.21.4
     - esferaId
     - Texto
     - Código da esfera a que pertence o Órgão. F - Federal; E - Estadual; M - Municipal; D - Distrital.
   * - 1.17.22
     - nomeRazaoSocialFornecedor
     - Texto
     - Nome ou razão social do fornecedor.
   * - 1.17.23
     - niFornecedorSubContratado
     - Texto
     - Número de identificação do fornecedor subcontratado.
   * - 1.17.24
     - nomeFornecedorSubContratado
     - Texto
     - Nome ou razão social do fornecedor subcontratado.
   * - 1.17.25
     - numeroControlePNCP
     - Texto
     - Número de Controle PNCP do contrato.
   * - 1.17.26
     - receita
     - Booleano
     - Indicador de receita.
   * - 1.17.27
     - numeroParcelas
     - Inteiro
     - Número de parcelas do contrato.
   * - 1.17.28
     - numeroRetificacao
     - Inteiro
     - Número da retificação do contrato.
   * - 1.17.29
     - temRemanejamento
     - Booleano
     - Indicador de existência de remanejamento.
   * - 1.17.30
     - emendaParlamentar
     - Booleano
     - Indicador de existência de emenda parlamentar.
   * - 1.17.31
     - frutoAdesao
     - Booleano
     - Indicador de que o contrato é fruto de adesão.
   * - 1.17.32
     - tipoPessoaSubContratada
     - Texto
     - Tipo de pessoa do fornecedor subcontratado.
   * - 1.17.33
     - objetoContrato
     - Texto
     - Descrição do objeto do contrato.
   * - 1.17.34
     - valorInicial
     - Decimal
     - Valor inicial do contrato.
   * - 1.17.35
     - valorParcela
     - Decimal
     - Valor da parcela do contrato.
   * - 1.17.36
     - valorGlobal
     - Decimal
     - Valor global do contrato.
   * - 1.17.37
     - valorAcumulado
     - Decimal
     - Valor acumulado do contrato.
   * - 1.17.38
     - dataAtualizacaoGlobal
     - Data/Hora
     - Data da última atualização global do registro do contrato.
   * - 1.17.39
     - identificadorCipi
     - Texto
     - Identificador do CIPI.
   * - 1.17.40
     - urlCipi
     - Texto
     - URL do CIPI.
   * - 1.17.41
     - usuarioNome
     - Texto
     - Nome do usuário/sistema que enviou o contrato.
   * - 2
     - totalRegistros
     - Inteiro
     - Total de registros encontrados.
   * - 3
     - totalPaginas
     - Inteiro
     - Total de páginas necessárias para a obtenção de todos os registros.
   * - 4
     - numeroPagina
     - Inteiro
     - Número da página em que a consulta foi realizada.
   * - 5
     - paginasRestantes
     - Inteiro
     - Total de páginas restantes.
   * - 6
     - empty
     - Booleano
     - Indicador se o atributo data está vazio.

Códigos de Retorno
~~~~~~~~~~~~~~~~~~
.. list-table::
   :width: 100%
   :widths: auto
   :header-rows: 1

   * - Código HTTP
     - Mensagem
     - Tipo
   * - 200
     - Created
     - Sucesso
   * - 400
     - BadRequest
     - Erro
   * - 422
     - Unprocessable Entity
     - Erro
   * - 500
     - Internal Server Error
     - Erro
