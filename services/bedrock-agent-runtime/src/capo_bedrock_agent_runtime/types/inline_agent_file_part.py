"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InlineAgentFilePart``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent_runtime._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.output_files


class InlineAgentFilePart(TypedDict, closed=True):
    files: NotRequired["capo_bedrock_agent_runtime.types.output_files.OutputFiles"]
    """<p>Files containing intermediate response for the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InlineAgentFilePart) -> dict:
    out: dict = {}
    if "files" in value:
        import capo_bedrock_agent_runtime.types.output_files

        out["files"] = capo_bedrock_agent_runtime.types.output_files.serialize_json(
            value["files"]
        )
    return out


def deserialize_json(data: dict) -> InlineAgentFilePart:
    out: InlineAgentFilePart = {}  # type: ignore[typeddict-item]
    if data.get("files") is not None:
        import capo_bedrock_agent_runtime.types.output_files

        out["files"] = capo_bedrock_agent_runtime.types.output_files.deserialize_json(
            data["files"]
        )
    return out


def serialize_event_json(value: InlineAgentFilePart) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "files",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> InlineAgentFilePart:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: InlineAgentFilePart = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
