"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessHookEvent``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.harness_hook_decision
    import capo_bedrock_agentcore.types.harness_hook_event_id
    import capo_bedrock_agentcore.types.harness_hook_event_type
    import capo_bedrock_agentcore.types.harness_hook_name


class HarnessHookEvent(TypedDict, closed=True):
    hook_event_id: (
        "capo_bedrock_agentcore.types.harness_hook_event_id.HarnessHookEventId"
    )
    """<p>The unique identifier for this hook event.</p>"""
    name: "capo_bedrock_agentcore.types.harness_hook_name.HarnessHookName"
    """<p>The name of the hook that ran.</p>"""
    type: "capo_bedrock_agentcore.types.harness_hook_event_type.HarnessHookEventType"
    """<p>The type of lifecycle hook event.</p>"""
    decision: NotRequired[
        "capo_bedrock_agentcore.types.harness_hook_decision.HarnessHookDecision"
    ]
    """<p>The decision applied to the hook event. This field is present only for blocking Lambda targets.</p>"""
    reason: NotRequired["str"]
    """<p>The optional reason for the applied decision.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessHookEvent) -> dict:
    out: dict = {}
    out["hookEventId"] = value["hook_event_id"]
    out["name"] = value["name"]
    import capo_bedrock_agentcore.types.harness_hook_event_type

    out["type"] = capo_bedrock_agentcore.types.harness_hook_event_type.serialize_json(
        value["type"]
    )
    if "decision" in value:
        import capo_bedrock_agentcore.types.harness_hook_decision

        out["decision"] = (
            capo_bedrock_agentcore.types.harness_hook_decision.serialize_json(
                value["decision"]
            )
        )
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> HarnessHookEvent:
    out: HarnessHookEvent = {}  # type: ignore[typeddict-item]
    if data.get("hookEventId") is not None:
        out["hook_event_id"] = data["hookEventId"]
    else:
        out["hook_event_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("type") is not None:
        import capo_bedrock_agentcore.types.harness_hook_event_type

        out["type"] = (
            capo_bedrock_agentcore.types.harness_hook_event_type.deserialize_json(
                data["type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_bedrock_agentcore.types.harness_hook_event_type.HarnessHookEventType",
            "",
        )
    if data.get("decision") is not None:
        import capo_bedrock_agentcore.types.harness_hook_decision

        out["decision"] = (
            capo_bedrock_agentcore.types.harness_hook_decision.deserialize_json(
                data["decision"]
            )
        )
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    return out


def serialize_event_json(value: HarnessHookEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "hookEvent",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> HarnessHookEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: HarnessHookEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
