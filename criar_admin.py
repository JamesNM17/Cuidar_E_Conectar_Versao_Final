from main import app
from dados1 import db1
from model import Funcionarios

def criar_usuario(usuario, senha, nome_completo, funcao, sexo):
    with app.app_context():

        # Verifica se o usuário já existe
        existente = Funcionarios.query.filter_by(usuario=usuario).first()
        if existente:
            print(f"⚠️ O usuário {usuario} já existe!")
            return

        # Cria o usuário com a senha diretamente
        usuario_criado = Funcionarios(
            nome_completo=nome_completo,
            usuario=usuario,
            funcao=funcao,
            sexo=sexo,
            senha=senha  # define diretamente a senha
        )

        db1.session.add(usuario_criado)
        db1.session.commit()

        print(f"✅ Usuário {usuario} ({funcao}) criado com sucesso!")
        print(f"Usuário: {usuario}")
        print(f"Senha: {senha}")


def criar_usuarios_padrao():
    # Dados dos usuários padrão a serem criados
    usuarios = [
        ("admin", "admin123", "Administrador do Sistema", "Administrador", "Masculino")
    ]

    for usuario in usuarios:
        criar_usuario(*usuario)

if __name__ == "__main__":
    criar_usuarios_padrao()