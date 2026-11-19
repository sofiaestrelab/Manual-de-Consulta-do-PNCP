Consultar Atas de Registro de Preço por Data de Atualização Global
==================================================================

Serviço destinado à consulta das Atas que foram incluídas ou que sofreram alterações no PNCP durante um determinado intervalo de datas, considerando a data de atualização global do registro.

Detalhes de Requisição
~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :width: 100%
   :widths: auto
   :header-rows: 1

   * - Endpoint
     - Método HTTP
   * - /v1/atas/atualizacao
     - GET

Exemplo de Payload
~~~~~~~~~~~~~~~~~~

.. code-block:: text
   :linenos:
   :emphasize-lines: 1

   Não se aplica.

Exemplo Requisição (cURL)
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash
   :linenos:
   :emphasize-lines: 1-3

   curl -X 'GET' \
     'https://pncp.gov.br/api/consulta/v1/atas/atualizacao?dataInicial=20260101&dataFinal=20260101&pagina=2' \
     -H 'accept: */*'

Dados de entrada
~~~~~~~~~~~~~~~~

.. note::

   Alimentar os parâmetros de consulta ``{dataInicial}``, ``{dataFinal}`` e ``{pagina}`` na requisição.

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
   * - :destaque-amarelo-claro:`1`
     - :destaque-amarelo-claro:`dataInicial`
     - :destaque-amarelo-claro:`String`
     - :destaque-amarelo-claro:`Sim`
     - :destaque-amarelo-claro:`Data inicial do período a ser consultado no formato AAAAMMDD.`
   * - :destaque-amarelo-claro:`2`
     - :destaque-amarelo-claro:`dadosFinal`
     - :destaque-amarelo-claro:`String`
     - :destaque-amarelo-claro:`Sim`
     - :destaque-amarelo-claro:`Data final do período a ser consultado no formato AAAAMMDD.`
   * - :destaque-amarelo-claro:`3`
     - :destaque-amarelo-claro:`idUsuario`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Não`
     - :destaque-amarelo-claro:`Identificador do sistema usuário (Sistema de Contratações Públicas) que publicou a ata.`
   * - :destaque-amarelo-claro:`4`
     - :destaque-amarelo-claro:`cnpj`
     - :destaque-amarelo-claro:`String`
     - :destaque-amarelo-claro:`Não`
     - :destaque-amarelo-claro:`CNPJ do órgão originário da contratação informado na inclusão (proprietário da contratação).`
   * - :destaque-amarelo-claro:`5`
     - :destaque-amarelo-claro:`codigoUnidadeAdministrativa`
     - :destaque-amarelo-claro:`String`
     - :destaque-amarelo-claro:`Não`
     - :destaque-amarelo-claro:`Código da Unidade Administrativa do Órgão originário da contratação informado na inclusão (proprietário da contratação).`
   * - :destaque-amarelo-claro:`6`
     - :destaque-amarelo-claro:`pagina`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Sim`
     - :destaque-amarelo-claro:`Número da página que se deseja obter os dados.`
   * - :destaque-amarelo-claro:`7`
     - :destaque-amarelo-claro:`tamanhoPagina`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Não`
     - :destaque-amarelo-claro:`Por padrão cada página contém no máximo 500 registros. O tamanho da página pode ser ajustado (até o limite de 500 registros) para tornar a entrega dos dados mais rápida.`

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
   * - :destaque-amarelo-claro:`1`
     - :destaque-amarelo-claro:`data`
     - :destaque-amarelo-claro:`Lista`
     - :destaque-amarelo-claro:`Lista de Atas de Registro de Preço.`
   * - :destaque-amarelo-claro:`1.1`
     - :destaque-amarelo-claro:`numeroControlePNCPAta`
     - :destaque-amarelo-claro:`String`
     - :destaque-amarelo-claro:`Número de controle PNCP da Ata.`
   * - :destaque-amarelo-claro:`1.2`
     - :destaque-amarelo-claro:`numeroAtaRegistroPreco`
     - :destaque-amarelo-claro:`Texto (50)`
     - :destaque-amarelo-claro:`Número da Ata no sistema de origem.`
   * - :destaque-amarelo-claro:`1.3`
     - :destaque-amarelo-claro:`anoAta`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Ano da Ata.`
   * - :destaque-amarelo-claro:`1.4`
     - :destaque-amarelo-claro:`numeroControlePncpCompra`
     - :destaque-amarelo-claro:`String`
     - :destaque-amarelo-claro:`Número de controle PNCP da compra.`
   * - :destaque-amarelo-claro:`1.5`
     - :destaque-amarelo-claro:`cancelado`
     - :destaque-amarelo-claro:`Booleano`
     - :destaque-amarelo-claro:`Indicador de cancelamento da Ata.`
   * - :destaque-amarelo-claro:`1.6`
     - :destaque-amarelo-claro:`dataCancelamento`
     - :destaque-amarelo-claro:`Data`
     - :destaque-amarelo-claro:`Data de cancelamento da Ata.`
   * - :destaque-amarelo-claro:`1.7`
     - :destaque-amarelo-claro:`dataAssinatura`
     - :destaque-amarelo-claro:`Data`
     - :destaque-amarelo-claro:`Data de assinatura da Ata.`
   * - :destaque-amarelo-claro:`1.8`
     - :destaque-amarelo-claro:`vigenciaInicio`
     - :destaque-amarelo-claro:`Data`
     - :destaque-amarelo-claro:`Data de início da vigência da Ata.`
   * - :destaque-amarelo-claro:`1.9`
     - :destaque-amarelo-claro:`vigenciaFim`
     - :destaque-amarelo-claro:`Data`
     - :destaque-amarelo-claro:`Data de término da vigência da Ata.`
   * - :destaque-amarelo-claro:`1.10`
     - :destaque-amarelo-claro:`dataPublicacaoPncp`
     - :destaque-amarelo-claro:`Data`
     - :destaque-amarelo-claro:`Data da publicação da Ata no PNCP.`
   * - :destaque-amarelo-claro:`1.11`
     - :destaque-amarelo-claro:`dataInclusao`
     - :destaque-amarelo-claro:`Data`
     - :destaque-amarelo-claro:`Data da inclusão do registro da Ata no PNCP.`
   * - :destaque-amarelo-claro:`1.12`
     - :destaque-amarelo-claro:`dataAtualizacao`
     - :destaque-amarelo-claro:`Data`
     - :destaque-amarelo-claro:`Data da última atualização do registro da Ata.`
   * - :destaque-amarelo-claro:`1.13`
     - :destaque-amarelo-claro:`dataAtualizacaoGlobal`
     - :destaque-amarelo-claro:`Data`
     - :destaque-amarelo-claro:`Data da última atualização global do registro da Ata.`
   * - :destaque-amarelo-claro:`1.14`
     - :destaque-amarelo-claro:`usuario`
     - :destaque-amarelo-claro:`String`
     - :destaque-amarelo-claro:`Nome do sistema usuário (Sistema de Contratações Públicas) que publicou a Ata.`
   * - :destaque-amarelo-claro:`1.15`
     - :destaque-amarelo-claro:`objetoContratacao`
     - :destaque-amarelo-claro:`String`
     - :destaque-amarelo-claro:`Descrição do objeto referente à Ata.`
   * - :destaque-amarelo-claro:`1.16`
     - :destaque-amarelo-claro:`cnpjOrgao`
     - :destaque-amarelo-claro:`String`
     - :destaque-amarelo-claro:`CNPJ do órgão referente à Ata.`
   * - :destaque-amarelo-claro:`1.17`
     - :destaque-amarelo-claro:`nomeOrgao`
     - :destaque-amarelo-claro:`String`
     - :destaque-amarelo-claro:`Razão social do órgão referente à Ata.`
   * - :destaque-amarelo-claro:`1.18`
     - :destaque-amarelo-claro:`cnpjOrgaoSubrogado`
     - :destaque-amarelo-claro:`String`
     - :destaque-amarelo-claro:`CNPJ do órgão subrogado referente à Ata.`
   * - :destaque-amarelo-claro:`1.19`
     - :destaque-amarelo-claro:`nomeOrgaoSubrogado`
     - :destaque-amarelo-claro:`String`
     - :destaque-amarelo-claro:`Razão social do órgão subrogado referente à Ata.`
   * - :destaque-amarelo-claro:`1.20`
     - :destaque-amarelo-claro:`codigoUnidadeOrgao`
     - :destaque-amarelo-claro:`String`
     - :destaque-amarelo-claro:`Código da unidade administrativa do órgão referente à Ata.`
   * - :destaque-amarelo-claro:`1.21`
     - :destaque-amarelo-claro:`nomeUnidadeOrgao`
     - :destaque-amarelo-claro:`String`
     - :destaque-amarelo-claro:`Nome da unidade administrativa do órgão referente à Ata.`
   * - :destaque-amarelo-claro:`1.22`
     - :destaque-amarelo-claro:`codigoUnidadeOrgaoSubrogado`
     - :destaque-amarelo-claro:`string`
     - :destaque-amarelo-claro:`Código da unidade administrativa subrogada do órgão subrogado referente à Ata.`
   * - :destaque-amarelo-claro:`1.23`
     - :destaque-amarelo-claro:`nomeUnidadeOrgaoSubrogado`
     - :destaque-amarelo-claro:`String`
     - :destaque-amarelo-claro:`Nome da unidade administrativa subrogada do órgão subrogado referente à Ata.`
   * - :destaque-amarelo-claro:`1.24`
     - :destaque-amarelo-claro:`possibilidadeAdesao`
     - :destaque-amarelo-claro:`Booleano`
     - :destaque-amarelo-claro:`Indicador se a Ata permite adesão de não participantes (False = Não / True = Sim).`
   * - :destaque-amarelo-claro:`2`
     - :destaque-amarelo-claro:`totalRegistros`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Total de registros de Atas encontrados.`
   * - :destaque-amarelo-claro:`3`
     - :destaque-amarelo-claro:`totalPaginas`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Total de páginas.`
   * - :destaque-amarelo-claro:`4`
     - :destaque-amarelo-claro:`numeroPagina`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Número da página consultada.`
   * - :destaque-amarelo-claro:`5`
     - :destaque-amarelo-claro:`paginasRestantes`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Quantidade de páginas restantes.`
   * - :destaque-amarelo-claro:`6`
     - :destaque-amarelo-claro:`empty`
     - :destaque-amarelo-claro:`Booleano`
     - :destaque-amarelo-claro:`Indica se o retorno está vazio.`

Códigos de Retorno
~~~~~~~~~~~~~~~~~~

.. list-table::
   :width: 100%
   :widths: auto
   :header-rows: 1

   * - Código HTTP
     - Mensagem
     - Tipo
   * - :destaque-amarelo-claro:`200`
     - :destaque-amarelo-claro:`OK`
     - :destaque-amarelo-claro:`Sucesso`
   * - :destaque-amarelo-claro:`204`
     - :destaque-amarelo-claro:`No Content`
     - :destaque-amarelo-claro:`Sucesso`
   * - :destaque-amarelo-claro:`400`
     - :destaque-amarelo-claro:`Bad Request`
     - :destaque-amarelo-claro:`Erro`
   * - :destaque-amarelo-claro:`422`
     - :destaque-amarelo-claro:`Unprocessable Entity`
     - :destaque-amarelo-claro:`Erro`
   * - :destaque-amarelo-claro:`500`
     - :destaque-amarelo-claro:`Internal Server Error`
     - :destaque-amarelo-claro:`Erro`
