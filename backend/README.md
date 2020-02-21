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

##### Restrições:
* Não deve ser possível criar mais de uma agenda para um médico em um mesmo dia
* Não deve ser possível criar uma agenda para um médico em um dia passado

### API
Você deverá construir uma API, seguindo os padrões e boas práticas do REST contendo os seguintes endpoints:

#### Autenticação

Com exceção dos endpoints de login e cadastro de usuário, todos os endpoints da API devem ser protegidos por autenticação e necessitam receber token via cabeçalho HTTP `Authorization`. Veja um exemplo de requisição:

```
GET /especialidades/
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

#### Listar especialidades médicas
Lista todas as especialidades médicas disponíveis na clínica

##### Requisição
```
GET /especialidades/
```

##### Resposta
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
GET /especialidades/?search=ped
```

#### Listar médicos
Lista todos os médicos que atendem pela clínica

##### Requisição
```
GET /medicos/
```
##### Retorno
```json
[
  {
    "id":1,
    "nome": "Drauzio Varella",
    "crm": "3711 - CE",
    "especialidade": {
      "id": 1,
      "nome": "Pediatria"
    }
  },
  {
    "id":2,
    "nome": "Gregory House",
    "crm": "2544 - DF",
    "especialidade": {
      "id": 3,
      "nome": "Cardiologia"
    }
  },
  {
    "id":3,
    "nome": "Tony Tony Chopper",
    "crm": "3087 - SP",
    "especialidade": {
      "id": 1,
      "nome": "Pediatria"
    }
  }
]
```

Deve ser possível filtrar a listagem de médicos pelo identificador de uma ou mais especialidades e nome do médico (termo de pesquisa), por exemplo:

```
GET /medicos/?search=maria&especialidade=1&especialidade=3
```

#### Listar consultas marcadas
Lista todas as consultas marcadas do usuário logado

##### Requisição
```
GET /consultas/
```

##### Retorno
```json
[
  {
    "id":1,
    "dia": "2020-02-05",
    "horario": "12:00",
    "especialidade": "Cardiologia",
    "medico": "Drauzio Varella",
    "data_agendamento": "2020-02-01T10:45:0-03:00"
  },
  {
    "id":1,
    "dia": "2020-03-01",
    "horario": "09:00",
    "especialidade": "Clínico Geral",
    "medico": "Stephen Vincent Strange",
    "data_agendamento": "2020-02-01T10:45:0-03:00"
  }
]
```

##### Restrições
* A listagem não deve exibir consultas para dia e horário passados
* Os itens da listagem devem vir ordenados por ordem decrescente do dia e horário da consulta. As consultas mais próximas de acontecer devem vir primeiro

#### Listar agendas disponíveis
Lista todas as agendas disponíveis na clínica

```json
[
  {
    "id":1,
    "dia": "2020-02-10",
    "medico":     {
      "id":1,
      "nome": "Drauzio Varella",
      "crm": "3711 - CE",
      "especialidade": {
        "id": 1,
        "nome": "Pediatria"
      }
    },
    "horarios": [
      "14:00",
      "14:15",
      "16:00"
    ]
  },
  {
    "id":2,
    "dia": "2020-02-10",
    "medico":   {
      "id":2,
      "nome": "Gregory House",
      "crm": "2544 - DF",
      "especialidade": {
        "id": 3,
        "nome": "Cardiologia"
      }
    },
    "horarios": [
      "08:00",
      "08:30",
      "09:00",
      "09:30",
      "14:00"
    ]
  }
]
```
