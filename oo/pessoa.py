class pessoa:
    def __init__(self, nome = nome, idade=17):
        self.idade = idade
        self.nome = nome

        def cumprimentar(self):
            return f'Olá{id(self)}'


if __name__=='__main__':
    p = pessoa('renata')
    print(pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'ana'
    print(p.nome)
    print(p.idade)
