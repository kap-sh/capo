# capo-dsql: typed, async Python SDK for AWS Dsql

`capo-dsql` is a typed Python SDK for Amazon Aurora DSQL: generate the IAM authentication token that is the password of a DSQL connection, and create and manage clusters. `AsyncDSQLClient` works with asyncio and trio, and `DSQLClient` has the same methods for sync code. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/dsql/](https://capo-sdk.dev/services/dsql/)

## Install capo-dsql

```
pip install capo-dsql
```

## Connect to Aurora DSQL with an IAM auth token

```python
import asyncpg
from capo_dsql import AsyncDSQLClient

HOST = "abc123.dsql.us-east-1.on.aws"


async def main():
    async with AsyncDSQLClient(region="us-east-1") as dsql:
        # The token is the password of the admin role. It is signed locally with
        # the client's credentials, so nothing is sent to AWS
        token = await dsql.generate_db_connect_admin_auth_token(hostname=HOST)

    conn = await asyncpg.connect(
        host=HOST, user="admin", password=token, database="postgres", ssl="require"
    )
    print(await conn.fetchval("SELECT current_user"))
    await conn.close()
```

```python
import psycopg
from capo_dsql import DSQLClient

HOST = "abc123.dsql.us-east-1.on.aws"


def main():
    # The sync client: the same method, without async and await
    with DSQLClient(region="us-east-1") as dsql:
        token = dsql.generate_db_connect_admin_auth_token(hostname=HOST)

    with psycopg.connect(
        host=HOST, user="admin", password=token, dbname="postgres", sslmode="require"
    ) as conn:
        print(conn.execute("SELECT current_user").fetchone())
```

## Connect to Aurora DSQL as your own database role

Connected as `admin`, create the role once and say which IAM identity may log in as it: `CREATE ROLE app WITH LOGIN` and `AWS IAM GRANT app TO 'arn:aws:iam::123456789012:role/app'`. Its tokens come from `generate_db_connect_auth_token`.

```python
import asyncpg
from capo_dsql import AsyncDSQLClient

HOST = "abc123.dsql.us-east-1.on.aws"


async def main():
    async with AsyncDSQLClient(region="us-east-1") as dsql:
        # Any role but admin takes a DbConnect token, here valid for an hour
        # instead of the default 15 minutes
        token = await dsql.generate_db_connect_auth_token(hostname=HOST, expires_in=3600)

    conn = await asyncpg.connect(
        host=HOST, user="app", password=token, database="postgres", ssl="require"
    )
    await conn.close()
```

## Use an Aurora DSQL connection pool with IAM tokens

```python
import asyncpg
from capo_dsql import AsyncDSQLClient

HOST = "abc123.dsql.us-east-1.on.aws"


async def main():
    async with AsyncDSQLClient(region="us-east-1") as dsql:
        # A token only has to be valid when a connection opens. asyncpg calls
        # password for every new connection, so each one gets a fresh token
        async with asyncpg.create_pool(
            host=HOST,
            user="admin",
            database="postgres",
            ssl="require",
            password=lambda: dsql.generate_db_connect_admin_auth_token(hostname=HOST),
        ) as pool:
            print(await pool.fetchval("SELECT current_user"))
```

## Create an Aurora DSQL cluster

```python
from capo_dsql import AsyncDSQLClient


async def main():
    async with AsyncDSQLClient(region="us-east-1") as dsql:
        cluster = await dsql.create_cluster(deletion_protection_enabled=False, tags={"Name": "my-cluster"})
        print(cluster["identifier"], cluster["status"])

        # Its endpoint is the hostname to connect to
        cluster = await dsql.get_cluster(cluster["identifier"])
        print(cluster.get("endpoint"))
```

## List and delete Aurora DSQL clusters

```python
from capo_dsql import AsyncDSQLClient


async def main():
    async with AsyncDSQLClient(region="us-east-1") as dsql:
        # Every cluster, however many pages that takes
        async for cluster in dsql.iter_list_clusters():
            print(cluster["identifier"], cluster["arn"])

        # Delete a cluster and wait until it is gone
        await dsql.delete_cluster("abc123")
        await dsql.wait_until_cluster_not_exists("abc123", max_wait_time=600)
```

## Handle Aurora DSQL errors

```python
from capo_dsql import AsyncDSQLClient
from capo_dsql.errors import ResourceNotFoundException, ServiceError


async def main():
    async with AsyncDSQLClient(region="us-east-1") as dsql:
        # An error the API describes has its own class
        try:
            await dsql.get_cluster("no-such-cluster")
        except ResourceNotFoundException as e:
            print(e.code, e.message)

        # Any error DSQL returns; one without a class of its own is an UnknownServiceError
        except ServiceError as e:
            print(e.code, e.message)
```

## Configure Aurora DSQL retries

```python
from capo_dsql import AsyncDSQLClient


async def main():
    async with AsyncDSQLClient(region="us-east-1", retry_max_attempts=5) as dsql:
        # Throttling, server errors and network failures are retried. Every call
        # of this client gets five attempts instead of the default three
        await dsql.get_cluster("abc123")
```

```python
from capo_dsql import AsyncDSQLClient


async def main():
    async with AsyncDSQLClient(region="us-east-1") as dsql:
        # No retries for this call
        await dsql.get_cluster("abc123", config_overrides={"retry_max_attempts": 1})
```
