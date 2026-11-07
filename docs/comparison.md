# capo vs AWS SDK for Python v4 vs boto3

AWS is building a new Python SDK, the [AWS SDK for Python v4](https://github.com/awslabs/aws-sdk-python), as the async-first successor to boto3. capo and v4 share the same starting point: both are generated from the official [Smithy](https://smithy.io) models and ship one package per service. They differ in what you can do with them today.

[boto3](https://github.com/boto/boto3), the SDK most Python code uses today, has been generally available since 2015. It is sync only and untyped: it builds its clients at runtime from JSON service models and relies heavily on reflection, so without third-party stubs your editor and type checker know nothing about its methods.

This comparison is as of **November 6, 2026**. Every claim about v4 links to its repository or developer guide, so you can check it yourself.

## At a glance

--8<-- "README.md:comparison"

## Size

capo depends only on [zapros](https://zapros.dev) and a few small pure-Python packages, so it is the same size on every platform. v4 pulls in its smithy runtime packages and aiohttp with its compiled dependencies. boto3 has no per-service packages: botocore ships the models of every AWS service, so you install all of them even if you only call Bedrock. Here is Bedrock Runtime, measured with `uv tree --show-sizes` (compressed wheel sizes, Python 3.13 on macOS arm64):

| Install | Packages | Total size |
| --- | --- | --- |
| `capo-bedrock-runtime` | 10 | **912 KiB** |
| `aws-sdk-bedrock-runtime` | 17 | 1,498 KiB |
| `aws-sdk-bedrock-runtime[awscrt]`, needed for bidirectional streaming | 18 | 4,774 KiB |
| `boto3`, every AWS service | 7 | 16,485 KiB |

capo's own package is larger than v4's, because it ships dedicated serialization code for each operation instead of a generic runtime. Everything around it is much smaller.

To see the same trees yourself:

```bash
uv init --bare --python 3.13 demo && cd demo
uv add capo-bedrock-runtime aws-sdk-bedrock-runtime boto3
uv tree --show-sizes --package capo-bedrock-runtime
uv tree --show-sizes --package aws-sdk-bedrock-runtime
uv tree --show-sizes --package boto3
```

=== "capo"

    ```text
    capo-bedrock-runtime v0.21.0 (367.5KiB)
    └── zapros[http2] v0.26.0 (131.0KiB)
        ├── h11 v0.16.0 (36.6KiB)
        ├── pywhatwgurl v0.1.2 (25.8KiB)
        │   └── idna v3.20 (68.0KiB)
        ├── typing-extensions v4.16.0 (44.5KiB)
        ├── anyio v4.16.0 (extra: http2) (131.4KiB)
        │   └── idna v3.20 (68.0KiB)
        └── h2 v4.4.1 (extra: http2) (61.2KiB)
            ├── hpack v4.2.0 (33.4KiB)
            └── hyperframe v6.1.0 (12.7KiB)
    ```

=== "AWS SDK for Python v4"

    ```text
    aws-sdk-bedrock-runtime v0.12.0 (89.6KiB)
    ├── smithy-aws-core[eventstream, json] v0.12.0 (62.7KiB)
    │   ├── aws-sdk-signers v0.4.0 (21.5KiB)
    │   ├── smithy-core v0.9.0 (71.5KiB)
    │   ├── smithy-http v0.6.0 (49.7KiB)
    │   │   └── smithy-core v0.9.0 (71.5KiB)
    │   ├── smithy-aws-event-stream v0.3.0 (extra: eventstream) (15.5KiB)
    │   │   └── smithy-core v0.9.0 (71.5KiB)
    │   └── smithy-json v0.3.0 (extra: json) (10.0KiB)
    │       ├── ijson v3.6.0 (86.6KiB)
    │       └── smithy-core v0.9.0 (71.5KiB)
    ├── smithy-core v0.9.0 (71.5KiB)
    └── smithy-http[aiohttp] v0.6.0 (49.7KiB)
        ├── smithy-core v0.9.0 (71.5KiB)
        ├── aiohttp v3.14.5 (extra: aiohttp) (526.3KiB)
        │   ├── aiohappyeyeballs v2.7.1 (14.7KiB)
        │   ├── aiosignal v1.4.0 (7.3KiB)
        │   │   └── frozenlist v1.8.0 (83.7KiB)
        │   ├── attrs v26.1.0 (66.0KiB)
        │   ├── frozenlist v1.8.0 (83.7KiB)
        │   ├── multidict v7.2.1 (100.8KiB)
        │   ├── propcache v0.5.4 (83.3KiB)
        │   └── yarl v1.25.1 (140.3KiB)
        │       ├── idna v3.20 (68.0KiB)
        │       ├── multidict v7.2.1 (100.8KiB)
        │       └── propcache v0.5.4 (83.3KiB)
        └── yarl v1.25.1 (extra: aiohttp) (140.3KiB) (*)
    (*) Package tree already displayed
    ```

=== "boto3"

    ```text
    boto3 v1.43.126 (136.8KiB)
    ├── botocore v1.43.126 (15.5MiB)
    │   ├── jmespath v1.1.0 (19.9KiB)
    │   ├── python-dateutil v2.9.0.post0 (224.5KiB)
    │   │   └── six v1.17.0 (10.8KiB)
    │   └── urllib3 v2.8.0 (132.5KiB)
    ├── jmespath v1.1.0 (19.9KiB)
    └── s3transfer v0.19.3 (88.1KiB)
        └── botocore v1.43.126 (15.5MiB) (*)
    (*) Package tree already displayed
    ```

## Service coverage

v4 publishes 25 clients, mostly Bedrock, AgentCore and streaming services, plus DynamoDB, Lambda, SQS, SNS, STS, Secrets Manager, CloudTrail and a few others. Amazon S3 and EC2 are not among them.

capo generates a package for every service in the AWS Smithy models, more than 440 of them. If your application uses S3 next to DynamoDB, or EC2 next to STS, capo covers all of them with the same API. With v4 you would keep boto3 alongside it.

## Sync and async

v4 clients are async only: every operation is a coroutine, so a script, a Django view or a Celery task has to wrap each call in `asyncio.run`.

capo generates both clients from the same model, with the same methods and types. Use `AsyncS3Client` in async code and `S3Client` everywhere else. Async clients work under asyncio and [trio](https://trio.readthedocs.io).

## Calling an operation

In capo, every input and output is typed with a [TypedDict](https://docs.python.org/3/library/typing.html#typing.TypedDict), so you pass plain dicts and your type checker still checks every nested key. v4 makes you import a class for every nested shape. In capo you import a type only when you want it, mostly to annotate your own code.

Here is the same Bedrock `Converse` call in each:

=== "capo"

    ```python
    from capo_bedrock_runtime import AsyncBedrockRuntimeClient

    async with AsyncBedrockRuntimeClient() as bedrock:
        response = await bedrock.converse(
            "amazon.nova-lite-v1:0",
            messages=[{"role": "user", "content": [{"text": "What's the weather in Yerevan?"}]}],
            system=[{"text": "You are a weather assistant. Always use the tool."}],
            inference_config={"max_tokens": 512, "temperature": 0.2, "stop_sequences": ["</answer>"]},
            tool_config={
                "tools": [
                    {
                        "toolSpec": {
                            "name": "get_weather",
                            "description": "Current weather for a city",
                            "input_schema": {
                                "json": {
                                    "type": "object",
                                    "properties": {"city": {"type": "string"}},
                                    "required": ["city"],
                                }
                            },
                        }
                    }
                ],
                "tool_choice": {"tool": {"name": "get_weather"}},
            },
        )
        print(response["stop_reason"])
    ```

=== "capo, with named types"

    ```python
    from capo_bedrock_runtime import AsyncBedrockRuntimeClient
    from capo_bedrock_runtime.types.content_block import ContentBlockTextMember
    from capo_bedrock_runtime.types.inference_configuration import InferenceConfiguration
    from capo_bedrock_runtime.types.message import Message
    from capo_bedrock_runtime.types.specific_tool_choice import SpecificToolChoice
    from capo_bedrock_runtime.types.system_content_block import SystemContentBlockTextMember
    from capo_bedrock_runtime.types.tool import ToolToolSpecMember
    from capo_bedrock_runtime.types.tool_choice import ToolChoiceToolMember
    from capo_bedrock_runtime.types.tool_configuration import ToolConfiguration
    from capo_bedrock_runtime.types.tool_input_schema import ToolInputSchemaJsonMember
    from capo_bedrock_runtime.types.tool_specification import ToolSpecification

    async with AsyncBedrockRuntimeClient() as bedrock:
        response = await bedrock.converse(
            "amazon.nova-lite-v1:0",
            messages=[
                Message(role="user", content=[ContentBlockTextMember(text="What's the weather in Yerevan?")])
            ],
            system=[SystemContentBlockTextMember(text="You are a weather assistant. Always use the tool.")],
            inference_config=InferenceConfiguration(max_tokens=512, temperature=0.2, stop_sequences=["</answer>"]),
            tool_config=ToolConfiguration(
                tools=[
                    ToolToolSpecMember(
                        toolSpec=ToolSpecification(
                            name="get_weather",
                            description="Current weather for a city",
                            input_schema=ToolInputSchemaJsonMember(
                                json={
                                    "type": "object",
                                    "properties": {"city": {"type": "string"}},
                                    "required": ["city"],
                                }
                            ),
                        )
                    )
                ],
                tool_choice=ToolChoiceToolMember(tool=SpecificToolChoice(name="get_weather")),
            ),
        )
        print(response["stop_reason"])
    ```

=== "AWS SDK for Python v4"

    ```python
    from aws_sdk_bedrock_runtime.client import AsyncBedrockRuntimeClient
    from aws_sdk_bedrock_runtime.models import (
        ContentBlockText,
        ConverseInput,
        InferenceConfiguration,
        Message,
        SpecificToolChoice,
        SystemContentBlockText,
        ToolChoiceTool,
        ToolConfiguration,
        ToolInputSchemaJson,
        ToolSpecification,
        ToolToolSpec,
    )
    from smithy_core.documents import Document

    async with AsyncBedrockRuntimeClient() as bedrock:
        response = await bedrock.converse(
            ConverseInput(
                model_id="amazon.nova-lite-v1:0",
                messages=[
                    Message(role="user", content=[ContentBlockText(value="What's the weather in Yerevan?")])
                ],
                system=[SystemContentBlockText(value="You are a weather assistant. Always use the tool.")],
                inference_config=InferenceConfiguration(
                    max_tokens=512, temperature=0.2, stop_sequences=["</answer>"]
                ),
                tool_config=ToolConfiguration(
                    tools=[
                        ToolToolSpec(
                            value=ToolSpecification(
                                name="get_weather",
                                description="Current weather for a city",
                                input_schema=ToolInputSchemaJson(
                                    value=Document(
                                        {
                                            "type": "object",
                                            "properties": {"city": {"type": "string"}},
                                            "required": ["city"],
                                        }
                                    )
                                ),
                            )
                        )
                    ],
                    tool_choice=ToolChoiceTool(value=SpecificToolChoice(name="get_weather")),
                ),
            )
        )
        print(response.stop_reason)
    ```

## Paginators, waiters and presigning

v4's own README tells you to choose boto3 if you need "paginators, waiters, and presigned URLs". v4 has none of them, so you write the `NextToken` loop, the polling loop and the URL signing yourself.

capo has all three:

```python
async for page in s3.iter_list_objects_v2("bucket"):
    ...

await s3.wait_until_object_exists("bucket", "key")

url = await s3.presigned_get_object("bucket", "key")
```

See [Waiters, Pagination, Presigning](operations.md).

## Credentials

v4's developer guide says it "supports fewer credential sources than other AWS SDKs" and "does not support AWS IAM Identity Center". If your team runs `aws sso login`, v4 cannot use those credentials yet, and its default chain has no web identity source, which EKS IRSA relies on. Its network-based sources (AssumeRole, container credentials, EC2 instance metadata) each ship as a separate package, and the chain skips them unless that package is installed.

capo's default chain includes environment variables, AssumeRole profiles (`role_arn` with `source_profile` or `credential_source`), web identity tokens (EKS IRSA), IAM Identity Center, the shared credentials and config files including `credential_process`, ECS and EKS Pod Identity, and EC2 instance metadata. See [Authentication](authentication.md).

## Streaming

Both SDKs support bidirectional event streams over HTTP/2, used by Bedrock `InvokeModelWithBidirectionalStream` (Nova Sonic), Transcribe Streaming and others.

In v4 the default aiohttp transport can't do it: you install the `awscrt` extra and pass `AWSCRTHTTPClient()` as the transport ([README](https://github.com/awslabs/aws-sdk-python#bidirectional-streaming-transport)). In capo it works with the default client. Uploads can also be retried safely: pass a `Body` and every attempt streams a fresh copy. See [Streaming](streaming.md).

## WASM

capo's async clients run under [Pyodide](https://pyodide.org), in the browser or in Node. The client picks a Pyodide HTTP handler automatically, so the code is the same as anywhere else. WASM support is fully tested: CI runs the async integration tests inside Pyodide on every commit. v4 does not support Pyodide. See [WASM (Pyodide)](wasm.md).

## Which one should you use?

v4 is AWS's official direction, and if you only need Bedrock or another of its 25 services from asyncio code, it is worth watching. AWS itself recommends against using it in production yet.

If you want a modern, typed, per-service SDK now, with sync and async clients, every AWS service, paginators, waiters, presigning and the credentials your team already uses, use capo.

```bash
uv add capo-s3 capo-dynamodb capo-sts
```

Moving from boto3? Operations keep the snake_case names you know from boto3 (`get_item`, `list_objects_v2`). Start with [Usage](usage.md).
