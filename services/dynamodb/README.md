# capo-dynamodb: typed, async Python SDK for Amazon DynamoDB

`capo-dynamodb` is a typed Python SDK for Amazon DynamoDB. `AsyncDynamoDBClient` works with asyncio and trio, and `DynamoDBClient` has the same methods for sync code. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

DynamoDB tags every value with its type, `{"S": "Ada"}` or `{"N": "36"}`. `marshal_item` turns an item of plain Python values into that form, and `unmarshal_item` turns one back.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/dynamodb/](https://capo-sdk.dev/services/dynamodb/)

## Install capo-dynamodb

```
pip install capo-dynamodb
```

## Put and get a DynamoDB item in Python

```python
from capo_dynamodb import AsyncDynamoDBClient, marshal_item, unmarshal_item


async def main():
    async with AsyncDynamoDBClient(region="us-east-1") as dynamodb:
        # Write an item: plain Python values, converted with marshal_item
        await dynamodb.put_item("users", marshal_item({"id": "u1", "name": "Ada", "age": 36}))

        # Read it back by its key, which is converted the same way
        response = await dynamodb.get_item("users", marshal_item({"id": "u1"}))
        if "item" in response:
            user = unmarshal_item(response["item"])
            print(user["name"], user["age"])
```

```python
from capo_dynamodb import DynamoDBClient, marshal_item, unmarshal_item


def main():
    with DynamoDBClient(region="us-east-1") as dynamodb:
        # The sync client: the same methods, without async and await
        dynamodb.put_item("users", marshal_item({"id": "u1", "name": "Ada"}))

        response = dynamodb.get_item("users", marshal_item({"id": "u1"}))
        if "item" in response:
            print(unmarshal_item(response["item"]))
```

## Convert Python values to DynamoDB attribute values

```python
from decimal import Decimal

from capo_dynamodb import marshal_item, unmarshal_item

item = marshal_item(
    {
        "name": "Ada",  # {"S": "Ada"}
        "age": 36,  # {"N": "36"}
        "score": Decimal("9.5"),  # {"N": "9.5"}
        "avatar": b"\x89PNG",  # {"B": b"\x89PNG"}
        "admin": True,  # {"BOOL": True}
        "manager": None,  # {"NULL": True}
        "languages": ["en", "fr"],  # {"L": [{"S": "en"}, {"S": "fr"}]}
        "address": {"city": "London"},  # {"M": {"city": {"S": "London"}}}
        # A set has to be non-empty and hold only strings, only numbers or only bytes
        "tags": {"math", "poetry"},  # {"SS": ["math", "poetry"]}
        "lucky": {7, 3},  # {"NS": ["3", "7"]}
    }
)

# A number comes back as an int when it is whole and as a Decimal otherwise
user = unmarshal_item(item)
print(user["age"], user["score"])  # 36 9.5

# A float raises TypeError, since it cannot hold every DynamoDB number
# exactly: write prices and other fractions as Decimal
marshal_item({"price": Decimal("19.99")})

# Any sequence, mapping or set goes in, such as a tuple or a frozenset;
# it comes back as a list, dict or set
marshal_item({"point": (1, 2), "roles": frozenset({"admin"})})
```

## Query and scan a DynamoDB table

```python
from capo_dynamodb import AsyncDynamoDBClient, marshal_item, unmarshal_item


async def main():
    async with AsyncDynamoDBClient(region="us-east-1") as dynamodb:
        # Every order of one customer, however many pages that takes. The values
        # an expression refers to are AttributeValues too
        async for item in dynamodb.iter_query(
            "orders",
            key_condition_expression="customer_id = :customer",
            expression_attribute_values=marshal_item({":customer": "c1"}),
        ):
            print(unmarshal_item(item))

        # Their orders since a date, newest first
        async for item in dynamodb.iter_query(
            "orders",
            key_condition_expression="customer_id = :customer AND created_at >= :since",
            expression_attribute_values=marshal_item({":customer": "c1", ":since": "2026-01-01"}),
            scan_index_forward=False,
        ):
            print(unmarshal_item(item))

        # Every item of the table; the filter drops items after they are read
        async for item in dynamodb.iter_scan(
            "orders",
            filter_expression="amount > :min",
            expression_attribute_values=marshal_item({":min": 100}),
        ):
            print(unmarshal_item(item))
```

## Update a DynamoDB item

```python
from capo_dynamodb import AsyncDynamoDBClient, marshal_item, unmarshal_item


async def main():
    async with AsyncDynamoDBClient(region="us-east-1") as dynamodb:
        # Count a visit and add a tag in one request, without reading the item first.
        # ALL_NEW returns the item as it is after the update
        response = await dynamodb.update_item(
            "users",
            marshal_item({"id": "u1"}),
            update_expression="SET visits = if_not_exists(visits, :zero) + :one ADD tags :tag",
            expression_attribute_values=marshal_item({":zero": 0, ":one": 1, ":tag": {"regular"}}),
            return_values="ALL_NEW",
        )
        print(unmarshal_item(response.get("attributes", {})))
```

## Write a DynamoDB item only if a condition holds

```python
from capo_dynamodb import AsyncDynamoDBClient, marshal_item, unmarshal_item
from capo_dynamodb.errors import ConditionalCheckFailedException


async def main():
    async with AsyncDynamoDBClient(region="us-east-1") as dynamodb:
        # Create the user only if there is none with this id yet
        try:
            await dynamodb.put_item(
                "users",
                marshal_item({"id": "u1", "name": "Ada", "version": 1}),
                condition_expression="attribute_not_exists(id)",
            )
        except ConditionalCheckFailedException:
            print("u1 already exists")

        # Optimistic locking: rename only if nobody changed the item since version 1.
        # ALL_OLD puts the item as it is now into the error
        try:
            await dynamodb.update_item(
                "users",
                marshal_item({"id": "u1"}),
                update_expression="SET #name = :name, version = :next",
                condition_expression="version = :seen",
                expression_attribute_names={"#name": "name"},
                expression_attribute_values=marshal_item({":name": "Ada L.", ":next": 2, ":seen": 1}),
                return_values_on_condition_check_failure="ALL_OLD",
            )
        except ConditionalCheckFailedException as e:
            print("changed meanwhile:", unmarshal_item(e.data.get("item", {})))
```

## Use DynamoDB Local

[DynamoDB Local](https://hub.docker.com/r/amazon/dynamodb-local) runs in Docker:

```
docker run -p 8000:8000 amazon/dynamodb-local
```

```python
from capo_dynamodb import AsyncDynamoDBClient, Credentials, marshal_item


async def main():
    async with AsyncDynamoDBClient(
        region="us-east-1",
        endpoint="http://localhost:8000",
        # DynamoDB Local takes any credentials
        credentials=Credentials(access_key="local", secret_key="local"),
    ) as dynamodb:
        # A table keyed by id, billed per request
        await dynamodb.create_table(
            "users",
            attribute_definitions=[{"attribute_name": "id", "attribute_type": "S"}],
            key_schema=[{"attribute_name": "id", "key_type": "HASH"}],
            billing_mode="PAY_PER_REQUEST",
        )
        await dynamodb.put_item("users", marshal_item({"id": "u1", "name": "Ada"}))
```

## Handle DynamoDB errors

```python
from capo_dynamodb import AsyncDynamoDBClient, marshal_item
from capo_dynamodb.errors import ResourceNotFoundException, ServiceError


async def main():
    async with AsyncDynamoDBClient(region="us-east-1") as dynamodb:
        # An error the API describes has its own class
        try:
            await dynamodb.get_item("no-such-table", marshal_item({"id": "u1"}))
        except ResourceNotFoundException as e:
            print(e.code, e.message)

        # Any error DynamoDB returns; one without a class of its own is an UnknownServiceError
        except ServiceError as e:
            print(e.code, e.message)
```

## Configure DynamoDB retries

```python
from capo_dynamodb import AsyncDynamoDBClient, marshal_item


async def main():
    async with AsyncDynamoDBClient(region="us-east-1", retry_max_attempts=5) as dynamodb:
        # Throttling, server errors and network failures are retried. Every call
        # of this client gets five attempts instead of the default three
        await dynamodb.get_item("users", marshal_item({"id": "u1"}))
```

```python
from capo_dynamodb import AsyncDynamoDBClient, marshal_item


async def main():
    async with AsyncDynamoDBClient(region="us-east-1") as dynamodb:
        # No retries for this call
        await dynamodb.get_item(
            "users",
            marshal_item({"id": "u1"}),
            config_overrides={"retry_max_attempts": 1},
        )
```
