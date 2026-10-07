Consultar PCA por Data de Atualização Global
============================================

Serviço de consultar os Plano de Contratações Anual (PCA) por data de Atualização Global no PNCP.

Detalhes de Requisição
~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :width: 100%
   :widths: auto
   :header-rows: 1

   * - Endpoint
     - Método HTTP
   * - /v1/pca
     - GET

Exemplo Requisição (cURL)
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash
   :linenos:

   curl -X 'GET' \
     'https://pncp.gov.br/api/consulta/v1/pca/atualizacao \
     -H 'accept: */*'

Dados de Entrada
~~~~~~~~~~~~~~~~

.. note::

   Alimentar os parâmetros ``{dataInicio}``, ``{dataFim}`` e ``{pagina}`` na URL.

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
     - dataInicio
     - Data 
     - Sim
     - Data início
   * - 2
     - dataFim
     - Data 
     - Sim
     - Data fim
   * - 3
     - cnpj
     - Texto 
     - Não
     - CNPJ do órgão
   * - 4
     - codigoUnidade
     - Texto 
     - Não
     - Código da unidade do órgão    
   * - 5
     - pagina
     - Inteiro 
     - Sim
     - Número da página que se deseja obter os dados.
   * - 6
     - tamanhoPagina
     - Inteiro 
     - Não
     - Por padrão cada página contém no máximo 500 registros, no entanto o tamanho de registros em cada página pode ser ajustado (até o limite de 500 registros) com vistas a tornar a entrega de dados mais rápida.

Dados de retorno
~~~~~~~~~~~~~~~~

.. list-table::
   :width: 100%
   :widths: 5 30 15 50
   :header-rows: 1
   :class: quebra-linha-dois-ultima 

   * - Id
     - Campo
     - Tipo
     - Descrição

   * - 1
     - codigoUnidade
     - Texto
     - Código da unidade administrativa responsável pelo PCA.
   * - 2
     - nomeUnidade
     - Texto
     - Nome da unidade administrativa responsável pelo PCA.
   * - 3
     - anoPca
     - Inteiro
     - Ano de referência do Plano de Contratações Anual.
   * - 4
     - orgaoEntidadeRazaoSocial
     - Texto
     - Razão social do órgão ou entidade responsável pelo PCA.
   * - 5
     - orgaoEntidadeCnpj
     - Texto
     - CNPJ do órgão ou entidade responsável pelo PCA.
   * - 5
     - idPcaPncp
     - Texto
     - Identificador do PCA no PNCP.
   * - 6
     - dataPublicacaoPNCP
     - Data/Hora
     - Data da publicação do PCA no PNCP.
   * - 7
     - dataAtualizacaoGlobalPCA
     - Data/Hora
     - Data da última atualização global do PCA.
   * - 8
     - itens
     - Lista
     - Lista de itens do PCA.
   * - 8.1
     - descricaoItem
     - Texto
     - Descrição do item do PCA.
   * - 8.2
     - categoriaItemPcaNome
     - Texto
     - Nome da categoria do item do PCA.
   * - 8.3
     - classificacaoCatalogoId
     - Inteiro
     - Código identificador da classificação do catálogo.
   * - 8.4
     - nomeClassificacaoCatalogo
     - Texto
     - Nome da classificação do catálogo.
   * - 8.5
     - quantidadeEstimada
     - Número
     - Quantidade estimada do item.
   * - 8.6
     - numeroItem
     - Inteiro
     - Número do item no PCA.
   * - 8.7
     - valorUnitario
     - Número
     - Valor unitário estimado do item.
   * - 8.8
     - valorTotal
     - Número
     - Valor total estimado do item.
   * - 8.9
     - dataInclusao
     - Data/Hora
     - Data de inclusão do item no PCA.
   * - 8.10
     - dataAtualizacao
     - Data/Hora
     - Data da última atualização do item.
   * - 8.11
     - classificacaoSuperiorNome
     - Texto
     - Nome da classificação superior.
   * - 8.12
     - pdmCodigo
     - Texto
     - Código do PDM.
   * - 8.13
     - pdmDescricao
     - Texto
     - Descrição do PDM.
   * - 8.14
     - codigoItem
     - Texto
     - Código do item.
   * - 8.15
     - unidadeFornecimento
     - Texto
     - Unidade de fornecimento do item.
   * - 8.16
     - valorOrcamentoExercicio
     - Número
     - Valor previsto para o exercício orçamentário.
   * - 8.17
     - unidadeRequisitante
     - Texto
     - Unidade requisitante do item.
   * - 8.18
     - dataDesejada
     - Data
     - Data desejada para a contratação.
   * - 8.19
     - grupoContratacaoCodigo
     - Texto
     - Código do grupo de contratação.
   * - 8.20
     - grupoContratacaoNome
     - Texto
     - Nome do grupo de contratação.
   * - 8.21
     - classificacaoSuperiorCodigo
     - Texto
     - Código da classificação superior.
   * - 9
     - totalRegistros
     - Inteiro
     - Total de registros encontrados.
   * - 10
     - totalPaginas
     - Inteiro
     - Total de páginas necessárias para a obtenção de todos os registros.
   * - 11
     - numeroPagina
     - Inteiro
     - Número da página que a consulta foi realizada.
   * - 12
     - paginasRestantes
     - Inteiro
     - Total de páginas restantes.
   * - 13
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
