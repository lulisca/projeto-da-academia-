import json
from tkinter import *
from tkinter import messagebox, simpledialog

'''
Caminhos de arquivos
'''
DATAPATH = 'db/exercicios.json'
TREINOS_PATH = 'db/treinos.json'

'''
Caminhos de mensagem
'''
MSG_EXERCICIO_CADASTRADO = "{} foi cadastrado com sucesso."
MSG_EXERCICIO_REMOVIDO = "{} removido com sucesso."
MSG_EXERCICIO_NAO_ENCONTRADO = "Exercício '{}' não encontrado."
MSG_ERRO_LER_ARQUIVO = "Erro ao ler o arquivo JSON. Verifique o formato."
MSG_ERRO_NUMERO_INTEIRO = "Por favor, insira um número inteiro."
MSG_OPCAO_INVALIDA = "Opção inválida!"
MSG_TREINO_CADASTRADO = "{} foi cadastrado como treino com sucesso."
MSG_TREINO_REMOVIDO = "{} removido como treino com sucesso."
MSG_TREINO_NAO_ENCONTRADO = "Treino '{}' não encontrado."

'''
funções exercicios
'''
def cadastrar_exercicio(nome, musculos, carga, serie, repeticoes):
    novo_exercicio = {
        "nome": nome,
        "musculos": musculos.split(","),
        "carga": carga.split(","),
        "serie": int(serie),
        "repeticoes": int(repeticoes)
    }

    try:
        with open(DATAPATH, "r+") as arquivo:
            dados = json.load(arquivo)
            dados.append(novo_exercicio)
            arquivo.seek(0)
            json.dump(dados, arquivo, indent = 4)
        messagebox.showinfo("Sucesso", MSG_EXERCICIO_CADASTRADO.format(novo_exercicio['nome']))

    except FileNotFoundError:
        with open(DATAPATH, "w") as arquivo:
            json.dump([novo_exercicio], arquivo, indent=4)
        messagebox.showinfo("Sucesso", MSG_EXERCICIO_CADASTRADO.format(novo_exercicio['nome']))

    except json.decoder.JSONDecodeError:
        messagebox.showerror("Erro", MSG_ERRO_LER_ARQUIVO)

def listar_exercicios():
    try:
        with open(DATAPATH, "r") as arquivo:
            dados = json.load(arquivo)
            exercicios = "\n".join(f"Nome: {exercicio['nome']}" for exercicio in dados)
            messagebox.showinfo("Exercícios", exercicios if exercicios else "Nenhum exercício cadastrado.")

    except (FileNotFoundError, json.decoder.JSONDecodeError):
        messagebox.showerror("Erro", MSG_ERRO_LER_ARQUIVO)

def buscar_exercicio(nome):
    try:
        with open(DATAPATH, "r") as arquivo:
            dados = json.load(arquivo)
            for exercicio in dados:
                if exercicio["nome"].lower() == nome.lower():
                    info = (
                        f"Nome: {exercicio['nome']}\n"
                        f"Músculos: {', '.join(exercicio['musculos'])}\n"
                        f"carga: {', '.join(exercicio['carga'])}\n"
                        f"Séries: {exercicio['serie']}\n"
                        f"Repetições: {exercicio['repeticoes']}"
                    )
                    messagebox.showinfo("Exercício Encontrado", info)
                    return
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        messagebox.showerror("Erro", MSG_ERRO_LER_ARQUIVO)
    messagebox.showwarning("Não Encontrado", MSG_EXERCICIO_NAO_ENCONTRADO.format(nome))

