Serviço de Consultar Atas de Registro de Preço por Dados de Atualização Global
==============================================================================

Serviço responsável por consultar Atas de Registro de Preço por dados de atualização global.

Detalhes de Requisição
~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :width: 100%
   :widths: auto
   :header-rows: 1

   * - Endpoint
     - Método HTTP
   * - /v1/atas
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
     'https://pncp.gov.br/api/consulta/v1/atas?dataInicial=20260101&dataFinal=20260101&idUsuario=3&cnpj=10000000000003&codigoUnidadeAdministrativa=2&pagina=5' \
     -H 'accept: */*'

Dados de entrada
~~~~~~~~~~~~~~~~

.. note::

   Alimentar os parâmetros de consulta ``dataInicial``, ``dadosFinal`` e ``página`` na requisição.

.. list-table::
   :width: 100%
   :widths: 5 10 15 55
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
     - dadosFinal
     - String
     - Sim
     - Data final do período a ser consultado no formato AAAAMMDD.
   * - 3
     - idUsuario
     - Inteiro
     - Não
     - Identificador do sistema usuário (Sistema de Contratações Públicas) que publicou a ata.
   * - 4
     - cnpj
     - String
     - Não
     - CNPJ do órgão originário da contratação informado na inclusão (proprietário da contratação).
   * - 5
     - codigoUnidadeAdministrativa
     - String
     - Não
     - Código da Unidade Administrativa do Órgão originário da contratação informado na inclusão (proprietário da contratação).
   * - 6
     - pagina
     - Inteiro
     - Sim
     - Número da página que se deseja obter os dados.
   * - 7
     - tamanhoPagina
     - Inteiro
     - Não
     - Por padrão cada página contém no máximo 500 registros. O tamanho da página pode ser ajustado (até o limite de 500 registros) para tornar a entrega dos dados mais rápida.

Dados de retorno
~~~~~~~~~~~~~~~~

.. list-table::
   :width: 100%
   :widths: 5 10 15 55
   :header-rows: 1
   :class: quebra-linha-dois-ultima

   * - Id
     - Campo
     - Tipo
     - Descrição
   * - 1
     - data
     - Lista
     - Lista de Atas de Registro de Preço.
   * - 1.1
     - numeroControlePNCPAta
     - String
     - Número de controle PNCP da Ata.
   * - 1.2
     - numeroAtaRegistroPreco
     - Texto (50)
     - Número da Ata no sistema de origem.
   * - 1.3
     - anoAta
     - Inteiro
     - Ano da Ata.
   * - 1.4
     - numeroControlePncpCompra
     - String
     - Número de controle PNCP da compra.
   * - 1.5
     - cancelado
     - Booleano
     - Indicador de cancelamento da Ata.
   * - 1.6
     - dataCancelamento
     - Data
     - Data de cancelamento da Ata.
   * - 1.7
     - dataAssinatura
     - Data
     - Data de assinatura da Ata.
   * - 1.8
     - vigenciaInicio
     - Data
     - Data de início da vigência da Ata.
   * - 1.9
     - vigenciaFim
     - Data
     - Data de término da vigência da Ata.
   * - 1.10
     - dataPublicacaoPncp
     - Data
     - Data da publicação da Ata no PNCP.
   * - 1.11
     - dataInclusao
     - Data
     - Data da inclusão do registro da Ata no PNCP.
   * - 1.12
     - dataAtualizacao
     - Data
     - Data da última atualização do registro da Ata.
   * - 1.13
     - dataAtualizacaoGlobal
     - Data
     - Data da última atualização global do registro da Ata.
   * - 1.14
     - usuario
     - String
     - Nome do sistema usuário (Sistema de Contratações Públicas) que publicou a Ata.
   * - 1.15
     - objetoContratacao
     - String
     - Descrição do objeto referente à Ata.
   * - 1.16
     - cnpjOrgao
     - String
     - CNPJ do órgão referente à Ata.
   * - 1.17
     - nomeOrgao
     - String
     - Razão social do órgão referente à Ata.
   * - 1.18
     - cnpjOrgaoSubrogado
     - String
     - CNPJ do órgão subrogado referente à Ata.
   * - 1.19
     - nomeOrgaoSubrogado
     - String
     - Razão social do órgão subrogado referente à Ata.
   * - 1.20
     - codigoUnidadeOrgao
     - String
     - Código da unidade administrativa do órgão referente à Ata.
   * - 1.21
     - nomeUnidadeOrgao
     - String
     - Nome da unidade administrativa do órgão referente à Ata.
   * - 1.22
     - codigoUnidadeOrgaoSubrogado
     - string
     - Código da unidade administrativa subrogada do órgão subrogado referente à Ata.
   * - 1.23
     - nomeUnidadeOrgaoSubrogado
     - String
     - Nome da unidade administrativa subrogada do órgão subrogado referente à Ata.
   * - 1.24
     - possibilidadeAdesao
     - Booleano
     - Indicador se a Ata permite adesão de não participantes (False = Não / True = Sim).
   * - 2
     - totalRegistros
     - Inteiro
     - Total de registros de Atas encontrados
   * - 3
     - totalPaginas
     - Inteiro
     - Total de páginas.
   * - 4
     - numeroPagina
     - Inteiro
     - Número da página consultada.
   * - 5
     - paginasRestantes
     - Inteiro
     - Quantidade de páginas restantes.
   * - 6
     - empty
     - Booleano
     - Indica se o retorno está vazio.
  
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
