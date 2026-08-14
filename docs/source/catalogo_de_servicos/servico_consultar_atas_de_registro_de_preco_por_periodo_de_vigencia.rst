6.5. Serviço Consultar Atas de Registro de Preço por Período de Vigência
------------------------------------------------------------------------

Serviço que permite consultar Atas de Registro de Preços publicadas no PNCP por um período informado.

A partir da data inicial e da data final informadas, serão recuperadas as atas cujo período de vigência coincida com o período informado. Opcionalmente poderá ser informado o CNPJ do Órgão/Entidade, o código da Unidade Administrativa do Órgão/Entidade ou o número de identificação do usuário (Portais de Contratações Públicas).

Detalhes da Requisição
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

.. code-block:: json
   :linenos:

   Não se aplica

Exemplo de Requisição (cURL)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash
   :linenos:

   curl -X 'GET' \
     '${BASE_URL}/v1/atas?dataInicial=20230701&dataFinal=20230831&pagina=1' \
     -H 'accept: */*'

Ou:

.. code-block:: bash
   :linenos:

   curl -X 'GET' \
     '${BASE_URL}/v1/atas?dataInicial=20231024&dataFinal=20241023&idUsuario=36&cnpjOrgao=00394429000100&pagina=1' \
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
     - idUsuario
     - Inteiro
     - Não
     - Identificador do sistema usuário (Sistema de Contratações Públicas) que publicou a ata.
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
   :widths: auto
   :header-rows: 1

   * - Id
     - Campo
     - Tipo
     - Descrição
   * - 1
     - Atas
     - Agrupador
     - Agrupador da lista de atas
   * - :destaque-amarelo-claro:`1.1`
     - :destaque-amarelo-claro:`numeroControlePNCPAta`
     - :destaque-amarelo-claro:`String`
     - :destaque-amarelo-claro:`Número de Controle PNCP da Ata (id Ata PNCP)`
   * - 1.2
     - numeroControlePNCPCompra
     - String
     - Número de Controle PNCP da Contratação (id Contratação PNCP) que a ata está vinculada
   * - 1.3
     - numeroAtaRegistroPreco
     - Texto (50)
     - Número da Ata no sistema de origem
   * - 1.4
     - anoAta
     - Inteiro
     - Ano da Ata
   * - 1.5
     - dataAssinatura
     - Data
     - Data de assinatura da Ata
   * - 1.6
     - vigenciaInicio
     - Data
     - Data de início de vigência da Ata
   * - 1.7
     - vigenciaFim
     - Data
     - Data de fim de vigência da Ata
   * - 1.8
     - dataCancelamento
     - Data
     - Data de cancelamento da Ata
   * - 1.9
     - cancelado
     - Booleano
     - Indicador de cancelamento da Ata
   * - 1.10
     - dataPublicacaoPncp
     - Data
     - Data da publicação da Ata no PNCP
   * - 1.11
     - dataInclusao
     - Data
     - Data da inclusão do registro da Ata no PNCP
   * - 1.12
     - dataAtualizacao
     - Data
     - Data da última atualização do registro da Ata
   * - 1.13
     - objetoContratacao
     - String
     - Descrição do Objeto referente à Contratação
   * - 1.14
     - cnpjOrgao
     - String
     - CNPJ do Órgão referente à Contratação
   * - 1.15
     - nomeOrgao
     - String
     - Razão Social do Órgão referente à Contratação
   * - 1.16
     - codigoUnidadeOrgao
     - String
     - Código da Unidade Administrativa do Órgão referente à Contratação
   * - 1.17
     - nomeUnidadeOrgao
     - String
     - Nome da Unidade Administrativa do Órgão referente à Contratação
   * - 1.18
     - cnpjOrgaoSubrogado
     - String
     - CNPJ do Órgão subrogado referente à Contratação
   * - 1.19
     - nomeOrgaoSubrogado
     - String
     - Razão Social do Órgão subrogado referente à Contratação
   * - 1.20
     - codigoUnidadeOrgaoSubrogado
     - String
     - Código da Unidade Administrativa subrogada do Órgão subrogado referente à Contratação
   * - 1.21
     - nomeUnidadeOrgaoSubrogado
     - String
     - Nome da Unidade Administrativa subrogada do Órgão subrogado referente à Contratação
   * - 1.22
     - usuario
     - String
     - Nome do sistema usuário (Sistema de Contratações Públicas) que publicou a ata.

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

Observação
~~~~~~~~~~

Em adição ao serviço **6.5. Serviço Consultar Atas de Registro de Preço por Período de Vigência** mencionado neste manual, é importante destacar que o Portal Nacional de Contratações Públicas (PNCP) oferece uma gama ampla de funcionalidades via API que permitem uma consulta detalhada sobre **CONTRATAÇÕES**.

Estas funcionalidades estão minuciosamente descritas no Manual de Integração — Portal Nacional de Contratações Públicas - PNCP, disponível no site oficial `www.gov.br <https://www.gov.br>`_. Abaixo, apresentamos uma lista com alguns exemplos de serviços disponíveis:

- 6.4.4. Consultar Atas de Registro de Preço por Compra
- 6.4.8. Consultar Todos os Documentos de uma Ata
- 6.4.9. Consultar Documento de uma Ata

Recomendamos a leitura detalhada do Manual de Integração do PNCP para uma compreensão abrangente de todas as funcionalidades e possibilidades oferecidas pela API.
