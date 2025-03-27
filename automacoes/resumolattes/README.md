
# Sobre

Este projeto é uma automação *scraping* que recebe uma lista de nomes e obtém, caso haja, os seus resumos do currículo Lattes. Esta programa veio com a finalidade de realizar um levantamento dos alunos egressos da Universidade Estadual do Ceará (UECE), mas pode ser alterado para finalidades de filtragem afins envolvendo a mesma plataforma.

##  Funcionamento
Para que o programa ocorra da forma esperada, é necessário um arquivo 
`lista.csv` simples com uma coluna apenas como o nome `ALUNO` conforme o adiante:

| PESSOAS   | 
| :---------- |  
| Coxiane de Catupyrellen |
| Jubilenildon da Costa |
| Kuzku Ovo | 
| ... |
 
**Observações:** São necessárias as bibliotecas Selenium e Pandas instaladas.

## Sugestões de Melhorias

Algumas melhorias podem ser feitas:
- Pode-se colocar um `input` para que o usuário decida como quer filtrar os resumos seja por outra instituição ou outra característica desejada.
- Necessita tratar o erro quando a pessoa não possui lattes. Caso o indivíduo pesquisado não possua lattes o programa irá gerar um erro. (Facilmente tratável)
- Precisa tratar o erro de busca por pessoas específica, pois em alguns casos  quando se abrem mais que uma aba como resultado da pesquisa LATTES. Nesse caso, o programa não para, mas não explora todos os nomes possíveis.
- Pode-se criar uma GUI uma vez que a demanda desse programa veio por uma pessoa que não sabia programar. Assim, ter uma interface tornaria o trabalho mais fácil podendo até mostrar o tempo de execução e omitindo a exposição do FireFox.
- Poder escolher qual navegador o usuário está utilizando (mais fácil com GUI).
- Pode-se optar por uma alternativa CLI sem problemas (porém menos elegante).