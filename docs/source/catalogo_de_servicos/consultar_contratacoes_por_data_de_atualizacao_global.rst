Consultar Contratações por Data de Atualização Global
======================================================

Serviço destinado à consulta das contratações que foram incluídas ou que sofreram alterações no PNCP durante um determinado intervalo de datas, considerando a data de atualização global do registro.

Detalhes de Requisição
~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :width: 100%
   :widths: auto
   :header-rows: 1

   * - Endpoint
     - Método HTTP
   * - /v1/contratacoes/atualizacao
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
     'https://pncp.gov.br/api/consulta/v1/contratacoes/atualizacao?dataInicial=20260101&dataFinal=20260101&codigoModalidadeContratacao=2&pagina=3' \
     -H 'accept: */*'

Dados de entrada
~~~~~~~~~~~~~~~~

.. note::

   Alimentar os parâmetros ``{dataInicial}``, ``{dataFinal}``, ``{codigoModalidadeContratacao}`` e ``{pagina}`` na URL.

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
     - :destaque-amarelo-claro:`dataFinal`
     - :destaque-amarelo-claro:`String`
     - :destaque-amarelo-claro:`Sim`
     - :destaque-amarelo-claro:`Data final do período a ser consultado no formato AAAAMMDD.`
   * - :destaque-amarelo-claro:`3`
     - :destaque-amarelo-claro:`codigoModalidadeContratacao`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Sim`
     - :destaque-amarelo-claro:`Código da tabela de domínio referente à Modalidade da Contratação.`
   * - :destaque-amarelo-claro:`4`
     - :destaque-amarelo-claro:`codigoModoDisputa`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Não`
     - :destaque-amarelo-claro:`Código da tabela de domínio referente ao Modo de Disputa.`
   * - :destaque-amarelo-claro:`5`
     - :destaque-amarelo-claro:`uf`
     - :destaque-amarelo-claro:`String`
     - :destaque-amarelo-claro:`Não`
     - :destaque-amarelo-claro:`Sigla da Unidade Federativa referente à Unidade Administrativa do órgão.`
   * - :destaque-amarelo-claro:`6`
     - :destaque-amarelo-claro:`codigoMunicipioIbge`
     - :destaque-amarelo-claro:`String`
     - :destaque-amarelo-claro:`Não`
     - :destaque-amarelo-claro:`Código IBGE do Município da Unidade Administrativa.`
   * - :destaque-amarelo-claro:`7`
     - :destaque-amarelo-claro:`cnpj`
     - :destaque-amarelo-claro:`String`
     - :destaque-amarelo-claro:`Não`
     - :destaque-amarelo-claro:`Cnpj do órgão originário da contratação informado na inclusão (proprietário da contratação).`
   * - :destaque-amarelo-claro:`8`
     - :destaque-amarelo-claro:`codigoUnidadeAdministrativa`
     - :destaque-amarelo-claro:`String`
     - :destaque-amarelo-claro:`Não`
     - :destaque-amarelo-claro:`Código da Unidade Administrativa do Órgão originário da contratação informado na inclusão (proprietário da contratação).`
   * - :destaque-amarelo-claro:`9`
     - :destaque-amarelo-claro:`idUsuario`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Não`
     - :destaque-amarelo-claro:`Identificado do sistema usuário (Sistema de Contratações Públicas) que publicou a contratação.`
   * - :destaque-amarelo-claro:`10`
     - :destaque-amarelo-claro:`pagina`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Sim`
     - :destaque-amarelo-claro:`Número da página que se deseja obter os dados.`
   * - :destaque-amarelo-claro:`11`
     - :destaque-amarelo-claro:`tamanhoPagina`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Não`
     - :destaque-amarelo-claro:`Por padrão cada página contém no máximo 500 registros, no entanto o tamanho de registros em cada página pode ser ajustado (até o limite de 500 registros) com vistas a tornar a entrega de dados mais rápida.`

Dados de retorno
~~~~~~~~~~~~~~~~

.. list-table::
   :width: 100%
   :widths: 5 25 15 55
   :header-rows: 1
   :class: quebra-linha-dois-ultima

   * - Id
     - Campo
     - Tipo
     - Descrição
   * - :destaque-amarelo-claro:`1`
     - :destaque-amarelo-claro:`data`
     - :destaque-amarelo-claro:`Lista`
     - :destaque-amarelo-claro:`Lista com os dados das contratações encontradas.`
   * - :destaque-amarelo-claro:`1.1`
     - :destaque-amarelo-claro:`valorTotalHomologado`
     - :destaque-amarelo-claro:`Decimal`
     - :destaque-amarelo-claro:`Valor total homologado com base nos resultados incluídos. Precisão de até 4 dígitos decimais; Ex: 100.0001.`
   * - :destaque-amarelo-claro:`1.2`
     - :destaque-amarelo-claro:`dataAberturaProposta`
     - :destaque-amarelo-claro:`Data/Hora`
     - :destaque-amarelo-claro:`Data de abertura do recebimento de propostas (horário de Brasília).`
   * - :destaque-amarelo-claro:`1.3`
     - :destaque-amarelo-claro:`informacaoComplementar`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Informação Complementar do objeto referente à Contratação.`
   * - :destaque-amarelo-claro:`1.4`
     - :destaque-amarelo-claro:`processo`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Número do processo de Contratação no sistema de origem.`
   * - :destaque-amarelo-claro:`1.5`
     - :destaque-amarelo-claro:`objetoCompra`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Descrição do Objeto referente à Contratação.`
   * - :destaque-amarelo-claro:`1.6`
     - :destaque-amarelo-claro:`linkSistemaOrigem`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`URL para página/portal do sistema de origem da contratação para recebimento de propostas.`
   * - :destaque-amarelo-claro:`1.7`
     - :destaque-amarelo-claro:`justificativaPresencial`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Justificativa pela escolha da modalidade presencial.`
   * - :destaque-amarelo-claro:`1.8`
     - :destaque-amarelo-claro:`unidadeSubRogada`
     - :destaque-amarelo-claro:`Lista`
     - :destaque-amarelo-claro:`Dados da unidade administrativa subrogada.`
   * - :destaque-amarelo-claro:`1.8.1`
     - :destaque-amarelo-claro:`ufNome`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome da unidade federativa do município.`
   * - :destaque-amarelo-claro:`1.8.2`
     - :destaque-amarelo-claro:`ufSigla`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Sigla da unidade federativa do município.`
   * - :destaque-amarelo-claro:`1.8.3`
     - :destaque-amarelo-claro:`municipioNome`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome do município.`
   * - :destaque-amarelo-claro:`1.8.4`
     - :destaque-amarelo-claro:`codigoUnidade`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Código da Unidade Administrativa pertencente ao Órgão subrogado.`
   * - :destaque-amarelo-claro:`1.8.5`
     - :destaque-amarelo-claro:`nomeUnidade`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome da Unidade Administrativa pertencente ao Órgão subrogado.`
   * - :destaque-amarelo-claro:`1.8.6`
     - :destaque-amarelo-claro:`codigoIbge`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Código IBGE do município.`
   * - :destaque-amarelo-claro:`1.9`
     - :destaque-amarelo-claro:`orgaoSubRogado`
     - :destaque-amarelo-claro:`Lista`
     - :destaque-amarelo-claro:`Dados do órgão/entidade subrogado.`
   * - :destaque-amarelo-claro:`1.9.1`
     - :destaque-amarelo-claro:`cnpj`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`CNPJ do Órgão referente à Contratação.`
   * - :destaque-amarelo-claro:`1.9.2`
     - :destaque-amarelo-claro:`esferaId`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Código da esfera a que pertence o Órgão. F - Federal; E - Estadual; M - Municipal; D - Distrital.`
   * - :destaque-amarelo-claro:`1.9.3`
     - :destaque-amarelo-claro:`razaoSocial`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Razão social do Órgão referente à Contratação.`
   * - :destaque-amarelo-claro:`1.9.4`
     - :destaque-amarelo-claro:`poderId`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Código do poder a que pertence o Órgão. L - Legislativo; E - Executivo; J - Judiciário.`
   * - :destaque-amarelo-claro:`1.10`
     - :destaque-amarelo-claro:`amparoLegal`
     - :destaque-amarelo-claro:`Lista`
     - :destaque-amarelo-claro:`Dados do amparo legal.`
   * - :destaque-amarelo-claro:`1.10.1`
     - :destaque-amarelo-claro:`codigo`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Código do Amparo Legal.`
   * - :destaque-amarelo-claro:`1.10.2`
     - :destaque-amarelo-claro:`descricao`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Descrição do Amparo legal.`
   * - :destaque-amarelo-claro:`1.10.3`
     - :destaque-amarelo-claro:`nome`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome do Amparo Legal.`
   * - :destaque-amarelo-claro:`1.11`
     - :destaque-amarelo-claro:`dataEncerramentoProposta`
     - :destaque-amarelo-claro:`Data/Hora`
     - :destaque-amarelo-claro:`Data de encerramento do recebimento de propostas (horário de Brasília).`
   * - :destaque-amarelo-claro:`1.12`
     - :destaque-amarelo-claro:`srp`
     - :destaque-amarelo-claro:`Booleano`
     - :destaque-amarelo-claro:`Identifica se a compra trata-se de um SRP (Sistema de registro de preços).`
   * - :destaque-amarelo-claro:`1.13`
     - :destaque-amarelo-claro:`orgaoEntidade`
     - :destaque-amarelo-claro:`Lista`
     - :destaque-amarelo-claro:`Dados do órgão/entidade.`
   * - :destaque-amarelo-claro:`1.13.1`
     - :destaque-amarelo-claro:`cnpj`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`CNPJ do Órgão referente à Contratação.`
   * - :destaque-amarelo-claro:`1.13.2`
     - :destaque-amarelo-claro:`esferaId`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Código da esfera a que pertence o Órgão. F - Federal; E - Estadual; M - Municipal; D - Distrital.`
   * - :destaque-amarelo-claro:`1.13.3`
     - :destaque-amarelo-claro:`razaoSocial`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Razão social do Órgão referente à Contratação.`
   * - :destaque-amarelo-claro:`1.13.4`
     - :destaque-amarelo-claro:`poderId`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Código do poder a que pertence o Órgão. L - Legislativo; E - Executivo; J - Judiciário.`
   * - :destaque-amarelo-claro:`1.14`
     - :destaque-amarelo-claro:`anoCompra`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Ano da Contratação.`
   * - :destaque-amarelo-claro:`1.15`
     - :destaque-amarelo-claro:`sequencialCompra`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Sequencial da Contratação no PNCP; Número sequencial gerado no momento que a contratação foi inserida no PNCP.`
   * - :destaque-amarelo-claro:`1.16`
     - :destaque-amarelo-claro:`dataInclusao`
     - :destaque-amarelo-claro:`Data/Hora`
     - :destaque-amarelo-claro:`Data da inclusão do registro da Contratação no PNCP.`
   * - :destaque-amarelo-claro:`1.17`
     - :destaque-amarelo-claro:`dataPublicacaoPncp`
     - :destaque-amarelo-claro:`Data/Hora`
     - :destaque-amarelo-claro:`Data da publicação da Contratação no PNCP.`
   * - :destaque-amarelo-claro:`1.18`
     - :destaque-amarelo-claro:`dataAtualizacao`
     - :destaque-amarelo-claro:`Data/Hora`
     - :destaque-amarelo-claro:`Data da última atualização do registro da Contratação.`
   * - :destaque-amarelo-claro:`1.19`
     - :destaque-amarelo-claro:`numeroCompra`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Número da Contratação no sistema de origem.`
   * - :destaque-amarelo-claro:`1.20`
     - :destaque-amarelo-claro:`unidadeOrgao`
     - :destaque-amarelo-claro:`Lista`
     - :destaque-amarelo-claro:`Dados da unidade administrativa.`
   * - :destaque-amarelo-claro:`1.20.1`
     - :destaque-amarelo-claro:`ufNome`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome da unidade federativa do município.`
   * - :destaque-amarelo-claro:`1.20.2`
     - :destaque-amarelo-claro:`ufSigla`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Sigla da unidade federativa do município.`
   * - :destaque-amarelo-claro:`1.20.3`
     - :destaque-amarelo-claro:`municipioNome`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome do município.`
   * - :destaque-amarelo-claro:`1.20.4`
     - :destaque-amarelo-claro:`codigoUnidade`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Código da Unidade Administrativa pertencente ao Órgão.`
   * - :destaque-amarelo-claro:`1.20.5`
     - :destaque-amarelo-claro:`nomeUnidade`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome da Unidade Administrativa pertencente ao Órgão.`
   * - :destaque-amarelo-claro:`1.20.6`
     - :destaque-amarelo-claro:`codigoIbge`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Código IBGE do município.`
   * - :destaque-amarelo-claro:`1.21`
     - :destaque-amarelo-claro:`modoDisputaId`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Código do modo de disputa referente à Contratação.`
   * - :destaque-amarelo-claro:`1.22`
     - :destaque-amarelo-claro:`emendaParlamentar`
     - :destaque-amarelo-claro:`Booleano`
     - :destaque-amarelo-claro:`Marcador de existência de emenda parlamentar na contratação.`
   * - :destaque-amarelo-claro:`1.23`
     - :destaque-amarelo-claro:`numeroControlePNCP`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Número de Controle PNCP da Contratação (id Contratação PNCP).`
   * - :destaque-amarelo-claro:`1.24`
     - :destaque-amarelo-claro:`modalidadeId`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Código da Modalidade referente à Contratação.`
   * - :destaque-amarelo-claro:`1.25`
     - :destaque-amarelo-claro:`linkProcessoEletronico`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`URL para página do sistema de controle de processos eletrônicos com os dados do processo desta contratação.`
   * - :destaque-amarelo-claro:`1.26`
     - :destaque-amarelo-claro:`dataAtualizacaoGlobal`
     - :destaque-amarelo-claro:`Data/Hora`
     - :destaque-amarelo-claro:`Data da última atualização global do registro da Contratação considerando seus dependentes (item da contratação, resultado da contratação, documento da contratação e imagem de item da contratação).`
   * - :destaque-amarelo-claro:`1.27`
     - :destaque-amarelo-claro:`valorTotalEstimado`
     - :destaque-amarelo-claro:`Decimal`
     - :destaque-amarelo-claro:`Valor total estimado da Contratação. Precisão de até 4 dígitos decimais; Ex: 100.0001; Obs: Retornará valor zero (0) se atributo orcamentoSigiloso for true e o item não possuir resultado.`
   * - :destaque-amarelo-claro:`1.28`
     - :destaque-amarelo-claro:`modalidadeNome`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Modalidade referente à Contratação.`
   * - :destaque-amarelo-claro:`1.29`
     - :destaque-amarelo-claro:`modoDisputaNome`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Modo de disputa referente à Contratação.`
   * - :destaque-amarelo-claro:`1.30`
     - :destaque-amarelo-claro:`tipoInstrumentoConvocatorioCodigo`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Código do instrumento convocatório da Contratação.`
   * - :destaque-amarelo-claro:`1.31`
     - :destaque-amarelo-claro:`tipoInstrumentoConvocatorioNome`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome do instrumento convocatório da Contratação.`
   * - :destaque-amarelo-claro:`1.32`
     - :destaque-amarelo-claro:`fontesOrcamentarias`
     - :destaque-amarelo-claro:`Lista`
     - :destaque-amarelo-claro:`Lista de fontes orçamentárias da contratação.`
   * - :destaque-amarelo-claro:`1.32.1`
     - :destaque-amarelo-claro:`codigo`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Código da fonte orçamentária.`
   * - :destaque-amarelo-claro:`1.32.2`
     - :destaque-amarelo-claro:`nome`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome da fonte orçamentária.`
   * - :destaque-amarelo-claro:`1.32.3`
     - :destaque-amarelo-claro:`descricao`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Descrição da fonte orçamentária.`
   * - :destaque-amarelo-claro:`1.32.4`
     - :destaque-amarelo-claro:`dataInclusao`
     - :destaque-amarelo-claro:`Data/Hora`
     - :destaque-amarelo-claro:`Data/hora da inclusão da fonte orçamentária na contratação.`
   * - :destaque-amarelo-claro:`1.33`
     - :destaque-amarelo-claro:`situacaoCompraId`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Código da situação da Contratação.`
   * - :destaque-amarelo-claro:`1.34`
     - :destaque-amarelo-claro:`situacaoCompraNome`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Situação da Contratação.`
   * - :destaque-amarelo-claro:`1.35`
     - :destaque-amarelo-claro:`usuarioNome`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome do Usuário/Sistema que enviou a Contratação.`
   * - :destaque-amarelo-claro:`2`
     - :destaque-amarelo-claro:`totalRegistros`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Total de registros encontrados.`
   * - :destaque-amarelo-claro:`3`
     - :destaque-amarelo-claro:`totalPaginas`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Total de páginas necessárias para a obtenção de todos os registros.`
   * - :destaque-amarelo-claro:`4`
     - :destaque-amarelo-claro:`numeroPagina`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Número da página que a consulta foi realizada.`
   * - :destaque-amarelo-claro:`5`
     - :destaque-amarelo-claro:`paginasRestantes`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Total de páginas restantes.`
   * - :destaque-amarelo-claro:`6`
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
