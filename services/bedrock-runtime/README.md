# capo-bedrock-runtime: typed, async Python SDK for AWS Bedrock Runtime

`capo-bedrock-runtime` is a typed Python SDK for AWS Bedrock Runtime: chat with Claude, Amazon Nova, Llama and the other Bedrock models. `AsyncBedrockRuntimeClient` works with asyncio and trio, and `BedrockRuntimeClient` has the same methods for sync code. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It covers the Converse API, response streaming, tool use, InvokeModel with a model's own request body, and real-time voice with Nova Sonic over a bidirectional HTTP/2 stream.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/bedrock-runtime/](https://capo-sdk.dev/services/bedrock-runtime/)

## Install capo-bedrock-runtime

```
pip install capo-bedrock-runtime
```

## Chat with Claude and other Bedrock models using the Converse API

```python
from capo_bedrock_runtime import AsyncBedrockRuntimeClient


async def main():
    async with AsyncBedrockRuntimeClient(region="us-east-1") as bedrock:
        # Converse takes the same messages for every model; only the model ID changes
        response = await bedrock.converse(
            "global.anthropic.claude-opus-5-5",
            messages=[{"role": "user", "content": [{"text": "What is the capital of France?"}]}],
            system=[{"text": "Answer in one sentence."}],
            inference_config={"max_tokens": 1024},
        )

        # The reply is a list of content blocks: text, tool calls, images and more
        match response["output"]:
            case {"message": {"content": list() as content}}:
                for block in content:
                    match block:
                        case {"text": str() as text}:
                            print(text)

        print(response["stop_reason"], response["usage"]["total_tokens"])
```

```python
from capo_bedrock_runtime import BedrockRuntimeClient


def main():
    with BedrockRuntimeClient(region="us-east-1") as bedrock:
        # The sync client: the same methods, without async and await
        response = bedrock.converse(
            "global.anthropic.claude-opus-5-5",
            messages=[{"role": "user", "content": [{"text": "Hello!"}]}],
        )
        print(response["output"])
```

## Keep a multi-turn conversation

```python
from capo_bedrock_runtime import AsyncBedrockRuntimeClient, UnknownUnionMember
from capo_bedrock_runtime.types.message import Message


async def main():
    async with AsyncBedrockRuntimeClient(region="us-east-1") as bedrock:
        # The model remembers nothing between calls: send the whole conversation each time
        messages: list[Message] = [{"role": "user", "content": [{"text": "My name is Ada."}]}]
        response = await bedrock.converse("global.anthropic.claude-opus-5-5", messages=messages)

        # The output is a union: UnknownUnionMember stands for a kind of output
        # newer than this client
        output = response["output"]
        if isinstance(output, UnknownUnionMember):
            raise RuntimeError(output.name)
        messages.append(output["message"])

        messages.append({"role": "user", "content": [{"text": "What is my name?"}]})
        response = await bedrock.converse("global.anthropic.claude-opus-5-5", messages=messages)
```

## Stream a model's response as it is written

```python
from capo_bedrock_runtime import AsyncBedrockRuntimeClient


async def main():
    async with AsyncBedrockRuntimeClient(region="us-east-1") as bedrock:
        async with bedrock.converse_stream(
            "global.anthropic.claude-opus-5-5",
            messages=[{"role": "user", "content": [{"text": "Write a haiku about rivers."}]}],
        ) as response:
            # Events arrive as the model writes: text deltas, then usage at the end
            async for event in response["stream"]:
                match event:
                    case {"contentBlockDelta": {"delta": {"text": str() as text}}}:
                        print(text, end="", flush=True)
                    case {"metadata": {"usage": {"total_tokens": int() as total}}}:
                        print(f"\n{total} tokens")
```

## Let the model call your tools

