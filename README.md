
# 📥 Automação - Coleta de Contatos Não Salvos no WhatsApp 📥

Este projeto automatiza o processo de **identificação e salvamento de contatos não salvos** no WhatsApp Web. Ideal para quem recebe muitas mensagens de números desconhecidos (clientes, interessados, etc.) e precisa **salvar esses números rapidamente em massa**.

---

## 🚀 Funcionalidades

- Acessa o WhatsApp Web e percorre automaticamente a lista de conversas.
- Identifica todos os contatos que ainda não estão salvos (apresentados apenas como número, ex: `+55 11 91234-5678`).
- Gera um arquivo `contatos_nao_salvos.csv` pronto para importação no Google Contatos.
- Os contatos são nomeados sequencialmente como `Contato 1`, `Contato 2`, etc.

---

## 💻 Requisitos

- Python 3.8+
- Google Chrome instalado
- Biblioteca Selenium instalada:
  ```bash
  pip install selenium
  ```
- WebDriver do Chrome compatível com sua versão do navegador.

---

## ⚙️ Como usar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/diegodutradev/automacao-contatos-whatsapp.git
   cd automacao-contatos-whatsapp
   ```

2. **Execute o script:**
   ```bash
   python coletar_contatos.py
   ```

3. **Siga as instruções do terminal:**
   - Escaneie o QR Code do WhatsApp Web.
   - Aguarde enquanto a automação percorre os contatos.
   - O arquivo `contatos_nao_salvos.csv` será criado com os números detectados.

---

## 🔄 Reutilização e Cuidados

Se você **já rodou o script antes** e vai usá-lo novamente, **é importante ajustar o índice inicial dos contatos**, para evitar duplicação de nomes.  

No código, altere esta linha:
```python
cliente_index = 1
```
Exemplo: se o último contato salvo anteriormente foi `Contato 55`, altere para:
```python
cliente_index = 56
```

---

## 💡 Dica Extra

Após gerar o `contatos_nao_salvos.csv`, você pode importar o arquivo diretamente no [Google Contatos](https://contacts.google.com/) para salvar todos os contatos de uma só vez!

---

## 👨‍💻 Autor

**Diego Dutra**  
[GitHub: @diegodutradev](https://github.com/diegodutradev)

---

## 📜 Licença

Este projeto está sob a licença MIT.
