Serviço Consultar Contratações por Data de Publicação
-----------------------------------------------------

Serviço que permite consultar contratações publicadas no PNCP por um período informado. Junto à data inicial e data final informadas deverá ser informado o código da
Modalidade da Contratação (vide tabela XXX). Opcionalmente poderá ser informado código do Modo de Disputa da Contratação (vide tabela XXX), código do IBGE do
Município, sigla da Unidade Federativa da Unidade Administrativa do Órgão, CNPJ do Órgão/Entidade, código da Unidade Administrativa do Órgão/Entidade ou código de
identificação do Usuário (Sistema de Contratações Públicas que publicou a Contratação) para refinar a consulta.

Detalhes de Requisição
~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :width: 100%
   :widths: auto
   :header-rows: 1

   * - Endpoint
     - Método HTTP
   * - /v1/contratacoes/publicacao
     - GET

Exemplo de Payload
~~~~~~~~~~~~~~~~~~

.. code-block:: json
   :linenos:

   Não se aplica

Exemplo Requisição (cURL)
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash
   :linenos:

   curl -X 'GET' \
     'https://pncp.gov.br/api/consulta/v1/contratacoes/publicacao?dataInicial=20230801&dataFinal=20230802&codigoModalidadeContratacao=8&uf=DF&codigoMunicipioIbge=5300108&cnpj=00059311000126&codigoUnidadeAdministrativa=194035&idUsuario=3&pagina=1' \
     -H 'accept: */*'

Dados de entrada
~~~~~~~~~~~~~~~~

.. note::

   Dados a serem enviados no cabeçalho da requisição.

.. list-table::
   :width: 100%
   :widths: auto
   :header-rows: 1

   * - Id
     - Campo
     - Tipo
     - Obrigatório
     - Descrição
   * - 1
     - dataInicial
     - Data
     - Sim
     - Data inicial do período a ser consultado no formato AAAAMMDD.
   * - 2
     - dataFinal
     - Data
     - Sim
     - Data final do período a ser consultado no formato AAAAMMDD.
   * - 3
     - codigoModalidadeContratacao
     - Inteiro
     - Sim
     - Código da tabela de domínio referente à Modalidade da Contratação.
   * - 4
     - codigoModoDisputa
     - Inteiro
     - Não
     - Código da tabela de domínio referente ao Modo de Disputa.
   * - 5
     - uf
     - String
     - Não
     - Sigla da Unidade Federativa referente à Unidade Administrativa do órgão.
   * - 6
     - codigoMunicipioIbge
     - String
     - Não
     - Código IBGE do Município da Unidade Administrativa.
   * - 7
     - cnpj
     - String
     - Não
     - CNPJ do órgão originário da contratação informado na inclusão (proprietário da contratação).
   * - 8
     - codigoUnidadeAdministrativa
     - String
     - Não
     - Código da Unidade Administrativa do Órgão originário da contratação informado na inclusão (proprietário da contratação).
   * - 9
     - idUsuario
     - Inteiro
     - Não
     - Identificador do sistema usuário (Sistema de Contratações Públicas) que publicou a contratação.
   * - 10
     - pagina
     - Inteiro
     - Sim
     - Número da página que se deseja obter os dados.
   * - 11
     - tamanhoPagina
     - Inteiro
     - Não
     - Por padrão cada página contém no máximo 50 registros, no entanto o tamanho de registros em cada página pode ser ajustado (até o limite de 500 registros) com vistas a tornar a entrega de dados mais rápida.

Dados de retorno
~~~~~~~~~~~~~~~~

