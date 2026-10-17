# capo-elastic-beanstalk: typed, async Python SDK for AWS Elastic Beanstalk

`capo-elastic-beanstalk` is a typed Python SDK for AWS Elastic Beanstalk. It has an async client, `AsyncElasticBeanstalkClient`, for asyncio and trio, and a sync client, `ElasticBeanstalkClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/elastic-beanstalk/](https://capo-sdk.dev/services/elastic-beanstalk/)

## Installation

```
pip install capo-elastic-beanstalk
```

## Usage

```python
from capo_elastic_beanstalk import AsyncElasticBeanstalkClient


async def main():
    async with AsyncElasticBeanstalkClient() as elastic_beanstalk:
        # Example: call the abort_environment_update operation
        response = await elastic_beanstalk.abort_environment_update()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_elastic_beanstalk import AsyncElasticBeanstalkClient


async def main():
    async with AsyncElasticBeanstalkClient() as elastic_beanstalk:
        # Example: paginate over describe_environment_managed_action_history
        async for item in elastic_beanstalk.iter_describe_environment_managed_action_history():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_elastic_beanstalk import AsyncElasticBeanstalkClient
from capo_elastic_beanstalk.error import InsufficientPrivilegesException


async def main():
    async with AsyncElasticBeanstalkClient() as elastic_beanstalk:
        try:
            await elastic_beanstalk.abort_environment_update()
        except InsufficientPrivilegesException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_elastic_beanstalk import AsyncElasticBeanstalkClient


async def main():
    async with AsyncElasticBeanstalkClient() as elastic_beanstalk:
        # Default: 3 attempts for every operation
        response = await elastic_beanstalk.abort_environment_update()

        # Override per operation
        response = await elastic_beanstalk.abort_environment_update(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await elastic_beanstalk.abort_environment_update(config_overrides={"retry_max_attempts": 1})
```
