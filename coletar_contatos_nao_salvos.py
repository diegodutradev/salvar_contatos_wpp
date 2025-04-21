from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import csv
import re
import random

# Inicia o driver
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
input("🟢 Escaneie o QR Code do WhatsApp Web e pressione ENTER quando a lista de conversas estiver visível.")

contatos_salvos = []
cliente_index = 1
numeros_detectados = set()

def is_phone_number(texto):
    texto_limpo = re.sub(r'\D', '', texto)
    return texto.startswith('+55') and len(texto_limpo) >= 10

# 🧠 Foco no grid lateral com TAB mais natural (13 TABs)
actions = ActionChains(driver)
for _ in range(13):
    actions.send_keys(Keys.TAB).perform()
    time.sleep(random.uniform(0.1, 0.3))  # Pausa entre os TABs
print("🎯 Foco no grid lateral definido. Iniciando navegação com setas...\n")

tentativas_sem_novos = 0
MAX_TENTATIVAS = 50
ultimos_coletados = 0

while tentativas_sem_novos < MAX_TENTATIVAS:
    # Rola para baixo
    ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
    time.sleep(random.uniform(0.7, 1.3))  # Simula pausa humana

    # Espera um pouco mais para garantir que novos elementos carreguem
    time.sleep(random.uniform(0.3, 0.6))

    # Busca todos os números visíveis no DOM
    spans = driver.find_elements(By.CSS_SELECTOR, 'span[title^="+55"]')
    novos = 0

    for span in spans:
        try:
            numero = span.get_attribute("title").strip()
            if numero in numeros_detectados or not is_phone_number(numero):
                continue

            numero_limpo = re.sub(r'\D', '', numero)
            numeros_detectados.add(numero)
            contatos_salvos.append({
                'Nome': f'Contato {cliente_index}',
                'Telefone': f'+{numero_limpo}'
            })
            print(f'[✔] Contato {cliente_index} - +{numero_limpo}')
            cliente_index += 1
            novos += 1

        except Exception as e:
            print(f"⚠️ Erro ao processar número: {e}")

    if novos == 0:
        tentativas_sem_novos += 1
    else:
        tentativas_sem_novos = 0

print(f"\n✅ Total de contatos coletados: {len(contatos_salvos)}")

# Salvar CSV
with open('contatos_nao_salvos.csv', 'w', newline='', encoding='utf-8') as arquivo:
    fieldnames = ['Nome', 'Telefone']
    writer = csv.DictWriter(arquivo, fieldnames=fieldnames)
    writer.writeheader()
    for contato in contatos_salvos:
        writer.writerow(contato)

print("📦 Arquivo 'contatos_nao_salvos.csv' salvo com sucesso.")
