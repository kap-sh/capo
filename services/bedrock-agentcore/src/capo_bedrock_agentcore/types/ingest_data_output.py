"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#IngestDataOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.session_id


class IngestDataOutput(TypedDict, closed=True):
    session_id: "capo_bedrock_agentcore.types.session_id.SessionId"
    """<p>The identifier of the session that the service ingested the content into. This value echoes the session identifier from the request, or the identifier that the service generated when you did not provide one.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IngestDataOutput) -> dict:
    out: dict = {}
    out["sessionId"] = value["session_id"]
    return out


def deserialize_json(data: dict) -> IngestDataOutput:
    out: IngestDataOutput = {}  # type: ignore[typeddict-item]
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        out["session_id"] = ""
    return out
