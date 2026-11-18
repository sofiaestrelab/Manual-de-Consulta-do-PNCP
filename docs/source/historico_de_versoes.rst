Histórico de Versões
====================

O Histórico de Versões do Manual de Consulta do PNCP tem como objetivo registrar a evolução cronológica das atualizações e melhorias técnicas do documento, 
assegurando que todas as equipes de desenvolvimento e órgãos integradores acompanhem as mudanças normativas e sistêmicas. Ao utilizar esse histórico, 
os desenvolvedores e gestores garantem o alinhamento com os schemas e endpoints vigentes, o que otimiza a manutenção das APIs, a correção de inconformidades e a implementação de novas 
funcionalidades no portal. O uso do histórico de versões contribui para a previsibilidade, a transparência e a governança das manutenções evolutivas no ecossistema de contratações públicas.

Versão: 2.0 (atual)
-------------------

.. Attention::

   As alterações da versão 2.0 estão destacadas em amarelo, conforme o exemplo a seguir:

.. list-table::
   :width: 100%
   :widths: 5 10 15 55
   :header-rows: 1
   :class: quebra-linha-ultima-coluna

   * - Id
     - Campo
     - Tipo
     - Descrição
   * - 1
     - cnpj
     - Texto
     - CNPJ do órgão do contrato/empenho
   * - :destaque-amarelo-claro:`2`
     - :destaque-amarelo-claro:`ano`
     - :destaque-amarelo-claro:`Inteiro`
     - :destaque-amarelo-claro:`Ano do contrato/empenho`
   * - 3
     - sequencialContrato
     - Inteiro
     - Sequencial do contrato/empenho no PNCP; número sequencial gerado no momento da inclusão

Versão: 1.0
------------

.. Attention::

   As alterações da versão 1.0 estão destacadas em azul, conforme o exemplo a seguir:

.. list-table::
   :width: 100%
   :widths: 5 10 15 55
   :header-rows: 1
   :class: quebra-linha-ultima-coluna

   * - Id
     - Campo
     - Tipo
     - Descrição
   * - 1
     - cnpj
     - Texto
     - CNPJ do órgão do contrato/empenho
   * - :destaque-azul-claro:`2`
     - :destaque-azul-claro:`ano`
     - :destaque-azul-claro:`Inteiro`
     - :destaque-azul-claro:`Ano do contrato/empenho`
   * - 3
     - sequencialContrato
     - Inteiro
     - Sequencial do contrato/empenho no PNCP; número sequencial gerado no momento da inclusão

**Catálogo de Serviços**

:doc:`Serviço Consultar Contratações por Data de Publicação <../catalogo_de_servicos/consultar_contratacoes_por_data_de_publicacao>`

:doc:`Serviço Consultar Contratações com Período de Recebimento de Propostas em Aberto  <../catalogo_de_servicos/consultar_contratacoes_com_periodo_de_recebimento_de_propostas_em_aberto>`

:doc:`Serviço Consultar Atas de Registro de Preço por Período de Vigência <../catalogo_de_servicos/consultar_atas_de_registro_de_preco_por_periodo_de_vigencia>`

:doc:`Serviço Consultar Contratos por Data de Publicação <../catalogo_de_servicos/consultar_contratos_por_data_de_publicacao>`
