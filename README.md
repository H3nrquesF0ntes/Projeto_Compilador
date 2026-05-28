# Compilador SimpleLang (Python + ANTLR4)

Compilador educacional para a linguagem do **Projeto I** (LF&C), com as quatro fases:

1. **Análise léxica** — tokens no formato do enunciado (`<TIPO>` ou `<TIPO, atributo>`)
2. **Análise sintática** — gramática `grammar/SimpleLang.g4` (sem conflitos; `valueAtom` = OPENG)
3. **Análise semântica** — tabela de símbolos, tipos e validações (ID 16 chars, CTE 2 bytes)
4. **Geração de código** — quádruplos + interpretador para demonstração

## Estrutura

```
Compiladores/
├── grammar/
│   └── SimpleLang.g4
├── src/
│   ├── main.py
│   ├── generated/          # lexer/parser (gerados pelo ANTLR)
│   └── compiler/
│       ├── lexer_phase.py
│       ├── parser_phase.py
│       ├── token_catalog.py
│       ├── pipeline.py
│       ├── semantic/
│       └── codegen/
├── examples/
│   └── exemplo.txt
├── scripts/
│   └── generate_parser.ps1
└── requirements.txt
```

## Pré-requisitos

- Python 3.13+ (com `pip install -r requirements.txt`)
- Java (instalado automaticamente pelo `antlr4-tools` na primeira execução)

## Gerar lexer/parser

```powershell
.\scripts\generate_parser.ps1
```

Se `antlr4` não estiver no PATH, use o caminho completo do Scripts do Python ou:

```powershell
py -3.13 -m pip install -r requirements.txt
& "$env:LOCALAPPDATA\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\Scripts\antlr4.exe" -Dlanguage=Python3 -visitor -no-listener -o src/generated grammar/SimpleLang.g4
```

## Executar

```powershell
# Pipeline completo (tokens + semântica + quádruplos)
py -3.13 src/main.py examples/exemplo.txt

# Somente léxico
py -3.13 src/main.py examples/exemplo.txt --fase lex

# Compilar e executar (interpretador dos quádruplos)
py -3.13 src/main.py examples/exemplo.txt --executar
```

## Relatório e vídeo

Documente no relatório: gramática original vs corrigida, conflitos resolvidos, classes em `src/compiler/` e decisões de implementação. O vídeo pode gravar a execução dos comandos acima.
