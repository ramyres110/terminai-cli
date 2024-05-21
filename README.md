# Tai 
![](assets/tai_img_capa.jpg)

Apresento uma aplicação de terminal que utiliza o poder do Gemini (inicialmente) para responder às suas dúvidas diretamente do console.

**Funcionalidades:**

* Interface simples e intuitiva via linha de comando.
* Acesso rápido à vasta base de conhecimento do Gemini (_somente ele por enquanto_).
* Resultados concisos e relevantes para suas perguntas.
* Ideal para encontrar soluções rápidas durante o uso do terminal/desenvolvimento.

**Exemplo de uso:**

```
>> tai "Como iterar sobre um dicionário em Python?"
```

A aplicação consultará o Gemini e retornará a resposta diretamente no seu terminal.

**Benefícios:**

* Aumento de produtividade: encontre respostas rapidamente sem sair do terminal.
* Eficiência: interface minimalista sem distrações.
* Simplicidade: fácil de usar e integrar ao seu fluxo de trabalho.


## Instalação

1. Install Python 3
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Add the bin directory to environment PATH

## Uso

1. Setup API KEY
```bash
tai --setup
```

* configure o apikey={{API do AI Studio <https://aistudio.google.com/app/apikey> }}

2. Ask with:
```
tai "How can I use Google"
```

3. Ajuda
```
tai --help
```