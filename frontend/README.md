## Frontend ## 
Se optar por desenvolver apenas o Frontend:
  - Os dados podem ser mockados
  - O Design proposto foi realizado no [Figma](https://www.figma.com/) está disponível nesse [link](https://www.figma.com/file/kJIvTRUJtKin3PFthaGXnj/Desafio-Full-Stack-Intmed?node-id=0%3A1) 
> _Para utilizar o Figma é necessário criar uma conta, ela será útil para visualizar as propriedades css do layout._
  - O fluxo para que o paciente possa realizar uma consulta é feito da seguinte forma:
    - O paciente escolhe a especialidade desejada para a consulta (ex: Dermatologista)
    - Com isso, deverão aparecer todos os médicos da especialidade escolhida para que o paciente possa selecionar
    - Uma vez escolhido o médico desejado, deverão aparecer os dias em que o médico está disponível para realizar uma consulta
    - Ao selecionar um dia específico, deverão aparecer os horário disponíveis do médico para a data escolhida
    - Ao final deste processo, o paciente poderá marcar a consulta com sucesso

## Backend ##
- O cadastro de Especialidades, Medicos e Horários disponíveis podem ser realizados no [Admin](https://docs.djangoproject.com/en/3.0/ref/contrib/admin/) 
- Pode ser utilizado qualquer versão do Django e qualquer pacote adicional.

- Os endpoints devem ser apresentados da seguinte maneira


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
