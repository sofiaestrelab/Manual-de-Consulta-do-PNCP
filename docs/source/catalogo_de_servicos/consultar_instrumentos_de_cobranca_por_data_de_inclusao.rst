Consultar Instrumentos de Cobrança por Data de Inclusão
=======================================================

Serviço destinado à consulta dos Instrumentos de Cobrança por data de inclusão no PNCP.


Detalhes de Requisição
~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :width: 100%
   :widths: auto
   :header-rows: 1

   * - Endpoint
     - Método HTTP
   * - /v1/instrumentoscobranca/inclusao
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
     'https://pncp.gov.br/api/consulta/v1/instrumentoscobranca/inclusao?dataInicial=20260101&dataFinal=20260101&pagina=2' \
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
     - :destaque-amarelo-claro:`string`
     - :destaque-amarelo-claro:`Sim`
     - :destaque-amarelo-claro:`Data inicial do período a ser consultado no formato AAAAMMDD.`
   * - :destaque-amarelo-claro:`2`
     - :destaque-amarelo-claro:`dataFinal`
     - :destaque-amarelo-claro:`string`
     - :destaque-amarelo-claro:`Sim`
     - :destaque-amarelo-claro:`Data final do período a ser consultado no formato AAAAMMDD.`
   * - :destaque-amarelo-claro:`3`
     - :destaque-amarelo-claro:`tipoInstrumentoCobranca`
     - :destaque-amarelo-claro:`integer (int64)`
     - :destaque-amarelo-claro:`Não`
     - :destaque-amarelo-claro:`Código do tipo de instrumento de cobrança.`
   * - :destaque-amarelo-claro:`4`
     - :destaque-amarelo-claro:`cnpjOrgao`
     - :destaque-amarelo-claro:`string`
     - :destaque-amarelo-claro:`Não`
     - :destaque-amarelo-claro:`CNPJ do órgão responsável pelo instrumento de cobrança.`
   * - :destaque-amarelo-claro:`5`
     - :destaque-amarelo-claro:`pagina`
     - :destaque-amarelo-claro:`integer (int32)`
     - :destaque-amarelo-claro:`Sim`
     - :destaque-amarelo-claro:`Número da página que se deseja obter os dados.`
   * - :destaque-amarelo-claro:`6`
     - :destaque-amarelo-claro:`tamanhoPagina`
     - :destaque-amarelo-claro:`integer (int32)`
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
     - :destaque-amarelo-claro:`Lista de Instrumentos de Cobrança.`
   * - :destaque-amarelo-claro:`1.1`
     - :destaque-amarelo-claro:`cnpj`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`CNPJ do órgão responsável pelo instrumento de cobrança.`
   * - :destaque-amarelo-claro:`1.2`
     - :destaque-amarelo-claro:`ano`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Ano do contrato relacionado ao instrumento de cobrança.`
   * - :destaque-amarelo-claro:`1.3`
     - :destaque-amarelo-claro:`sequencialContrato`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Sequencial do contrato no PNCP.`
   * - :destaque-amarelo-claro:`1.4`
     - :destaque-amarelo-claro:`sequencialInstrumentoCobranca`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Sequencial do instrumento de cobrança.`
   * - :destaque-amarelo-claro:`1.5`
     - :destaque-amarelo-claro:`tipoInstrumentoCobranca`
     - :destaque-amarelo-claro:`Lista`
     - :destaque-amarelo-claro:`Dados do tipo de instrumento de cobrança.`
   * - :destaque-amarelo-claro:`1.5.1`
     - :destaque-amarelo-claro:`id`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Código do tipo de instrumento de cobrança.`
   * - :destaque-amarelo-claro:`1.5.2`
     - :destaque-amarelo-claro:`nome`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome do tipo de instrumento de cobrança.`
   * - :destaque-amarelo-claro:`1.5.3`
     - :destaque-amarelo-claro:`descricao`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Descrição do tipo de instrumento de cobrança.`
   * - :destaque-amarelo-claro:`1.5.4`
     - :destaque-amarelo-claro:`dataInclusao`
     - :destaque-amarelo-claro:`Data/Hora`
     - :destaque-amarelo-claro:`Data da inclusão do tipo de instrumento de cobrança.`
   * - :destaque-amarelo-claro:`1.5.5`
     - :destaque-amarelo-claro:`dataAtualizacao`
     - :destaque-amarelo-claro:`Data/Hora`
     - :destaque-amarelo-claro:`Data da última atualização do tipo de instrumento de cobrança.`
   * - :destaque-amarelo-claro:`1.5.6`
     - :destaque-amarelo-claro:`statusAtivo`
     - :destaque-amarelo-claro:`Booleano`
     - :destaque-amarelo-claro:`Indicador de status ativo do tipo de instrumento de cobrança.`
   * - :destaque-amarelo-claro:`1.6`
     - :destaque-amarelo-claro:`numeroInstrumentoCobranca`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Número do instrumento de cobrança.`
   * - :destaque-amarelo-claro:`1.7`
     - :destaque-amarelo-claro:`dataEmissaoDocumento`
     - :destaque-amarelo-claro:`Data`
     - :destaque-amarelo-claro:`Data de emissão do documento.`
   * - :destaque-amarelo-claro:`1.8`
     - :destaque-amarelo-claro:`observacao`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Observação referente ao instrumento de cobrança.`
   * - :destaque-amarelo-claro:`1.9`
     - :destaque-amarelo-claro:`chaveNFe`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Chave da Nota Fiscal Eletrônica.`
   * - :destaque-amarelo-claro:`1.10`
     - :destaque-amarelo-claro:`fonteNFe`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Código da fonte da Nota Fiscal Eletrônica.`
   * - :destaque-amarelo-claro:`1.11`
     - :destaque-amarelo-claro:`dataConsultaNFe`
     - :destaque-amarelo-claro:`Data/Hora`
     - :destaque-amarelo-claro:`Data da consulta da Nota Fiscal Eletrônica.`
   * - :destaque-amarelo-claro:`1.12`
     - :destaque-amarelo-claro:`statusResponseNFe`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Status da resposta da Nota Fiscal Eletrônica.`
   * - :destaque-amarelo-claro:`1.13`
     - :destaque-amarelo-claro:`jsonResponseNFe`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Resposta da consulta da Nota Fiscal Eletrônica em formato JSON.`
   * - :destaque-amarelo-claro:`1.14`
     - :destaque-amarelo-claro:`notaFiscalEletronica`
     - :destaque-amarelo-claro:`Lista`
     - :destaque-amarelo-claro:`Dados da Nota Fiscal Eletrônica.`
   * - :destaque-amarelo-claro:`1.14.1`
     - :destaque-amarelo-claro:`instrumentoCobrancaId`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Identificador do instrumento de cobrança relacionado à Nota Fiscal Eletrônica.`
   * - :destaque-amarelo-claro:`1.14.2`
     - :destaque-amarelo-claro:`chave`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Chave da Nota Fiscal Eletrônica.`
   * - :destaque-amarelo-claro:`1.14.3`
     - :destaque-amarelo-claro:`nfTransparenciaID`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Identificador da Nota Fiscal na Transparência.`
   * - :destaque-amarelo-claro:`1.14.4`
     - :destaque-amarelo-claro:`numero`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Número da Nota Fiscal Eletrônica.`
   * - :destaque-amarelo-claro:`1.14.5`
     - :destaque-amarelo-claro:`serie`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Série da Nota Fiscal Eletrônica.`
   * - :destaque-amarelo-claro:`1.14.6`
     - :destaque-amarelo-claro:`dataEmissao`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Data de emissão da Nota Fiscal Eletrônica.`
   * - :destaque-amarelo-claro:`1.14.7`
     - :destaque-amarelo-claro:`niEmitente`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Número de identificação do emitente da Nota Fiscal Eletrônica.`
   * - :destaque-amarelo-claro:`1.14.8`
     - :destaque-amarelo-claro:`nomeEmitente`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome do emitente da Nota Fiscal Eletrônica.`
   * - :destaque-amarelo-claro:`1.14.9`
     - :destaque-amarelo-claro:`nomeMunicipioEmitente`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome do município do emitente da Nota Fiscal Eletrônica.`
   * - :destaque-amarelo-claro:`1.14.10`
     - :destaque-amarelo-claro:`codigoOrgaoDestinatario`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Código do órgão destinatário da Nota Fiscal Eletrônica.`
   * - :destaque-amarelo-claro:`1.14.11`
     - :destaque-amarelo-claro:`nomeOrgaoDestinatario`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome do órgão destinatário da Nota Fiscal Eletrônica.`
   * - :destaque-amarelo-claro:`1.14.12`
     - :destaque-amarelo-claro:`codigoOrgaoSuperiorDestinatario`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Código do órgão superior destinatário da Nota Fiscal Eletrônica.`
   * - :destaque-amarelo-claro:`1.14.13`
     - :destaque-amarelo-claro:`nomeOrgaoSuperiorDestinatario`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome do órgão superior destinatário da Nota Fiscal Eletrônica.`
   * - :destaque-amarelo-claro:`1.14.14`
     - :destaque-amarelo-claro:`valorNotaFiscal`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Valor da Nota Fiscal Eletrônica.`
   * - :destaque-amarelo-claro:`1.14.15`
     - :destaque-amarelo-claro:`tipoEventoMaisRecente`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Tipo do evento mais recente da Nota Fiscal Eletrônica.`
   * - :destaque-amarelo-claro:`1.14.16`
     - :destaque-amarelo-claro:`dataTipoEventoMaisRecente`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Data do evento mais recente da Nota Fiscal Eletrônica.`
   * - :destaque-amarelo-claro:`1.14.17`
     - :destaque-amarelo-claro:`dataInclusao`
     - :destaque-amarelo-claro:`Data/Hora`
     - :destaque-amarelo-claro:`Data da inclusão da Nota Fiscal Eletrônica.`
   * - :destaque-amarelo-claro:`1.14.18`
     - :destaque-amarelo-claro:`dataAtualizacao`
     - :destaque-amarelo-claro:`Data/Hora`
     - :destaque-amarelo-claro:`Data da última atualização da Nota Fiscal Eletrônica.`
   * - :destaque-amarelo-claro:`1.14.19`
     - :destaque-amarelo-claro:`itens`
     - :destaque-amarelo-claro:`Lista`
     - :destaque-amarelo-claro:`Lista de itens da Nota Fiscal Eletrônica.`
   * - :destaque-amarelo-claro:`1.14.19.1`
     - :destaque-amarelo-claro:`numeroItem`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Número do item da Nota Fiscal Eletrônica.`
   * - :destaque-amarelo-claro:`1.14.19.2`
     - :destaque-amarelo-claro:`descricaoProdutoServico`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Descrição do produto ou serviço.`
   * - :destaque-amarelo-claro:`1.14.19.3`
     - :destaque-amarelo-claro:`codigoNCM`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Código NCM do produto ou serviço.`
   * - :destaque-amarelo-claro:`1.14.19.4`
     - :destaque-amarelo-claro:`descricaoNCM`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Descrição do NCM do produto ou serviço.`
   * - :destaque-amarelo-claro:`1.14.19.5`
     - :destaque-amarelo-claro:`cfop`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Código Fiscal de Operações e Prestações (CFOP).`
   * - :destaque-amarelo-claro:`1.14.19.6`
     - :destaque-amarelo-claro:`quantidade`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Quantidade do item.`
   * - :destaque-amarelo-claro:`1.14.19.7`
     - :destaque-amarelo-claro:`unidade`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Unidade de medida do item.`
   * - :destaque-amarelo-claro:`1.14.19.8`
     - :destaque-amarelo-claro:`valorUnitario`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Valor unitário do item.`
   * - :destaque-amarelo-claro:`1.14.19.9`
     - :destaque-amarelo-claro:`valorTotal`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Valor total do item.`
   * - :destaque-amarelo-claro:`1.14.20`
     - :destaque-amarelo-claro:`eventos`
     - :destaque-amarelo-claro:`Lista`
     - :destaque-amarelo-claro:`Lista de eventos da Nota Fiscal Eletrônica.`
   * - :destaque-amarelo-claro:`1.14.20.1`
     - :destaque-amarelo-claro:`dataEvento`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Data do evento.`
   * - :destaque-amarelo-claro:`1.14.20.2`
     - :destaque-amarelo-claro:`tipoEvento`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Tipo do evento.`
   * - :destaque-amarelo-claro:`1.14.20.3`
     - :destaque-amarelo-claro:`evento`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Descrição do evento.`
   * - :destaque-amarelo-claro:`1.14.20.4`
     - :destaque-amarelo-claro:`motivoEvento`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Motivo do evento.`
   * - :destaque-amarelo-claro:`1.15`
     - :destaque-amarelo-claro:`dataInclusao`
     - :destaque-amarelo-claro:`Data/Hora`
     - :destaque-amarelo-claro:`Data da inclusão do instrumento de cobrança.`
   * - :destaque-amarelo-claro:`1.16`
     - :destaque-amarelo-claro:`dataAtualizacao`
     - :destaque-amarelo-claro:`Data/Hora`
     - :destaque-amarelo-claro:`Data da última atualização do instrumento de cobrança.`
   * - :destaque-amarelo-claro:`1.17`
     - :destaque-amarelo-claro:`recuperarContratoDTO`
     - :destaque-amarelo-claro:`Lista`
     - :destaque-amarelo-claro:`Dados do contrato relacionado ao instrumento de cobrança.`
   * - :destaque-amarelo-claro:`1.17.1`
     - :destaque-amarelo-claro:`numeroControlePncpCompra`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Número de Controle PNCP da contratação.`
   * - :destaque-amarelo-claro:`1.17.2`
     - :destaque-amarelo-claro:`numeroControlePncpAta`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Número de Controle PNCP da Ata.`
   * - :destaque-amarelo-claro:`1.17.3`
     - :destaque-amarelo-claro:`codigoPaisFornecedor`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Código do país do fornecedor.`
   * - :destaque-amarelo-claro:`1.17.4`
     - :destaque-amarelo-claro:`anoContrato`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Ano do contrato.`
   * - :destaque-amarelo-claro:`1.17.5`
     - :destaque-amarelo-claro:`tipoContrato`
     - :destaque-amarelo-claro:``
     - :destaque-amarelo-claro:`Dados do tipo de contrato.`
   * - :destaque-amarelo-claro:`1.17.5.1`
     - :destaque-amarelo-claro:`id`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Código do tipo de contrato.`
   * - :destaque-amarelo-claro:`1.17.5.2`
     - :destaque-amarelo-claro:`nome`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome do tipo de contrato.`
   * - :destaque-amarelo-claro:`1.17.6`
     - :destaque-amarelo-claro:`numeroContratoEmpenho`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Número do contrato ou empenho.`
   * - :destaque-amarelo-claro:`1.17.7`
     - :destaque-amarelo-claro:`dataAssinatura`
     - :destaque-amarelo-claro:`Data`
     - :destaque-amarelo-claro:`Data de assinatura do contrato.`
   * - :destaque-amarelo-claro:`1.17.8`
     - :destaque-amarelo-claro:`dataVigenciaInicio`
     - :destaque-amarelo-claro:`Data`
     - :destaque-amarelo-claro:`Data de início da vigência do contrato.`
   * - :destaque-amarelo-claro:`1.17.9`
     - :destaque-amarelo-claro:`dataVigenciaFim`
     - :destaque-amarelo-claro:`Data`
     - :destaque-amarelo-claro:`Data de término da vigência do contrato.`
   * - :destaque-amarelo-claro:`1.17.10`
     - :destaque-amarelo-claro:`niFornecedor`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Número de identificação do fornecedor.`
   * - :destaque-amarelo-claro:`1.17.11`
     - :destaque-amarelo-claro:`tipoPessoa`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Tipo de pessoa do fornecedor.`
   * - :destaque-amarelo-claro:`1.17.12`
     - :destaque-amarelo-claro:`orgaoEntidade`
     - :destaque-amarelo-claro:`Lista`
     - :destaque-amarelo-claro:`Dados do Órgão/Entidade.`
   * - :destaque-amarelo-claro:`1.17.12.1`
     - :destaque-amarelo-claro:`cnpj`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`CNPJ do Órgão referente à contratação.`
   * - :destaque-amarelo-claro:`1.17.12.2`
     - :destaque-amarelo-claro:`razaoSocial`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Razão social do Órgão referente à contratação.`
   * - :destaque-amarelo-claro:`1.17.12.3`
     - :destaque-amarelo-claro:`poderId`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Código do poder a que pertence o Órgão. L - Legislativo; E - Executivo; J - Judiciário.`
   * - :destaque-amarelo-claro:`1.17.12.4`
     - :destaque-amarelo-claro:`esferaId`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Código da esfera a que pertence o Órgão. F - Federal; E - Estadual; M - Municipal; D - Distrital.`
   * - :destaque-amarelo-claro:`1.17.13`
     - :destaque-amarelo-claro:`categoriaProcesso`
     - :destaque-amarelo-claro:`Lista`
     - :destaque-amarelo-claro:`Dados da categoria do processo.`
   * - :destaque-amarelo-claro:`1.17.13.1`
     - :destaque-amarelo-claro:`id`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Código da categoria do processo.`
   * - :destaque-amarelo-claro:`1.17.13.2`
     - :destaque-amarelo-claro:`nome`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome da categoria do processo.`
   * - :destaque-amarelo-claro:`1.17.14`
     - :destaque-amarelo-claro:`dataPublicacaoPncp`
     - :destaque-amarelo-claro:`Data/Hora`
     - :destaque-amarelo-claro:`Data da publicação do contrato no PNCP.`
   * - :destaque-amarelo-claro:`1.17.15`
     - :destaque-amarelo-claro:`dataAtualizacao`
     - :destaque-amarelo-claro:`Data/Hora`
     - :destaque-amarelo-claro:`Data da última atualização do registro do contrato.`
   * - :destaque-amarelo-claro:`1.17.16`
     - :destaque-amarelo-claro:`sequencialContrato`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Sequencial do contrato no PNCP.`
   * - :destaque-amarelo-claro:`1.17.17`
     - :destaque-amarelo-claro:`unidadeOrgao`
     - :destaque-amarelo-claro:`Lista`
     - :destaque-amarelo-claro:`Dados da Unidade Administrativa.`
   * - :destaque-amarelo-claro:`1.17.17.1`
     - :destaque-amarelo-claro:`ufNome`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome da unidade federativa do município.`
   * - :destaque-amarelo-claro:`1.17.17.2`
     - :destaque-amarelo-claro:`codigoIbge`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Código IBGE do município.`
   * - :destaque-amarelo-claro:`1.17.17.3`
     - :destaque-amarelo-claro:`codigoUnidade`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Código da Unidade Administrativa pertencente ao Órgão.`
   * - :destaque-amarelo-claro:`1.17.17.4`
     - :destaque-amarelo-claro:`nomeUnidade`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome da Unidade Administrativa pertencente ao Órgão.`
   * - :destaque-amarelo-claro:`1.17.17.5`
     - :destaque-amarelo-claro:`ufSigla`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Sigla da unidade federativa do município.`
   * - :destaque-amarelo-claro:`1.17.17.6`
     - :destaque-amarelo-claro:`municipioNome`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome do município.`
   * - :destaque-amarelo-claro:`1.17.18`
     - :destaque-amarelo-claro:`informacaoComplementar`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Informação complementar referente ao contrato.`
   * - :destaque-amarelo-claro:`1.17.19`
     - :destaque-amarelo-claro:`processo`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Número do processo de contratação no sistema de origem.`
   * - :destaque-amarelo-claro:`1.17.20`
     - :destaque-amarelo-claro:`unidadeSubRogada`
     - :destaque-amarelo-claro:`Lista`
     - :destaque-amarelo-claro:`Dados da Unidade Administrativa do Órgão subrogado.`
   * - :destaque-amarelo-claro:`1.17.20.1`
     - :destaque-amarelo-claro:`ufNome`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome da unidade federativa do município.`
   * - :destaque-amarelo-claro:`1.17.20.2`
     - :destaque-amarelo-claro:`codigoIbge`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Código IBGE do município.`
   * - :destaque-amarelo-claro:`1.17.20.3`
     - :destaque-amarelo-claro:`codigoUnidade`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Código da Unidade Administrativa pertencente ao Órgão subrogado.`
   * - :destaque-amarelo-claro:`1.17.20.4`
     - :destaque-amarelo-claro:`nomeUnidade`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome da Unidade Administrativa pertencente ao Órgão subrogado.`
   * - :destaque-amarelo-claro:`1.17.20.5`
     - :destaque-amarelo-claro:`ufSigla`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Sigla da unidade federativa do município.`
   * - :destaque-amarelo-claro:`1.17.20.6`
     - :destaque-amarelo-claro:`municipioNome`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome do município.`
   * - :destaque-amarelo-claro:`1.17.21`
     - :destaque-amarelo-claro:`orgaoSubRogado`
     - :destaque-amarelo-claro:`Lista`
     - :destaque-amarelo-claro:`Dados do Órgão/Entidade subrogado.`
   * - :destaque-amarelo-claro:`1.17.21.1`
     - :destaque-amarelo-claro:`cnpj`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`CNPJ do Órgão referente à contratação.`
   * - :destaque-amarelo-claro:`1.17.21.2`
     - :destaque-amarelo-claro:`razaoSocial`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Razão social do Órgão referente à contratação.`
   * - :destaque-amarelo-claro:`1.17.21.3`
     - :destaque-amarelo-claro:`poderId`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Código do poder a que pertence o Órgão. L - Legislativo; E - Executivo; J - Judiciário.`
   * - :destaque-amarelo-claro:`1.17.21.4`
     - :destaque-amarelo-claro:`esferaId`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Código da esfera a que pertence o Órgão. F - Federal; E - Estadual; M - Municipal; D - Distrital.`
   * - :destaque-amarelo-claro:`1.17.22`
     - :destaque-amarelo-claro:`nomeRazaoSocialFornecedor`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome ou razão social do fornecedor.`
   * - :destaque-amarelo-claro:`1.17.23`
     - :destaque-amarelo-claro:`niFornecedorSubContratado`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Número de identificação do fornecedor subcontratado.`
   * - :destaque-amarelo-claro:`1.17.24`
     - :destaque-amarelo-claro:`nomeFornecedorSubContratado`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Nome ou razão social do fornecedor subcontratado.`
   * - :destaque-amarelo-claro:`1.17.25`
     - :destaque-amarelo-claro:`numeroControlePNCP`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Número de Controle PNCP do contrato.`
   * - :destaque-amarelo-claro:`1.17.26`
     - :destaque-amarelo-claro:`receita`
     - :destaque-amarelo-claro:`Booleano`
     - :destaque-amarelo-claro:`Indicador de receita.`
   * - :destaque-amarelo-claro:`1.17.27`
     - :destaque-amarelo-claro:`numeroParcelas`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Número de parcelas do contrato.`
   * - :destaque-amarelo-claro:`1.17.28`
     - :destaque-amarelo-claro:`numeroRetificacao`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Número da retificação do contrato.`
   * - :destaque-amarelo-claro:`1.17.29`
     - :destaque-amarelo-claro:`temRemanejamento`
     - :destaque-amarelo-claro:`Booleano`
     - :destaque-amarelo-claro:`Indicador de existência de remanejamento.`
   * - :destaque-amarelo-claro:`1.17.30`
     - :destaque-amarelo-claro:`emendaParlamentar`
     - :destaque-amarelo-claro:`Booleano`
     - :destaque-amarelo-claro:`Indicador de existência de emenda parlamentar.`
   * - :destaque-amarelo-claro:`1.17.31`
     - :destaque-amarelo-claro:`frutoAdesao`
     - :destaque-amarelo-claro:`Booleano`
     - :destaque-amarelo-claro:`Indicador de que o contrato é fruto de adesão.`
   * - :destaque-amarelo-claro:`1.17.32`
     - :destaque-amarelo-claro:`tipoPessoaSubContratada`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Tipo de pessoa do fornecedor subcontratado.`
   * - :destaque-amarelo-claro:`1.17.33`
     - :destaque-amarelo-claro:`objetoContrato`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Descrição do objeto do contrato.`
   * - :destaque-amarelo-claro:`1.17.34`
     - :destaque-amarelo-claro:`valorInicial`
     - :destaque-amarelo-claro:`Decimal`
     - :destaque-amarelo-claro:`Valor inicial do contrato.`
   * - :destaque-amarelo-claro:`1.17.35`
     - :destaque-amarelo-claro:`valorParcela`
     - :destaque-amarelo-claro:`Decimal`
     - :destaque-amarelo-claro:`Valor da parcela do contrato.`
   * - :destaque-amarelo-claro:`1.17.36`
     - :destaque-amarelo-claro:`valorGlobal`
     - :destaque-amarelo-claro:`Decimal`
     - :destaque-amarelo-claro:`Valor global do contrato.`
   * - :destaque-amarelo-claro:`1.17.37`
     - :destaque-amarelo-claro:`valorAcumulado`
     - :destaque-amarelo-claro:`Decimal`
     - :destaque-amarelo-claro:`Valor acumulado do contrato.`
   * - :destaque-amarelo-claro:`1.17.38`
     - :destaque-amarelo-claro:`dataAtualizacaoGlobal`
     - :destaque-amarelo-claro:`Data/Hora`
     - :destaque-amarelo-claro:`Data da última atualização global do registro do contrato.`
   * - :destaque-amarelo-claro:`1.17.39`
     - :destaque-amarelo-claro:`identificadorCipi`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`Identificador do CIPI.`
   * - :destaque-amarelo-claro:`1.17.40`
     - :destaque-amarelo-claro:`urlCipi`
     - :destaque-amarelo-claro:`Texto`
     - :destaque-amarelo-claro:`URL do CIPI.`
   * - :destaque-amarelo-claro:`1.17.41`
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
     - :destaque-amarelo-claro:`Número da página em que a consulta foi realizada.`
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
     - :destaque-amarelo-claro:`Created`
     - :destaque-amarelo-claro:`Sucesso`
   * - :destaque-amarelo-claro:`400`
     - :destaque-amarelo-claro:`BadRequest`
     - :destaque-amarelo-claro:`Erro`
   * - :destaque-amarelo-claro:`422`
     - :destaque-amarelo-claro:`Unprocessable Entity`
     - :destaque-amarelo-claro:`Erro`
   * - :destaque-amarelo-claro:`500`
     - :destaque-amarelo-claro:`Internal Server Error`
     - :destaque-amarelo-claro:`Erro`
