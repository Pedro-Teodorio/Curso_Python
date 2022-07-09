"""
TODO: Dicionários

    ? OBS: Em algumas linguagens de  programação, os dicionários Python são conhecidos por mapas.
    ? OBS: Sobre dicionários
        ? - Chave e Valor são separados por dois pontos 'chave:valor'
        ? - Tanto chave quanto valor podem ser de qualquer tipo de dados
        ? - Podemos misturar tipos de dados:

    * Dicionários são coleções do tipo chave/valor
    * [1,2,3] - Listas
    * (1,2,3) - Tuplas
    * Dicionários são representadas por chaves {}
    * print (type({}))

    TODO: Criação de Dicionários

        ! Forma 1 (Mais Comum)
            * paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguay'}
            * print(paises)
            * print(type(paises))
        ! Forma 2 (Menos Comum)
            * paises = dict(br = "Brasil", eua = "Estados Unidos", py ="Paraguay")
            * print(paises)
            * print(type(paises))

    TODO: Acessando Elementos

        ! Forma 1 - Acessando via chave, da mesma forma que lista/tupla
            * print(paises['br'])
            * print(paises['ru'])
            ? OBS: Caso tentamos fazer acesso utilizando uma chave que não existe, teremos o erro KeyError

        ! Forma 2 - Acessando via get - Recomendado
            * print(paises.get('br'))
            * print(paises.get('ru'))
            ! Exemplo 1:
                * pais = paises.get('ru')
                * if pais:
                *     print(f"Encontrei o país {pais}!")
                * else:
                *     print("Não Encontrei o país!")
                ? OBS : Caso o get não encontre o objeto com a chave informada será retornado o valor None e não será gerado KeyError

            ! Exemplo 2:
                * pais = paises.get('ru','Não encontrado')
                * print(f"Encontrei o país {pais}")
                ? OBS : Podemos definir um padrão para caso não encontremos o objeto com a chave informada

        ! Verificando se determinada chave se encontra em um dicionário.

            * print('br' in paises)
            * print('ru' in paises)

        ! Utilizando qualquer tipo em um dicionário

        * localidades = {
        *    (35.4343,39.434): "Escritorio de LA",
        *    (37.4346,39.43466): "Escritorio de Santa Mônica"
        * }
        ? OBS: Tuplas são ótimas para serem chaves de dicionários pois elas são imutaveis

    TODO: Adiconando Elementos em um Dicionário

         * receita = {'Janeiro': 100,'Fevereiro': 300, 'Março': 120}
         * print(receita)
        ! Forma 1 - Mais Comum
            * receita['Abril'] = 450
            * print(receita)

        ! Forma 2
            * novo_dado = {'Maio': 500}
            * receita.update(novo_dado) # = receita.update({'Maio': 500}) 
            * print(receita)

    TODO: Atualizando Elementos em um Dicionário

        ! Forma 1
            * receita['Maio'] = 550
            * print(receita)

        ! Forma 2
            * receita.update({'Maio': 600}) 
            * print(receita)

        ? CONCLUSÃO 1: A forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma.
        ? CONCLUSÃO 2: Em dicionários, NÂO podemos ter chaves repetidas.

    TODO: Removendo Elementos de um dicionário

        * receita = {'Janeiro': 100,'Fevereiro': 300, 'Março': 120}
        * print(receita)
        ! Forma 1 - Mais Comum
            * ret = receita.pop('Março')
            * print(ret)
            * print(receita)
            ? OBS 1 : Precisamos sempre informar a chave e caso não encontre o elemento, um KeyError é retornado.
            ? OBS 2 : Ao removermos um elemento , o valor deste elemento é sempre retornado.
        ! Forma 2
            * del receita['Fevereiro']
            * print(receita)
            ? OBS : Neste caso o valor removido não é retornado.
"""
