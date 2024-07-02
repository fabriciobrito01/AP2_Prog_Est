import json
import os.path

from ..personagens.aventureiro.guerreiro import Guerreiro
from ..personagens.aventureiro.paladino import Paladino
from ..personagens.aventureiro.segredo import Segredo
from ..personagens.pocao import Pocao
from ..personagens.tesouro import Tesouro

NOME_SAVE = os.path.join("out", "save.json")

def existe_save():
    return os.path.exists(NOME_SAVE)

def salvar_jogo(aventureiro, tesouro, pocao):
    conteudo = {
        "aventureiro": aventureiro.info(),
        "tesouro": tesouro.info(),
        "pocao": pocao.info()
    }
    with open(NOME_SAVE, "w") as handler:
        json.dump(conteudo, handler, indent=4)

def abrir_arquivo():
    with open(NOME_SAVE, "r") as handler:
        conteudo = json.load(handler)

    match conteudo["aventureiro"]["classe"]:
        case "Guerreiro":
            aventureiro = Guerreiro(conteudo["aventureiro"]["nome"])
        case "Paladino":
            aventureiro = Paladino(conteudo["aventureiro"]["nome"])
        case "Segredo":
            aventureiro = Segredo(conteudo["aventureiro"]["nome"])

    aventureiro.carregar(conteudo["aventureiro"])

    tesouro = Tesouro()
    tesouro.carregar(conteudo["tesouro"])

    pocao = Pocao(tesouro)
    pocao.carregar(conteudo["pocao"])
    
    return aventureiro, tesouro, pocao

def apagar_save():
    if existe_save():
        os.remove(NOME_SAVE)
