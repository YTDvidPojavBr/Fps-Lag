import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import win32com.client

# Nome do Launcher
NOME_LAUNCHER = "BS Launcher"

# Caminhos onde o Windows guarda atalhos dos programas
start_menu_paths = [
    os.path.expandvars(r"%ProgramData%\Microsoft\Windows\Start Menu\Programs"),
    os.path.expandvars(r"%AppData%\Microsoft\Windows\Start Menu\Programs")
]

# Função para encontrar atalhos (.lnk)
def listar_programas():
    programas = {}
    shell = win32com.client.Dispatch("WScript.Shell")
    for path in start_menu_paths:
        for root, _, files in os.walk(path):
            for file in files:
                if file.endswith(".lnk"):
                    caminho_lnk = os.path.join(root, file)
                    try:
                        target = shell.CreateShortcut(caminho_lnk).TargetPath
                        nome = os.path.splitext(file)[0]
                        if target:
                            programas[nome] = target
                    except:
                        pass
    return programas

# Função para abrir programa selecionado
def abrir_selecionado():
    selecao = lista.curselection()
    if selecao:
        nome = lista.get(selecao)
        caminho = programas[nome]
        try:
            os.startfile(caminho)
        except Exception as e:
            messagebox.showerror("Erro", str(e))

# Função para mostrar ícone (simples)
def mostrar_icone(event=None):
    selecao = lista.curselection()
    if selecao:
        nome = lista.get(selecao)
        label_imagem.config(text=nome, fg="white", bg="#1b1b1b", font=("Arial", 18, "bold"))

# Carregar programas
programas = listar_programas()

# Criar janela
root = tk.Tk()
root.title(NOME_LAUNCHER)
root.geometry("600x400")
root.configure(bg="#1b1b1b")

# Título
titulo = tk.Label(root, text=NOME_LAUNCHER, bg="#1b1b1b", fg="#ff0000",
                  font=("Arial Black", 20, "bold"))
titulo.pack(pady=10)

# Frame da lista
frame_lista = tk.Frame(root, bg="#1b1b1b")
frame_lista.pack(side="left", fill="y", padx=10, pady=10)

scroll = tk.Scrollbar(frame_lista)
scroll.pack(side="right", fill="y")

lista = tk.Listbox(frame_lista, yscrollcommand=scroll.set, bg="#2b2b2b", fg="white",
                   font=("Arial", 12), selectbackground="#ff0000", width=25, height=15)
for nome in sorted(programas.keys()):
    lista.insert("end", nome)
lista.pack(side="left", fill="y")
scroll.config(command=lista.yview)

lista.bind("<<ListboxSelect>>", mostrar_icone)

# Área da imagem/nome
frame_imagem = tk.Frame(root, bg="#1b1b1b")
frame_imagem.pack(side="top", fill="both", expand=True)

label_imagem = tk.Label(frame_imagem, text="", bg="#1b1b1b", fg="white")
label_imagem.pack(pady=20)

# Botão Abrir
btn_abrir = tk.Button(root, text="ABRIR", command=abrir_selecionado,
                      bg="#ff0000", fg="white", font=("Arial Black", 14),
                      relief="flat", width=20)
btn_abrir.pack(side="bottom", pady=20)

root.mainloop()