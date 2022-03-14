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
Você pode utilizar a sua API caso tenha sido desenvolvida, ou utilizar a nossa [aplicação de teste](https://github.com/Intmed-Software/desafio-mock-server) que imita o funcionamento de uma API real do Medicar.
