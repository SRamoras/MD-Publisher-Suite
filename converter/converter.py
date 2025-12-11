import markdown
import os
import datetime

INPUT_DIR = '/app/conteudo'
OUTPUT_DIR = '/app/html'

print(f"[{datetime.datetime.now()}] --- INICIANDO PROCESSO DE PUBLICAÇÃO ---")

if not os.path.exists(OUTPUT_DIR):
    print(f"A criar diretoria de saida: {OUTPUT_DIR}")
    os.makedirs(OUTPUT_DIR)

header = """
<!DOCTYPE html>
<html>
<head>
    <title>Blog DevOps Enterprise</title>
    <link rel="stylesheet" type="text/css" href="style.css">
    <meta charset="UTF-8">
</head>
<body>
    <div class="main-container">
        <header><h1>Notícias DevOps</h1></header>
        <div class="content">
"""

footer = """
        </div>
        <footer>Gerado automaticamente via Docker</footer>
    </div>
</body>
</html>
"""

files_processed = 0

if os.path.exists(INPUT_DIR):
    for filename in os.listdir(INPUT_DIR):
        if filename.endswith(".md"):
            print(f" > A converter: {filename}...")
            
            try:
                with open(os.path.join(INPUT_DIR, filename), 'r', encoding='utf-8') as f:
                    text = f.read()
                    html_content = markdown.markdown(text)
                
                output_filename = filename.replace(".md", ".html")
                with open(os.path.join(OUTPUT_DIR, output_filename), 'w', encoding='utf-8') as f:
                    f.write(header + html_content + footer)
                
                files_processed += 1
            except Exception as e:
                print(f" [ERRO] Falha ao converter {filename}: {e}")
else:
    print(f" [ERRO] A pasta de entrada {INPUT_DIR} não foi encontrada dentro do container.")

print(f"[{datetime.datetime.now()}] --- CONCLUSÃO: {files_processed} ficheiros gerados. ---")