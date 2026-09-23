Consultar Itens de PCA por Ano do PCA e Código de Classificação Superior
=========================================================================

Serviço de consultar os itens do Plano de Contratações Anual (PCA) a partir do ano do PCA e do código de classificação superior.

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
     'https://pncp.gov.br/api/consulta/v1/pca/?anoPca=2026&codigoClassificacaoSuperior=2&pagina=2' \
     -H 'accept: */*'

Dados de Entrada
~~~~~~~~~~~~~~~~

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
     - anoPca
     - Inteiro 
     - Sim
     - 
   * - 2
     - codigoClassificacaoSuperior
     - Texto
     - Sim
     -
   * - 3
     - pagina
     - Inteiro 
     - Sim
     -
   * - 4
     - tamanhoPagina
     - Inteiro 
     - Não
     -

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
     - data
     - Lista
     - Lista de Planos de Contratações Anuais encontrados.
   * - 1.1
     - itens
     - Lista
     - Lista de itens do PCA.
   * - 1.1.1
     - descricaoItem
     - Texto
     - Descrição do item do PCA.
   * - 1.1.2
     - nomeClassificacaoCatalogo
     - Texto
     - Nome da classificação do catálogo.
   * - 1.1.3
     - quantidadeEstimada
     - Número
     - Quantidade estimada do item.
   * - 1.1.4
     - pdmCodigo
     - Texto
     - Código do PDM.
   * - 1.1.5
     - dataInclusao
     - Data/Hora
     - Data de inclusão do item no PCA.
   * - 1.1.6
     - numeroItem
     - Inteiro
     - Número do item no PCA.
   * - 1.1.7
     - dataAtualizacao
     - Data/Hora
     - Data da última atualização do item.
   * - 1.1.8
     - valorTotal
     - Número
     - Valor total estimado do item.
   * - 1.1.9
     - pdmDescricao
     - Texto
     - Descrição do PDM.
   * - 1.1.10
     - codigoItem
     - Texto
     - Código do item.
   * - 1.1.11
     - unidadeRequisitante
     - Texto
     - Unidade requisitante do item.
   * - 1.1.12
     - grupoContratacaoCodigo
     - Texto
     - Código do grupo de contratação.
   * - 1.1.13
     - grupoContratacaoNome
     - Texto
     - Nome do grupo de contratação.
   * - 1.1.14
     - classificacaoSuperiorCodigo
     - Texto
     - Código da classificação superior.
   * - 1.1.15
     - classificacaoSuperiorNome
     - Texto
     - Nome da classificação superior.
   * - 1.1.16
     - unidadeFornecimento
     - Texto
     - Unidade de fornecimento do item.
   * - 1.1.17
     - valorUnitario
     - Número
     - Valor unitário estimado do item.
   * - 1.1.18
     - valorOrcamentoExercicio
     - Número
     - Valor previsto para o exercício orçamentário.
   * - 1.1.19
     - dataDesejada
     - Data
     - Data desejada para a contratação.
   * - 1.1.20
     - categoriaItemPcaNome
     - Texto
     - Nome da categoria do item do PCA.
   * - 1.1.21
     - classificacaoCatalogoId
     - Inteiro
     - Código identificador da classificação do catálogo.
   * - 1.2
     - codigoUnidade
     - Texto
     - Código da unidade administrativa responsável pelo PCA.
   * - 1.3
     - nomeUnidade
     - Texto
     - Nome da unidade administrativa responsável pelo PCA.
   * - 1.4
     - anoPca
     - Inteiro
     - Ano de referência do Plano de Contratações Anual.
   * - 1.5
     - idPcaPncp
     - Texto
     - Identificador do PCA no PNCP.
   * - 1.6
     - orgaoEntidadeCnpj
     - Texto
     - CNPJ do órgão ou entidade responsável pelo PCA.
   * - 1.7
     - orgaoEntidadeRazaoSocial
     - Texto
     - Razão social do órgão ou entidade responsável pelo PCA.
   * - 1.8
     - dataPublicacaoPNCP
     - Data/Hora
     - Data da publicação do PCA no PNCP.
   * - 1.9
     - dataAtualizacaoGlobalPCA
     - Data/Hora
     - Data da última atualização global do PCA.
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
