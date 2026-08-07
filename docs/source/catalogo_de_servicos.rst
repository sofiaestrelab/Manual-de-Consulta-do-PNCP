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
     - CNPJ do Órgão pertencente ao PCA
   * - 2
     - orgaoEntidadeRazaoSocial
     - Texto
     - Razão Social do Órgão pertencente ao PCA
   * - 3
     - codigoUnidade
     - Texto
     - Código da Unidade Responsável do Órgão
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

Serviço Consultar Contratações por Data de Publicação
-----------------------------------------------------

Serviço que permite consultar contratações publicadas no PNCP por um período informado. Junto à data inicial e data final informadas deverá ser informado o código da
Modalidade da Contratação (vide tabela XXX). Opcionalmente poderá ser informado código do Modo de Disputa da Contratação (vide tabela XXX), código do IBGE do
Município, sigla da Unidade Federativa da Unidade Administrativa do Órgão, CNPJ do Órgão/Entidade, código da Unidade Administrativa do Órgão/Entidade ou código de
identificação do Usuário (Sistema de Contratações Públicas que publicou a Contratação) para refinar a consulta.

Detalhes de Requisição
~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :width: 100%
   :widths: auto
   :header-rows: 1

   * - Endpoint
     - Método HTTP
   * - /v1/contratacoes/publicacao
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
     'https://pncp.gov.br/api/consulta/v1/contratacoes/publicacao?dataInicial=20230801&dataFinal=20230802&codigoModalidadeContratacao=8&uf=DF&codigoMunicipioIbge=5300108&cnpj=00059311000126&codigoUnidadeAdministrativa=194035&idUsuario=3&pagina=1' \
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
     - CNPJ do órgão originário da contratação informado na inclusão (proprietário da contratação).
   * - 8
     - codigoUnidadeAdministrativa
     - String
     - Não
     - Código da Unidade Administrativa do Órgão originário da contratação informado na inclusão (proprietário da contratação).
   * - 9
     - idUsuario
     - Inteiro
     - Não
     - Identificador do sistema usuário (Sistema de Contratações Públicas) que publicou a contratação.
   * - 10
     - pagina
     - Inteiro
     - Sim
     - Número da página que se deseja obter os dados.
   * - 11
     - tamanhoPagina
     - Inteiro
     - Não
     - Por padrão cada página contém no máximo 50 registros, no entanto o tamanho de registros em cada página pode ser ajustado (até o limite de 500 registros) com vistas a tornar a entrega de dados mais rápida.

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
     - numeroControlePNCP
     - String
     - Número de Controle PNCP da Contratação (id Contratação PNCP)
   * - 2
     - numeroCompra
     - Texto (50)
     - Número da Contratação no sistema de origem
   * - 3
     - anoCompra
     - Inteiro
     - Ano da Contratação
   * - 4
     - processo
     - Texto (50)
     - Número do processo de Contratação no sistema de origem
   * - 5
     - tipoInstrumentoConvocatorioId
     - Inteiro
     - Código do instrumento convocatório da Contratação
   * - 6
     - tipoInstrumentoConvocatorioNome
     - String
     - Nome do instrumento convocatório da Contratação
   * - 7
     - modalidadeId
     - Inteiro
     - Código da Modalidade referente à Contratação
   * - 8
     - modalidadeNome
     - String
     - Modalidade referente à Contratação
   * - 9
     - modoDisputaId
     - Inteiro
     - Código do modo de disputa referente à Contratação
   * - 10
     - modoDisputaNome
     - String
     - Modo de disputa referente à Contratação
   * - 11
     - situacaoCompraId
     - Inteiro
     - Código da situação da Contratação
   * - 12
     - situacaoCompraNome
     - Inteiro
     - Situação da Contratação
   * - 13
     - objetoCompra
     - Texto (5120)
     - Descrição do Objeto referente à Contratação
   * - 14
     - informacaoComplementar
     - Texto (5120)
     - Informação Complementar do objeto referente à Contratação
   * - 15
     - srp
     - Booleano
     - Identifica se a compra trata-se de um SRP (Sistema de Registro de Preços)
   * - 16
     - amparoLegal
     - Dados
     - Dados do amparo legal
   * - 16.1
     - codigo
     - Inteiro
     - Código do Amparo Legal
   * - 16.2
     - nome
     - String
     - Nome do Amparo Legal
   * - 16.3
     - descricao
     - String
     - Descrição do Amparo Legal
   * - 17
     - valorTotalEstimado
     - Decimal
     - Valor total estimado da Contratação. Precisão de até 4 dígitos decimais; Ex: 100.0001. Obs: retornará valor zero (0) se o atributo ``orcamentoSigiloso`` for ``true`` e o item não possuir resultado.
   * - 18
     - valorTotalHomologado
     - Decimal
     - Valor total homologado com base nos resultados incluídos. Precisão de até 4 dígitos decimais; Ex: 100.0001.
   * - 19
     - dataAberturaProposta
     - Data e Hora
     - Data de abertura do recebimento de propostas (horário de Brasília)
   * - 20
     - dataEncerramentoProposta
     - Data e Hora
     - Data de encerramento do recebimento de propostas (horário de Brasília)
   * - 21
     - dataPublicacaoPncp
     - Data
     - Data da publicação da Contratação no PNCP
   * - 22
     - dataInclusao
     - Data
     - Data da inclusão do registro da Contratação no PNCP
   * - 23
     - dataAtualizacao
     - Data
     - Data da última atualização do registro da Contratação no PNCP
   * - 24
     - sequencialCompra
     - Inteiro
     - Sequencial da Contratação no PNCP; número sequencial gerado no momento em que a contratação foi inserida no PNCP.
   * - 25
     - orgaoEntidade
     - Dados
     - Dados do Órgão/Entidade
   * - 25.1
     - cnpj
     - String
     - CNPJ do Órgão referente à Contratação
   * - 25.2
     - razaosocial
     - String
     - Razão social do Órgão referente à Contratação
   * - 25.3
     - poderId
     - String
     - Código do poder a que pertence o Órgão. L - Legislativo; E - Executivo; J - Judiciário
   * - 25.4
     - esferaId
     - String
     - Código da esfera a que pertence o Órgão. F - Federal; E - Estadual; M - Municipal; D - Distrital
   * - 26
     - unidadeOrgao
     - Dados
     - Dados da Unidade Administrativa
   * - 26.1
     - codigoUnidade
     - String
     - Código da Unidade Administrativa pertencente ao Órgão
   * - 26.2
     - nomeUnidade
     - String
     - Nome da Unidade Administrativa pertencente ao Órgão
   * - 26.3
     - codigoIbge
     - Inteiro
     - Código IBGE do município
   * - 26.4
     - municipioNome
     - String
     - Nome do município
   * - 26.5
     - ufSigla
     - String
     - Sigla da unidade federativa do município
   * - 26.6
     - ufNome
     - String
     - Nome da unidade federativa do município
   * - 27
     - orgaoSubRogado
     - Dados
     - Dados do Órgão/Entidade subrogado
   * - 28.1
     - cnpj
     - String
     - CNPJ do Órgão referente à Contratação
   * - 28.2
     - razaosocial
     - String
     - Razão social do Órgão referente à Contratação
   * - 28.3
     - poderId
     - String
     - Código do poder a que pertence o Órgão. L - Legislativo; E - Executivo; J - Judiciário
   * - 28.4
     - esferaId
     - String
     - Código da esfera a que pertence o Órgão. F - Federal; E - Estadual; M - Municipal; D - Distrital
   * - 29
     - unidadeSubRogada
     - Dados
     - Dados da Unidade Administrativa do Órgão subrogado
   * - 29.1
     - codigoUnidade
     - String
     - Código da Unidade Administrativa pertencente ao Órgão subrogado
   * - 29.2
     - nomeUnidade
     - String
     - Nome da Unidade Administrativa pertencente ao Órgão subrogado
   * - 29.3
     - codigoIbge
     - Inteiro
     - Código IBGE do município
   * - 29.4
     - municipioNome
     - String
     - Nome do município
   * - 29.5
     - ufSigla
     - String
     - Sigla da unidade federativa do município
   * - 29.6
     - ufNome
     - String
     - Nome da unidade federativa do município
   * - 30
     - usuarioNome
     - String
     - Nome do Usuário/Sistema que enviou a Contratação
   * - 31
     - linkSistemaOrigem
     - String
     - URL para página/portal do sistema de origem da contratação para recebimento de propostas.
   * - 32
     - justificativaPresencial
     - String
     - Justificativa pela escolha da modalidade presencial.

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