```python
from capo_bedrock_runtime import AsyncBedrockRuntimeClient, UnknownUnionMember
from capo_bedrock_runtime.types.content_block import ContentBlock
from capo_bedrock_runtime.types.message import Message
from capo_bedrock_runtime.types.tool import Tool


async def main():
    async with AsyncBedrockRuntimeClient(region="us-east-1") as bedrock:
        # A tool is a name, a description and a JSON schema for its input
        weather: Tool = {
            "toolSpec": {
                "name": "get_weather",
                "description": "The current weather in a city",
                "input_schema": {
                    "json": {
                        "type": "object",
                        "properties": {"city": {"type": "string"}},
                        "required": ["city"],
                    }
                },
            }
        }
        messages: list[Message] = [
            {"role": "user", "content": [{"text": "Do I need an umbrella in Paris?"}]},
        ]
        response = await bedrock.converse(
            "global.anthropic.claude-opus-5-5", messages=messages, tool_config={"tools": [weather]}
        )

        # The model stops to ask for tool results until it can answer
        while response["stop_reason"] == "tool_use":
            output = response["output"]
            if isinstance(output, UnknownUnionMember):
                raise RuntimeError(output.name)
            messages.append(output["message"])
            results: list[ContentBlock] = []
            for block in output["message"]["content"]:
                match block:
                    case {"toolUse": {"tool_use_id": str() as tool_use_id, "input": tool_input}}:
                        # Run the tool with tool_input here; this one always forecasts rain
                        result = {"forecast": "rain"}
                        results.append(
                            {"toolResult": {"tool_use_id": tool_use_id, "content": [{"json": result}]}}
                        )
            messages.append({"role": "user", "content": results})
            response = await bedrock.converse(
                "global.anthropic.claude-opus-5-5", messages=messages, tool_config={"tools": [weather]}
            )
```

## Send an image to a Bedrock model

```python
from capo_bedrock_runtime import AsyncBedrockRuntimeClient


async def main():
    async with AsyncBedrockRuntimeClient(region="us-east-1") as bedrock:
        with open("photo.png", "rb") as f:
            photo = f.read()

        # Images go in as raw bytes next to the text; the SDK encodes them
        response = await bedrock.converse(
            "global.anthropic.claude-opus-5-5",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"image": {"format": "png", "source": {"bytes": photo}}},
                        {"text": "What is in this picture?"},
                    ],
                }
            ],
        )
```

## Call a model with its native request body using InvokeModel

```python
from capo_bedrock_runtime import AsyncBedrockRuntimeClient
import json


async def main():
    async with AsyncBedrockRuntimeClient(region="us-east-1") as bedrock:
        # InvokeModel sends the model's own JSON, here Anthropic's Messages format
        body = json.dumps(
            {
                "anthropic_version": "bedrock-2023-05-31",
                "max_tokens": 1024,
                "messages": [{"role": "user", "content": "What is the capital of France?"}],
            }
        ).encode()
        response = await bedrock.invoke_model("global.anthropic.claude-opus-5-5", body=body)
        print(json.loads(response["body"])["content"][0]["text"])

        # The same request, streamed: each chunk is one of the model's own events
        async with bedrock.invoke_model_with_response_stream("global.anthropic.claude-opus-5-5", body=body) as response:
            async for event in response["body"]:
                match event:
                    case {"chunk": {"bytes": bytes() as data}}:
                        chunk = json.loads(data)
                        if chunk["type"] == "content_block_delta":
                            print(chunk["delta"].get("text", ""), end="", flush=True)
```

## Real-time voice conversations with Nova Sonic (bidirectional streaming)

`invoke_model_with_bidirectional_stream` keeps one HTTP/2 request open in both directions: you keep sending events while the model answers, and what you send next can depend on what came back. It is async only. This program speaks the question in `question.wav` to Nova Sonic, prints both transcripts and saves the spoken answer to `answer.wav`; a microphone and speakers plug in the same way. It reads and writes the files with anyio (`pip install "capo-bedrock-runtime[anyio]"`), so it runs on asyncio and trio alike.

