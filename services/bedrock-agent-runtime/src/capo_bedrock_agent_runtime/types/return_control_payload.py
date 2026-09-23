"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ReturnControlPayload``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent_runtime._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.invocation_inputs


class ReturnControlPayload(TypedDict, closed=True):
    invocation_inputs: NotRequired[
        "capo_bedrock_agent_runtime.types.invocation_inputs.InvocationInputs"
    ]
    """<p>A list of objects that contain information about the parameters and inputs that need to be sent into the API operation or function, based on what the agent determines from its session with the user.</p>"""
    invocation_id: NotRequired["str"]
    """<p>The identifier of the action group invocation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReturnControlPayload) -> dict:
    out: dict = {}
    if "invocation_inputs" in value:
        import capo_bedrock_agent_runtime.types.invocation_inputs

        out["invocationInputs"] = (
            capo_bedrock_agent_runtime.types.invocation_inputs.serialize_json(
                value["invocation_inputs"]
            )
        )
    if "invocation_id" in value:
        out["invocationId"] = value["invocation_id"]
    return out


def deserialize_json(data: dict) -> ReturnControlPayload:
    out: ReturnControlPayload = {}  # type: ignore[typeddict-item]
    if data.get("invocationInputs") is not None:
        import capo_bedrock_agent_runtime.types.invocation_inputs

        out["invocation_inputs"] = (
            capo_bedrock_agent_runtime.types.invocation_inputs.deserialize_json(
                data["invocationInputs"]
            )
        )
    if data.get("invocationId") is not None:
        out["invocation_id"] = data["invocationId"]
    return out


def serialize_event_json(value: ReturnControlPayload) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "returnControl",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> ReturnControlPayload:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: ReturnControlPayload = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
