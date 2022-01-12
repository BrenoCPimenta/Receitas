# Receitas
Sistema para auxiliar a encontrar receitas baseadas nos ingredientes que a pessoa já tem em casa.

#### Time:
* Back-end:
    * Breno de Castro Pimenta
    * Luiz Felipe Nery 
* Front-end:
    * Pedro Fonseca Wildemberg
    * Rafael Gonçalves de Oliveira

#### Tecnologias:
* **Back-end**: Django
* **Front-end**: Vue.js
* **DataBase**: PostgreSQL


---
### SCM (Sistema de controle de versão)
A main só recebe merge das branchs de sprint.<br>
As brachs de sprint só recebem branchs de strories.<br>
As branchs de stories só recebem merge das branchs de task.<br>
As branchs de task que realmente possuem os commits. <br>

E os merges serão através de PullRequests.<br>
E as branchs serão divididas entre Front e Back como são aplicações independentes.

*Exemplo:*
- back/task-01 -> back/story-01 -> back/sprint_01
- ao terminar a sprint: back/sprint_01 -> master

---

## Backlog

### Backlog do Produto

1. Como usuário, quero buscar receitas por nome.
2. Como usuário, quero buscar receitas que usem o que tenho na geladeira.
3. Como usuário, quero escolher a forma de visualização dos resultados.
4. Como usuário, quero ter mais informações sobre uma receita.
5. Como usuário, quero uma página inicial com receitas relevantes.
6. Como usuário quero fazer buscas avançadas (com filtros, por tipos de receita, por avaliação, por porções, por tempo de preparo).
7. Como usuário, quero enviar feedback a respeito dos resultados das buscas.
8. Como usuário, quero criar uma conta.
9. Como usuário, quero fazer login.
10. Como usuário, quero salvar minhas receitas favoritas.
11. Como usuário, quero resultados personalizados. (Extra)
12. Como usuário, quero a opção de visualizar a aplicação em Dark Mode.
13. Como desenvolvedor, quero entender os feedbacks recebidos.

### Backlog Sprint 1

Histórias: 0, 1, 2, 3 e 4.




0. (Fazer setup do ambiente, banco de dados, etc)
    - [x] 1 Adicionar linter Front (Rafael)
    - [x] 2 Adicionar linter Back (Breno)
    - [x] 3 Adicionar elasticsearch no projeto (Luiz)
      - caso seja muito difícil usar essa ferramenta, usar um banco de dados padrão (https://sunscrapers.com/blog/how-to-use-elasticsearch-with-django/)
    - [x] 5 Inicializar o projeto django (Breno)
    - [x] 6 Integrar elasticsearch com o django (Luiz)
    - [x] 7 Criar regras no repositório para seguir o SCM definido. (Breno / Rafael / Luiz / Pedro)
    - [x] 8 Obter dados (Luiz)
    - [x] 9 Adicionar receitas no elasticsearch (Luiz)
1. Como usuário, quero buscar receitas por nome.
    - [x] 10 Criar página inicial com um componente contendo duas abas. (Rafael)
    - [x] 11 Criar componente na primeira aba para realizar busca por nome de receita. (Rafael)
      - Esse componente deve possuir um campo para o usuário entrar com o texto a ser pesquisado.
    - [x] 13 Criar um componente para listar as receitas que serão retornadas pela API. (Pedro)
    - [x] 14 Criar endpoint com requisição GET (Breno)
      - Essa requisição deve aceitar um parâmetro do tipo string, que será utilizado como filtro para receitas, e retornar uma lista de receitas.
    - [x] 16 Criar busca no elasticsearch para receitas (por 'nome') (Luiz)
2. Como usuário, quero buscar receitas que usem o que tenho na geladeira. 
    - [x] 17 Criar componente da segunda aba de pesquisa para informar os ingredientes a serem adicionados na busca. (Pedro)
    - [x] 20 Criar busca no elasticsearch para ingredientes (lista) (Luiz)
3. Como usuário, quero escolher a forma de visualização dos resultados. 
    - [x] 18 Fornecer 2 formas de visualização: grid com imagens e lista. (Pedro)
      - Grid como default (?), botão para alternar entre formas.
4. Como usuário, quero ter mais informações sobre uma receita.
    - [x] 19 Ao clicar na receita, o usuário deve ser redirecionado para a página original da receita. (Rafael)



### A repensar:
- 4 Conteinerizar todo o ambiente 
- 21 Criar models e etc para elastic
- 47 Definir e criar funções para calcular estatísticas de feedback
- 48 Criar Mapper para estatísticas serem recebidas pelo framework de gráficos do front 
- 49 Criar endpoints para obter as estatísticas de feedback mapeadas 
- 50 Criar testes unitários para as funções de estatísticas dos feedbacks 
- 42 Retornar ID da pesquisa junto da resposta
- 43 Teste dos IDs das respostas

### Backlog Sprint 2

Histórias: 6, 7 e 13.



6. Como usuário quero fazer buscas avançadas (com filtros, por tipos de receita, por avaliação, por porções, por tempo de preparo).
     - [X] 22 Teste GET ingredientes; (Breno)
     - [X] 23 Teste GET receitas; (Breno)
     - [X] 24 Teste GET filtros; (Breno)
     - [X] 25 Teste com Elastic (Breno)
     - [X] 26 Implementar filtro por avaliação (Luiz)
     - [X] 27 Implementar filtro por tipo de receita (Luiz)
     - [X] 28 Implementar filtro por porções (Luiz)
     - [X] 29 Implementar filtro por tempo de preparo (Luiz)
     - [X] 30 Modificar endpoints para suportar filtros (Breno e Luiz)
     - [x] 31 Integrar e utilizar endpoints (Pedro)
     - [x] 32 Adicionar filtro por avaliação (Pedro)
     - [x] 33 Adicionar filtro por tipo de receita (Pedro)
     - [x] 34 Adicionar filtro por porções (Pedro)
     - [x] 35 Adicionar filtro por tempo de preparo (Pedro)
7. Como usuário, quero enviar feedback a respeito dos resultados das buscas.
     - [ ] 36 Criar conexão com o Postgre (Breno)
     - [X] 37 Criar DB Postgre (Breno)
     - [X] 38 Criar Tabela feedback no banco Postgre (Breno)
     - [ ] 39 Criar endpoint para receber e armazenar feedback (Luiz)
     - [x] 40 Criar UI para registrar feedback (Rafael)
     - [X] 41 Criar serviço para enviar feedback (Rafael)   
   <br>
* 13   Como desenvolvedor, quero entender os feedbacks recebidos.
     - [X] 44 Criar tela de dashboard (Rafael)
     - [X] 45 Criar rota para a tela de dashboard (Rafael)
     - [X] 46 Criar componente com gráfico para visualizar qualidade das pesquisas (Rafael)


