# Getting Started

## Installation

```
pip install capo-geo-routes
```

## Usage

```python
from capo_geo_routes import AsyncGeoRoutesClient


async def main():
    async with AsyncGeoRoutesClient() as geo_routes:
        # Example: call the calculate_isolines operation
        response = await geo_routes.calculate_isolines()
        print(response["arrival_time"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_geo_routes import AsyncGeoRoutesClient
from capo_geo_routes.error import AccessDeniedException


async def main():
    async with AsyncGeoRoutesClient() as geo_routes:
        try:
            await geo_routes.calculate_isolines()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_geo_routes import AsyncGeoRoutesClient


async def main():
    async with AsyncGeoRoutesClient() as geo_routes:
        # Default: 3 attempts for every operation
        response = await geo_routes.calculate_isolines()

        # Override per operation
        response = await geo_routes.calculate_isolines(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await geo_routes.calculate_isolines(config_overrides={"retry_max_attempts": 1})
```
