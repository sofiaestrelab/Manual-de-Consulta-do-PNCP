Acesso ao PNCP
==============

Objetivo
--------

Este documento contempla as orientações para consultas aos dados de contratações,
alienação de bens móveis e imóveis, atas de registro de preços e contratos
realizados no âmbito da Lei nº 14.133/2021.

Protocolo de Comunicação
------------------------

As consultas serão realizadas por meio de API (*Application Programming Interface*)
que utiliza o protocolo de comunicação REST (*Representational State Transfer*)
sobre HTTP/1.1, cujos dados trafegados utilizam a notação JSON (*JavaScript Object Notation*).

Acesso ao PNCP
--------------

Endereços de Acesso
^^^^^^^^^^^^^^^^^^^

A invocação dos serviços será realizada através das URLs citadas abaixo,
conforme requisitos de segurança detalhados na seção seguinte.

Ambiente de Produção
^^^^^^^^^^^^^^^^^^^^

- Portal: https://pncp.gov.br
- Documentação Técnica (Serviços):
  https://pncp.gov.br/api/consulta/swaggerui/index.html
- Serviços (``${BASE_URL}``):
  https://pncp.gov.br/api/consulta

.. note::

   ``${BASE_URL}`` será utilizada nos exemplos de requisições citados neste
   documento. É a URL base para acesso aos serviços disponíveis no PNCP.
>>>>>>> 5b537965d518f2156f63db5d430d7cab7ba7800d
