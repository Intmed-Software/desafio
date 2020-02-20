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
  <a href="#critérios-de-avaliação">Critérios de avaliação</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#backend">Backend</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#frontend">Frontend</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-entrega">Entrega</a>&nbsp;&nbsp;&nbsp;
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
Todas as implementações de backend devem atender as especificações descritas as seguir

### Interface administrativa
Você deverá implementar uma interface administrativa na qual gestor da clínica (superusuário) poderá cadastrar especialidades, médicos e disponibilizar horários nos quais os clientes poderão marcar as consultas. Utilize a ferramenta de geração de interface administrativa automática do Django para criar esta interface (veja a [documentação](https://docs.djangoproject.com/en/3.0/ref/contrib/admin/)).

A interface administrativa deve conter as funcionalidades a seguir:

#### Cadastrar especialidades
Deve ser possível cadastrar as especialidades médicas (ex: CARDIOLOGIA, PEDIATRIA) que a clínica atende fornecendo as seguintes informações:

* **Nome:** nome da especialidade médica (obrigatório)

#### Cadastrar médicos
Deve ser possível cadastrar os médicos que podem atender na clínica fornecendo as seguintes informações:

* **Nome:** Nome do médico (obrigatório)
* **CRM:** Número do médico no conselho regional de medicina (obrigatório)
* **E-mail:** Endereço de e-mail do médico
* **Telefone:** Telefone do médico
* **Especialidade:** Especialidade na qual o médico atende

#### Criar agenda para médico
Deve ser possível criar uma agenda para um médico em um dia específico fornecendo as seguintes informações:

* **Médico:** Médico que será alocado (obrigatório)
* **Dia:** Data de alocação do médico (obrigatório)
* **Horários:** Lista de horários na qual o médico deverá ser alocado para o dia especificado (obrigatório)

#### Restrições:
* Não deve ser possível criar mais de uma agenda para um médico em um mesmo dia
* Não deve ser possível criar uma agenda para um médico em um dia passado

### API
Você deverá construir uma API, seguindo os padrões e boas práticas do REST contendo os seguintes endpoints:

#### Listar especialidades médicas
Lista todas as especialidades médicas disponíveis na clínica

#### Requisição
```
GET /especialidades/
```

#### Resposta
```json
[
    {
      "id":1,
      "nome": "Pediatria"
    },
    {
      "id":2,
      "nome": "Ginecologia"
    },
    {
      "id":3,
      "nome": "Cardiologia"
    },
    {
      "id":4,
      "nome": "Clínico Geral"
    }
]
```

Deve ser possível filtrar a lista de especialidades retornadas por um termo de pesquisa, por exemplo:

```
http://medicar.backend.com/especialidades/?search=ped
```

## :art: Frontend

## 📅 Entrega
Adicione todo o código da sua aplicação em um repositório **Github** contendo os códigos de cada parte do sistema implementada dentro de duas pastas: **backend** e/ou **frontend**. Dentro de um arquivo **README** adicione todas as instruções necessárias para que um de nossos instrutores consiga executar a aplicação.

Com tudo pronto, envie um email para contato@intmed.com.br com o título sendo o nome da vaga desejada, no qual se encontra na sessão de [issues](https://github.com/Intmed-Software/vagas/issues) deste repositório, contendo o link para o repositório Github do projeto.

Você tem até o prazo acordado com o recrutador para entregar o seu projeto. Entregas após o prazo devem ser justificadas anteriormente, caso contrário não serão avaliadas.

## Frontend ## 
Se optar por desenvolver apenas o Frontend:
  - Os dados podem ser mockados
  - O Design proposto foi realizado no [Figma](https://www.figma.com/) está disponível nesse [link](https://www.figma.com/file/kJIvTRUJtKin3PFthaGXnj/Desafio-Full-Stack-Intmed?node-id=0%3A1) 
> _Para utilizar o Figma é necessário criar uma conta, ela será útil para visualizar as propriedades css do layout._

## Backend ##
- O cadastro de Especialidades, Medicos e Horários disponíveis podem ser realizados no [Admin](https://docs.djangoproject.com/en/3.0/ref/contrib/admin/) 
- Pode ser utilizado qualquer versão do Django e qualquer pacote adicional.

- Os endpoints devem ser apresentados da seguinte maneira

**Lista as Especialidades**
_<url_base>/especialidades/_
```
{
  "count": 50,
  "next": "<url_base>/especialidades/?page=",
  "previous": "<url_base>/especialidades/?page=",
  "results": [
    {
      "id":1,
      "descricao": "Pediatria"
    },
    {
      "id":2,
      "descricao": "Ginecologia"
    },
    {
      "id":3,
      "descricao": "Cardiologia"
    },
    {
      "id":4,
      "descricao": "Clínico Geral"
    }
    ...
  ]
}
```
**Lista os Médicos de uma Especialidade**
_<url_base>/especialidades/<especialidade_id>/medicos/_
```
{
  "count": 50,
  "next": "<url_base>/especialidades/<especialidade_id>/medicos/?page=",
  "previous": "<url_base>/especialidades/<especialidade_id>/medicos/?page=",
  "results": [
    {
      "id":1,
      "nome": "Drauzio Varella",
      "crm": "9999 - CE"
    },
    {
      "id":2,
      "nome": "Gregory House",
      "crm": "9999 - DF"
    },
    {
      "id":3,
      "nome": "Tony Tony Chopper",
      "crm": "9999 - SP"
    },
    {
      "id":4,
      "nome": "Stephen Vincent Strange",
      "crm": "9999 - GO"
    }
    ...
  ]
}
```
**Lista as Consultas de um médico**
_<url_base>/medicos/<medico_id>/consultas/_
```
{
  "count": 50,
  "next": "<url_base>/medicos/<medico_id>/consultas/?page=",
  "previous": "<url_base>/medicos/<medico_id>/consultas/?page=",
  "results": [
    {
      "id":1,
      "dia": "01/01/2020",
      "horarios": [
          {
            "id":1,
            "hora": "12:00"
          },
          {
            "id":1,
            "hora": "13:00"
          },
          {
            "id":1,
            "hora": "14:00"
          }
      ]
    },
    {
      "id":1,
      "dia": "05/01/2020",
      "horarios": [
          {
            "id":1,
            "hora": "08:00"
          },
          {
            "id":1,
            "hora": "09:00"
          },
          {
            "id":1,
            "hora": "10:00"
          }
      ]
    },
    ...
  ]
}
```

**Dados de um Paciente**
_<url_base>/pacientes/<paciente_id>/_
```
{
  "nome": "Lucas Freitas",
  "email": "lucasfreitas@email.com"
}
```


**Lista as Consultas de um Paciente**
_<url_base>/pacientes/<paciente_id>/consultas/_
```
{
  "count": 50,
  "next": "<url_base>/pacientes/<paciente_id>/consultas/?page=",
  "previous": "<url_base>/pacientes/<paciente_id>/consultas/?page=",
  "results": [
    {
      "id":1,
      "dia": "01/01/2020",
      "horario": "12:00",
      "especialidade": "Cardiologia",
      "medico": "Drauzio Varella",
      "data_agendamento": "2019-12-20T10:45:0-03:00"
    },
    {
      "id":1,
      "dia": "05/01/2020",
      "horario": "09:00",
      "especialidade": "Clínico Geral",
      "medico": "Stephen Vincent Strange",
      "data_agendamento": "2019-12-20T10:45:0-03:00"
    },
    ...
  ]
}
```

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

