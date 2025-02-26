import secrets
import string
from cryptography.fernet import Fernet

def gerar_senha(tamanho=16):
  """
  Gera uma senha forte composta por letras (maúsculas e minúsculas)
  dígitos e caracteres especiais.
  """
  caracteres = string.ascii_letters + string.digits + string.punctuation
  senha = ''.join(secrets.choice(caracteres) for _ in range (tamanho))
  return senha

def gerar_chave():
  """
  Gera uma chave criptografada utilizando a biblioteca Fernet.
  """
  chave = Fernet.generate_key()
  return chave

def criptografar_senha(senha, chave):
  """
  Criptografa a senha utilizando a chave fornecida.

  Parâmetros:
  - senha (str): A senha a ser criptografada.
  - chave (bytes): A chave gerada pela biblioteca Fernet.

  Rotorna:
  - senha_criptografada (bytes): A senha criptografada.
  """
  fernet = Fernet(chave)
  senha_bytes = senha.encode() #Aqui converte a chave em criptografia
  senha_criptografada = fernet.encrypt(senha_bytes)
  return senha_criptografada

def descriptografar_senha(senha_criptografada, chave):
  """
  Descriptografa a senha utilizando a chave fornecida.

  Parâmetros:
  - senha_criptografada (bytes): A senha criptografada.
  - chave (bytes): A chave utilizada na criptografia.

  Retorna:
  - senha (str): A senha original descriptografada.
  """
  fernet = Fernet(chave)
  senha_bytes = fernet.decrypt(senha_criptografada)
  senha = senha_bytes.decode()
  return senha

if __name__ == "__main__":
  # Nesta parte gera uma senha forte
  senha = gerar_senha()
  print("Senha gerada: ", senha)

  # Nesta parte gera a chave de criptografia
  chave = gerar_chave()
  print("Chave de criptografia: ", chave.decode())

  # Nesta parte mostra a senha criptografada
  senha_criptografada = criptografar_senha(senha, chave)
  print("Senha criptografada: ", senha_criptografada.decode())

  # Para servir de exemplo aqui mostra-se a a senha descriptografada
  senha_descriptografada = descriptografar_senha(senha_criptografada, chave)
  print("Senha descriptografar: ", senha_descriptografada)