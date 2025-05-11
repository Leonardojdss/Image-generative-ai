# Projeto: Geração de Imagens Avançada (OpenAI GPT-Image-1)

Este projeto demonstra o uso do modelo avançado de inteligência artificial de geração de imagens da OpenAI, o GPT-Image-1, para criar ou editar imagens a partir de prompts bem definidos pelo usuário.

## Objetivo
O objetivo é apresentar, de forma simples, como utilizar o modelo GPT-Image-1 da OpenAI para criar ou editar imagens, facilitando a integração e experimentação com modelos generativos de última geração.

## Estrutura do Projeto
- `src/`
  - `main.py`: Script principal para execução do projeto.
  - `generate_image.py`: Módulo responsável pela integração com o modelo GPT-Image-1 e geração das imagens.
  - `output/`: Pasta onde as imagens geradas são salvas, organizadas por data e hora.
- `env/`: Ambiente virtual Python com as dependências do projeto.

## Requisitos
- Python 3.10 ou superior
- Ambiente virtual configurado (ver abaixo)
- Dependências instaladas (ver abaixo)
- Chave de API da OpenAI com acesso ao modelo GPT-Image-1

## Instalação
1. Clone este repositório.
2. Ative o ambiente virtual:
   ```bash
   source env/bin/activate
   ```
3. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```
   *(Se não houver um arquivo `requirements.txt`, instale as bibliotecas utilizadas nos scripts manualmente.)*

## Como Executar
1. Defina a variável de ambiente `OPENAI_API_KEY` com sua chave de API:
   ```bash
   export OPENAI_API_KEY="sua-chave-aqui"
   ```
2. Com o ambiente virtual ativado, execute o script principal:
   ```bash
   streamlit run src/main.py
   ```
3. As imagens geradas serão salvas na pasta `src/output/` em subpastas organizadas por data e hora.

## Observações
- O projeto utiliza exclusivamente o modelo GPT-Image-1 da OpenAI para geração das imagens.
- Consulte os arquivos em `src/` para entender e modificar os parâmetros de geração.
- Certifique-se de que sua chave de API possui permissão para uso do modelo GPT-Image-1.

---

*Este projeto é apenas para fins educacionais e demonstração.*
