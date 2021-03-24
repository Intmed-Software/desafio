# Especificações técnicas de backend do Medicar

## Interface administrativa
Você deverá implementar uma interface administrativa na qual gestor da clínica (superusuário) poderá cadastrar especialidades, médicos e disponibilizar horários nos quais os clientes poderão marcar as consultas. Utilize a ferramenta de geração de interface administrativa automática do Django para criar esta interface (veja a [documentação](https://docs.djangoproject.com/en/3.0/ref/contrib/admin/)).

A interface administrativa deve conter as funcionalidades a seguir:

### Cadastrar especialidades
Deve ser possível cadastrar as especialidades médicas (ex: CARDIOLOGIA, PEDIATRIA) que a clínica atende fornecendo as seguintes informações:

* **Nome:** nome da especialidade médica (obrigatório)

### Cadastrar médicos
Deve ser possível cadastrar os médicos que podem atender na clínica fornecendo as seguintes informações:

* **Nome:** Nome do médico (obrigatório)
* **CRM:** Número do médico no conselho regional de medicina (obrigatório)
* **E-mail:** Endereço de e-mail do médico
* **Telefone:** Telefone do médico
* **Especialidade:** Especialidade na qual o médico atende

### Criar agenda para médico
Deve ser possível criar uma agenda para um médico em um dia específico fornecendo as seguintes informações:

* **Médico:** Médico que será alocado (obrigatório)
* **Dia:** Data de alocação do médico (obrigatório)
* **Horários:** Lista de horários na qual o médico deverá ser alocado para o dia especificado (obrigatório)

#### Restrições:
* Não deve ser possível criar mais de uma agenda para um médico em um mesmo dia
* Não deve ser possível criar uma agenda para um médico em um dia passado

## :gear:API
Você deverá construir uma API, seguindo os padrões e boas práticas do REST contendo os seguintes endpoints:

### Autenticação

Com exceção dos endpoints de login e cadastro de usuário, todos os endpoints da API devem ser protegidos por autenticação e necessitam receber token via cabeçalho HTTP `Authorization`. Veja um exemplo de requisição:

```
GET /especialidades/
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

### Listar especialidades médicas
Lista todas as especialidades médicas disponíveis na clínica

#### Requisição
```
GET /especialidades/
```

#### Resposta
```json
[
    {
      "id": 1,
      "nome": "Pediatria"
    },
    {
      "id": 2,
      "nome": "Ginecologia"
    },
    {
      "id": 3,
      "nome": "Cardiologia"
    },
    {
      "id": 4,
      "nome": "Clínico Geral"
    }
]
```

#### Filtros
* Nome da especialidade (termo de pesquisa)

```
GET /especialidades/?search=ped
```

### Listar médicos
Lista todos os médicos que atendem pela clínica

#### Requisição
```
GET /medicos/
```
#### Retorno
```json
[
    {
      "id": 1,
      "crm": 3711,
      "nome": "Drauzio Varella",
      "especialidade": {
            "id":2,
            "nome": "Pediatria"
        }
    },
    {
      "id": 2,
      "crm": 2544,
      "nome": "Gregory House",
      "especialidade": {
          "id": 3,
          "nome": "Cardiologia"
        }
    },
    {
      "id": 3,
      "crm": 3087,
      "nome": "Tony Tony Chopper",
      "especialidade": {
            "id":2,
            "nome": "Pediatria"
        }
    }
]
```

#### Filtros

* Identificador de uma ou mais especialidades
* Nome do médico (termo de pesquisa)

```
GET /medicos/?search=maria&especialidade=1&especialidade=3
```

### Listar consultas marcadas
Lista todas as consultas marcadas do usuário logado

#### Requisição
```
GET /consultas/
```

#### Retorno
```json
[
    {
      "id": 1,
      "dia": "2020-02-05",
      "horario": "12:00",
      "data_agendamento": "2020-02-01T10:45:0-03:00",
      "medico": {
        "id": 2,
        "crm": 2544,
        "nome": "Gregory House",
        "especialidade": {
          "id": 3,
          "nome": "Cardiologia"
        }
      }
    },
    {
      "id": 2,
      "dia": "2020-03-01",
      "horario": "09:00",
      "data_agendamento": "2020-02-01T10:45:0-03:00",
      "medico": {
        "id": 1,
        "crm": 3711,
        "nome": "Drauzio Varella",
        "especialidade": {
            "id":2,
            "nome": "Pediatria"
        }
      }
    }
]
```

#### Regras de negócio
* A listagem não deve exibir consultas para dia e horário passados
* Os itens da listagem devem vir ordenados por ordem crescente do dia e horário da consulta

### Listar agendas disponíveis
Lista todas as agendas disponíveis na clínica

```json
[
    {
      "id": 1,
      "medico": {
        "id": 3,
        "crm": 3087,
        "nome": "Tony Tony Chopper",
        "especialidade": {
            "id":2,
            "nome": "Pediatria"
        }
      },
      "dia": "2020-02-10",
      "horarios": ["14:00", "14:15", "16:00"]
    },
    {
      "id": 2,
      "medico": {
        "id": 2,
        "crm": 2544,
        "nome": "Gregory House",
        "especialidade": {
          "id": 3,
          "nome": "Cardiologia"
        }
      },
      "dia": "2020-02-10",
      "horarios": ["08:00", "08:30", "09:00", "09:30", "14:00"]
    }
]
```

#### Filtros
* Identificador de um ou mais médicos
* Identificador de uma ou mais especialidades
* Intervalo de data

```
GET /agendas/?medico=1&especialidade=2&data_inicio=2020-01-01&data_final=2020-01-05
```

#### Regras de negócio
* As agendas devem vir ordenadas por ordem crescente de data
* Agendas para datas passadas ou que todos os seus horários já foram preenchidos devem ser excluídas da listagem
* Horários dentro de uma agenda que já passaram ou que foram preenchidos devem ser excluídos da listagem

### Marcar consulta
Marca uma consulta para o usuário logado

#### Requisição

```
POST /consultas/
{
  "agenda_id": 1,
  "horario": "14:15"
}
```
#### Retorno

```json
{
  "id": 2,
  "dia": "2020-03-01",
  "horario": "09:00",
  "data_agendamento": "2020-02-01T10:45:0-03:00",
  "medico": {
    "id": 1,
    "crm": 3711,
    "nome": "Drauzio Varella",
    "especialidade": {
            "id":2,
            "nome": "Pediatria"
        }
  }
}
```

#### Regras de negócio
* A data em que o agendamento foi feito deve ser salva ao se marcar uma consulta
* Não deve ser possível marcar uma consulta para um dia e horário passados
* Não deve ser possível marcar uma consulta se o usuário já possui uma consulta marcada no mesmo dia e horário
* Não deve ser possível marcar uma consulta se o dia e horário já foram preenchidos


### Desmarcar consulta
Desmarca uma consulta marcada pelo usuário

#### Requisição
```
DELETE /consultas/<consulta_id>
```

#### Retorno
Não há retorno (vazio)

#### Regras de negócio
* Não deve ser possível desmarcar uma consulta que não foi marcada pelo usuário logado
* Não deve ser possível desmarcar uma consulta que nunca foi marcada (identificador inexistente)
* Não deve ser possível desmarcar uma consulta que já aconteceu
