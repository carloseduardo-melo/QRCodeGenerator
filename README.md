
# Gerador de QR Code Personalizado

Este projeto é para você que deseja criar QR Codes personalizados de forma simples e prática. Basta fornecer o conteúdo (como um link ou texto), escolher as cores que mais combinam com seu estilo, e salvar o QR Code gerado.

---

## Sobre o Projeto

Com este script Python, você pode:
- Criar QR Codes para links, textos ou qualquer outro conteúdo.
- Personalizar as cores de fundo e frente.
- Salvar o QR Code como uma imagem PNG para uso imediato.

---

## Pré-requisitos

Certifique-se de ter o Python instalado no seu computador e as bibliotecas necessárias:
- **qrcode** para gerar o QR Code.
- **Pillow** para manipulação da imagem.

Instale as dependências com:
```bash
pip install qrcode[pil] pillow
```

---

## Como Usar

1. **Edite o Script:**  
   Abra o arquivo Python e configure as variáveis principais:
   - **URL ou Conteúdo:** Altere a variável `url` para o link ou texto que deseja codificar.
   - **Cores:** Escolha as cores ajustando `cor_frente` (frente) e `cor_fundo` (fundo). Pode usar nomes de cores ou códigos hexadecimais.
   - **Nome do Arquivo:** Defina `nome_arquivo` para salvar a imagem gerada.

   Exemplo:
   ```python
   url = "https://google.com/"
   cor_frente = "black"  # Pode ser "blue", "#FF5733", etc.
   cor_fundo = "white"
   nome_arquivo = "meu_qrcode.png"
   ```

2. **Execute o Script:**  
   No terminal, execute o comando:
   ```bash
   python gerar_qrcode.py
   ```

3. **Resultado:**  
   O QR Code será salvo no arquivo especificado (ex.: `meu_qrcode.png`) no mesmo diretório do script.

---

## Exemplo

**Configuração no Script:**
```python
url = "https://ousadiaintima.com.br/"
cor_frente = "black"
cor_fundo = "white"
nome_arquivo = "meu_qrcode.png"
```

**QR Code Gerado:**  
Será salvo como `meu_qrcode.png`, pronto para uso.

---

## Funcionalidades Utilizadas

Este projeto utiliza:
- **qrcode:** Para a geração de QR Codes.
- **Pillow:** Para trabalhar com imagens.

---

## Contribua

Gostou do projeto? Sinta-se à vontade para melhorá-lo:
- Abra uma issue com sugestões.
- Envie um pull request com suas melhorias.

---

## Licença

Este projeto está licenciado sob a licença MIT. Você pode usá-lo e adaptá-lo como preferir.