Serviço Consultar Contratações com Período de Recebimento de Propostas em Aberto
--------------------------------------------------------------------------------

Serviço que permite consultar contratações publicadas no PNCP por um período informado. Opcionalmente poderá ser informado o código da Modalidade da
Contratação código do IBGE do Município, sigla da Unidade Federativa da Unidade Administrativa do Órgão, CNPJ do Órgão/Entidade, código da Unidade Administrativa do
Órgão/Entidade ou código de identificação do Usuário (Sistema de Contratações Públicas que publicou a Contratação) para refinar a consulta.

Detalhes de Requisição
~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :width: 100%
   :widths: auto
   :header-rows: 1

   * - Endpoint
     - Método HTTP
   * - /v1/contratacoes/proposta
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

   curl -k -X 'GET' \
     "${BASE_URL}/v1/contratacoes/proposta?dataFinal=20230831&codigoModalidadeContratacao=8&pagina=1" \
     -H "accept: */*"

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
     - dataFinal
     - Data
     - Sim
     - Data final do período a ser consultado no formato AAAAMMDD.
   * - 2
     - codigoModalidadeContratacao
     - Inteiro
     - Sim
     - Código da tabela de domínio Modalidade da Contratação.
   * - 3
     - uf
     - String
     - Não
     - Sigla da Unidade Federativa referente à Unidade Administrativa do órgão.
   * - 4
     - codigoMunicipioIbge
     - String
     - Não
     - Código IBGE do Município da Unidade Administrativa.
   * - 5
     - cnpj
     - String
     - Não
     - CNPJ do órgão originário da contratação informado na inclusão (proprietário da contratação).
   * - 6
     - codigoUnidadeAdministrativa
     - String
     - Não
     - Código da Unidade Administrativa do Órgão originário da contratação informado na inclusão (proprietário da contratação).
   * - 7
     - idUsuario
     - Inteiro
     - Não
     - Identificador do sistema usuário (Sistema de Contratações Públicas) que publicou a contratação.
   * - 8
     - pagina
     - Inteiro
     - Sim
     - Número da página que se deseja obter os dados.
   * - 9
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
     - numeroControlePNCP
     - String
     - Número de Controle PNCP da Contratação (id Contratação PNCP)
   * - 2
     - numeroCompra
     - Texto (50)
     - Número da Contratação no sistema de origem
   * - 3
     - anoCompra
     - Inteiro
     - Ano da Contratação
   * - 4
     - processo
     - Texto (50)
     - Número do processo de Contratação no sistema de origem
   * - 5
     - tipoInstrumentoConvocatorioId
     - Inteiro
     - Código do instrumento convocatório da Contratação
   * - 6
     - tipoInstrumentoConvocatorioNome
     - String
     - Nome do instrumento convocatório da Contratação
   * - 7
     - modalidadeId
     - Inteiro
     - Código da Modalidade referente à Contratação
   * - 8
     - modalidadeNome
     - String
     - Modalidade referente à Contratação
   * - 9
     - modoDisputaId
     - Inteiro
     - Código do modo de disputa referente à Contratação
   * - 10
     - modoDisputaNome
     - String
     - Modo de disputa referente à Contratação
   * - 11
     - situacaoCompraId
     - Inteiro
     - Código da situação da Contratação
   * - 12
     - situacaoCompraNome
     - Inteiro
     - Situação da Contratação
   * - 13
     - objetoCompra
     - Texto (5120)
     - Descrição do Objeto referente à Contratação
   * - 14
     - informacaoComplementar
     - Texto (5120)
     - Informação Complementar do objeto referente à Contratação
   * - 15
     - srp
     - Booleano
     - Identifica se a compra trata-se de um SRP (Sistema de Registro de Preços)
   * - 16
     - amparoLegal
     - Dados
     - Dados do amparo legal
   * - 16.1
     - codigo
     - Inteiro
     - Código do Amparo Legal
   * - 16.2
     - nome
     - String
     - Nome do Amparo Legal
   * - 16.3
     - descricao
     - String
     - Descrição do Amparo Legal
   * - 17
     - valorTotalEstimado
     - Decimal
     - Valor total estimado da Contratação. Precisão de até 4 dígitos decimais; Ex: 100.0001. Obs: retornará valor zero (0) se o atributo ``orcamentoSigiloso`` for ``true`` e o item não possuir resultado.
   * - 18
     - valorTotalHomologado
     - Decimal
     - Valor total homologado com base nos resultados incluídos. Precisão de até 4 dígitos decimais; Ex: 100.0001.
   * - 19
     - dataAberturaProposta
     - Data e Hora
     - Data de abertura do recebimento de propostas (horário de Brasília)
   * - 20
     - dataEncerramentoProposta
     - Data e Hora
     - Data de encerramento do recebimento de propostas (horário de Brasília)
   * - 21
     - dataPublicacaoPncp
     - Data
     - Data da publicação da Contratação no PNCP
   * - 22
     - dataInclusao
     - Data
     - Data da inclusão do registro da Contratação no PNCP
   * - 23
     - dataAtualizacao
     - Data
     - Data da última atualização do registro da Contratação
   * - 24
     - sequencialCompra
     - Inteiro
     - Sequencial da Contratação no PNCP. Número sequencial gerado no momento em que a contratação foi inserida no PNCP.
   * - 25
     - orgaoEntidade
     - Dados
     - Dados do Órgão/Entidade
   * - 25.1
     - cnpj
     - String
     - CNPJ do Órgão referente à Contratação
   * - 25.2
     - razaosocial
     - String
     - Razão social do Órgão referente à Contratação
   * - 25.3
     - poderId
     - String
     - Código do poder a que pertence o Órgão. L - Legislativo; E - Executivo; J - Judiciário
   * - 25.4
     - esferaId
     - String
     - Código da esfera a que pertence o Órgão. F - Federal; E - Estadual; M - Municipal; D - Distrital
   * - 26
     - unidadeOrgao
     - Dados
     - Dados da Unidade Administrativa
   * - 26.1
     - codigoUnidade
     - String
     - Código da Unidade Administrativa pertencente ao Órgão
   * - 26.2
     - nomeUnidade
     - String
     - Nome da Unidade Administrativa pertencente ao Órgão
   * - 26.3
     - codigoIbge
     - Inteiro
     - Código IBGE do município
   * - 26.4
     - municipioNome
     - String
     - Nome do município
   * - 26.5
     - ufSigla
     - String
     - Sigla da unidade federativa do município
   * - 26.6
     - ufNome
     - String
     - Nome da unidade federativa do município
   * - 27
     - orgaoSubRogado
     - Dados
     - Dados do Órgão/Entidade subrogado
   * - 28.1
     - cnpj
     - String
     - CNPJ do Órgão referente à Contratação
   * - 28.2
     - razaosocial
     - String
     - Razão social do Órgão referente à Contratação
   * - 28.3
     - poderId
     - String
     - Código do poder a que pertence o Órgão. L - Legislativo; E - Executivo; J - Judiciário
   * - 28.4
     - esferaId
     - String
     - Código da esfera a que pertence o Órgão. F - Federal; E - Estadual; M - Municipal; D - Distrital
   * - 29
     - unidadeSubRogada
     - Dados
     - Dados da Unidade Administrativa do Órgão subrogado
   * - 29.1
     - codigoUnidade
     - String
     - Código da Unidade Administrativa pertencente ao Órgão subrogado
   * - 29.2
     - nomeUnidade
     - String
     - Nome da Unidade Administrativa pertencente ao Órgão subrogado
   * - 29.3
     - codigoIbge
     - Inteiro
     - Código IBGE do município
   * - 29.4
     - municipioNome
     - String
     - Nome do município
   * - 29.5
     - ufSigla
     - String
     - Sigla da unidade federativa do município
   * - 29.6
     - ufNome
     - String
     - Nome da unidade federativa do município
   * - 30
     - usuarioNome
     - String
     - Nome do Usuário/Sistema que enviou a Contratação
   * - 31
     - linkSistemaOrigem
     - String
     - URL para página/portal do sistema de origem da contratação para recebimento de propostas.
   * - 32
     - justificativaPresencial
     - String
     - Justificativa pela escolha da modalidade presencial.

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
