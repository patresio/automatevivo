# AUTOMATEVIVO - Oi eu sou o ROBO 🤖

Sistema desenvolvido para fazer o download das faturas no site da [VIVO](http://www.vivo.com.br), no plano empresarial.

### Necessidades:

- Agilizar o trabalho manual;
- Site da VIVO só disponibiliza download de uma conta por vez;
- Tempo;

🏢 A Prefeitura Municipal de Novo Horizonte viu a necessidade de desenvolver, e o Setor de TI o fez.

## Tecnologias Usadas

| Tecnologia | Versão             | Descrição       |
| :--------- | :----------------- | :-------------- |
| `python`   | `3.11.x or later`  | **Obrigatório** |
| `selenium` | `4.15.x`           | **Obrigatório** |
| `firefox`  | `119.0.1 (64-bit)` | **Obrigatório** |

## Como utilizar:

```bash
git clone https://github.com/patresio/automatevivo.git automatevivo

cd automatevivo

python -m venv .venv
```

Caso esteja no linux ou unix:

```bash
source .venv/bin/activate
```

Caso esteja no windows:

```bash
.venv\Scripts\activate.bat
```

### Proximo passo instalar as dependências:

```bash
pip install --upgrade pip

pip install -r requirements.txt
```

## Arquivo de secret key:

```bash
cp contrib/.env-sample .env
```

Feito isso, adicionar as senhas no arquivo .env

## Após isso vamos rodar o ROBO!

Com todos os passos acima feito vamos rodar o comando!

```bash
python app.py
```
