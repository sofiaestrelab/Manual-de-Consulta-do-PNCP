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


Exemplo Requisição (cURL)
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash
   :linenos:


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
     - array
     - Lista de Atas de Registro de Preço.
   * - 2
     - numeroControlePNCPAta
     - string
     - Número de controle PNCP da Ata.
   * - 3
     - numeroAtaRegistroPreco
     - Texto (50)
     - Número da Ata no sistema de origem.
   * - 4
     - anoAta
     - inteiro
     - Ano da Ata.
   * - 5
     - numeroControlePncpCompra
     - string
     - Número de controle PNCP da compra.
   * - 6
     - cancelado
     - Booleano
     - Indicador de cancelamento da Ata.
   * - 7
     - dataCancelamento
     - Data
     - Data de cancelamento da Ata. 
   * - 8
     - dataAssinatura
     - Data
     - Data de assinatura da Ata.
   * - 9
     - vigenciaInicio
     - string (date-time)
     - Data de início da vigência da Ata.
   * - 10
     - vigenciaFim
     - string (date-time)
     - Data de término da vigência da Ata.
   * - 11
     - dataPublicacaoPncp
     - string (date-time)
     - Data de publicação no PNCP.
   * - 12
     - dataInclusao
     - string (date-time)
     - Data de inclusão do registro.
   * - 13
     - dataAtualizacao
     - string (date-time)
     - Data de atualização do registro.
   * - 14
     - dataAtualizacaoGlobal
     - string (date-time)
     - Data de atualização global do registro.
   * - 15
     - usuario
     - string
     - Usuário responsável pela operação.
   * - 16
     - objetoContratacao
     - string
     - Objeto da contratação.
   * - 17
     - cnpjOrgao
     - string
     - CNPJ do órgão.
   * - 18
     - nomeOrgao
     - string
     - Nome do órgão.
   * - 19
     - cnpjOrgaoSubrogado
     - string
     - CNPJ do órgão sub-rogado.
   * - 20
     - nomeOrgaoSubrogado
     - string
     - Nome do órgão sub-rogado.
   * - 21
     - codigoUnidadeOrgao
     - string
     - Código da unidade do órgão.
   * - 22
     - nomeUnidadeOrgao
     - string
     - Nome da unidade do órgão.
   * - 23
     - codigoUnidadeOrgaoSubrogado
     - string
     - Código da unidade do órgão sub-rogado.
   * - 24
     - nomeUnidadeOrgaoSubrogado
     - String
     - Nome da unidade do órgão sub-rogado.
   * - 25
     - possibilidadeAdesao
     - Booleano
     - Indicador se a Ata permite adesão de não participantes (False = Não / True = Sim)
  
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
     - application/json
   * - 204
     - Sem conteúdo
     - application/json
   * - 400
     - Pedido ruim
     - application/json
   * - 401
     - Não autorizado
     - string
   * - 422
     - Entidade não processável
     - application/json
   * - 500
     - Erro do Servidor Interno
     - string
