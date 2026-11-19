Consultar Contratos e Empenhos por Data de Atualização Global
===============================================================

Serviço destinado à consulta dos contratos que foram incluídos ou que sofreram alterações no PNCP durante um determinado intervalo de datas, considerando a data de atualização global do registro.

Detalhes da Requisição
~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :width: 100%
   :widths: auto
   :header-rows: 1

   * - Endpoint
     - Método HTTP
   * - /v1/contratos/atualizacao
     - GET

Exemplo de Payload
~~~~~~~~~~~~~~~~~~

.. code-block:: text
   :linenos:
   :emphasize-lines: 1

   Não se aplica

Exemplo de Requisição (cURL)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash
   :linenos:
   :emphasize-lines: 1-3

   curl -X 'GET' \
     'https://pncp.gov.br/api/consulta/v1/contratos/atualizacao?dataInicial=20260101&dataFinal=20260101&pagina=3' \
     -H 'accept: */*'

Dados de entrada
~~~~~~~~~~~~~~~~

.. note::

   Alimentar os parâmetros ``{dataInicial}``, ``{dataFinal}`` e ``{pagina}`` na URL.

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
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Sim`
     - :destaque-amarelo-claro:`Data inicial do período a ser consultado no formato AAAAMMDD.`
   * - :destaque-amarelo-claro:`2`
     - :destaque-amarelo-claro:`dataFinal`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Sim`
     - :destaque-amarelo-claro:`Data final do período a ser consultado no formato AAAAMMDD.`
   * - :destaque-amarelo-claro:`3`
     - :destaque-amarelo-claro:`cnpjOrgao`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Não`
     - :destaque-amarelo-claro:`CNPJ do órgão originário da contratação.`
   * - :destaque-amarelo-claro:`4`
     - :destaque-amarelo-claro:`codigoUnidadeAdministrativa`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Não`
     - :destaque-amarelo-claro:`Código da Unidade Administrativa do Órgão.`
   * - :destaque-amarelo-claro:`5`
     - :destaque-amarelo-claro:`usuarioId`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Não`
     - :destaque-amarelo-claro:`Identificador do usuário do sistema de contratações públicas.`
   * - :destaque-amarelo-claro:`6`
     - :destaque-amarelo-claro:`pagina`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Sim`
     - :destaque-amarelo-claro:`Número da página que se deseja obter os dados.`
   * - :destaque-amarelo-claro:`7`
     - :destaque-amarelo-claro:`tamanhoPagina`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Não`
     - :destaque-amarelo-claro:`Tamanho da página para retorno dos registros.`

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
     - :destaque-amarelo-claro:`Lista.`
   * - :destaque-amarelo-claro:`1.1`
     - :destaque-amarelo-claro:`numeroControlePncpAta`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Número de Controle PNCP da Ata.`
   * - :destaque-amarelo-claro:`1.2`
     - :destaque-amarelo-claro:`codigoPaisFornecedor`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Código do país do fornecedor.`
   * - :destaque-amarelo-claro:`1.3`
     - :destaque-amarelo-claro:`numeroControlePncpCompra`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Número de Controle PNCP da contratação.`
   * - :destaque-amarelo-claro:`1.4`
     - :destaque-amarelo-claro:`informacaoComplementar`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Informação complementar referente ao contrato ou empenho.`
   * - :destaque-amarelo-claro:`1.5`
     - :destaque-amarelo-claro:`processo`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Número do processo de contratação no sistema de origem.`
   * - :destaque-amarelo-claro:`1.6`
     - :destaque-amarelo-claro:`unidadeSubRogada`
     - :destaque-amarelo-claro:`Lista`
     - :destaque-amarelo-claro:`Dados da Unidade Administrativa do Órgão subrogado.`
   * - :destaque-amarelo-claro:`1.6.1`
     - :destaque-amarelo-claro:`ufNome`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome da unidade federativa do município.`
   * - :destaque-amarelo-claro:`1.6.2`
     - :destaque-amarelo-claro:`ufSigla`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Sigla da unidade federativa do município.`
   * - :destaque-amarelo-claro:`1.6.3`
     - :destaque-amarelo-claro:`municipioNome`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome do município.`
   * - :destaque-amarelo-claro:`1.6.4`
     - :destaque-amarelo-claro:`codigoUnidade`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Código da Unidade Administrativa pertencente ao Órgão subrogado.`
   * - :destaque-amarelo-claro:`1.6.5`
     - :destaque-amarelo-claro:`nomeUnidade`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome da Unidade Administrativa pertencente ao Órgão subrogado.`
   * - :destaque-amarelo-claro:`1.6.6`
     - :destaque-amarelo-claro:`codigoIbge`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Código IBGE do município.`
   * - :destaque-amarelo-claro:`1.7`
     - :destaque-amarelo-claro:`orgaoSubRogado`
     - :destaque-amarelo-claro:`Lista`
     - :destaque-amarelo-claro:`Dados do Órgão/Entidade subrogado.`
   * - :destaque-amarelo-claro:`1.7.1`
     - :destaque-amarelo-claro:`cnpj`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`CNPJ do Órgão referente à contratação.`
   * - :destaque-amarelo-claro:`1.7.2`
     - :destaque-amarelo-claro:`esferaId`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Código da esfera a que pertence o Órgão. F - Federal; E - Estadual; M - Municipal; D - Distrital.`
   * - :destaque-amarelo-claro:`1.7.3`
     - :destaque-amarelo-claro:`razaoSocial`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Razão social do Órgão referente à contratação.`
   * - :destaque-amarelo-claro:`1.7.4`
     - :destaque-amarelo-claro:`poderId`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Código do poder a que pertence o Órgão. L - Legislativo; E - Executivo; J - Judiciário.`
   * - :destaque-amarelo-claro:`1.8`
     - :destaque-amarelo-claro:`nomeRazaoSocialFornecedor`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome ou razão social do fornecedor.`
   * - :destaque-amarelo-claro:`1.9`
     - :destaque-amarelo-claro:`anoContrato`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Ano do contrato.`
   * - :destaque-amarelo-claro:`1.10`
     - :destaque-amarelo-claro:`tipoContrato`
     - :destaque-amarelo-claro:`Lista`
     - :destaque-amarelo-claro:`Dados do tipo de contrato.`
   * - :destaque-amarelo-claro:`1.10.1`
     - :destaque-amarelo-claro:`id`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Código do tipo de contrato.`
   * - :destaque-amarelo-claro:`1.10.2`
     - :destaque-amarelo-claro:`nome`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome do tipo de contrato.`
   * - :destaque-amarelo-claro:`1.11`
     - :destaque-amarelo-claro:`numeroContratoEmpenho`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Número do contrato ou empenho.`
   * - :destaque-amarelo-claro:`1.12`
     - :destaque-amarelo-claro:`dataAssinatura`
     - :destaque-amarelo-claro:`Data`
     - :destaque-amarelo-claro:`Data de assinatura do contrato.`
   * - :destaque-amarelo-claro:`1.13`
     - :destaque-amarelo-claro:`dataVigenciaInicio`
     - :destaque-amarelo-claro:`Data`
     - :destaque-amarelo-claro:`Data de início da vigência do contrato.`
   * - :destaque-amarelo-claro:`1.14`
     - :destaque-amarelo-claro:`dataVigenciaFim`
     - :destaque-amarelo-claro:`Data`
     - :destaque-amarelo-claro:`Data de término da vigência do contrato.`
   * - :destaque-amarelo-claro:`1.15`
     - :destaque-amarelo-claro:`niFornecedor`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Número de identificação do fornecedor.`
   * - :destaque-amarelo-claro:`1.16`
     - :destaque-amarelo-claro:`tipoPessoa`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Tipo de pessoa do fornecedor.`
   * - :destaque-amarelo-claro:`1.17`
     - :destaque-amarelo-claro:`orgaoEntidade`
     - :destaque-amarelo-claro:`Lista`
     - :destaque-amarelo-claro:`Dados do Órgão/Entidade.`
   * - :destaque-amarelo-claro:`1.17.1`
     - :destaque-amarelo-claro:`cnpj`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`CNPJ do Órgão referente à contratação.`
   * - :destaque-amarelo-claro:`1.17.2`
     - :destaque-amarelo-claro:`esferaId`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Código da esfera a que pertence o Órgão. F - Federal; E - Estadual; M - Municipal; D - Distrital.`
   * - :destaque-amarelo-claro:`1.17.3`
     - :destaque-amarelo-claro:`razaoSocial`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Razão social do Órgão referente à contratação.`
   * - :destaque-amarelo-claro:`1.17.4`
     - :destaque-amarelo-claro:`poderId`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Código do poder a que pertence o Órgão. L - Legislativo; E - Executivo; J - Judiciário.`
   * - :destaque-amarelo-claro:`1.18`
     - :destaque-amarelo-claro:`categoriaProcesso`
     - :destaque-amarelo-claro:`Lista`
     - :destaque-amarelo-claro:`Dados da categoria do processo.`
   * - :destaque-amarelo-claro:`1.18.1`
     - :destaque-amarelo-claro:`id`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Código da categoria do processo.`
   * - :destaque-amarelo-claro:`1.18.2`
     - :destaque-amarelo-claro:`nome`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome da categoria do processo.`
   * - :destaque-amarelo-claro:`1.19`
     - :destaque-amarelo-claro:`dataPublicacaoPncp`
     - :destaque-amarelo-claro:`Data/Hora`
     - :destaque-amarelo-claro:`Data da publicação do contrato no PNCP.`
   * - :destaque-amarelo-claro:`1.20`
     - :destaque-amarelo-claro:`dataAtualizacao`
     - :destaque-amarelo-claro:`Data/Hora`
     - :destaque-amarelo-claro:`Data da última atualização do registro do contrato.`
   * - :destaque-amarelo-claro:`1.21`
     - :destaque-amarelo-claro:`sequencialContrato`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Sequencial do contrato no PNCP.`
   * - :destaque-amarelo-claro:`1.22`
     - :destaque-amarelo-claro:`unidadeOrgao`
     - :destaque-amarelo-claro:`Lista`
     - :destaque-amarelo-claro:`Dados da Unidade Administrativa.`
   * - :destaque-amarelo-claro:`1.22.1`
     - :destaque-amarelo-claro:`ufNome`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome da unidade federativa do município.`
   * - :destaque-amarelo-claro:`1.22.2`
     - :destaque-amarelo-claro:`ufSigla`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Sigla da unidade federativa do município.`
   * - :destaque-amarelo-claro:`1.22.3`
     - :destaque-amarelo-claro:`municipioNome`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome do município.`
   * - :destaque-amarelo-claro:`1.22.4`
     - :destaque-amarelo-claro:`codigoUnidade`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Código da Unidade Administrativa pertencente ao Órgão.`
   * - :destaque-amarelo-claro:`1.22.5`
     - :destaque-amarelo-claro:`nomeUnidade`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome da Unidade Administrativa pertencente ao Órgão.`
   * - :destaque-amarelo-claro:`1.22.6`
     - :destaque-amarelo-claro:`codigoIbge`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Código IBGE do município.`
   * - :destaque-amarelo-claro:`1.23`
     - :destaque-amarelo-claro:`niFornecedorSubContratado`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Número de identificação do fornecedor subcontratado.`
   * - :destaque-amarelo-claro:`1.24`
     - :destaque-amarelo-claro:`nomeFornecedorSubContratado`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome ou razão social do fornecedor subcontratado.`
   * - :destaque-amarelo-claro:`1.25`
     - :destaque-amarelo-claro:`receita`
     - :destaque-amarelo-claro:`Booleano`
     - :destaque-amarelo-claro:`Indicador de receita.`
   * - :destaque-amarelo-claro:`1.26`
     - :destaque-amarelo-claro:`numeroParcelas`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Número de parcelas do contrato.`
   * - :destaque-amarelo-claro:`1.27`
     - :destaque-amarelo-claro:`numeroRetificacao`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Número da retificação do contrato.`
   * - :destaque-amarelo-claro:`1.28`
     - :destaque-amarelo-claro:`temRemanejamento`
     - :destaque-amarelo-claro:`Booleano`
     - :destaque-amarelo-claro:`Indicador de existência de remanejamento.`
   * - :destaque-amarelo-claro:`1.29`
     - :destaque-amarelo-claro:`emendaParlamentar`
     - :destaque-amarelo-claro:`Booleano`
     - :destaque-amarelo-claro:`Indicador de existência de emenda parlamentar.`
   * - :destaque-amarelo-claro:`1.30`
     - :destaque-amarelo-claro:`frutoAdesao`
     - :destaque-amarelo-claro:`Booleano`
     - :destaque-amarelo-claro:`Indicador de que o contrato é fruto de adesão.`
   * - :destaque-amarelo-claro:`1.31`
     - :destaque-amarelo-claro:`objetoContrato`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Descrição do objeto do contrato.`
   * - :destaque-amarelo-claro:`1.32`
     - :destaque-amarelo-claro:`numeroControlePNCP`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Número de Controle PNCP do contrato.`
   * - :destaque-amarelo-claro:`1.33`
     - :destaque-amarelo-claro:`tipoPessoaSubContratada`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Tipo de pessoa do fornecedor subcontratado.`
   * - :destaque-amarelo-claro:`1.34`
     - :destaque-amarelo-claro:`valorInicial`
     - :destaque-amarelo-claro:`Decimal`
     - :destaque-amarelo-claro:`Valor inicial do contrato.`
   * - :destaque-amarelo-claro:`1.35`
     - :destaque-amarelo-claro:`valorParcela`
     - :destaque-amarelo-claro:`Decimal`
     - :destaque-amarelo-claro:`Valor da parcela do contrato.`
   * - :destaque-amarelo-claro:`1.36`
     - :destaque-amarelo-claro:`valorGlobal`
     - :destaque-amarelo-claro:`Decimal`
     - :destaque-amarelo-claro:`Valor global do contrato.`
   * - :destaque-amarelo-claro:`1.37`
     - :destaque-amarelo-claro:`valorAcumulado`
     - :destaque-amarelo-claro:`Decimal`
     - :destaque-amarelo-claro:`Valor acumulado do contrato.`
   * - :destaque-amarelo-claro:`1.38`
     - :destaque-amarelo-claro:`dataAtualizacaoGlobal`
     - :destaque-amarelo-claro:`Data/Hora`
     - :destaque-amarelo-claro:`Data da última atualização global do registro do contrato.`
   * - :destaque-amarelo-claro:`1.39`
     - :destaque-amarelo-claro:`identificadorCipi`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Identificador do CIPI.`
   * - :destaque-amarelo-claro:`1.40`
     - :destaque-amarelo-claro:`urlCipi`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`URL do CIPI.`
   * - :destaque-amarelo-claro:`1.41`
     - :destaque-amarelo-claro:`usuarioNome`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome do usuário/sistema que enviou o contrato.`
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
