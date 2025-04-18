
# YouTube Video Transcriber

Este projeto é um analisador de vídeo que baixa o áudio de vídeos do YouTube, converte para `.wav` e transcreve automaticamente o conteúdo em texto usando o modelo Whisper da OpenAI.

---

## Funcionalidades

- Baixa o áudio de vídeos do YouTube (via `pytubefix`)
- Converte o áudio para `.wav` com `ffmpeg-python`
- Transcreve automaticamente usando o modelo `whisper-1` da OpenAI
- Salva a transcrição em um arquivo `.txt`

---

## Requisitos

Antes de rodar, instale:

```bash
pip install pytubefix ffmpeg-python openai
sudo apt install ffmpeg  # Linux
```

---

## Como usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repo.git
   cd nome-do-repo
   ```

2. Edite sua chave da OpenAI no arquivo Python:
   ```python
   openai.api_key = "sua-chave-aqui"
   ```

3. Rode o script:
   ```bash
   python analisador.py
   ```

---

## Estrutura esperada

Após rodar, o programa vai salvar:

- O áudio `.wav` do vídeo
- A transcrição em texto: `nome_do_arquivo_transcricao.txt`

---

## Sobre o desenvolvimento

Este projeto foi desenvolvido com apoio de ferramentas de IA como o ChatGPT, com o objetivo de aprendizado e automação de tarefas envolvendo áudio, vídeo e processamento de linguagem natural.

---

## Tecnologias usadas

- Python
- pytubefix
- ffmpeg-python
- OpenAI Whisper API

---

## Licença

Este projeto é livre para fins educacionais e experimentais.

---

### Sessão inspirada do interpretador de código

Este projeto nasceu como uma forma prática de aprender a manipular vídeos, converter áudios e integrar modelos de inteligência artificial no mundo real.

Grande parte da lógica foi construída com o apoio de ferramentas de interpretação de código assistidas por IA. A ideia era compreender, testar e montar cada etapa de forma autônoma, com apoio técnico pontual — uma forma de aprendizado ativo onde o raciocínio e a prática andam juntos.

Essa abordagem permitiu:
- Que o código fosse desenvolvido com foco em aprendizado, não apenas em funcionalidade.
- A adaptação de bibliotecas e conceitos complexos com clareza.
- Um processo de construção incremental, sempre testando e entendendo cada parte.

Este projeto é, portanto, tanto uma ferramenta quanto um registro de aprendizado sobre automação, processamento de mídia e inteligência artificial.