def atualizar_exercicio(nome):
    try:
        with open(DATAPATH, "r+", encoding='utf-8') as file:
            exercicios = json.load(file)


        for exercicio in exercicios:
            if exercicio["nome"].lower() == nome.lower():

                novo_nome = simpledialog.askstring("Atualizar Exercício", "Novo nome do exercício:", initialvalue = exercicio["nome"])
                musculos = simpledialog.askstring("Atualizar Exercício", "Músculos que o exercício trabalha (separados por vírgula):", initialvalue = ", ".join(exercicio["musculos"]))
                carga = simpledialog.askstring("Atualizar Exercício", "Carga que o exercício usa (separados por vírgula):", initialvalue = ", ".join(exercicio["carga"]))
                serie = simpledialog.askinteger("Atualizar Exercício", "Quantas séries:", initialvalue = exercicio["serie"])
                repeticoes = simpledialog.askinteger("Atualizar Exercício", "Repetições:", initialvalue = exercicio["repeticoes"])

                exercicio["nome"] = novo_nome if novo_nome else exercicio["nome"]
                exercicio["musculos"] = musculos.split(",") if musculos else exercicio["musculos"]
                exercicio["carga"] = carga.split(",") if carga else exercicio["carga"]
                exercicio["serie"] = serie if serie is not None else exercicio["serie"]
                exercicio["repeticoes"] = repeticoes if repeticoes is not None else exercicio["repeticoes"]


                file.seek(0)
                json.dump(exercicios, file, indent=4)
                file.truncate()

                messagebox.showinfo("Sucesso", f"Exercício '{nome}' atualizado com sucesso!")
                return True
        messagebox.showwarning("Não Encontrado", MSG_EXERCICIO_NAO_ENCONTRADO.format(nome))
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        messagebox.showerror("Erro", MSG_ERRO_LER_ARQUIVO)

def remover_exercicio(nome):
    try:
        with open(DATAPATH, "r", encoding='utf-8') as file:
            exercicios = json.load(file)
        exercicios_filtrados = [exercicio for exercicio in exercicios if exercicio["nome"].lower() != nome.lower()]

        if len(exercicios_filtrados) < len(exercicios):
            with open(DATAPATH, "w", encoding='utf-8') as file:
                json.dump(exercicios_filtrados, file, indent = 4)
            messagebox.showinfo("Sucesso", MSG_EXERCICIO_REMOVIDO.format(nome))
            return True
        else:
            messagebox.showwarning("Não Encontrado", MSG_EXERCICIO_NAO_ENCONTRADO.format(nome))
            return False
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        messagebox.showerror("Erro", MSG_ERRO_LER_ARQUIVO)
    messagebox.showwarning("Não Encontrado", MSG_EXERCICIO_NAO_ENCONTRADO.format(nome))

'''
Funções treino
'''
def cadastrar_treino(nome, exercicios):
    novo_treino = {
        "nome": nome,
        "exercicios": exercicios.split(",")
    }

    try:
        with open(TREINOS_PATH, "r+") as arquivo:
            dados = json.load(arquivo)
            dados.append(novo_treino)
            arquivo.seek(0)
            json.dump(dados, arquivo, indent=4)
        messagebox.showinfo("Sucesso", MSG_TREINO_CADASTRADO.format(novo_treino['nome']))

    except FileNotFoundError:
        with open(TREINOS_PATH, "w") as arquivo:
            json.dump([novo_treino], arquivo, indent=4)
        messagebox.showinfo("Sucesso", MSG_TREINO_CADASTRADO.format(novo_treino['nome']))

    except json.decoder.JSONDecodeError:
        messagebox.showerror("Erro", MSG_ERRO_LER_ARQUIVO)

def listar_treinos():
    try:
        with open(TREINOS_PATH, "r") as arquivo:
            dados = json.load(arquivo)
            treinos = "\n".join(f"Nome: {treino['nome']}, Exercícios: {', '.join(treino['exercicios'])}" for treino in dados)
            messagebox.showinfo("Treinos", treinos if treinos else "Nenhum treino cadastrado.")

    except (FileNotFoundError, json.decoder.JSONDecodeError):
        messagebox.showerror("Erro", MSG_ERRO_LER_ARQUIVO)

def buscar_treino(nome):
    try:
        with open(TREINOS_PATH, "r") as arquivo:
            dados = json.load(arquivo)
            for treino in dados:
                if treino["nome"].lower() == nome.lower():
                    info = f"Nome: {treino['nome']}, Exercícios: {', '.join(treino['exercicios'])}"
                    messagebox.showinfo("Treino Encontrado", info)
                    return
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        messagebox.showerror("Erro", MSG_ERRO_LER_ARQUIVO)
    messagebox.showwarning("Não Encontrado", MSG_TREINO_NAO_ENCONTRADO.format(nome))

