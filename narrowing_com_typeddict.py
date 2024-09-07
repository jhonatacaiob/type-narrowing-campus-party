from json import load
from typing import TypedDict, TypeGuard

from rich import print


class Personagem(TypedDict):
    nome: str
    cor: str


class Tartaruga(Personagem):
    arma: str


class Humano(Personagem):
    habilidade: str


def is_tartaruga(obj: object) -> TypeGuard[Tartaruga]:
    return (
        isinstance(obj, dict)
        and all(isinstance(key, str) for key in obj)
        and 'nome' in obj
        and 'cor' in obj
        and 'arma' in obj
        and isinstance(obj['nome'], str)
        and isinstance(obj['cor'], str)
        and isinstance(obj['arma'], str)
    )


def is_humano(obj: object) -> TypeGuard[Humano]:
    return (
        isinstance(obj, dict)
        and all(isinstance(key, str) for key in obj)
        and 'nome' in obj
        and 'cor' in obj
        and 'habilidade' in obj
        and isinstance(obj['nome'], str)
        and isinstance(obj['cor'], str)
        and isinstance(obj['habilidade'], str)
    )


def lutar(tartaruga: Tartaruga) -> None:
    print(
        f'[{tartaruga["cor"]}]{tartaruga["nome"]}[/] atacou com sua arma: {tartaruga["arma"]}'
    )


def ajudar(humano: Humano) -> None:
    print(
        f'[{humano["cor"]}]{humano["nome"]}[/] usa a habilidade {humano["habilidade"]} para ajudar!'
    )


def executar_acao(personagem: Personagem):
    if is_tartaruga(personagem):
        lutar(personagem)

    elif is_humano(personagem):
        ajudar(personagem)
    else:
        print('Não é possível executar uma ação')


with open('./dados.json', mode='r', encoding='utf8') as f:
    dados = load(f)


for personagem in dados['personagens']:
    executar_acao(personagem=personagem)