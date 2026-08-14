Consultar Itens de PCA por Ano e Classificação Superior
-------------------------------------------------------

Serviço que permite recuperar a lista de itens pertencentes a um determinado Plano de Contratações Anual (PCA), opcionalmente filtrando por ordem de classificação superior.

Detalhes de Requisição
~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :width: 100%
   :widths: auto
   :header-rows: 1

   * - Endpoint
     - Método HTTP
   * - /v1/pca/
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
     'https://pncp.gov.br/api/consulta/v1/pca/?anoPca=2023&codigoClassificacaoSuperior=979&pagina=1' \
     -H 'accept: */*'

Dados de entrada
~~~~~~~~~~~~~~~~

.. note::

   Alimentar o parâmetro ``{ano}`` na URL.

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
     - anoPca
     - Inteiro
     - Sim
     - Ano do PCA.
   * - 2
     - codigoClassificacaoSuperior
     - Texto (100)
     - Sim
     - Código da Classe do material ou Grupo do serviço conforme catálogos de matérias e serviços utilizados pelos portais de compras.
   * - 3
     - pagina
     - Inteiro
     - Sim
     - Número da página que se deseja obter os dados.
   * - 4
     - tamanhoPagina
     - Inteiro
     - Não
     - Por padrão cada página contém no máximo 500 registros, no entanto o tamanho de registros em cada página pode ser ajustado (até o limite de 500 registros) com vistas a tornar a entrega de dados mais rápida.

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
     - orgaoEntidadeCnpj
     - Texto
     - CNPJ do Órgão
   * - 2
     - orgaoEntidadeRazaoSocial
     - Texto
     - Razão Social do Órgão
   * - 3
     - codigoUnidade
     - Texto
     - Código da Unidade Responsável
   * - 4
     - nomeUnidade
     - Texto
     - Nome da Unidade Responsável
   * - 5
     - anoPca
     - Inteiro
     - Ano do Plano de Contratações da Unidade
   * - 6
     - idPcaPncp
     - Texto
     - Número de Controle PNCP do PCA (id PCA PNCP)
   * - 7
     - dataPublicacaoPncp
     - Data
     - Data da publicação do item do plano no PNCP
   * - 8
     - Lista
     - Lista
     - Lista de Itens do PCA da Unidade
   * - 8.1
     - numeroItem
     - Inteiro
     - Número do item no Plano (único e sequencial crescente)
   * - 8.2
     - categoriaItemPcaNome
     - Texto
     - Nome categoria do item conforme tabela de domínio Categoria do Item do Plano de Contratações
   * - 8.3
     - classificacaoCatalogoId
     - Texto
     - Código da Indicação se Item é Material ou Serviço. Domínio: 1 - Material; 2 - Serviço;
   * - 8.4
     - nomeClassificacaoCatalogo
     - Texto
     - Nome da Indicação se Item é Material ou Serviço. Domínio: 1 - Material; 2 - Serviço;
   * - 8.5
     - classificacaoSuperiorCodigo
     - Texto (100)
     - Código da Classe do material ou Grupo do serviço conforme catálogo
   * - 8.6
     - classificacaoSuperiorNome
     - Texto (255)
     - Descrição da Classe do material ou Grupo do serviço conforme catálogo
   * - 8.7
     - pdmCodigo
     - Texto (100)
     - Código PDM referente ao material conforme o CNBS
   * - 8.8
     - pdmDescricao
     - Texto (255)
     - Descrição PDM referente ao material conforme o CNBS
   * - 8.9
     - codigoItem
     - Texto (100)
     - Código do Material ou Serviço conforme o catálogo utilizado
   * - 8.10
     - descricaoItem
     - Texto (2048)
     - Descrição do material ou serviço conforme catálogo utilizado
   * - 8.11
     - unidadeFornecimento
     - Texto
     - Unidade de fornecimento
   * - 8.12
     - quantidadeEstimada
     - Decimal
     - Quantidade estimada do item do plano de contratação (maior ou igual a zero). Precisão de até 4 dígitos decimais; Ex: 10.0001;
   * - 8.13
     - valorUnitario
     - Decimal
     - Valor unitário do item (maior ou igual a zero). Precisão de até 4 dígitos decimais; Ex: 100.0001;
   * - 8.14
     - valorTotal
     - Decimal
     - Valor total do item (maior ou igual a zero). Precisão de até 4 dígitos decimais; Ex: 100.0001;
   * - 8.15
     - valorOrcamentoExercicio
     - Decimal
     - Valor orçamentário estimado para o exercício (maior ou igual a zero). Precisão de até 4 dígitos decimais; Ex: 100.0001;
   * - 8.16
     - dataDesejada
     - Data
     - Data desejada para a contratação
   * - 8.17
     - unidadeRequisitante
     - Texto
     - Nome da unidade requisitante
   * - 8.18
     - grupoContratacaoCodigo
     - Texto
     - Código da Contratação Futura
   * - 8.19
     - grupoContratacaoNome
     - Texto
     - Nome da Contratação Futura
   * - 8.20
     - dataInclusao
     - Data
     - Data da inclusão do registro do item do plano no PNCP
   * - 8.21
     - dataAtualizacao
     - Data
     - Data da última atualização do registro do item do plano

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