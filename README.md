# Paniel e-sus

O projeto consiste em uma aplicação simples e eficiente para leitura e filtragem de arquivos de atendimentos provenientes de um sistema do e-SUS. Através dessa aplicação, os usuários poderão obter informações valiosas e relevantes sobre os atendimentos registrados no sistema, de forma a facilitar a análise e o gerenciamento desses dados.

A aplicação oferece recursos avançados de filtragem, permitindo aos usuários especificar critérios personalizados para extrair os atendimentos desejados. Isso possibilita uma análise mais precisa e focada, economizando tempo e esforço na busca por informações específicas.

## Como rodar?


0) Clone esse repositorio;
1) Entre na pasta `paniel-esus` usando `cd paniel-esus`.
2) Digite `sudo docker compose build` pressione enter e espere finalizar.
3) Digite `sudo docker compose up` pressione enter e aguarde a aplicação migrar o banco e inicialigar.
4) Prontinho a sua aplicação vai rodar na porta `8001`

## Documentação
Os endpoints devem estar acessível na URL: `http://localhost:8001`.

-   [GET] Inicio `/`
    -   Retornará a versão atual e a contagem de documentos no banco de dados.

-   [GET] Atendimentos `/api/v1/atendimentos`
    -   Retornará todos os atendimentos realizados.
    -   Opções de filtragens:
        -   `data_atendimento (str): Formato 'YYYY-mm-dd'`
        -   `condicao_saude (str): hipertensao|diabetes|ferida vascular|dengue|tuberculose`.
        -   `unidade (str)`.
