import tkinter as tk
from tkinter import ttk
from tkinter import font

from funcoes import on_buscar_exercicio, on_listar_exercicios, on_cadastrar_exercicio, on_remover_exercicio
from funcoes import on_cadastrar_treino, on_listar_treinos, on_buscar_treino, on_remover_treino
from funcoes import on_atualizar_exercicio, on_atualizar_treino

def mostrar_exercicios():
    limpar_frame()
    ttk.Label(frame_conteudo, text = "Exercícios 💪", font = ("Helvetica", 16, "bold"), foreground = "#FFFFFF", background = "#232323").pack(pady = 10)
    ttk.Button(frame_conteudo, text = "Cadastrar Exercício 📝", style="Lime.TButton", command=on_cadastrar_exercicio).pack(pady = 5)
    ttk.Button(frame_conteudo, text = "Listar Exercícios 📋", style="Lime.TButton", command=on_listar_exercicios).pack(pady = 5)
    ttk.Button(frame_conteudo, text = "Buscar Exercício 🔍", style="Lime.TButton", command=on_buscar_exercicio).pack(pady = 5)
    ttk.Button(frame_conteudo, text = "Atualizar Exercício 🔄", style="Lime.TButton", command=on_atualizar_exercicio).pack(pady = 5)
    ttk.Button(frame_conteudo, text = "Remover Exercício ❌", style="Lime.TButton", command=on_remover_exercicio).pack(pady = 5)
    

def mostrar_treinos():
    limpar_frame()
    ttk.Label(frame_conteudo, text = "Treinos 🏋️", font = ("Helvetica", 16, "bold"), foreground = "#FFFFFF", background="#232323").pack(pady = 10)
    ttk.Button(frame_conteudo, text = "Cadastrar Treino 📝", style = "Purple.TButton", command = on_cadastrar_treino).pack(pady = 5)
    ttk.Button(frame_conteudo, text = "Listar Treinos 📋", style = "Purple.TButton", command = on_listar_treinos).pack(pady = 5)
    ttk.Button(frame_conteudo, text = "Buscar Treino 🔍", style = "Purple.TButton", command = on_buscar_treino).pack(pady = 5)
    ttk.Button(frame_conteudo, text = "Atualizar Treino 🔄", style = "Purple.TButton", command = on_atualizar_treino).pack(pady = 5)
    ttk.Button(frame_conteudo, text = "Remover Treino ❌", style = "Purple.TButton", command = on_remover_treino).pack(pady = 5)
    

def limpar_frame():
    for widget in frame_conteudo.winfo_children():
        widget.destroy()

def criar_interface():
    root = tk.Tk()
    root.title("Gerenciamento de Exercícios e Treinos")
    root.geometry("450x550")
    root.configure(bg = "#232323")

    title_font = font.Font(family = "Helvetica", size = 18, weight = "bold")

    title_label = tk.Label(root, text = "Gerenciamento de Exercícios e Treinos", font = title_font, bg = "#232323", fg = "#FFFFFF")
    title_label.pack(pady = 20)

    style = ttk.Style()
    style.theme_use("clam")

    style.configure("Lime.TButton", font = ("Helvetica", 12, "bold"), foreground = "#232323", background = "#E2F163", padding = 10)
    style.map("Lime.TButton", foreground = [("active", "#232323")], background = [("active", "#A0C334")])

    style.configure("Purple.TButton", font = ("Helvetica", 12, "bold"), foreground = "#232323", background = "#896CFE", padding = 10)
    style.map("Purple.TButton", foreground = [("active", "#232323")], background = [("active", "#6753C7")])

    frame_navegacao = tk.Frame(root, bg = "#232323")
    frame_navegacao.pack(fill = "x", padx = 20, pady = 10)

    ttk.Button(frame_navegacao, text = "Exercícios 💪", style = "Lime.TButton", command = mostrar_exercicios).pack(side = "left", expand = True, padx =  5)
    ttk.Button(frame_navegacao, text = "Treinos 🏋️", style = "Purple.TButton", command = mostrar_treinos).pack(side = "left", expand = True, padx = 5)

    global frame_conteudo
    frame_conteudo = tk.Frame(root, bg = "#232323")
    frame_conteudo.pack(fill = "both", expand = True, padx = 20, pady = 10)

    mostrar_exercicios()

    root.mainloop()
