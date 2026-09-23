Consultar Contratações por Dados de Atualização Global
======================================================

Serviços de Consultar Contratações por Dados de Atualização Global no PNCP.

Detalhes de Requisição
~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :width: 100%
   :widths: auto
   :header-rows: 1

   * - Endpoint
     - Método HTTP
   * - /v1/contratacoes/atualizacao
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
     'https://pncp.gov.br/api/consulta/v1/contratacoes/atualizacao?dataInicial=20260101&dataFinal=20260101&codigoModalidadeContratacao=2&pagina=3' \
     -H 'accept: */*'

Dados de entrada
~~~~~~~~~~~~~~~~

.. note::

   Alimentar os parâmetros de consulta da requisição.

.. list-table::
   :width: 100%
   :widths: 5 25 15 55
   :header-rows: 1
   :class: quebra-linha-dois-ultima 

   * - Id
     - Campo
     - Tipo
     - Obrigatório
     - Descrição
   * - 1
     - dataInicial
     - String
     - Sim
     - Data inicial do período a ser consultado no formato AAAAMMDD.
   * - 2
     - dataFinal
     - String
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
     - Cnpj do órgão originário da contratação informado na inclusão (proprietário da contratação).
   * - 8
     - codigoUnidadeAdministrativa
     - String
     - Não
     - Código da Unidade Administrativa do Órgão originário da contratação informado na inclusão (proprietário da contratação).
   * - 9
     - idUsuario
     - Inteiro
     - Não
     - Identificado do sistema usuário (Sistema de Contratações Públicas) que publicou a contratação.
   * - 10
     - pagina
     - Inteiro
     - Sim
     - Número da página que se deseja obter os dados.
   * - 11
     - tamanhoPagina
     - Inteiro
     - Não
     - Por padrão cada página contém no máximo 500 registros, no entanto o tamanho de registros em cada página pode ser ajustado (até o limite de 500 registros) com vistas a tornar a entrega de dados mais rápida.

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
     - Lista com os dados das contratações encontradas.
   * - 1.1
     - valorTotalHomologado
     - Decimal
     - Valor total homologado com base nos resultados incluídos. Precisão de até 4 dígitos decimais; Ex: 100.0001.
   * - 1.2
     - dataAberturaProposta
     - Data/Hora
     - Data de abertura do recebimento de propostas (horário de Brasília).
   * - 1.3
     - informacaoComplementar
     - Texto
     - Informação Complementar do objeto referente à Contratação.
   * - 1.4
     - processo
     - Texto
     - Número do processo de Contratação no sistema de origem.
   * - 1.5
     - objetoCompra
     - Texto
     - Descrição do Objeto referente à Contratação.
   * - 1.6
     - linkSistemaOrigem
     - Texto
     - URL para página/portal do sistema de origem da contratação para recebimento de propostas.
   * - 1.7
     - justificativaPresencial
     - Texto
     - Justificativa pela escolha da modalidade presencial.
   * - 1.8
     - unidadeSubRogada
     - Lista
     - Dados da unidade administrativa subrogada.
   * - 1.8.1
     - ufNome
     - Texto
     - Nome da unidade federativa do município.
   * - 1.8.2
     - ufSigla
     - Texto
     - Sigla da unidade federativa do município.
   * - 1.8.3
     - municipioNome
     - Texto
     - Nome do município.
   * - 1.8.4
     - codigoUnidade
     - Texto
     - Código da Unidade Administrativa pertencente ao Órgão subrogado.
   * - 1.8.5
     - nomeUnidade
     - Texto
     - Nome da Unidade Administrativa pertencente ao Órgão subrogado.
   * - 1.8.6
     - codigoIbge
     - Texto
     - Código IBGE do município.
   * - 1.9
     - orgaoSubRogado
     - Lista
     - Dados do órgão/entidade subrogado.
   * - 1.9.1
     - cnpj
     - Texto
     - CNPJ do Órgão referente à Contratação.
   * - 1.9.2
     - esferaId
     - Texto
     - Código da esfera a que pertence o Órgão. F - Federal; E - Estadual; M - Municipal; D - Distrital.
   * - 1.9.3
     - razaoSocial
     - Texto
     - Razão social do Órgão referente à Contratação.
   * - 1.9.4
     - poderId
     - Texto
     - Código do poder a que pertence o Órgão. L - Legislativo; E - Executivo; J - Judiciário.
   * - 1.10
     - amparoLegal
     - Lista
     - Dados do amparo legal.
   * - 1.10.1
     - codigo
     - Inteiro
     - Código do Amparo Legal.
   * - 1.10.2
     - descricao
     - Texto
     - Descrição do Amparo legal.
   * - 1.10.3
     - nome
     - Texto
     - Nome do Amparo Legal.
   * - 1.11
     - dataEncerramentoProposta
     - Data/Hora
     - Data de encerramento do recebimento de propostas (horário de Brasília).
   * - 1.12
     - srp
     - Booleano
     - Identifica se a compra trata-se de um SRP (Sistema de registro de preços).
   * - 1.13
     - orgaoEntidade
     - Lista
     - Dados do órgão/entidade.
   * - 1.13.1
     - cnpj
     - Texto
     - CNPJ do Órgão referente à Contratação.
   * - 1.13.2
     - esferaId
     - Texto
     - Código da esfera a que pertence o Órgão. F - Federal; E - Estadual; M - Municipal; D - Distrital.
   * - 1.13.3
     - razaoSocial
     - Texto
     - Razão social do Órgão referente à Contratação.
   * - 1.13.4
     - poderId
     - Texto
     - Código do poder a que pertence o Órgão. L - Legislativo; E - Executivo; J - Judiciário.
   * - 1.14
     - anoCompra
     - Inteiro
     - Ano da Contratação.
   * - 1.15
     - sequencialCompra
     - Inteiro
     - Sequencial da Contratação no PNCP; Número sequencial gerado no momento que a contratação foi inserida no PNCP.
   * - 1.16
     - dataInclusao
     - Data/Hora
     - Data da inclusão do registro da Contratação no PNCP.
   * - 1.17
     - dataPublicacaoPncp
     - Data/Hora
     - Data da publicação da Contratação no PNCP.
   * - 1.18
     - dataAtualizacao
     - Data/Hora
     - Data da última atualização do registro da Contratação.
   * - 1.19
     - numeroCompra
     - Texto
     - Número da Contratação no sistema de origem.
   * - 1.20
     - unidadeOrgao
     - Lista
     - Dados da unidade administrativa.
   * - 1.20.1
     - ufNome
     - Texto
     - Nome da unidade federativa do município.
   * - 1.20.2
     - ufSigla
     - Texto
     - Sigla da unidade federativa do município.
   * - 1.20.3
     - municipioNome
     - Texto
     - Nome do município.
   * - 1.20.4
     - codigoUnidade
     - Texto
     - Código da Unidade Administrativa pertencente ao Órgão.
   * - 1.20.5
     - nomeUnidade
     - Texto
     - Nome da Unidade Administrativa pertencente ao Órgão.
   * - 1.20.6
     - codigoIbge
     - Texto
     - Código IBGE do município.
   * - 1.21
     - modoDisputaId
     - Inteiro
     - Código do modo de disputa referente à Contratação.
   * - 1.22
     - emendaParlamentar
     - Booleano
     - Marcador de existência de emenda parlamentar na contratação.
   * - 1.23
     - numeroControlePNCP
     - Texto
     - Número de Controle PNCP da Contratação (id Contratação PNCP).
   * - 1.24
     - modalidadeId
     - Inteiro
     - Código da Modalidade referente à Contratação.
   * - 1.25
     - linkProcessoEletronico
     - Texto
     - URL para página do sistema de controle de processos eletrônicos com os dados do processo desta contratação.
   * - 1.26
     - dataAtualizacaoGlobal
     - Data/Hora
     - Data da última atualização global do registro da Contratação considerando seus dependentes (item da contratação, resultado da contratação, documento da contratação e imagem de item da contratação).
   * - 1.27
     - valorTotalEstimado
     - Decimal
     - Valor total estimado da Contratação. Precisão de até 4 dígitos decimais; Ex: 100.0001; Obs: Retornará valor zero (0) se atributo orcamentoSigiloso for true e o item não possuir resultado.
   * - 1.28
     - modalidadeNome
     - Texto
     - Modalidade referente à Contratação.
   * - 1.29
     - modoDisputaNome
     - Texto
     - Modo de disputa referente à Contratação.
   * - 1.30
     - tipoInstrumentoConvocatorioCodigo
     - Inteiro
     - Código do instrumento convocatório da Contratação.
   * - 1.31
     - tipoInstrumentoConvocatorioNome
     - Texto
     - Nome do instrumento convocatório da Contratação.
   * - 1.32
     - fontesOrcamentarias
     - Lista
     - Lista de fontes orçamentárias da contratação.
   * - 1.32.1
     - codigo
     - Inteiro
     - Código da fonte orçamentária.
   * - 1.32.2
     - nome
     - Texto
     - Nome da fonte orçamentária.
   * - 1.32.3
     - descricao
     - Texto
     - Descrição da fonte orçamentária.
   * - 1.32.4
     - dataInclusao
     - Data/Hora
     - Data/hora da inclusão da fonte orçamentária na contratação.
   * - 1.33
     - situacaoCompraId
     - Texto
     - Código da situação da Contratação.
   * - 1.34
     - situacaoCompraNome
     - Texto
     - Situação da Contratação.
   * - 1.35
     - usuarioNome
     - Texto
     - Nome do Usuário/Sistema que enviou a Contratação.
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
     - Número da página que a consulta foi realizada.
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
     - OK
     - Sucesso
   * - 204
     - No Content
     - Sucesso
   * - 400
     - Bad Request
     - Erro
   * - 422
     - Unprocessable Entity
     - Erro
   * - 500
     - Internal Server Error
     - Erro
