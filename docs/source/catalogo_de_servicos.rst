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
   :widths: 5 25 15 55
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
   * - :destaque-amarelo-claro:`1`
     - :destaque-amarelo-claro:`numeroControlePNCP`
     - :destaque-amarelo-claro:`String`
     - :destaque-amarelo-claro:`Número de Controle PNCP da Contratação (id Contratação PNCP)`
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

Observação
----------

Em adição ao serviço **6.4. Serviço Consultar Contratações com Período de Recebimento de Propostas em Aberto** mencionado neste manual, é importante destacar que o Portal Nacional de Contratações Públicas (PNCP) oferece uma gama ampla de funcionalidades via API que permitem uma consulta detalhada sobre **Contratações**.

Essas funcionalidades estão descritas no **Manual de Integração — Portal Nacional de Contratações Públicas (PNCP)**, disponível no site oficial do Governo Federal.

Alguns exemplos de serviços disponíveis são:

- 6.3.5. Consultar uma Contratação
- 6.3.8. Consultar Todos os Documentos de uma Contratação
- 6.3.13. Consultar Itens de uma Contratação
- 6.3.14. Consultar Item de uma Contratação
- 6.3.17. Consultar Resultados de Item de uma Contratação
- 6.3.18. Consultar um Resultado Específico de Item de uma Contratação
- 6.3.19. Consultar Histórico da Contratação
- 6.3.22. Consultar Imagens de um Item de Contratação

