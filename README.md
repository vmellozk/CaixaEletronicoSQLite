# Sistema Bancário - Projeto Pessoal

## Visão Geral

Este projeto consiste na implementação de um sistema bancário básico em Python, utilizando SQLite para o armazenamento de dados. O sistema inclui funcionalidades básicas de criação de contas, depósitos, saques, transferências e geração de extratos. Está sendo desenvolvido como parte de um projeto pessoal e está em constante evolução.

## Funcionalidades Implementadas

- **Cadastro de Clientes e Contas:**
  - Permite o cadastro de novos clientes associados a contas bancárias.
  - Armazena informações como CPF, nome, endereço e saldo das contas.

- **Operações Bancárias:**
  - Depósito de valores em contas.
  - Saque de valores, verificando saldo disponível.
  - Transferência de valores entre contas, com validação de saldo suficiente.

- **Geração de Extrato:**
  - Exibe um extrato detalhado das transações realizadas em uma conta específica.

## Funcionalidades Planejadas

- **Melhorias na Interface de Usuário:**
  - Implementação de uma interface gráfica mais intuitiva utilizando PySimpleGUI.
  - Melhorias na apresentação dos extratos e das informações das contas.

- **Integração com Outros Projetos:**
  - Planejo integrar este sistema bancário a outro projeto no meu repositório do GitHub para oferecer uma solução completa de gerenciamento de contas bancárias.

## Como Utilizar

1. **Pré-requisitos:**
   - Python 3.x instalado.
   - Bibliotecas necessárias listadas no arquivo `requirements.txt`.
   - Banco de dados SQLite (`banco.db`) criado automaticamente ao executar o sistema pela primeira vez.

2. **Configuração Inicial:**
   - Clone este repositório para sua máquina local.
   - Instale as dependências executando `pip install -r requirements.txt`.

3. **Execução:**
   - Execute o arquivo principal `main.py` para iniciar o sistema bancário.
   - Utilize a interface de linha de comando para interagir com as funcionalidades disponíveis.

## Notas

Este projeto está em fase de desenvolvimento ativo. Estou trabalhando para adicionar novas funcionalidades e melhorar a robustez e usabilidade do sistema. Se você tiver sugestões ou encontrar problemas, sinta-se à vontade para abrir uma issue ou entrar em contato diretamente.
