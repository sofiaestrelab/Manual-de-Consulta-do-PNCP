Consultar Contratos/Empenhos por Dados de Atualização Global
===============================================================

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

   Não se aplica

Exemplo de Requisição (cURL)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash
   :linenos:

   curl -X 'GET' \
     'https://pncp.gov.br/api/consulta/v1/contratos/atualizacao?dataInicial=20260101&dataFinal=20260101&pagina=3' \
     -H 'accept: */*'

Dados de entrada
~~~~~~~~~~~~~~~~

.. list-table::
   :width: 100%
   :widths: 5 25 15 55
   :header-rows: 1
   :class: quebra-linha-dois-ultima 

   * - Id
     - Campo
     - Tipo
     - Obrigatório
     - Descrição
   * - 1
     - dataInicial
     - Texto
     - Sim
     - Data inicial do período a ser consultado no formato AAAAMMDD.
   * - 2
     - dataFinal
     - Texto
     - Sim
     - Data final do período a ser consultado no formato AAAAMMDD.
   * - 3
     - cnpjOrgao
     - Texto
     - Não
     - CNPJ do órgão originário da contratação.
   * - 4
     - codigoUnidadeAdministrativa
     - Texto
     - Não
     - Código da Unidade Administrativa do Órgão.
   * - 5
     - usuarioId
     - Inteiro
     - Não
     - Identificador do usuário do sistema de contratações públicas.
   * - 6
     - pagina
     - Inteiro
     - Sim
     - Número da página que se deseja obter os dados.
   * - 7
     - tamanhoPagina
     - Inteiro
     - Não
     - Tamanho da página para retorno dos registros.

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
   * - 1
     - data
     - Lista
     - Lista.
   * - 1.1
     - numeroControlePncpAta
     - Texto
     - Número de Controle PNCP da Ata.
   * - 1.2
     - codigoPaisFornecedor
     - Texto
     - Código do país do fornecedor.
   * - 1.3
     - numeroControlePncpCompra
     - Texto
     - Número de Controle PNCP da contratação.
   * - 1.4
     - informacaoComplementar
     - Texto
     - Informação complementar referente ao contrato ou empenho.
   * - 1.5
     - processo
     - Texto
     - Número do processo de contratação no sistema de origem.
   * - 1.6
     - unidadeSubRogada
     - Lista
     - Dados da Unidade Administrativa do Órgão subrogado.
   * - 1.6.1
     - ufNome
     - Texto
     - Nome da unidade federativa do município.
   * - 1.6.2
     - ufSigla
     - Texto
     - Sigla da unidade federativa do município.
   * - 1.6.3
     - municipioNome
     - Texto
     - Nome do município.
   * - 1.6.4
     - codigoUnidade
     - Texto
     - Código da Unidade Administrativa pertencente ao Órgão subrogado.
   * - 1.6.5
     - nomeUnidade
     - Texto
     - Nome da Unidade Administrativa pertencente ao Órgão subrogado.
   * - 1.6.6
     - codigoIbge
     - Texto
     - Código IBGE do município.
   * - 1.7
     - orgaoSubRogado
     - Lista
     - Dados do Órgão/Entidade subrogado.
   * - 1.7.1
     - cnpj
     - Texto
     - CNPJ do Órgão referente à contratação.
   * - 1.7.2
     - esferaId
     - Texto
     - Código da esfera a que pertence o Órgão. F - Federal; E - Estadual; M - Municipal; D - Distrital.
   * - 1.7.3
     - razaoSocial
     - Texto
     - Razão social do Órgão referente à contratação.
   * - 1.7.4
     - poderId
     - Texto
     - Código do poder a que pertence o Órgão. L - Legislativo; E - Executivo; J - Judiciário.
   * - 1.8
     - nomeRazaoSocialFornecedor
     - Texto
     - Nome ou razão social do fornecedor.
   * - 1.9
     - anoContrato
     - Inteiro
     - Ano do contrato.
   * - 1.10
     - tipoContrato
     - Lista
     - Dados do tipo de contrato.
   * - 1.10.1
     - id
     - Inteiro
     - Código do tipo de contrato.
   * - 1.10.2
     - nome
     - Texto
     - Nome do tipo de contrato.
   * - 1.11
     - numeroContratoEmpenho
     - Texto
     - Número do contrato ou empenho.
   * - 1.12
     - dataAssinatura
     - Data
     - Data de assinatura do contrato.
   * - 1.13
     - dataVigenciaInicio
     - Data
     - Data de início da vigência do contrato.
   * - 1.14
     - dataVigenciaFim
     - Data
     - Data de término da vigência do contrato.
   * - 1.15
     - niFornecedor
     - Texto
     - Número de identificação do fornecedor.
   * - 1.16
     - tipoPessoa
     - Texto
     - Tipo de pessoa do fornecedor.
   * - 1.17
     - orgaoEntidade
     - Lista
     - Dados do Órgão/Entidade.
   * - 1.17.1
     - cnpj
     - Texto
     - CNPJ do Órgão referente à contratação.
   * - 1.17.2
     - esferaId
     - Texto
     - Código da esfera a que pertence o Órgão. F - Federal; E - Estadual; M - Municipal; D - Distrital.
   * - 1.17.3
     - razaoSocial
     - Texto
     - Razão social do Órgão referente à contratação.
   * - 1.17.4
     - poderId
     - Texto
     - Código do poder a que pertence o Órgão. L - Legislativo; E - Executivo; J - Judiciário.
   * - 1.18
     - categoriaProcesso
     - Lista
     - Dados da categoria do processo.
   * - 1.18.1
     - id
     - Inteiro
     - Código da categoria do processo.
   * - 1.18.2
     - nome
     - Texto
     - Nome da categoria do processo.
   * - 1.19
     - dataPublicacaoPncp
     - Data/Hora
     - Data da publicação do contrato no PNCP.
   * - 1.20
     - dataAtualizacao
     - Data/Hora
     - Data da última atualização do registro do contrato.
   * - 1.21
     - sequencialContrato
     - Inteiro
     - Sequencial do contrato no PNCP.
   * - 1.22
     - unidadeOrgao
     - Lista
     - Dados da Unidade Administrativa.
   * - 1.22.1
     - ufNome
     - Texto
     - Nome da unidade federativa do município.
   * - 1.22.2
     - ufSigla
     - Texto
     - Sigla da unidade federativa do município.
   * - 1.22.3
     - municipioNome
     - Texto
     - Nome do município.
   * - 1.22.4
     - codigoUnidade
     - Texto
     - Código da Unidade Administrativa pertencente ao Órgão.
   * - 1.22.5
     - nomeUnidade
     - Texto
     - Nome da Unidade Administrativa pertencente ao Órgão.
   * - 1.22.6
     - codigoIbge
     - Texto
     - Código IBGE do município.
   * - 1.23
     - niFornecedorSubContratado
     - Texto
     - Número de identificação do fornecedor subcontratado.
   * - 1.24
     - nomeFornecedorSubContratado
     - Texto
     - Nome ou razão social do fornecedor subcontratado.
   * - 1.25
     - receita
     - Booleano
     - Indicador de receita.
   * - 1.26
     - numeroParcelas
     - Inteiro
     - Número de parcelas do contrato.
   * - 1.27
     - numeroRetificacao
     - Inteiro
     - Número da retificação do contrato.
   * - 1.28
     - temRemanejamento
     - Booleano
     - Indicador de existência de remanejamento.
   * - 1.29
     - emendaParlamentar
     - Booleano
     - Indicador de existência de emenda parlamentar.
   * - 1.30
     - frutoAdesao
     - Booleano
     - Indicador de que o contrato é fruto de adesão.
   * - 1.31
     - objetoContrato
     - Texto
     - Descrição do objeto do contrato.
   * - 1.32
     - numeroControlePNCP
     - Texto
     - Número de Controle PNCP do contrato.
   * - 1.33
     - tipoPessoaSubContratada
     - Texto
     - Tipo de pessoa do fornecedor subcontratado.
   * - 1.34
     - valorInicial
     - Decimal
     - Valor inicial do contrato.
   * - 1.35
     - valorParcela
     - Decimal
     - Valor da parcela do contrato.
   * - 1.36
     - valorGlobal
     - Decimal
     - Valor global do contrato.
   * - 1.37
     - valorAcumulado
     - Decimal
     - Valor acumulado do contrato.
   * - 1.38
     - dataAtualizacaoGlobal
     - Data/Hora
     - Data da última atualização global do registro do contrato.
   * - 1.39
     - identificadorCipi
     - Texto
     - Identificador do CIPI.
   * - 1.40
     - urlCipi
     - Texto
     - URL do CIPI.
   * - 1.41
     - usuarioNome
     - Texto
     - Nome do usuário/sistema que enviou o contrato.
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