```python
import base64
import io
import json
import uuid
import wave

import anyio
from capo_bedrock_runtime import AsyncBedrockRuntimeClient

PROMPT = str(uuid.uuid4())
# Nova Sonic hears 16 kHz and speaks 24 kHz: 16-bit mono PCM both ways
AUDIO = {"mediaType": "audio/lpcm", "sampleSizeBits": 16, "channelCount": 1, "encoding": "base64"}


def event(name: str, **fields: object):
    """A Nova Sonic event: JSON, carried as the bytes of a chunk."""
    return {"chunk": {"bytes": json.dumps({"event": {name: fields}}).encode()}}


async def conversation(speech: bytes, replied: anyio.Event):
    yield event("sessionStart", inferenceConfiguration={"maxTokens": 1024})
    yield event(
        "promptStart",
        promptName=PROMPT,
        textOutputConfiguration={"mediaType": "text/plain"},
        audioOutputConfiguration={**AUDIO, "sampleRateHertz": 24000, "voiceId": "matthew"},
    )
    # The system prompt is a text content block
    system = str(uuid.uuid4())
    yield event(
        "contentStart",
        promptName=PROMPT,
        contentName=system,
        type="TEXT",
        interactive=False,
        role="SYSTEM",
        textInputConfiguration={"mediaType": "text/plain"},
    )
    yield event(
        "textInput",
        promptName=PROMPT,
        contentName=system,
        content="You are a friendly assistant. Keep answers short.",
    )
    yield event("contentEnd", promptName=PROMPT, contentName=system)

    # Then the user speaks: audio in 100 ms chunks, as a microphone would send
    # it, and a second of silence so the model hears the turn end
    mic = str(uuid.uuid4())
    yield event(
        "contentStart",
        promptName=PROMPT,
        contentName=mic,
        type="AUDIO",
        interactive=True,
        role="USER",
        audioInputConfiguration={**AUDIO, "sampleRateHertz": 16000, "audioType": "SPEECH"},
    )
    for i in range(0, len(speech), 3200):
        chunk = base64.b64encode(speech[i : i + 3200]).decode()
        yield event("audioInput", promptName=PROMPT, contentName=mic, content=chunk)
    silence = base64.b64encode(bytes(3200)).decode()
    for _ in range(10):
        yield event("audioInput", promptName=PROMPT, contentName=mic, content=silence)

    # The request stays open while the model answers: end the session only
    # once the reply has been spoken
    await replied.wait()
    yield event("contentEnd", promptName=PROMPT, contentName=mic)
    yield event("promptEnd", promptName=PROMPT)
    yield event("sessionEnd")


async def main():
    # The files go through anyio, so the event loop never waits on the disk;
    # wave only parses and builds the WAV bytes in memory
    question = await anyio.Path("question.wav").read_bytes()
    with wave.open(io.BytesIO(question)) as f:  # 16 kHz, 16-bit, mono
        speech = f.readframes(f.getnframes())

    replied = anyio.Event()
    reply = bytearray()
    role = stage = None
    async with AsyncBedrockRuntimeClient(region="us-east-1") as bedrock:
        async with bedrock.invoke_model_with_bidirectional_stream(
            "amazon.nova-2-sonic-v1:0", conversation(speech, replied)
        ) as response:
            async for output in response["body"]:
                match output:
                    case {"chunk": {"bytes": bytes() as payload}}:
                        pass
                    case _:
                        continue
                match json.loads(payload)["event"]:
                    case {"contentStart": start}:
                        role = start["role"]
                        stage = json.loads(start.get("additionalModelFields", "{}")).get("generationStage")
                    case {"textOutput": {"content": text}} if role == "USER" or stage == "SPECULATIVE":
                        # What was heard, then the reply as it is spoken; after an
                        # interruption the reply comes again as FINAL text, cut where it stopped
                        print(f"{role}: {text}")
                    case {"audioOutput": {"content": audio}}:
                        reply += base64.b64decode(audio)
                    case {"contentEnd": {"type": "AUDIO", "stopReason": "END_TURN"}}:
                        replied.set()

    answer = io.BytesIO()
    with wave.open(answer, "wb") as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(24000)
        f.writeframes(reply)
    await anyio.Path("answer.wav").write_bytes(answer.getvalue())


anyio.run(main)
```

## Handle Bedrock errors

```python
from capo_bedrock_runtime import AsyncBedrockRuntimeClient
from capo_bedrock_runtime.errors import ServiceError, ThrottlingException, ValidationException


async def main():
    async with AsyncBedrockRuntimeClient(region="us-east-1") as bedrock:
        # An error the API describes has its own class
        try:
            await bedrock.converse("global.anthropic.claude-opus-5-5", messages=[{"role": "user", "content": []}])
        except ValidationException as e:
            print(e.code, e.message)
        except ThrottlingException:
            print("too many requests; the client already retried")

        # Any error Bedrock returns; one without a class of its own is an UnknownServiceError
        except ServiceError as e:
            print(e.code, e.message)
```

## Configure Bedrock retries

```python
from capo_bedrock_runtime import AsyncBedrockRuntimeClient


async def main():
    async with AsyncBedrockRuntimeClient(region="us-east-1", retry_max_attempts=5) as bedrock:
        # Throttling, server errors and network failures are retried. Every call
        # of this client gets five attempts instead of the default three
        await bedrock.converse("global.anthropic.claude-opus-5-5", messages=[{"role": "user", "content": [{"text": "Hi"}]}])
```

```python
from capo_bedrock_runtime import AsyncBedrockRuntimeClient


async def main():
    async with AsyncBedrockRuntimeClient(region="us-east-1") as bedrock:
        # No retries for this call
        await bedrock.converse(
            "global.anthropic.claude-opus-5-5",
            messages=[{"role": "user", "content": [{"text": "Hi"}]}],
            config_overrides={"retry_max_attempts": 1},
        )
```