def atualizar_treino(nome):
    try:
        with open(TREINOS_PATH, "r+", encoding='utf-8') as file:
            treinos = json.load(file)

        for treino in treinos:
            if treino["nome"].lower() == nome.lower():

                novo_nome = simpledialog.askstring("Atualizar Treino", "Novo nome do treino:", initialvalue=treino["nome"])
                exercicios = simpledialog.askstring("Atualizar Treino", "Exercícios do treino (separados por vírgula):", initialvalue=", ".join(treino["exercicios"]))

                treino["nome"] = novo_nome if novo_nome else treino["nome"]
                treino["exercicios"] = exercicios.split(",") if exercicios else treino["exercicios"]

                file.seek(0)
                json.dump(treinos, file, indent=4)
                file.truncate()

                messagebox.showinfo("Sucesso", f"Treino '{nome}' atualizado com sucesso!")
                return True
        messagebox.showwarning("Não Encontrado", MSG_TREINO_NAO_ENCONTRADO.format(nome))
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        messagebox.showerror("Erro", MSG_ERRO_LER_ARQUIVO)

def remover_treino(nome):
    try:
        with open(TREINOS_PATH, "r", encoding='utf-8') as file:
            treinos = json.load(file)
        treinos_filtrados = [treino for treino in treinos if treino["nome"].lower() != nome.lower()]

        if len(treinos_filtrados) < len(treinos):
            with open(TREINOS_PATH, "w", encoding='utf-8') as file:
                json.dump(treinos_filtrados, file, indent=4)
            messagebox.showinfo("Sucesso", MSG_TREINO_REMOVIDO.format(nome))
            return True
        else:
            messagebox.showwarning("Não Encontrado", MSG_TREINO_NAO_ENCONTRADO.format(nome))
            return False
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao excluir treino: {e}")


def on_cadastrar_exercicio():
        nome = simpledialog.askstring("Cadastrar Exercício", "Nome do exercício:")
        musculos = simpledialog.askstring("Cadastrar Exercício", "Músculos que o exercício trabalha (separados por vírgula):")
        carga = simpledialog.askstring("Cadastrar Exercício", "carga que o exercício usa (separados por vírgula):")
        serie = simpledialog.askinteger("Cadastrar Exercício", "Quantas séries:")
        repeticoes = simpledialog.askinteger("Cadastrar Exercício", "Repetições:")
        if nome and musculos and carga and serie is not None and repeticoes is not None:
            cadastrar_exercicio(nome, musculos, carga, serie, repeticoes)

def on_listar_exercicios():
    listar_exercicios()

def on_buscar_exercicio():
    nome = simpledialog.askstring("Buscar Exercício", "Nome do exercício:")
    if nome:
        buscar_exercicio(nome)

def on_atualizar_exercicio():
    nome = simpledialog.askstring("Atualizar Exercício", "Nome do exercício a ser atualizado:")
    if nome:
        atualizar_exercicio(nome)

def on_remover_exercicio():
    nome = simpledialog.askstring("Remover Exercício", "Nome do exercício:")
    if nome:
        remover_exercicio(nome)

def on_cadastrar_treino():
    nome = simpledialog.askstring("Cadastrar Treino", "Nome do treino:")
    exercicios = simpledialog.askstring("Cadastrar Treino", "Exercícios do treino (separados por vírgula):")
    if nome and exercicios:
        cadastrar_treino(nome, exercicios)

def on_listar_treinos():
        listar_treinos()

def on_buscar_treino():
    nome = simpledialog.askstring("Buscar Treino", "Nome do treino:")
    if nome:
        buscar_treino(nome)

def on_atualizar_treino():
    nome = simpledialog.askstring("Atualizar Treino", "Nome do treino a ser atualizado:")
    if nome:
        atualizar_treino(nome)

def on_remover_treino():
    nome = simpledialog.askstring("Remover Treino", "Nome do treino:")
    if nome:
        remover_treino(nome)


