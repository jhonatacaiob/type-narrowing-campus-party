from dataclasses import dataclass
from json import load
from typing import TypeGuard, Self

from beartype import beartype
from rich import print


@dataclass
class Personagem:
    nome: str
    cor: str


@dataclass
class Tartaruga(Personagem):
    arma: str

    def lutar(self: Self) -> None:
        print(f'[{self.cor}]{self.nome}[/] atacou com sua arma: {self.arma}')


@dataclass
class Humano(Personagem):
    habilidade: str

    def ajudar(self: Self) -> None:
        print(
            f'[{self.cor}]{self.nome}[/] usa a habilidade {self.habilidade} para ajudar!'
        )


def is_tartaruga(obj: object) -> TypeGuard[Tartaruga]:
    return isinstance(obj, Tartaruga)


def is_humano(obj: object) -> TypeGuard[Humano]:
    return isinstance(obj, Humano)


@beartype
def executar_acao(personagem: Personagem):
    if is_tartaruga(personagem):
        personagem.lutar()  # Narrowed para Tartaruga
    elif is_humano(personagem):
        personagem.ajudar()  # Narrowed para Humano
    else:
        print('Não é possível executar uma ação')


def criar_personagem(dados: dict) -> Personagem:
    try:
        return Tartaruga(**dados)
    except TypeError:
        try:
            return Humano(**dados)
        except TypeError:
            raise ValueError(
                f'Dados inválidos para criar um personagem: {dados}'
            )


with open('./dados.json', mode='r', encoding='utf8') as f:
    c = load(f)


for p in c['personagens']:
    personagem = criar_personagem(p)
    executar_acao(personagem)
