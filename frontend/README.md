# Especificações técnicas de Frontend do Medicar #

## Experiência de Usuário ##
O Design proposto foi realizado no [Figma](https://www.figma.com/) está disponível nesse [link](https://www.figma.com/file/kJIvTRUJtKin3PFthaGXnj/Desafio-Full-Stack-Intmed?node-id=0%3A1) 
> *_Dica: Para utilizar o Figma é necessário criar uma conta, ela será útil para visualizar as propriedades css do layout._
  - O fluxo para que o paciente possa agendar uma consulta é feito da seguinte maneira:
    1. O paciente clica no botão "Nova Consulta" e vai exibir uma modal com os campos para preechimento
    2. O paciente escolhe a especialidade desejada para a consulta (ex: Dermatologista)
    3. Com isso, deverão aparecer todos os médicos da especialidade escolhida para que o paciente possa selecionar
    4. Uma vez escolhido o médico desejado, deverão aparecer os dias em que o médico está disponível para realizar uma consulta
    5. Ao selecionar um dia específico, deverão aparecer os horário disponíveis do médico para a data escolhida
    6. Ao final deste processo, o paciente poderá marcar a consulta com sucesso
    7. A consulta marcada deve está na lista do Paciente quando fechar a modal
> *_Dica: No Figma, no canto superior direito tem um botão "Present", ele apresenta uma simulaçaõ do fluxo das telas_

 - O fluxo para o paciente cancelar uma consulta:
    1. O paciente clica em "Desmarcar" de uma das opções da lista
    2. Deverá exibir uma modal de confirmação
    3. Ao clicar "Sim" a consulta deve ser desmarcada e não deverá está mais na lista

 ## Considerações ##
- Deve ser exibido _feedback_ para o usuários quando ocorrer sucesso ou falha nas chamadas de serviços
- Deve ser tratado corretamente os códigos HTTP

## Links importantes ##
Alguns links que podem ajudar no desafio ;)

- https://www.diolinux.com.br/2019/12/figma-ferramenta-design-prototipacao-navegador.html
- https://angular.io/guide/styleguide
- https://danielkummer.github.io/git-flow-cheatsheet/index.pt_BR.html
- https://developer.mozilla.org/pt-BR/docs/Web