.. list-table::
   :width: 100%
   :widths: auto
   :header-rows: 1

   * - Id
     - Campo
     - Tipo
     - Descrição
   * - :destaque-amarelo-claro:`1`
     - :destaque-amarelo-claro:`numeroControlePNCP`
     - :destaque-amarelo-claro:`String`
     - :destaque-amarelo-claro:`Número de Controle PNCP da Contratação (id Contratação PNCP)`
   * - 2
     - numeroCompra
     - Texto (50)
     - Número da Contratação no sistema de origem
   * - 3
     - anoCompra
     - Inteiro
     - Ano da Contratação
   * - 4
     - processo
     - Texto (50)
     - Número do processo de Contratação no sistema de origem
   * - 5
     - tipoInstrumentoConvocatorioId
     - Inteiro
     - Código do instrumento convocatório da Contratação
   * - 6
     - tipoInstrumentoConvocatorioNome
     - String
     - Nome do instrumento convocatório da Contratação
   * - 7
     - modalidadeId
     - Inteiro
     - Código da Modalidade referente à Contratação
   * - 8
     - modalidadeNome
     - String
     - Modalidade referente à Contratação
   * - 9
     - modoDisputaId
     - Inteiro
     - Código do modo de disputa referente à Contratação
   * - 10
     - modoDisputaNome
     - String
     - Modo de disputa referente à Contratação
   * - 11
     - situacaoCompraId
     - Inteiro
     - Código da situação da Contratação
   * - 12
     - situacaoCompraNome
     - Inteiro
     - Situação da Contratação
   * - 13
     - objetoCompra
     - Texto (5120)
     - Descrição do Objeto referente à Contratação
   * - 14
     - informacaoComplementar
     - Texto (5120)
     - Informação Complementar do objeto referente à Contratação
   * - 15
     - srp
     - Booleano
     - Identifica se a compra trata-se de um SRP (Sistema de Registro de Preços)
   * - 16
     - amparoLegal
     - Dados
     - Dados do amparo legal
   * - 16.1
     - codigo
     - Inteiro
     - Código do Amparo Legal
   * - 16.2
     - nome
     - String
     - Nome do Amparo Legal
   * - 16.3
     - descricao
     - String
     - Descrição do Amparo Legal
   * - 17
     - valorTotalEstimado
     - Decimal
     - Valor total estimado da Contratação. Precisão de até 4 dígitos decimais; Ex: 100.0001. Obs: retornará valor zero (0) se o atributo ``orcamentoSigiloso`` for ``true`` e o item não possuir resultado.
   * - 18
     - valorTotalHomologado
     - Decimal
     - Valor total homologado com base nos resultados incluídos. Precisão de até 4 dígitos decimais; Ex: 100.0001.
   * - 19
     - dataAberturaProposta
     - Data e Hora
     - Data de abertura do recebimento de propostas (horário de Brasília)
   * - 20
     - dataEncerramentoProposta
     - Data e Hora
     - Data de encerramento do recebimento de propostas (horário de Brasília)
   * - 21
     - dataPublicacaoPncp
     - Data
     - Data da publicação da Contratação no PNCP
   * - 22
     - dataInclusao
     - Data
     - Data da inclusão do registro da Contratação no PNCP
   * - 23
     - dataAtualizacao
     - Data
     - Data da última atualização do registro da Contratação no PNCP
   * - 24
     - sequencialCompra
     - Inteiro
     - Sequencial da Contratação no PNCP; número sequencial gerado no momento em que a contratação foi inserida no PNCP.
   * - 25
     - orgaoEntidade
     - Dados
     - Dados do Órgão/Entidade
   * - 25.1
     - cnpj
     - String
     - CNPJ do Órgão referente à Contratação
   * - 25.2
     - razaosocial
     - String
     - Razão social do Órgão referente à Contratação
   * - 25.3
     - poderId
     - String
     - Código do poder a que pertence o Órgão. L - Legislativo; E - Executivo; J - Judiciário
   * - 25.4
     - esferaId
     - String
     - Código da esfera a que pertence o Órgão. F - Federal; E - Estadual; M - Municipal; D - Distrital
   * - 26
     - unidadeOrgao
     - Dados
     - Dados da Unidade Administrativa
   * - 26.1
     - codigoUnidade
     - String
     - Código da Unidade Administrativa pertencente ao Órgão
   * - 26.2
     - nomeUnidade
     - String
     - Nome da Unidade Administrativa pertencente ao Órgão
   * - 26.3
     - codigoIbge
     - Inteiro
     - Código IBGE do município
   * - 26.4
     - municipioNome
     - String
     - Nome do município
   * - 26.5
     - ufSigla
     - String
     - Sigla da unidade federativa do município
   * - 26.6
     - ufNome
     - String
     - Nome da unidade federativa do município
   * - 27
     - orgaoSubRogado
     - Dados
     - Dados do Órgão/Entidade subrogado
   * - 28.1
     - cnpj
     - String
     - CNPJ do Órgão referente à Contratação
   * - 28.2
     - razaosocial
     - String
     - Razão social do Órgão referente à Contratação
   * - 28.3
     - poderId
     - String
     - Código do poder a que pertence o Órgão. L - Legislativo; E - Executivo; J - Judiciário
   * - 28.4
     - esferaId
     - String
     - Código da esfera a que pertence o Órgão. F - Federal; E - Estadual; M - Municipal; D - Distrital
   * - 29
     - unidadeSubRogada
     - Dados
     - Dados da Unidade Administrativa do Órgão subrogado
   * - 29.1
     - codigoUnidade
     - String
     - Código da Unidade Administrativa pertencente ao Órgão subrogado
   * - 29.2
     - nomeUnidade
     - String
     - Nome da Unidade Administrativa pertencente ao Órgão subrogado
   * - 29.3
     - codigoIbge
     - Inteiro
     - Código IBGE do município
   * - 29.4
     - municipioNome
     - String
     - Nome do município
   * - 29.5
     - ufSigla
     - String
     - Sigla da unidade federativa do município
   * - 29.6
     - ufNome
     - String
     - Nome da unidade federativa do município
   * - 30
     - usuarioNome
     - String
     - Nome do Usuário/Sistema que enviou a Contratação
   * - 31
     - linkSistemaOrigem
     - String
     - URL para página/portal do sistema de origem da contratação para recebimento de propostas.
   * - 32
     - justificativaPresencial
     - String
     - Justificativa pela escolha da modalidade presencial.

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
     - OK
     - Sucesso
   * - 204
     - No Content
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