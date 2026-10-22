"""Generated from Smithy shape ``com.amazonaws.healthlake#ErrorEvent``."""

import json
from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_healthlake._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import capo_healthlake.types.agent_error_type
    import capo_healthlake.types.agent_message_string


class ErrorEvent(TypedDict, closed=True):
    error: "capo_healthlake.types.agent_error_type.AgentErrorType"
    """<p>The type of the exception.</p>"""
    message: "capo_healthlake.types.agent_message_string.AgentMessageString"
    """<p>The exception message.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ErrorEvent) -> dict:
    out: dict = {}
    import capo_healthlake.types.agent_error_type

    out["Error"] = capo_healthlake.types.agent_error_type.serialize_aws_json_1_0(
        value["error"]
    )
    out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ErrorEvent:
    out: ErrorEvent = {}  # type: ignore[typeddict-item]
    if data.get("Error") is not None:
        import capo_healthlake.types.agent_error_type

        out["error"] = capo_healthlake.types.agent_error_type.deserialize_aws_json_1_0(
            data["Error"]
        )
    else:
        import typing

        out["error"] = typing.cast(
            "capo_healthlake.types.agent_error_type.AgentErrorType", ""
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    return out


def serialize_event_aws_json_1_0(value: ErrorEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "ErrorEvent",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_aws_json_1_0(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_aws_json_1_0(message: Message) -> ErrorEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: ErrorEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_aws_json_1_0(json.loads(payload))
    return out


def redact_sensitive(value: ErrorEvent) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "message" in value:
        out["message"] = "*** Sensitive Data Redacted ***"
    return out
