[x] desenhar um mapa
[x] estabelecer os movimentos
[x] ver os atributos na tela
[x] colocar um resumo do combate na tela

[x] armadilhas
- Alterar as escolhas após movimento
- Possíveis efeitos:
    - Morrer
    - Reduzir a vida
    - Reduzir a força/defesa

[x] mudar skin
- Montar uma lista para possíveis skins
- Montar uma lista para possíveis cores do aventureiro
- Montar uma resposta do teclado para trocar a skin
- Alterar as funções de render para usar as informações do aventureiro

[x] chefe final a cada fase
- Criar uma subclasse de Monstro
- Iniciar o combate quando o aventureiro chegar no tesouro
- Disparar uma mensagem de sucesso no final

[x] customizar o nome do personagem
- Modificar a classe Aventureiro para ela receber um parâmetro `nome`
- Criar uma nova tela para o input do usuário
- Criar uma nova função que inicia essa tela e executa a leitura do teclado
- Modificar o loop principal para chamar essa função

[x] sistema de classes
- Criar duas novas subclasses para a classe `Aventureiro`
- Criar uma nova tela para seleção da classe
- Criar uma nova função que inicia a tela e mapear o clique do usuário
- Modificar o loop principal para chamar a função e decidir qual classe de jogador vai iniciar

[x] variedade de inimigos
- Criar três subclasses de `Inimigo`, substituindo a subclasse `Monstro`
- Criar características distintas para elas
- Alterar a função movimentar para chamar diferentes tipos de monstro

[x] sistema de níveis
- Criar um atributo `xp` para todos os inimigos
- Criar atributos `xp` e `nivel` para o `Aventureiro`
- Criar um mecanismo para ganhar experiência
- Criar um método para fazer a progressão
- Chamar o método para ganhar xp na função de combate
- Atualizar a GUI para incluir o nível na tela

[ ] checkpoint
- Criar uma tecla de ação para salvar o jogo
- Criar uma função que vai salvar os dados do jogo em um arquivo
- Criar uma função para inicializar o jogo novamente
- Alterar a classe `Tesouro` para ter um método para modificar a posição
- Alterar a função `loop` para chamar a função de abrir arquivo ao invés das telas de nome e classe



[ ] sistema de itens
[ ] possíveis ações (desafios)
[ ] recuperar vida
[ ] mecânica de ataque e defesa
[ ] habilidades do aventureiro
[ ] mapa maior
[ ] aliado
[ ] puzzle
[ ] loja in-game
[ ] armas e armaduras
[ ] mudar objetivos do jogo
[ ] sistema de loot
[ ] tipos de dano diferentes
[ ] NPCs
[ ] tela de abertura do jogo
[ ] sistema de menus
[ ] usar sprites
[ ] cliente/servidor
