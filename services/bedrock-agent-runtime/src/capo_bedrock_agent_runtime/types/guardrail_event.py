"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GuardrailEvent``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent_runtime._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.guadrail_action


class GuardrailEvent(TypedDict, closed=True):
    action: NotRequired[
        "capo_bedrock_agent_runtime.types.guadrail_action.GuadrailAction"
    ]
    """<p>The guardrail action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailEvent) -> dict:
    out: dict = {}
    if "action" in value:
        import capo_bedrock_agent_runtime.types.guadrail_action

        out["action"] = capo_bedrock_agent_runtime.types.guadrail_action.serialize_json(
            value["action"]
        )
    return out


def deserialize_json(data: dict) -> GuardrailEvent:
    out: GuardrailEvent = {}  # type: ignore[typeddict-item]
    if data.get("action") is not None:
        import capo_bedrock_agent_runtime.types.guadrail_action

        out["action"] = (
            capo_bedrock_agent_runtime.types.guadrail_action.deserialize_json(
                data["action"]
            )
        )
    return out


def serialize_event_json(value: GuardrailEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "guardrail",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> GuardrailEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: GuardrailEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
