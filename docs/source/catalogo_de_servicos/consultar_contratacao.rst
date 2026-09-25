Consultar Contratação
======================

Serviço que permite consultar uma contratação.

Detalhes da Requisição
~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :width: 100%
   :widths: auto
   :header-rows: 1

   * - Endpoint
     - Método HTTP
   * - /v1/orgaos/{cnpj}/compras/{ano}/{sequencial} 
     - GET

Exemplo Requisição (cURL)
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash
  :linenos:

	curl -k -X GET \
	  "${BASE_URL}/v1/orgaos/10000000000003/compras/2021/1" \
	  -H "accept: */*"

Dados de Entrada
~~~~~~~~~~~~~~~~

.. note::
   Alimentar os parâmetros ``{cnpj}``, ``{ano}`` e ``{sequencial}`` na URL.

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
     - cnpj
     - Texto (14)
     - Sim
     - Cnpj do órgão originário da contratação informado na inclusão (proprietário da contratação ou alienação de bens)
   * - 2
     - ano
     - Inteiro
     - Sim
     - Ano da contratação
   * - 3
     - sequencial
     - Inteiro
     - Sim
     - Sequencial da contratação no PNCP; Número sequencial gerado no momento que a contratação foi inserida no PNCP

Dados de Retorno
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

   * - 1
     - valorTotalEstimado
     - Decimal
     - Valor total estimado da Contratação. Precisão de até 4 dígitos decimais; Ex: 100.0001; Obs: Retornará valor zero (0) se atributo orcamentoSigiloso for true e o item não possuir resultado.

   * - 2
     - valorTotalHomologado
     - Decimal
     - Valor total homologado com base nos resultados incluídos. Precisão de até 4 dígitos decimais; Ex: 100.0001;

   * - 3
     - orcamentoSigilosoCodigo
     - Inteiro
     - Código se a Compra tem itens cujo orçamento é sigiloso. 1 - COMPRA_SEM_SIGILO, 2 - COMPRA_PARCIALMENTE_SIGILOSA ou 3 - COMPRA TOTALMENTE SIGILOSA

   * - 4
     - orcamentoSigilosoDescricao
     - Texto
     - Descrição se a Compra tem itens cujo orçamento é sigiloso. 1 - COMPRA_SEM_SIGILO, 2 - COMPRA_PARCIALMENTE_SIGILOSA ou 3 - COMPRA TOTALMENTE SIGILOSA

   * - 5
     - numeroControlePNCP
     - Texto
     - Número de Controle PNCP da Contratação (id Contratação PNCP)

   * - 6
     - linkSistemaOrigem
     - Texto
     - URL para página/portal do sistema de origem da contratação para recebimento de propostas.

   * - 7
     - linkProcessoEletronico
     - Texto
     - URL para página do sistema de controle de processos eletrônicos com os dados do processo desta contratação.

   * - 8
     - anoCompra
     - Inteiro
     - Ano da contratação

   * - 9
     - sequencialCompra
     - Inteiro
     - Sequencial da Contratação no PNCP; Número sequencial gerado no momento que a contratação foi inserida no PNCP;

   * - 10
     - numeroCompra
     - Texto (50)
     - Número da contratação no sistema de origem

   * - 11
     - processo
     - Texto (50)
     - Número do processo de Contratação no sistema de origem

   * - 12
     - orgaoEntidade
     - Lista
     - Dados do órgão/entidade

   * - 12.1
     - cnpj
     - Texto
     - CNPJ do Órgão referente à Contratação

   * - 12.2
     - esferaId
     - Texto
     - Código da esfera a que pertence o Órgão. F - Federal; E - Estadual; M - Municipal; D - Distrital

   * - 12.3
     - razaoSocial
     - Texto
     - Razão social do Órgão referente à Contratação

   * - 12.4
     - poderId
     - Texto
     - Código do poder a que pertence o Órgão. L - Legislativo; E - Executivo; J - Judiciário

   * - 13
     - unidadeOrgao
     - Lista
     - Dados da unidade administrativa

   * - 13.1
     - ufNome
     - Texto
     - Nome da unidade federativa do município (UF)

   * - 13.2
     - ufSigla
     - Texto
     - Sigla da unidade federativa do município (UF)

   * - 13.3
     - municipioNome
     - Texto
     - Nome do município

   * - 13.4
     - codigoUnidade
     - Texto
     - Código da Unidade Administrativa pertencente ao Órgão

   * - 13.5
     - nomeUnidade
     - Texto
     - Nome da Unidade Administrativa pertencente ao Órgão

   * - 13.6
     - codigoIbge
     - Inteiro
     - Código IBGE do município

   * - 14
     - orgaoSubRogado
     - Lista
     - Dados do Órgão/Entidade subrogado

   * - 14.1
     - cnpj
     - Texto
     - CNPJ do Órgão referente à Contratação

   * - 14.2
     - esferaId
     - Texto
     - Código da esfera a que pertence o Órgão. F - Federal; E - Estadual; M - Municipal; D - Distrital

   * - 14.3
     - razaoSocial
     - Texto
     - Razão social do Órgão referente à Contratação

   * - 14.4
     - poderId
     - Texto
     - Código do poder a que pertence o Órgão. L - Legislativo; E - Executivo; J - Judiciário

   * - 15
     - unidadeSubRogada
     - Lista
     - Código da Unidade Administrativa pertencente ao Órgão subrogado

   * - 15.1
     - ufNome
     - Texto
     - Nome da unidade federativa do município (UF)

   * - 15.2
     - ufSigla
     - Texto
     - Sigla da unidade federativa do município (UF)

   * - 15.3
     - municipioNome
     - Texto
     - Nome do município

   * - 15.4
     - codigoUnidade
     - Texto
     - Nome da Unidade Administrativa pertencente ao Órgão subrogado

   * - 15.5
     - nomeUnidade
     - Texto
     - Nome da unidade

   * - 15.6
     - codigoIbge
     - Inteiro
     - Código IBGE do município

   * - 16
     - modalidadeId
     - Inteiro
     - Código da Modalidade referente à Contratação

   * - 17
     - modalidadeNome
     - Texto
     - Modalidade referente à Contratação

   * - 18
     - justificativaPresencial
     - Texto
     - Justificativa pela escolha da modalidade presencial.

   * - 19
     - modoDisputaId
     - Inteiro
     - Código do modo de disputa referente à Contratação

   * - 20
     - modoDisputaNome
     - Texto
     - Modo de disputa referente à Contratação

   * - 21
     - tipoInstrumentoConvocatorioCodigo
     - Inteiro
     - Código do instrumento convocatório da Contratação

   * - 22
     - tipoInstrumentoConvocatorioNome
     - Texto
     - Nome do instrumento convocatório da Contratação

   * - 23
     - amparoLegal
     - Lista
     - Dados do Amparo Legal

   * - 23.1
     - codigo
     - Inteiro
     - Código do Amparo Legal.

   * - 23.2
     - descricao
     - Texto (100)
     - Descrição do Amparo Legal da tabela de domínio Amparo legal

   * - 23.3
     - nome
     - String
     - Amparo Legal da tabela de domínio Amparo Legal

   * - 24
     - objetoCompra
     - Texto (5120)
     - Descrição do objeto da contratação

   * - 25
     - informacaoComplementar
     - Texto (5120)
     - Informação Complementar do objeto referente à Contratação

   * - 26
     - srp
     - Booleano
     - Identifica se a compra se trata de um SRP (Sistema de registro de preços)

   * - 27
     - fontesOrcamentarias
     - Lista
     - Lista de fontes orçamentárias da contratação

   * - 27.1
     - codigo
     - Inteiro
     - Código da fonte orçamentária

   * - 27.2
     - nome
     - Texto
     - Nome da fonte orçamentária

   * - 27.3
     - descricao
     - Texto
     - Descrição da fonte orçamentária

   * - 27.4
     - dataInclusao
     - Data/Hora
     - Data/hora da inclusão da fonte orçamentária na contratação

   * - 28
     - emendaParlamentar
     - Booleano
     - Marcador de existência de emenda parlamentar na contratação (False – Não / True – Sim )

   * - 29
     - dataPublicacaoPncp
     - Data
     - Data da publicação da Contratação no PNCP

   * - 30
     - dataAberturaProposta
     - Data/Hora
     - Data de abertura do recebimento de propostas (horário de Brasília)

   * - 31
     - dataEncerramentoProposta
     - Data/Hora
     - Data de encerramento do recebimento de propostas (horário de Brasília)

   * - 32
     - situacaoCompraId
     - Inteiro
     - Código da situação da Contratação

   * - 33
     - situacaoCompraNome
     - Texto
     - Nome da situação da contratação

   * - 34
     - dataInclusao
     - Data
     - Data da inclusão do registro da Contratação no PNCP

   * - 35
     - dataAtualizacao
     - Data
     - Data da última atualização do registro da Contratação

   * - 36
     - dataAtualizacaoGlobal
     - Data
     - Data da última atualização global do registro da Contratação considerando seus dependentes (item da contratação, resultado da contratação, documento da contratação e imagem de item da contratação)

   * - 37
     - usuarioNome
     - Texto
     - Nome do Usuário/Sistema que enviou a Contratação

   * - 38
     - existeResultado
     - Booleano
     - Marcador de existência de resultado na contratação (False – Não / True – Sim )
 
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
