<img src="images/segmentacao-publico-alvo.jpg" width="1000" height="270" style="float:center; margin-right:10px;">

# Customer Clustering

Este projeto utiliza a técnica de aprendizado não-supervisionado denominado como clusterização, tal técnica busca agrupar elementos dentro de um conjunto de dados conforme padrões observados pela máquina. Mais especificamente, iremos atuar na área de segmentação de clientes, cujo estudo está direcionado aos padrões entre diferentes clientes ou usuários de um serviço. Para isso, é necessário levantar informações a respeitos dos indivíduos, estas podem estar contidas dentro das classe de informações $\textbf{Comportamentais, Demográficas, Psicológicas,}$ e entre outras que são utilizadas para interesses mais particulares. A segmentação de clientes é um importante processo dentro das empresas, seus resultados podem gerar insights para diferentes setores como o Marketing e Negócios, auxiliando em decisões relevantes.

## 1. Introdução

Neste projeto foi utilizado dados de uma rede de super-mercados norte americana focada em vendas de produtos "FMCG", na tradução "Bens de consumo rápido", estes foram coletados a partir do cadastro de clientes em cartões de fidelidade, os dados contém informações da classe demográfica dos clientes, como a idade, o sexo, o estado civil, o nível de educação, o salário anual, a ocupação e o tamanho da cidade. O conjunto está disponível no Kaggle e pode ser acessado pelo link [Dados Kaggle](https://www.kaggle.com/datasets/dev0914sharma/customer-clustering). 

Após aplicações de ferramentas de exploração e visualização de dados compreendemos que existia potenciais grupos no cojunto, então, com o auxílio das técnicas $\textbf{Elbow}$ e  $\textbf{Silhouette}$ evidenciamos a presença de 4 clusters, a segmentação foi realizada com o método de $\textbf{KMeans}$, cuja performance nos revelou perfis leais ao estabelecimento e perfis potenciais para compras. Com base nisso, concebemos possíveis estratégias para serem implementadas pela rede de super-mercados afim de converter os clientes potenciais em compras e aumentar a frequência de aquisição de clientes leais. 

## 2. Objetivos

O principal objetivo, consiste em gerar insights para o setor de marketing desse estabelecimento, evidenciando os clientes-alvos, e auxiliando na tarefa de construir uma estratégia eficaz. No entanto, no decorrer do projeto buscamos atingir alguns objetivos específicos, tais como:

- Explorar os dados e com isso explicar possíveis clusters que irâo surgir;

- Estudar as maneiras de se obter o número ótimo de grupos em meio aos dados;

- Realizar a clusterização e construir os perfis dos clientes de cada grupo;

- Definir estratégias eficientes com base nos perfis;

- Implementar um método de classificação de novos clientes.

## 3. Métodos

Os métodos aplicados neste projeto e a construção dos notebooks foram baseados nas etapas $\textbf{crisp-dm}$, as quais compreendem:

1. Entendimento do negócio;
2. Entendimento dos dados;
3. Preparação dos dados;
4. Modelagem;
5. Avaliação;
6. Implementação.

  

  ## 4. Desenvolvimento

  1. 
