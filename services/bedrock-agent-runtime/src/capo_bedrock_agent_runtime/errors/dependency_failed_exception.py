"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#DependencyFailedException``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent_runtime._protocol.eventstream import HeaderValue, Message
from capo_bedrock_agent_runtime.errors import ServiceError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.non_blank_string


class DependencyFailedException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_bedrock_agent_runtime.types.non_blank_string.NonBlankString"
    ]
    resource_name: NotRequired[
        "capo_bedrock_agent_runtime.types.non_blank_string.NonBlankString"
    ]
    """<p>The name of the dependency that caused the issue, such as Amazon Bedrock, Lambda, or STS.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DependencyFailedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "resource_name" in value:
        out["resourceName"] = value["resource_name"]
    return out


def deserialize_json(data: dict) -> DependencyFailedException_:
    out: DependencyFailedException_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("resourceName") is not None:
        out["resource_name"] = data["resourceName"]
    return out


class DependencyFailedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.bedrockagentruntime#DependencyFailedException``."""

    code: str | None = "DependencyFailedException"

    def __init__(self, data: DependencyFailedException_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DependencyFailedException",
            message=message,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None
    ) -> "DependencyFailedException":
        return cls(deserialize_json(data), message)


def serialize_event_json(value: DependencyFailedException_) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "dependencyFailedException",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> DependencyFailedException_:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: DependencyFailedException_ = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
