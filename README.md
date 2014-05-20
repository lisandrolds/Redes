REDES DE COMPUTADORES (1110039–M1)

Prof. Maurício Lima Pilla
Versão 28-04-2014
TRABALHO 1
Descrição
Desenvolva um webcrawler HTTP/1.1 multithreaded, com um subconjunto da RFC 2616 [1]. O webcrawler recebe como
parâmetro na linha de comando a profundidade de busca e uma URL. A partir disso, o webcrawler recursivamente busca a
página, as páginas ligadas com tags < ahref > e as imagens, até o nível máximo especiﬁcado na profundidade de busca. Os
parâmetros serão fornecidos na seguinte ordem:
executeme profundidade URL
As seguintes linguagens de programação podem ser usadas, desde que seja possível executar em Linux:
 C, C++ e Objective C
 Java
 Ruby
 Python
 Perl
Bibliotecas, componentes ou códigos disponíveis na Internet que implementem o protocolo HTTP não podem ser usados.
Caso seja detectado desrespeito a este detalhe, o trabalho receberá nota zero.
Para compilar o programa (caso necessário), os alunos devem fornecer um Makeﬁle. Um script chamado executeme deve
ser fornecido para disparar o programa. No máximo 8 threads devem executar em paralelo em um determinado instante. Não é
necessário respeitar o arquivo robots.txt no servidor (embora seja desejável).
O trabalho deve ser todo desenvolvido com o sistema de gerenciamento de versões git. Todas as modiﬁcações nos códigos
devem ser registradas com comentários que façam sentido. Uma opção para compartilhar um repositório apenas com os colegas
que fazem parte do grupo é usar o Sparkleshare. O trabalho pode ser feito em grupos de até 2 alunos, desde que seja possível
identiﬁcar commits de todos os integrantes do grupo com contribuição ao projeto.
O trabalho não deve estar disponível em um repositório aberto.
Produtos
A entrega será realizadas pelo Moodle e deverá conter:
 Fontes do programa e cópia do repositório do sistema de gerenciamento de versões;
 Makeﬁle que gere o programa;
 Script para disparar o executável;
 README.txt contendo nome completo dos alunos e curso, descrevendo a implementação e os testes realizados.
O arquivo entregue deverá estar no formato tgz, com o nome composto pelo id do Google Apps da Computação do primeiro
aluno, _, id do segundo aluno.tgz. Por exemplo: mlpilla_llpilla.tgz
