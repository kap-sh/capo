"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#OptimizedPromptEvent``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent_runtime._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.optimized_prompt


class OptimizedPromptEvent(TypedDict, closed=True):
    optimized_prompt: NotRequired[
        "capo_bedrock_agent_runtime.types.optimized_prompt.OptimizedPrompt"
    ]
    """<p>Contains information about the optimized prompt.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OptimizedPromptEvent) -> dict:
    out: dict = {}
    if "optimized_prompt" in value:
        import capo_bedrock_agent_runtime.types.optimized_prompt

        out["optimizedPrompt"] = (
            capo_bedrock_agent_runtime.types.optimized_prompt.serialize_json(
                value["optimized_prompt"]
            )
        )
    return out


def deserialize_json(data: dict) -> OptimizedPromptEvent:
    out: OptimizedPromptEvent = {}  # type: ignore[typeddict-item]
    if data.get("optimizedPrompt") is not None:
        import capo_bedrock_agent_runtime.types.optimized_prompt

        out["optimized_prompt"] = (
            capo_bedrock_agent_runtime.types.optimized_prompt.deserialize_json(
                data["optimizedPrompt"]
            )
        )
    return out


def serialize_event_json(value: OptimizedPromptEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "optimizedPromptEvent",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> OptimizedPromptEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: OptimizedPromptEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
