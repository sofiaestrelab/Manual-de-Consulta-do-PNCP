Consultar PCA por Data de Atualização Global
============================================

Serviço destinado à consulta dos Planos de Contratações Anual (PCA) que foram incluídos ou que sofreram alterações no PNCP durante um determinado intervalo de datas, considerando a data de atualização global do registro.

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
   :emphasize-lines: 1-3

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
   * - :destaque-amarelo-claro:`1`
     - :destaque-amarelo-claro:`dataInicio`
     - :destaque-amarelo-claro:`Data`
     - :destaque-amarelo-claro:`Sim`
     - :destaque-amarelo-claro:`Data início`
   * - :destaque-amarelo-claro:`2`
     - :destaque-amarelo-claro:`dataFim`
     - :destaque-amarelo-claro:`Data`
     - :destaque-amarelo-claro:`Sim`
     - :destaque-amarelo-claro:`Data fim`
   * - :destaque-amarelo-claro:`3`
     - :destaque-amarelo-claro:`cnpj`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Não`
     - :destaque-amarelo-claro:`CNPJ do órgão`
   * - :destaque-amarelo-claro:`4`
     - :destaque-amarelo-claro:`codigoUnidade`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Não`
     - :destaque-amarelo-claro:`Código da unidade do órgão`
   * - :destaque-amarelo-claro:`5`
     - :destaque-amarelo-claro:`pagina`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Sim`
     - :destaque-amarelo-claro:`Número da página que se deseja obter os dados.`
   * - :destaque-amarelo-claro:`6`
     - :destaque-amarelo-claro:`tamanhoPagina`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Não`
     - :destaque-amarelo-claro:`Por padrão cada página contém no máximo 500 registros, no entanto o tamanho de registros em cada página pode ser ajustado (até o limite de 500 registros) com vistas a tornar a entrega de dados mais rápida.`

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

   * - :destaque-amarelo-claro:`1`
     - :destaque-amarelo-claro:`codigoUnidade`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Código da unidade administrativa responsável pelo PCA.`
   * - :destaque-amarelo-claro:`2`
     - :destaque-amarelo-claro:`nomeUnidade`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome da unidade administrativa responsável pelo PCA.`
   * - :destaque-amarelo-claro:`3`
     - :destaque-amarelo-claro:`anoPca`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Ano de referência do Plano de Contratações Anual.`
   * - :destaque-amarelo-claro:`4`
     - :destaque-amarelo-claro:`orgaoEntidadeRazaoSocial`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Razão social do órgão ou entidade responsável pelo PCA.`
   * - :destaque-amarelo-claro:`5`
     - :destaque-amarelo-claro:`orgaoEntidadeCnpj`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`CNPJ do órgão ou entidade responsável pelo PCA.`
   * - :destaque-amarelo-claro:`5`
     - :destaque-amarelo-claro:`idPcaPncp`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Identificador do PCA no PNCP.`
   * - :destaque-amarelo-claro:`6`
     - :destaque-amarelo-claro:`dataPublicacaoPNCP`
     - :destaque-amarelo-claro:`Data/Hora`
     - :destaque-amarelo-claro:`Data da publicação do PCA no PNCP.`
   * - :destaque-amarelo-claro:`7`
     - :destaque-amarelo-claro:`dataAtualizacaoGlobalPCA`
     - :destaque-amarelo-claro:`Data/Hora`
     - :destaque-amarelo-claro:`Data da última atualização global do PCA.`
   * - :destaque-amarelo-claro:`8`
     - :destaque-amarelo-claro:`itens`
     - :destaque-amarelo-claro:`Lista`
     - :destaque-amarelo-claro:`Lista de itens do PCA.`
   * - :destaque-amarelo-claro:`8.1`
     - :destaque-amarelo-claro:`descricaoItem`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Descrição do item do PCA.`
   * - :destaque-amarelo-claro:`8.2`
     - :destaque-amarelo-claro:`categoriaItemPcaNome`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome da categoria do item do PCA.`
   * - :destaque-amarelo-claro:`8.3`
     - :destaque-amarelo-claro:`classificacaoCatalogoId`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Código identificador da classificação do catálogo.`
   * - :destaque-amarelo-claro:`8.4`
     - :destaque-amarelo-claro:`nomeClassificacaoCatalogo`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome da classificação do catálogo.`
   * - :destaque-amarelo-claro:`8.5`
     - :destaque-amarelo-claro:`quantidadeEstimada`
     - :destaque-amarelo-claro:`Número`
     - :destaque-amarelo-claro:`Quantidade estimada do item.`
   * - :destaque-amarelo-claro:`8.6`
     - :destaque-amarelo-claro:`numeroItem`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Número do item no PCA.`
   * - :destaque-amarelo-claro:`8.7`
     - :destaque-amarelo-claro:`valorUnitario`
     - :destaque-amarelo-claro:`Número`
     - :destaque-amarelo-claro:`Valor unitário estimado do item.`
   * - :destaque-amarelo-claro:`8.8`
     - :destaque-amarelo-claro:`valorTotal`
     - :destaque-amarelo-claro:`Número`
     - :destaque-amarelo-claro:`Valor total estimado do item.`
   * - :destaque-amarelo-claro:`8.9`
     - :destaque-amarelo-claro:`dataInclusao`
     - :destaque-amarelo-claro:`Data/Hora`
     - :destaque-amarelo-claro:`Data de inclusão do item no PCA.`
   * - :destaque-amarelo-claro:`8.10`
     - :destaque-amarelo-claro:`dataAtualizacao`
     - :destaque-amarelo-claro:`Data/Hora`
     - :destaque-amarelo-claro:`Data da última atualização do item.`
   * - :destaque-amarelo-claro:`8.11`
     - :destaque-amarelo-claro:`classificacaoSuperiorNome`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome da classificação superior.`
   * - :destaque-amarelo-claro:`8.12`
     - :destaque-amarelo-claro:`pdmCodigo`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Código do PDM.`
   * - :destaque-amarelo-claro:`8.13`
     - :destaque-amarelo-claro:`pdmDescricao`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Descrição do PDM.`
   * - :destaque-amarelo-claro:`8.14`
     - :destaque-amarelo-claro:`codigoItem`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Código do item.`
   * - :destaque-amarelo-claro:`8.15`
     - :destaque-amarelo-claro:`unidadeFornecimento`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Unidade de fornecimento do item.`
   * - :destaque-amarelo-claro:`8.16`
     - :destaque-amarelo-claro:`valorOrcamentoExercicio`
     - :destaque-amarelo-claro:`Número`
     - :destaque-amarelo-claro:`Valor previsto para o exercício orçamentário.`
   * - :destaque-amarelo-claro:`8.17`
     - :destaque-amarelo-claro:`unidadeRequisitante`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Unidade requisitante do item.`
   * - :destaque-amarelo-claro:`8.18`
     - :destaque-amarelo-claro:`dataDesejada`
     - :destaque-amarelo-claro:`Data`
     - :destaque-amarelo-claro:`Data desejada para a contratação.`
   * - :destaque-amarelo-claro:`8.19`
     - :destaque-amarelo-claro:`grupoContratacaoCodigo`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Código do grupo de contratação.`
   * - :destaque-amarelo-claro:`8.20`
     - :destaque-amarelo-claro:`grupoContratacaoNome`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome do grupo de contratação.`
   * - :destaque-amarelo-claro:`8.21`
     - :destaque-amarelo-claro:`classificacaoSuperiorCodigo`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Código da classificação superior.`
   * - :destaque-amarelo-claro:`9`
     - :destaque-amarelo-claro:`totalRegistros`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Total de registros encontrados.`
   * - :destaque-amarelo-claro:`10`
     - :destaque-amarelo-claro:`totalPaginas`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Total de páginas necessárias para a obtenção de todos os registros.`
   * - :destaque-amarelo-claro:`11`
     - :destaque-amarelo-claro:`numeroPagina`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Número da página que a consulta foi realizada.`
   * - :destaque-amarelo-claro:`12`
     - :destaque-amarelo-claro:`paginasRestantes`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Total de páginas restantes.`
   * - :destaque-amarelo-claro:`13`
     - :destaque-amarelo-claro:`empty`
     - :destaque-amarelo-claro:`Booleano`
     - :destaque-amarelo-claro:`Indicador se o atributo data está vazio.`

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