Recomenda-se a leitura detalhada do Manual de Integração do PNCP para uma compreensão abrangente de todas as funcionalidades e possibilidades oferecidas pela API.

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
   * - 4`
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
   * - 1.1
     - numeroControlePNCPAta
     - String
     - Número de Controle PNCP da Ata (id Ata PNCP)
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

Serviço Consultar Contratos por Data de Publicação
--------------------------------------------------

Serviço que permite consultar contratos e/ou empenhos com força de contrato publicados no PNCP por um período informado. A partir da data inicial e data final
informadas serão recuperados os contratos/empenhos publicados no período. Opcionalmente poderá ser informado CNPJ do Órgão/Entidade, código da Unidade Administrativa do Órgão/Entidade ou número de identificação do Usuário (Portais de Contratações Públicas).

Detalhes de Requisição
~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :width: 100%
   :widths: auto
   :header-rows: 1

   * - Endpoint
     - Método HTTP
     - Exemplo de Payload
   * - /v1/contratos
     - GET
     - Não se aplica

Exemplo Requisição (cURL)
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash
   :linenos:

   curl -k -X GET "${BASE_URL}/v1/contratos?dataInicial=20230801&dataFinal=20230831&pagina=1" \
     -H "accept: */*"

Ou:

.. code-block:: bash
   :linenos:

   curl -k -X GET "${BASE_URL}/v1/contratos?dataInicial=20230801&dataFinal=20230831&cnpjOrgao=00394544000185&pagina=1" \
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
     - cnpjOrgao
     - String
     - Não
     - CNPJ do órgão originário da contratação informado na inclusão (proprietário do contrato)
   * - 4
     - codigoUnidadeAdministrativa
     - String
     - Não
     - Código da Unidade Administrativa do Órgão originário da contratação informado na inclusão (proprietário do contrato)
   * - 5
     - usuarioId
     - Inteiro
     - Não
     - Identificador do sistema usuário (Sistema de Contratações Públicas) que publicou o contrato.
   * - 6
     - pagina
     - Inteiro
     - Sim
     - Número da página a ser requisitada
   * - 7
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
     - Número de controle PNCP do contrato (id contrato PNCP)
   * - 2
     - numeroControlePNCPCompra
     - String
     - Número de controle PNCP da contratação relacionada (id contratação PNCP)
   * - 3
     - numeroContratoEmpenho
     - Texto (50)
     - Número do contrato ou empenho com força de contrato
   * - 4
     - anoContrato
     - Inteiro
     - Ano do contrato
   * - 5
     - sequencialContrato
     - Inteiro
     - Número sequencial do contrato (gerado pelo PNCP)
   * - 6
     - processo
     - Texto (50)
     - Número do processo
   * - 7
     - tipoContrato
     - Dados
     - Dados do tipo de contrato
   * - 7.1
     - Id
     - Inteiro
     - Código da tabela de domínio Tipo de contrato
   * - 7.2
     - Nome
     - String
     - Nome do Tipo de Contrato
   * - 8
     - categoriaProcesso
     - Dados
     - Dados da categoria do processo
   * - 8.1
     - Id
     - Inteiro
     - Código da tabela de domínio Categoria
   * - 8.2
     - Nome
     - String
     - Nome da Categoria do processo
   * - 9
     - receita
     - Booleano
     - Receita ou despesa: True - Receita; False - Despesa;
   * - 10
     - objetoContrato
     - Texto (5120)
     - Descrição do objeto do contrato
   * - 11
     - informacaoComplementar
     - Texto (5120)
     - Informações complementares; Se existir;
   * - 12
     - orgaoEntidade
     - Dados
     - Dados do Órgão/Entidade do Contrato
   * - 12.1
     - cnpj
     - String
     - CNPJ do Órgão referente à Contrato
   * - 12.2
     - razaoSocial
     - String
     - Razão social do Órgão referente à Contrato
   * - 12.3
     - poderId
     - String
     - Código do poder a que pertence o Órgão. L - Legislativo; E - Executivo; J - Judiciário
   * - 12.4
     - esferaId
     - String
     - Código da esfera a que pertence o Órgão. F - Federal; E - Estadual; M - Municipal; D - Distrital
   * - 13
     - unidadeOrgao
     - Dados
     - Dados da Unidade executora do Órgão do Contrato
   * - 13.1
     - codigoUnidade
     - String
     - Código da Unidade Executora pertencente ao Órgão
   * - 13.2
     - nomeUnidade
     - String
     - Nome da Unidade Executora pertencente ao Órgão
   * - 13.3
     - codigoIbge
     - Inteiro
     - Código IBGE do município
   * - 13.4
     - municipioNome
     - String
     - Nome do município
   * - 13.5
     - ufSigla
     - String
     - Sigla da unidade federativa do município
   * - 13.6
     - ufNome
     - String
     - Nome da unidade federativa do município
   * - 14
     - orgaoSubRogado
     - Dados
     - Dados do Órgão/Entidade subrogado do Contrato
   * - 14.1
     - cnpj
     - String
     - CNPJ do Órgão referente à Contrato
   * - 14.2
     - razaoSocial
     - String
     - Razão social do Órgão referente à Contrato
   * - 14.3
     - poderId
     - String
     - Código do poder a que pertence o Órgão. L - Legislativo; E - Executivo; J - Judiciário
   * - 14.4
     - esferaId
     - String
     - Código da esfera a que pertence o Órgão. F - Federal; E - Estadual; M - Municipal; D - Distrital
   * - 15
     - unidadeSubRogada
     - Dados
     - Dados da Unidade Executora do Órgão subrogado
   * - 15.1
     - codigoUnidade
     - String
     - Código da Unidade Executora pertencente ao Órgão
   * - 15.2
     - nomeUnidade
     - String
     - Nome da Unidade Executora pertencente ao Órgão
   * - 15.3
     - codigoIbge
     - Inteiro
     - Código IBGE do município
   * - 15.4
     - municipioNome
     - String
     - Nome do município
   * - 15.5
     - ufSigla
     - String
     - Sigla da unidade federativa do município
   * - 15.6
     - ufNome
     - String
     - Nome da unidade federativa do município
   * - 16
     - tipoPessoa
     - Texto (2)
     - PJ - Pessoa jurídica; PF - Pessoa física; PE - Pessoa estrangeira;
   * - 17
     - niFornecedor
     - Texto (30)
     - Número de identificação do fornecedor/arrematante; CNPJ, CPF ou identificador de empresa estrangeira;
   * - 18
     - nomeRazaoSocialFornecedor
     - Texto (100)
     - Nome ou razão social do fornecedor/arrematante
   * - 19
     - tipoPessoaSubContratada
     - Texto (2)
     - PJ - Pessoa jurídica; PF - Pessoa física; PE - Pessoa estrangeira; Somente em caso de subcontratação;
   * - 20
     - niFornecedorSubContratado
     - Texto (30)
     - Número de identificação do fornecedor subcontratado; CNPJ, CPF ou identificador de empresa estrangeira; Somente em caso de subcontratação;
   * - 21
     - nomeFornecedorSubContratado
     - Texto (100)
     - Nome ou razão social do fornecedor subcontratado; Somente em caso de subcontratação;
   * - 22
     - valorInicial
     - Decimal
     - Valor inicial do contrato. Precisão de até 4 dígitos decimais; Ex: 100.0001;
   * - 23
     - numeroParcelas
     - Inteiro
     - Número de parcelas
   * - 24
     - valorParcela
     - Decimal
     - Valor da parcela. Precisão de até 4 dígitos decimais; Ex: 100.0001;
   * - 25
     - valorGlobal
     - Decimal
     - Valor global do contrato. Precisão de até 4 dígitos decimais; Ex: 100.0001;
   * - 26
     - valorAcumulado
     - Decimal
     - Valor acumulado do contrato. Precisão de até 4 dígitos decimais; Ex: 100.0001;
   * - 27
     - dataAssinatura
     - Data
     - Data de assinatura do contrato
   * - 28
     - dataVigenciaInicio
     - Data
     - Data de início de vigência do contrato
   * - 29
     - dataVigenciaFim
     - Data
     - Data do término da vigência do contrato
   * - 30
     - numeroRetificacao
     - Inteiro
     - Número de retificações; Número de vezes que este registro está sendo alterado;
   * - 31
     - usuarioNome
     - String
     - Nome do sistema/portal que enviou o contrato
   * - 32
     - dataPublicacaoPncp
     - Data/Hora
     - Data de publicação do contrato no PNCP
   * - 33
     - dataAtualizacao
     - Data/Hora
     - Data da última atualização do contrato no PNCP
   * - 34
     - identificadorCipi
     - String
     - Identificador do contrato no Cadastro Integrado de Projetos de Investimento
   * - 35
     - urlCipi
     - String
     - Url com informações do contrato no sistema de Cadastro Integrado de Projetos de Investimento

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

Em adição ao serviço **6.6. Serviço Consultar Contratos por Data de Publicação** mencionado neste manual, é importante destacar que o Portal Nacional de Contratações Públicas (PNCP) oferece uma gama ampla de funcionalidades via API que permitem uma consulta detalhada sobre **CONTRATAÇÕES**.

Estas funcionalidades estão minuciosamente descritas no Manual de Integração — Portal Nacional de Contratações Públicas - PNCP, disponível no site oficial `www.gov.br <https://www.gov.br>`_. Abaixo, apresentamos uma lista com alguns exemplos de serviços disponíveis:

- 6.5.7. Consultar Documento de um Contrato
- 6.5.9. Consultar Contratos de uma Contratação

Recomendamos a leitura detalhada do Manual de Integração do PNCP para uma compreensão abrangente de todas as funcionalidades e possibilidades oferecidas pela API.
