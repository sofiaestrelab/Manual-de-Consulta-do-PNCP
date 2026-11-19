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
  :emphasize-lines: 1-3

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
   * - :destaque-amarelo-claro:`1`
     - :destaque-amarelo-claro:`cnpj`
     - :destaque-amarelo-claro:`Texto (14)`
     - :destaque-amarelo-claro:`Sim`
     - :destaque-amarelo-claro:`Cnpj do órgão originário da contratação informado na inclusão (proprietário da contratação ou alienação de bens).`
   * - :destaque-amarelo-claro:`2`
     - :destaque-amarelo-claro:`ano`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Sim`
     - :destaque-amarelo-claro:`Ano da contratação.`
   * - :destaque-amarelo-claro:`3`
     - :destaque-amarelo-claro:`sequencial`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Sim`
     - :destaque-amarelo-claro:`Sequencial da contratação no PNCP; Número sequencial gerado no momento que a contratação foi inserida no PNCP.`

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

   * - :destaque-amarelo-claro:`1`
     - :destaque-amarelo-claro:`valorTotalEstimado`
     - :destaque-amarelo-claro:`Decimal`
     - :destaque-amarelo-claro:`Valor total estimado da Contratação. Precisão de até 4 dígitos decimais; Ex: 100.0001; Obs: Retornará valor zero (0) se atributo orcamentoSigiloso for true e o item não possuir resultado.`
   * - :destaque-amarelo-claro:`2`
     - :destaque-amarelo-claro:`valorTotalHomologado`
     - :destaque-amarelo-claro:`Decimal`
     - :destaque-amarelo-claro:`Valor total homologado com base nos resultados incluídos. Precisão de até 4 dígitos decimais; Ex: 100.0001.`
   * - :destaque-amarelo-claro:`3`
     - :destaque-amarelo-claro:`orcamentoSigilosoCodigo`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Código se a Compra tem itens cujo orçamento é sigiloso. 1 - COMPRA_SEM_SIGILO, 2 - COMPRA_PARCIALMENTE_SIGILOSA ou 3 - COMPRA TOTALMENTE SIGILOSA.`
   * - :destaque-amarelo-claro:`4`
     - :destaque-amarelo-claro:`orcamentoSigilosoDescricao`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Descrição se a Compra tem itens cujo orçamento é sigiloso. 1 - COMPRA_SEM_SIGILO, 2 - COMPRA_PARCIALMENTE_SIGILOSA ou 3 - COMPRA TOTALMENTE SIGILOSA.`
   * - :destaque-amarelo-claro:`5`
     - :destaque-amarelo-claro:`numeroControlePNCP`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Número de Controle PNCP da Contratação (id Contratação PNCP).`
   * - :destaque-amarelo-claro:`6`
     - :destaque-amarelo-claro:`linkSistemaOrigem`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`URL para página/portal do sistema de origem da contratação para recebimento de propostas.`
   * - :destaque-amarelo-claro:`7`
     - :destaque-amarelo-claro:`linkProcessoEletronico`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`URL para página do sistema de controle de processos eletrônicos com os dados do processo desta contratação.`
   * - :destaque-amarelo-claro:`8`
     - :destaque-amarelo-claro:`anoCompra`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Ano da contratação.`
   * - :destaque-amarelo-claro:`9`
     - :destaque-amarelo-claro:`sequencialCompra`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Sequencial da Contratação no PNCP; Número sequencial gerado no momento que a contratação foi inserida no PNCP.`
   * - :destaque-amarelo-claro:`10`
     - :destaque-amarelo-claro:`numeroCompra`
     - :destaque-amarelo-claro:`Texto (50)`
     - :destaque-amarelo-claro:`Número da contratação no sistema de origem.`
   * - :destaque-amarelo-claro:`11`
     - :destaque-amarelo-claro:`processo`
     - :destaque-amarelo-claro:`Texto (50)`
     - :destaque-amarelo-claro:`Número do processo de Contratação no sistema de origem.`
   * - :destaque-amarelo-claro:`12`
     - :destaque-amarelo-claro:`orgaoEntidade`
     - :destaque-amarelo-claro:`Lista`
     - :destaque-amarelo-claro:`Dados do órgão/entidade.`
   * - :destaque-amarelo-claro:`12.1`
     - :destaque-amarelo-claro:`cnpj`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`CNPJ do Órgão referente à Contratação.`
   * - :destaque-amarelo-claro:`12.2`
     - :destaque-amarelo-claro:`esferaId`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Código da esfera a que pertence o Órgão. F - Federal; E - Estadual; M - Municipal; D - Distrital.`
   * - :destaque-amarelo-claro:`12.3`
     - :destaque-amarelo-claro:`razaoSocial`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Razão social do Órgão referente à Contratação.`
   * - :destaque-amarelo-claro:`12.4`
     - :destaque-amarelo-claro:`poderId`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Código do poder a que pertence o Órgão. L - Legislativo; E - Executivo; J - Judiciário.`
   * - :destaque-amarelo-claro:`13`
     - :destaque-amarelo-claro:`unidadeOrgao`
     - :destaque-amarelo-claro:`Lista`
     - :destaque-amarelo-claro:`Dados da unidade administrativa.`
   * - :destaque-amarelo-claro:`13.1`
     - :destaque-amarelo-claro:`ufNome`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome da unidade federativa do município (UF).`
   * - :destaque-amarelo-claro:`13.2`
     - :destaque-amarelo-claro:`ufSigla`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Sigla da unidade federativa do município (UF).`
   * - :destaque-amarelo-claro:`13.3`
     - :destaque-amarelo-claro:`municipioNome`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome do município.`
   * - :destaque-amarelo-claro:`13.4`
     - :destaque-amarelo-claro:`codigoUnidade`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Código da Unidade Administrativa pertencente ao Órgão.`
   * - :destaque-amarelo-claro:`13.5`
     - :destaque-amarelo-claro:`nomeUnidade`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome da Unidade Administrativa pertencente ao Órgão.`
   * - :destaque-amarelo-claro:`13.6`
     - :destaque-amarelo-claro:`codigoIbge`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Código IBGE do município.`
   * - :destaque-amarelo-claro:`14`
     - :destaque-amarelo-claro:`orgaoSubRogado`
     - :destaque-amarelo-claro:`Lista`
     - :destaque-amarelo-claro:`Dados do Órgão/Entidade subrogado.`
   * - :destaque-amarelo-claro:`14.1`
     - :destaque-amarelo-claro:`cnpj`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`CNPJ do Órgão referente à Contratação.`
   * - :destaque-amarelo-claro:`14.2`
     - :destaque-amarelo-claro:`esferaId`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Código da esfera a que pertence o Órgão. F - Federal; E - Estadual; M - Municipal; D - Distrital.`
   * - :destaque-amarelo-claro:`14.3`
     - :destaque-amarelo-claro:`razaoSocial`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Razão social do Órgão referente à Contratação.`
   * - :destaque-amarelo-claro:`14.4`
     - :destaque-amarelo-claro:`poderId`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Código do poder a que pertence o Órgão. L - Legislativo; E - Executivo; J - Judiciário.`
   * - :destaque-amarelo-claro:`15`
     - :destaque-amarelo-claro:`unidadeSubRogada`
     - :destaque-amarelo-claro:`Lista`
     - :destaque-amarelo-claro:`Código da Unidade Administrativa pertencente ao Órgão subrogado.`
   * - :destaque-amarelo-claro:`15.1`
     - :destaque-amarelo-claro:`ufNome`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome da unidade federativa do município (UF).`
   * - :destaque-amarelo-claro:`15.2`
     - :destaque-amarelo-claro:`ufSigla`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Sigla da unidade federativa do município (UF).`
   * - :destaque-amarelo-claro:`15.3`
     - :destaque-amarelo-claro:`municipioNome`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome do município.`
   * - :destaque-amarelo-claro:`15.4`
     - :destaque-amarelo-claro:`codigoUnidade`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome da Unidade Administrativa pertencente ao Órgão subrogado.`
   * - :destaque-amarelo-claro:`15.5`
     - :destaque-amarelo-claro:`nomeUnidade`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome da unidade.`
   * - :destaque-amarelo-claro:`15.6`
     - :destaque-amarelo-claro:`codigoIbge`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Código IBGE do município.`
   * - :destaque-amarelo-claro:`16`
     - :destaque-amarelo-claro:`modalidadeId`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Código da Modalidade referente à Contratação.`
   * - :destaque-amarelo-claro:`17`
     - :destaque-amarelo-claro:`modalidadeNome`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Modalidade referente à Contratação.`
   * - :destaque-amarelo-claro:`18`
     - :destaque-amarelo-claro:`justificativaPresencial`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Justificativa pela escolha da modalidade presencial.`
   * - :destaque-amarelo-claro:`19`
     - :destaque-amarelo-claro:`modoDisputaId`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Código do modo de disputa referente à Contratação.`
   * - :destaque-amarelo-claro:`20`
     - :destaque-amarelo-claro:`modoDisputaNome`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Modo de disputa referente à Contratação.`
   * - :destaque-amarelo-claro:`21`
     - :destaque-amarelo-claro:`tipoInstrumentoConvocatorioCodigo`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Código do instrumento convocatório da Contratação.`
   * - :destaque-amarelo-claro:`22`
     - :destaque-amarelo-claro:`tipoInstrumentoConvocatorioNome`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome do instrumento convocatório da Contratação.`
   * - :destaque-amarelo-claro:`23`
     - :destaque-amarelo-claro:`amparoLegal`
     - :destaque-amarelo-claro:`Lista`
     - :destaque-amarelo-claro:`Dados do Amparo Legal.`
   * - :destaque-amarelo-claro:`23.1`
     - :destaque-amarelo-claro:`codigo`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Código do Amparo Legal.`
   * - :destaque-amarelo-claro:`23.2`
     - :destaque-amarelo-claro:`descricao`
     - :destaque-amarelo-claro:`Texto (100)`
     - :destaque-amarelo-claro:`Descrição do Amparo Legal da tabela de domínio Amparo legal.`
   * - :destaque-amarelo-claro:`23.3`
     - :destaque-amarelo-claro:`nome`
     - :destaque-amarelo-claro:`String`
     - :destaque-amarelo-claro:`Amparo Legal da tabela de domínio Amparo Legal.`
   * - :destaque-amarelo-claro:`24`
     - :destaque-amarelo-claro:`objetoCompra`
     - :destaque-amarelo-claro:`Texto (5120)`
     - :destaque-amarelo-claro:`Descrição do objeto da contratação.`
   * - :destaque-amarelo-claro:`25`
     - :destaque-amarelo-claro:`informacaoComplementar`
     - :destaque-amarelo-claro:`Texto (5120)`
     - :destaque-amarelo-claro:`Informação Complementar do objeto referente à Contratação.`
   * - :destaque-amarelo-claro:`26`
     - :destaque-amarelo-claro:`srp`
     - :destaque-amarelo-claro:`Booleano`
     - :destaque-amarelo-claro:`Identifica se a compra se trata de um SRP (Sistema de registro de preços).`
   * - :destaque-amarelo-claro:`27`
     - :destaque-amarelo-claro:`fontesOrcamentarias`
     - :destaque-amarelo-claro:`Lista`
     - :destaque-amarelo-claro:`Lista de fontes orçamentárias da contratação.`
   * - :destaque-amarelo-claro:`27.1`
     - :destaque-amarelo-claro:`codigo`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Código da fonte orçamentária.`
   * - :destaque-amarelo-claro:`27.2`
     - :destaque-amarelo-claro:`nome`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome da fonte orçamentária.`
   * - :destaque-amarelo-claro:`27.3`
     - :destaque-amarelo-claro:`descricao`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Descrição da fonte orçamentária.`
   * - :destaque-amarelo-claro:`27.4`
     - :destaque-amarelo-claro:`dataInclusao`
     - :destaque-amarelo-claro:`Data/Hora`
     - :destaque-amarelo-claro:`Data/hora da inclusão da fonte orçamentária na contratação.`
   * - :destaque-amarelo-claro:`28`
     - :destaque-amarelo-claro:`emendaParlamentar`
     - :destaque-amarelo-claro:`Booleano`
     - :destaque-amarelo-claro:`Marcador de existência de emenda parlamentar na contratação (False – Não / True – Sim).`
   * - :destaque-amarelo-claro:`29`
     - :destaque-amarelo-claro:`dataPublicacaoPncp`
     - :destaque-amarelo-claro:`Data`
     - :destaque-amarelo-claro:`Data da publicação da Contratação no PNCP.`
   * - :destaque-amarelo-claro:`30`
     - :destaque-amarelo-claro:`dataAberturaProposta`
     - :destaque-amarelo-claro:`Data/Hora`
     - :destaque-amarelo-claro:`Data de abertura do recebimento de propostas (horário de Brasília).`
   * - :destaque-amarelo-claro:`31`
     - :destaque-amarelo-claro:`dataEncerramentoProposta`
     - :destaque-amarelo-claro:`Data/Hora`
     - :destaque-amarelo-claro:`Data de encerramento do recebimento de propostas (horário de Brasília).`
   * - :destaque-amarelo-claro:`32`
     - :destaque-amarelo-claro:`situacaoCompraId`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Código da situação da Contratação.`
   * - :destaque-amarelo-claro:`33`
     - :destaque-amarelo-claro:`situacaoCompraNome`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome da situação da contratação.`
   * - :destaque-amarelo-claro:`34`
     - :destaque-amarelo-claro:`dataInclusao`
     - :destaque-amarelo-claro:`Data`
     - :destaque-amarelo-claro:`Data da inclusão do registro da Contratação no PNCP.`
   * - :destaque-amarelo-claro:`35`
     - :destaque-amarelo-claro:`dataAtualizacao`
     - :destaque-amarelo-claro:`Data`
     - :destaque-amarelo-claro:`Data da última atualização do registro da Contratação.`
   * - :destaque-amarelo-claro:`36`
     - :destaque-amarelo-claro:`dataAtualizacaoGlobal`
     - :destaque-amarelo-claro:`Data`
     - :destaque-amarelo-claro:`Data da última atualização global do registro da Contratação considerando seus dependentes (item da contratação, resultado da contratação, documento da contratação e imagem de item da contratação).`
   * - :destaque-amarelo-claro:`37`
     - :destaque-amarelo-claro:`usuarioNome`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome do Usuário/Sistema que enviou a Contratação.`
   * - :destaque-amarelo-claro:`38`
     - :destaque-amarelo-claro:`existeResultado`
     - :destaque-amarelo-claro:`Booleano`
     - :destaque-amarelo-claro:`Marcador de existência de resultado na contratação (False – Não / True – Sim).`

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
