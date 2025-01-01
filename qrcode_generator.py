import qrcode
from PIL import Image

def gerar_qrcode(conteudo: str, cor_frente: str, cor_fundo: str, nome_arquivo: str):   
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    
    qr.add_data(conteudo)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color=cor_frente, back_color=cor_fundo)
    qr_img = qr_img.convert("RGBA")
    qr_img.save(nome_arquivo)
    print(f"QR code salvo em: {nome_arquivo}")


if __name__ == "__main__":
    
    url = "https://google.com/"
    cor_frente = "black"   #nomes de cores ou hexadecimal
    cor_fundo = "white"    #nomes de cores ou hexadecimal
    nome_arquivo = "meu_qrcode.png"

    gerar_qrcode(url, cor_frente, cor_fundo, nome_arquivo)
