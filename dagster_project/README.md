# dagster_project

Tudo relacionado à orquestração com Dagster fica agrupado aqui, separado da
lógica de transformação (que mora em `scripts/`, na raiz do projeto).

- `assets/` — um asset do Dagster por camada, cada um só chamando a função
  correspondente em `scripts/`.
- `definitions.py` — arquivo que registra todos os assets para o Dagster.

Para rodar (a partir da raiz do projeto):

```
dagster dev -f dagster_project/definitions.py
```

Abre a interface visual em `http://localhost:3000`, mostrando o grafo de
dependências entre as camadas e permitindo materializar (rodar) o pipeline
completo ou camada por camada.
