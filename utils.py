from models import Pessoas


def insere_pessoas():
    pessoa = Pessoas(nome='Felipe', idade=39)
    print(pessoa)
    pessoa.save()


# consultar a lista de pessoas, imprimir esta lista,
# consultar a idade de uma determindada pessoa da lista, filtra uma pessoa pelo nome
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    # pessoa = Pessoas.query.filter_by(nome='Carol').first()
    # print(pessoa.idade)
    # for p in pessoa:
    #    print(p)


# alteracao da idade, podendo trocar pelo 'nome'
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Carol').first()
    pessoa.idade = 21
    pessoa.save()

# excluir a primeira pessoa com determindo nome
def excluir_pessoa():
    pessoa = Pessoas.query.filter_by(nome='João').first()
    pessoa.delete()


if __name__ == '__main__':
    # insere_pessoas()
    # altera_pessoa()
    # excluir_pessoa()
    consulta_pessoas()
