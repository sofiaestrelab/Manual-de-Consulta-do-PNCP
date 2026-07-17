Catálogo de Serviços
====================

Consultar Itens de PCA por Ano, idUsuario e Classificação Superior
------------------------------------------------------------------

Serviço que permite recuperar a lista de itens pertencentes a um determinado Plano de Contratações Anual (PCA) por determinado ano e usuário (Portais de
Contratações), opcionalmente filtrando por ordem de classificação superior.

Detalhes da Requisição
~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :width: 100%
   :widths: 50 15
   :header-rows: 1

   * - Endpoint
     - Método HTTP
   * - /v1/pca/usuario
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
   'https://pncp.gov.br/api/consulta/v1/pca/usuario?anoPca=2023&idUsuario=3&codigoClassificacaoSuperior=979&pagina=1' \
   -H 'accept: */*'

Dados de entrada
~~~~~~~~~~~~~~~~

.. note::
   Alimentar o parâmetro ``{anoPca}``, ``{idUsuario}`` e ``{pagina}`` na URL.

.. list-table::
   :width: 100%
   :widths: 5 15 15 15 50
   :header-rows: 1
   :class: quebra-linha-ultima-coluna

   * - Id
     - Campo
     - Tipo
     - Obrigatório
     - Descrição

   * - 1
     - anoPca
     - Inteiro
     - Sim
     - Ano do PCA

   * - 2
     - idUsuario
     - Inteiro
     - Sim
     - Número de identificação do usuário (Sistema de Contratações Públicas) que publicou a informação no Portal PNCP.

   * - 3
     - codigoClassificacaoSuperior
     - Texto (100)
     - Não
     - Código da Classe do material ou Grupo do serviço conforme catálogos de matérias e serviços utilizados pelos portais de compras.

   * - 4
     - pagina
     - Inteiro
     - Sim
     - Número da página que se deseja obter os dados.

   * - 5
     - tamanhoPagina
     - Inteiro
     - Não
     - Por padrão cada página contém no máximo 500 registros, no entanto o tamanho de registros em cada página pode ser ajustado (até o limite de 500 registros) com vistas a tornar a entrega de dados mais rápida.

