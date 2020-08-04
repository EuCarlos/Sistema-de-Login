from tkinter import *
from tkinter import messagebox
import banco

def bt_Sair():
    login.destroy()
def criar_Cadastro():
    # Formulario de Registro
    register.place(x=1000)
    enter.place(x=1000)
    estado.place(x=50, y=125)
    estadoF.place(x=100, y=125)
    user.place(x=50, y=75)
    userF.place(x=100, y=75)
    password.place(x=50, y=100)
    passwordF.place(x=100, y=100)
    name.place(x=50, y=50)
    nameF.place(x=100, y=50)
    # Base para o SQLite
    register1.place(x=100, y=150)
    retornar.place(x=100, y=180)
def retornar_login():
    # Retorna o necessario
    user.place(x=50, y=50)
    userF.place(x=100, y=50)
    password.place(x=50, y=75)
    passwordF.place(x=100, y=75)
    register.place(x=143, y=150)
    register.place(x=143, y=150)
    retornar.place(x=500)
    enter.place(x=50, y=150)
    # Remover o desnecessario
    nameF.place(x=500)
    name.place(x=500)
    estadoF.place(x=500)
    estado.place(x=500)
    register1.place(x=500)
def registrar_Cadastro():
    # Pegar informações para o Banco
    NameBanco = nameF.get()
    EmailBanco = userF.get()
    PasswordBanco = passwordF.get()
    EstadoBanco = estadoF.get()

    if(NameBanco == "" and EmailBanco == "" and PasswordBanco == "" and EstadoBanco == ""):
        messagebox.showerror(title="Erro de Registro", message="Preencha todos os Campos")
    else:
        # Inserir no Banco
        banco.cursor.execute("""
        INSERT INTO Users(Name, Email, Password, Estado) VALUES(?, ?, ?, ?)
        """,(NameBanco, EmailBanco, PasswordBanco, EstadoBanco))
        banco.conn.commit()
        messagebox.showinfo(title="Register Info", message="Conta criada com sucess")
def acessando_Login():
    EmailLogin = userF.get()
    PasswordLogin = passwordF.get()

    banco.cursor.execute("""
    SELECT * FROM Users
    WHERE Email = ? AND Password = ?
    """,(EmailLogin, PasswordLogin))
    VerificarLogin = banco.cursor.fetchone()
    try:
        if(EmailLogin in VerificarLogin and PasswordLogin in VerificarLogin):
            messagebox.showinfo(title="Login", message="Seja Bem-vindo!")
    except:
        messagebox.showinfo(title="Login", message="Não te encontramos: Certifique se está cadastrado no nosso sistema. ")
login = Tk()

corDeFundo= '#0d1e24'
login.title('LOGIN')
login["bg"] = corDeFundo
login.geometry("300x300+100+100")
login.resizable(width=False, height=False)
login.iconbitmap(default="recursos/icone.ico")

image = PhotoImage(file="recursos/imagelogin.png")
img = Label(login, image=image, bg='#0d1e24')
img.place(x=110, y=205)

title = Label(login, text='LOGIN', bg=corDeFundo, foreground='white')
title.pack(side=TOP, fill=X)

user = Label(login, text='Usuario:', bg=corDeFundo, foreground='white')
user.place(x=50, y=50)
userF = Entry(login)
userF.place(x=100, y=50)
password = Label(login, text='Senha:', bg=corDeFundo, foreground='white')
password.place(x=50, y=75)
passwordF = Entry(login, show="•")
passwordF.place(x=100, y=75)

enter = Button(login, width='10', text='ENTRAR', command=acessando_Login)
enter.place(x=50, y=150)
register = Button(login, width='10', text='CADASTRAR', command=criar_Cadastro)
register.place(x=143, y=150)

register1 = Button(login, width='15', text='CRIAR CADASTRO', command=registrar_Cadastro)
retornar = Button(login, width='15', text='RETORNAR', command=retornar_login)
estado = Label(login, text='Estado:', bg='#0d1e24', foreground='white')
name = Label(login, text='Nome:', bg='#0d1e24', foreground='white')
estadoF = Entry(login)
nameF = Entry(login)

login.mainloop()
