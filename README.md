# Gerador e Criptografador de Senhas

Este script em Python tem como objetivo gerar senhas fortes e criptografá-las utilizando a biblioteca **Fernet** da **cryptography**, garantindo maior segurança no armazenamento de senhas sensíveis.

## Funcionalidades

- **Geração de Senha Forte**: A função `gerar_senha(tamanho=16)` cria uma senha composta por letras maiúsculas e minúsculas, dígitos e caracteres especiais. O tamanho da senha pode ser personalizado.
  
- **Geração de Chave de Criptografia**: A função `gerar_chave()` gera uma chave criptografada usando a biblioteca Fernet, que será utilizada para criptografar e descriptografar as senhas.

- **Criptografia de Senha**: A função `criptografar_senha(senha, chave)` criptografa a senha fornecida utilizando a chave gerada anteriormente. A senha é convertida para bytes e criptografada.

- **Descriptografia de Senha**: A função `descriptografar_senha(senha_criptografada, chave)` descriptografa uma senha criptografada utilizando a chave fornecida. O resultado é a senha original.

## Como Funciona

1. O script começa gerando uma senha aleatória forte através da função `gerar_senha()`.
2. Em seguida, uma chave de criptografia é gerada pela função `gerar_chave()`.
3. A senha gerada é criptografada com a chave utilizando a função `criptografar_senha()`.
4. A senha criptografada pode ser armazenada de forma segura, e para recuperá-la, basta usar a função `descriptografar_senha()`.

## Exemplos de Uso

Ao rodar o script, será exibido no terminal:

1. A senha gerada.
2. A chave de criptografia.
3. A senha criptografada.
4. A senha descriptografada, demonstrando o processo completo de segurança.

