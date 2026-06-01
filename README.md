# Compilador SimpleLang (Python + ANTLR4)

Compilador educacional para a linguagem do **Projeto I** (LF&C), com as quatro fases:

1. **Análise léxica** — tokens no formato do enunciado (`<TIPO>` ou `<TIPO, atributo>`)
2. **Análise sintática** — gramática `grammar/SimpleLang.g4` (sem conflitos; `valueAtom` = OPENG); árvore exportada em PNG
3. **Análise semântica** — tabela de símbolos, tipos e validações (ID 16 chars, CTE 0..65535 — 2 bytes sem sinal)
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
├── testes/                 # fontes de teste por fase (ver seção abaixo)
│   ├── lex/
│   ├── syntax/
│   ├── semantic/
│   └── codegen/
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
# Pipeline completo (tokens + PNG da árvore + semântica + quádruplos)
py -3.13 src/main.py examples/exemplo.txt
# Gera examples/exemplo.arvore.png (abra a imagem no explorador de arquivos)

# PNG em caminho customizado
py -3.13 src/main.py examples/exemplo.txt --arvore-png saida/minha_arvore.png

# Somente léxico
py -3.13 src/main.py examples/exemplo.txt --fase lex

# Compilar e executar (interpretador dos quádruplos)
py -3.13 src/main.py examples/exemplo.txt --executar
```

A árvore sintática **não** é mais impressa no terminal: é salva como imagem PNG (matplotlib). O terminal só informa o caminho do arquivo gerado.

## Pasta `testes/`

Conjunto de **30 programas-fonte** (`.txt`) para validar cada fase do compilador de forma isolada — útil para o relatório, demonstrações em vídeo e depuração. Os arquivos estão numerados (`01_`, `02_`, …) e agrupados por pasta conforme a fase que se pretende exercitar.

| Pasta | Quantidade | Finalidade |
|-------|------------|------------|
| `testes/lex/` | 7 | Tokenização: palavras reservadas, operadores, comentários, ID truncado (16 chars), CTE fora de 2 bytes, caractere inválido |
| `testes/syntax/` | 7 | Gramática: erros propositais (`;` faltando, `end program` ausente, `.` final ausente, etc.) e `06_valido_controle.txt` (deve compilar) |
| `testes/semantic/` | 11 | Tipos e tabela de símbolos: redeclaração, variável não declarada, decl sem init, `while` com condição inválida, limites de CTE, programa completo |
| `testes/codegen/` | 5 | Quádruplos e execução: aritmética, expressões aninhadas, lógica, laço `while`, `read`/`write` |

**Observações de sintaxe** (conforme `grammar/SimpleLang.g4`):

- O programa deve terminar com **`.`** após `end program` (ex.: `end program.`).
- Após `end while` **não** use `;`.
- `read` usa identificador direto: `read n;` (sem parênteses).
- Declarações podem omitir `:= expressão` (ex.: `integer x;`).

### Como utilizar

Substitua o caminho do arquivo nos comandos abaixo. Muitos testes em `lex/`, `syntax/` e `semantic/` **devem falhar** — o objetivo é confirmar que a fase correta reporta o erro.

```powershell
# Análise léxica (somente lista de tokens)
py -3.13 src/main.py testes/lex/01_valido_baseline.txt --fase lex

# Pipeline completo: léxico + sintaxe + semântica + quádruplos
py -3.13 src/main.py testes/syntax/06_valido_controle.txt
py -3.13 src/main.py testes/semantic/09_cte_limite_2bytes.txt
py -3.13 src/main.py testes/codegen/01_aritmetica_simples.txt

# Erro esperado (exemplos)
py -3.13 src/main.py testes/lex/07_caractere_invalido.txt --fase lex
py -3.13 src/main.py testes/syntax/02_sem_ponto_virgula.txt
py -3.13 src/main.py testes/semantic/02_redeclaracao.txt

# Interpretador (após compilação bem-sucedida)
py -3.13 src/main.py testes/codegen/04_laco_while.txt --executar
py -3.13 src/main.py testes/codegen/05_read_interativo.txt --executar
```

| Comando | Fase exercitada |
|---------|-----------------|
| `--fase lex` | Apenas léxica |
| Sem flags (padrão `full`) | Léxica → árvore sintática → semântica → geração de quádruplos |
| `--executar` | Igual ao `full`, mais interpretador dos quádruplos |

Se a saída contiver `Erro léxico`, `Erro sintático` ou mensagem de identificador/tipo, a falha ocorreu na fase indicada — compare com a tabela da pasta (`lex` vs `syntax` vs `semantic`). Programas em `codegen/` devem concluir com a seção **Código intermediário (quádruplos)**.

A pasta `examples/` mantém um único exemplo mínimo; `testes/` cobre cenários positivos e negativos para documentação e gravação do vídeo.

## Relatório e vídeo

Documente no relatório: gramática original vs corrigida, conflitos resolvidos, classes em `src/compiler/` e decisões de implementação. O vídeo pode gravar a execução dos comandos da seção **Executar** e dos exemplos em `testes/`.
