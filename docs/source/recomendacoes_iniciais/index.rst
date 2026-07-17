Recomendações Iniciais
======================

Composição do Número de Controle PNCP de PCA/Contratação/Ata/Contrato
---------------------------------------------------------------------

O PNCP gera automaticamente um identificador, denominado **número de controle**, utilizado para reconhecer todas as demais transações realizadas para determinado registro.

Atualmente encontram-se disponíveis os seguintes tipos de registros:

- Plano de Contratações Anual (PCA);
- Contratação (licitação ou contratação direta);
- Ata de Registro de Preços;
- Contrato.

Conforme a composição descrita a seguir.

**Número de Controle do PCA**

id pca pncp

**Máscara:** 99999999999999-0-999999/9999

Cada PCA receberá um número de controle composto por:

- CNPJ do órgão/entidade do PCA (14 dígitos);
- Dígito 0 — marcador que indica tratar-se de um Plano de Contratação Anual;
- Número sequencial do Plano no PNCP*;
- Ano do Plano (4 dígitos).

**Número de Controle da Contratação**

id contratacao pncp

**Máscara:** 99999999999999-1-999999/9999

Cada contratação receberá um número de controle composto por:

- CNPJ do órgão/entidade da contratação (14 dígitos);
- Dígito 1 — marcador que indica tratar-se de uma contratação;
- Número sequencial da contratação no PNCP*;
- Ano da contratação (4 dígitos).

**Número de Controle da Ata**

id ata pncp

**Máscara:** 99999999999999-1-999999/9999-999999

Cada ata receberá um número de controle composto por:

- Número de Controle PNCP da Contratação (24 dígitos);
- Número sequencial da ata no PNCP*.

**Número de Controle do Contrato**

id contrato pncp

**Máscara:** 99999999999999-2-999999/9999

Cada contrato receberá um número de controle composto por:

- CNPJ do órgão/entidade do contrato (14 dígitos);
- Dígito 2 — marcador que indica tratar-se de um contrato;
- Número sequencial do contrato no PNCP*;
- Ano do contrato (4 dígitos).

.. note::

   O número PNCP será gerado sequencialmente com 6 dígitos e reiniciado a cada mudança de ano.

Dados de Retorno Padronizados
-----------------------------

Ao realizar consultas para obter dados dos Planos Anuais de Contratações (PCA) e das Contratações, a API executará a busca pelos registros solicitados e retornará:

- o total de registros encontrados;
- o total de páginas necessárias para obtenção de todos os registros;
- o número da página consultada;
- o total de páginas restantes.

Essas informações são essenciais para tornar a entrega dos dados mais rápida possível, evitando demora ou interrupção na transferência dos pacotes de dados pelo servidor do PNCP.

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
     - Vetor
     - Vetor com os dados dos registros encontrados.
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
     - Número da página em que a consulta foi realizada.
   * - 5
     - paginasRestantes
     - Inteiro
     - Total de páginas restantes.
   * - 6
     - empty
     - Booleano
     - Indica se o atributo data está vazio.
