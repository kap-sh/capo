# capo-rds: typed, async Python SDK for AWS RDS

`capo-rds` is a typed Python SDK for Amazon RDS and Aurora: connect to a database with an IAM authentication token instead of a password, and manage instances, clusters and snapshots. `AsyncRDSClient` works with asyncio and trio, and `RDSClient` has the same methods for sync code. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/rds/](https://capo-sdk.dev/services/rds/)

## Install capo-rds

```
pip install capo-rds
```

## Connect to an RDS database with IAM authentication

The instance needs IAM database authentication enabled, and the database user has to be set up for it: `GRANT rds_iam TO app` on PostgreSQL, `CREATE USER app IDENTIFIED WITH AWSAuthenticationPlugin AS 'RDS'` on MySQL. The credentials the client signs with need the `rds-db:connect` permission.

```python
import asyncpg
from capo_rds import AsyncRDSClient

HOST = "mydb.123456789012.us-east-1.rds.amazonaws.com"


async def main():
    async with AsyncRDSClient(region="us-east-1") as rds:
        # The token is the password. It is signed locally with the client's
        # credentials, so nothing is sent to AWS, and it is valid for 15 minutes
        token = await rds.generate_db_auth_token(hostname=HOST, port=5432, username="app")

    # IAM authentication needs TLS
    conn = await asyncpg.connect(
        host=HOST, port=5432, user="app", password=token, database="postgres", ssl="require"
    )
    print(await conn.fetchval("SELECT current_user"))
    await conn.close()
```

```python
import psycopg
from capo_rds import RDSClient

HOST = "mydb.123456789012.us-east-1.rds.amazonaws.com"


def main():
    # The sync client: the same method, without async and await
    with RDSClient(region="us-east-1") as rds:
        token = rds.generate_db_auth_token(hostname=HOST, port=5432, username="app")

    with psycopg.connect(
        host=HOST, port=5432, user="app", password=token, dbname="postgres", sslmode="require"
    ) as conn:
        print(conn.execute("SELECT current_user").fetchone())
```

## Keep a connection pool authenticated with IAM tokens

```python
import asyncpg
from capo_rds import AsyncRDSClient

HOST = "mydb.123456789012.us-east-1.rds.amazonaws.com"


async def main():
    async with AsyncRDSClient(region="us-east-1") as rds:
        # A token expires after 15 minutes, but a connection opened with it stays
        # open. asyncpg calls password for every new connection, so each one gets
        # a fresh token
        async with asyncpg.create_pool(
            host=HOST,
            port=5432,
            user="app",
            database="postgres",
            ssl="require",
            password=lambda: rds.generate_db_auth_token(hostname=HOST, port=5432, username="app"),
        ) as pool:
            print(await pool.fetchval("SELECT current_user"))
```

## List RDS database instances

```python
from capo_rds import AsyncRDSClient


async def main():
    async with AsyncRDSClient(region="us-east-1") as rds:
        # Every instance, however many pages that takes
        async for db in rds.iter_describe_db_instances():
            endpoint = db.get("endpoint", {})
            print(db.get("db_instance_identifier"), db.get("db_instance_status"), endpoint.get("address"))

        # One instance, by its identifier
        response = await rds.describe_db_instances(db_instance_identifier="mydb")
        for db in response.get("db_instances", []):
            print(db.get("engine"), db.get("engine_version"))
```

## Create an RDS database with IAM authentication

```python
from capo_rds import AsyncRDSClient


async def main():
    async with AsyncRDSClient(region="us-east-1") as rds:
        # RDS keeps the master password in Secrets Manager; the application
        # connects with IAM tokens instead
        response = await rds.create_db_instance(
            db_instance_identifier="mydb",
            engine="postgres",
            db_instance_class="db.t4g.micro",
            allocated_storage=20,
            master_username="postgres",
            manage_master_user_password=True,
            enable_iam_database_authentication=True,
        )
        print(response.get("db_instance", {}).get("db_instance_status"))
```

## Stop, start and snapshot an RDS database

```python
from capo_rds import AsyncRDSClient


async def main():
    async with AsyncRDSClient(region="us-east-1") as rds:
        await rds.create_db_snapshot(
            db_snapshot_identifier="mydb-before-upgrade", db_instance_identifier="mydb"
        )

        # A stopped instance starts again by itself after seven days
        await rds.stop_db_instance(db_instance_identifier="mydb")
        await rds.start_db_instance(db_instance_identifier="mydb")
```

## Handle RDS errors

```python
from capo_rds import AsyncRDSClient
from capo_rds.errors import DBInstanceNotFoundFault, ServiceError


async def main():
    async with AsyncRDSClient(region="us-east-1") as rds:
        # An error the API describes has its own class
        try:
            await rds.describe_db_instances(db_instance_identifier="no-such-db")
        except DBInstanceNotFoundFault as e:
            print(e.code, e.message)

        # Any error RDS returns; one without a class of its own is an UnknownServiceError
        except ServiceError as e:
            print(e.code, e.message)
```

## Configure RDS retries

```python
from capo_rds import AsyncRDSClient


async def main():
    async with AsyncRDSClient(region="us-east-1", retry_max_attempts=5) as rds:
        # Throttling, server errors and network failures are retried. Every call
        # of this client gets five attempts instead of the default three
        await rds.describe_db_instances()
```

```python
from capo_rds import AsyncRDSClient


async def main():
    async with AsyncRDSClient(region="us-east-1") as rds:
        # No retries for this call
        await rds.describe_db_instances(config_overrides={"retry_max_attempts": 1})
```
