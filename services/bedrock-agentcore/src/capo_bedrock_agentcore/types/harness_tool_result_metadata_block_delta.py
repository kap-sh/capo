"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessToolResultMetadataBlockDelta``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.sensitive_text


class HarnessToolResultMetadataBlockDelta(TypedDict, closed=True):
    metadata: "capo_bedrock_agentcore.types.sensitive_text.SensitiveText"
    """<p>The partial JSON-string fragment of the tool result metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessToolResultMetadataBlockDelta) -> dict:
    out: dict = {}
    out["metadata"] = value["metadata"]
    return out


def deserialize_json(data: dict) -> HarnessToolResultMetadataBlockDelta:
    out: HarnessToolResultMetadataBlockDelta = {}  # type: ignore[typeddict-item]
    if data.get("metadata") is not None:
        out["metadata"] = data["metadata"]
    else:
        raise DeserializationError(
            "HarnessToolResultMetadataBlockDelta.metadata required"
        )
    return out


def redact_sensitive(value: HarnessToolResultMetadataBlockDelta) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "metadata" in value:
        out["metadata"] = "*** Sensitive Data Redacted ***"
    return out
