# Especificações técnicas do frontend do Medicar
A seguir estão descritas as especificações de implementação do frontend do Medicar

## :art: Layout
O layout do desafio foi desenvolvido no [Figma](https://www.figma.com/) está disponível nesse [link](https://www.figma.com/file/kJIvTRUJtKin3PFthaGXnj/Desafio-Full-Stack-Intmed?node-id=0%3A1). 

Você deve usar este link para visualizar as telas da aplicação e as propriedades dos componentes do layout para guiar a sua implementação.

## Fluxo na marcação de consultas
O fluxo para que o paciente possa marcar uma consulta deve seguir os seguintes passsos:
1. O paciente escolhe a especialidade desejada para a consulta (ex: Dermatologista)
1. Com isso, deverão aparecer todos os médicos da especialidade escolhida para que o paciente possa selecionar
1. Uma vez escolhido o médico desejado, deverão aparecer os dias em que o médico está disponível para realizar uma consulta
1. Ao selecionar um dia específico, deverão aparecer os horário disponíveis do médico para a data escolhida
1. Ao final deste processo, o paciente poderá confirmar a marcação da consulta e voltar para a tela de listagem

## Utilizando API Medicar
Você pode utilizar uma API do Medicar hospedado no [Heroku](https://www.heroku.com/). 

O endereço da API é [https://intmed-api-medicar.herokuapp.com](https://intmed-api-medicar.herokuapp.com).
Para ter acessos aos _endpoints_ é preciso possuir um usuário, conforme é descrito na sessão [backend](https://github.com/Intmed-Software/desafio/tree/master/backend#api) desse desafio. 

### Criar usuário
É necessário implementar a criação de usuário para acesso ao sistema

#### Requisição
```
POST /users/

{
  "username": <string 150>,
  "email": <string 255>,
  "password": <string 128>
}
```

#### Resposta
```
code status 201
{
  "username": <string 150>,
  "email": <string 255>
}
```

### Obter token
Após criar um usuário é preciso implementar login para obter token para utilizar a API

#### Requisição
```
POST /users/login

{
  "username":,
  "password":
}
```

#### Resposta
```
code status 200
{
  "token": <string>
}
```

Agora basta adicionar nas requisições via cabeçalho HTTP `Authorization` conforme exemplo abaixo:
```
GET /especialidades/
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

### Observações
Nessa API disponibilizada os dados são apresentados de forma **paginada**, então é importante aplicar os filtros conforme é descrito na sessão [backend](https://github.com/Intmed-Software/desafio/tree/master/backend#api) desse desafio.

#### Padrão de paginação
```
{
  "count": <número total de registros>,
  "next": "<próxima página com dados ou null se não houver>",
  "previous": "<página anterior com dados ou null se não houver>",
  "results": [<array com resultados>]
}
```

