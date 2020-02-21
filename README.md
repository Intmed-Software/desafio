<h1 align="center">
  <img alt="Fastfeet" title="Medicar" src="assets/logo.png" width="300px" />
</h1>

<h3 align="center">
  Desafio: Medicar
</h3>

<p align="center">Sistema para gestão de consultas em uma clínica médica</p>

<p align="center">
  <a href="#sobre-o-desafio">Sobre o desafio</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#histórias-de-usuário">Histórias de usuário</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#pencil-critérios-de-avaliação">Critérios de avaliação</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#gear-backend">Backend</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#art-frontend">Frontend</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#date-entrega">Entrega</a>&nbsp;&nbsp;&nbsp;
</p>


## Sobre o desafio
Durante este desafio você irá construir um sistema para uma clínica chamada Medicar com o intuito de auxiliar seus clientes na marcação de consultas e gerenciar seu corpo médico. 

## Histórias de usuário
* O cliente da clínica pode criar uma conta no sistema
* O cliente da clínica pode se autenticar no sistema
* O cliente pode marcar uma consulta
  * Não deve ser possível marcar consultas para um dia e horário não disponível ou já alocado para outro cliente
  * Não deve ser possível marcar consultas para dia e horário passados
  * Não deve ser possível marcar consultas para um dia horário na qual o paciente já tem uma consulta marcada
* O cliente pode desmarcar uma consulta
  * Não deve ser possível desmarcar uma consulta que já aconteceu
* O cliente pode visualizar as suas consultas marcadas que ainda não aconteceram
* O gestor da clínica pode cadastrar especialidades médicas
* O gestor da clínica pode cadastrar médicos
* O gestor da clínica pode alocar médicos em horários específicos de um dia


## :pencil: Critérios de avaliação
Serão avaliados os seguintes pontos no desafio final:

1. **Cumprimento dos requisitos:** A aplicação não possui escopo aberto e as funcionalidades implementadas devem atender os objetivos especificados. Neste critério vamos avaliar se a sua aplicação atende todos os requisitos de forma funcional
1. **Conhecimento e uso dos recursos da linguagem/framework:** Não recrie a roda! Utilize as ferramentas disponíveis na linguagem e framework utilizados a seu favor e consulte a documentação sempre que necessário. Nesse critério iremos avaliar o seu conhecimento na linguagem e framework utilizados e o empenho em entender e utilizar seus recursos
1. **Organização do projeto e padronização de código:** O seu projeto está organizado? É fácil se guiar na estrutura de pastas do código-fonte? Ela faz sentido diante do seu propósito? O seu código segue um padrão de escrita (próprio ou conveniconado pela comunidade)? Nesse critério iremos avaliar o nível de organização e padronização de escrita do seu código visando a legibilidade e entendimento
1. **Estilização e usabilidade:** Iremos avaliar se a sua aplicação segue o layout proposto e a facilidade em usá-lo

## :gear: Backend
Todas as implementações de backend devem atender as especificações descritas na seguinte [seção](backend/README.md)

## :art: Frontend
Todas as implementações de frontend devem atender as especificações descritas na seguinte [seção](frontend/README.md)

## :date: Entrega
Adicione todo o código da sua aplicação em um repositório **Github** contendo os códigos de cada parte do sistema implementada dentro de duas pastas: **backend** e/ou **frontend**. Dentro de um arquivo **README** adicione todas as instruções necessárias para que um de nossos instrutores consiga executar a aplicação.

Com tudo pronto, envie um email para contato@intmed.com.br com o título sendo o nome da vaga desejada, no qual se encontra na sessão de [issues](https://github.com/Intmed-Software/vagas/issues) deste repositório, contendo o link para o repositório Github do projeto.

Você tem até o prazo acordado com o recrutador para entregar o seu projeto. Entregas após o prazo devem ser justificadas anteriormente, caso contrário não serão avaliadas.

## :bulb: Observações ##
- O repositório deve conter um README com as instruções de instalação
- Pode se feito a entrega parcial do desafio caso não tenha conseguido chegar até o fim
  
## Opcionais ##
Esses são alguns itens opcionais que pode ser adicionado na solução

_Melhorias de Negócio_
- Login e Cadastro de Médico
- Tela de Gerenciamente de Consultas do Médico
- Notificação do Médico de um Consulta Marcada ou Cancelada
- Recuperação de Senha
- Dashboard para Gestão da Rede Clínica (relatório de quantidade de consultas, gráficos, Rank, etc)

_Melhoria Técnica_
 - Testes
 - Deploy
 - Inspeção de código

## :mega: Alguns links úteis para ajudar ##
Algumas dicas que podem ser importante:
- https://www.diolinux.com.br/2019/12/figma-ferramenta-design-prototipacao-navegador.html
- https://danielkummer.github.io/git-flow-cheatsheet/index.pt_BR.html
- https://angular.io/guide/styleguide
- https://www.django-rest-framework.org/tutorial/quickstart/#quickstart
- https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/
- https://devcenter.heroku.com/articles/deploying-python
- https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/

