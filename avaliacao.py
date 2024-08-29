class Avaliacao:
    def _init_(self, cliente, nota):
        self._cliente = cliente # Nome do cliente que fez a avaliação
        self._nota = nota # Nota dada pelo cliente
    
    # Método para converter o objeto Avaliacao em um dicionário para salvar em JSON
    def _dict_(self):
        return {
            'cliente': self._cliente,
            'nota': self._nota
        }