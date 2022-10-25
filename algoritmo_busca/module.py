'''
    Módulo de tipagens para a construção do grafo
'''

from typing import List


class CidadeAdjacente(object):
    '''
        Classe responsável por gerenciar a arquitetura das cidades vizinhas
    '''
    nome: str
    distancia_real: int

class Mapa(object):
    '''
        Classe responsável por gerenciar a arquitetura da cidade
    '''
    nome: str
    distancia_linha_reta: int
    adjacentes: List[CidadeAdjacente]
