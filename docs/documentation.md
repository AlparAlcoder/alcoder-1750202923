# Descrição geral

Este é um simples API de armazenamento de itens usando FastAPI. O API permite que você crie novos itens e obtenha um item específico de acordo com o ID.

## Dependências necessárias

- fastapi
- pydantic

Você pode instalar essas dependências usando o pip:

```shell
pip install fastapi pydantic
```

## Rotas do API

- POST /items/
- GET /items/{item_id}

### POST /items/

Crie um novo item.

#### Parâmetros

- `item` (corpo da requisição): Um objeto que inclui `name` (string), `description` (string), e `price` (float).

#### Exemplo de uso

```json
POST /items/
{
    "name": "Item1",
    "description": "This is item1",
    "price": 19.99
}
```

#### Notas importantes

- O item criado será adicionado ao fim da lista de itens. O índice deste item na lista será usado como o item_id para o GET /items/{item_id}.

### GET /items/{item_id}

Obtenha um item por ID.

#### Parâmetros

- `item_id` (na rota): Um inteiro que representa o índice do item na lista de itens.

#### Exemplo de uso

```json
GET /items/0
```

#### Notas importantes

- O índice começa em 0. Portanto, o primeiro item terá um item_id de 0.
- Se o item_id for menos que 0 ou maior ou igual ao comprimento da lista de itens, uma exceção HTTP 404 será lançada com detalhes "Item not found".