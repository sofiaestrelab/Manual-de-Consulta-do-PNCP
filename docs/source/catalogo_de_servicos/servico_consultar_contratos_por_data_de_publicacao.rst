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
   * - :destaque-amarelo-claro:`4`
     - :destaque-amarelo-claro:`codigoUnidadeAdministrativa`
     - :destaque-amarelo-claro:`String`
     - :destaque-amarelo-claro:`Não`
     - :destaque-amarelo-claro:`Código da Unidade Administrativa do Órgão originário da contratação informado na inclusão (proprietário do contrato)`
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
   * - :destaque-amarelo-claro:`1`
     - :destaque-amarelo-claro:`numeroControlePNCP`
     - :destaque-amarelo-claro:`String`
     - :destaque-amarelo-claro:`Número de controle PNCP do contrato (id contrato PNCP)`
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

.. tip::

   Em adição ao serviço **6.6. Serviço Consultar Contratos por Data de Publicação** mencionado neste manual, é importante destacar que o Portal Nacional de Contratações Públicas (PNCP) oferece uma gama ampla de funcionalidades via API que permitem uma consulta detalhada sobre **CONTRATAÇÕES**.

Estas funcionalidades estão minuciosamente descritas no Manual de Integração — Portal Nacional de Contratações Públicas - PNCP, disponível no site oficial `www.gov.br <https://www.gov.br>`_. Abaixo, apresentamos uma lista com alguns exemplos de serviços disponíveis:

- 6.5.7. Consultar Documento de um Contrato
- 6.5.9. Consultar Contratos de uma Contratação

Recomendamos a leitura detalhada do Manual de Integração do PNCP para uma compreensão abrangente de todas as funcionalidades e possibilidades oferecidas pela API.
