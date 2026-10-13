"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FinalResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.final_response_string
    import capo_bedrock_agent_runtime.types.metadata


class FinalResponse(TypedDict, closed=True):
    text: NotRequired[
        "capo_bedrock_agent_runtime.types.final_response_string.FinalResponseString"
    ]
    """<p>The text in the response to the user.</p>"""
    metadata: NotRequired["capo_bedrock_agent_runtime.types.metadata.Metadata"]
    """<p>Contains information about the invoke agent operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FinalResponse) -> dict:
    out: dict = {}
    if "text" in value:
        out["text"] = value["text"]
    if "metadata" in value:
        import capo_bedrock_agent_runtime.types.metadata

        out["metadata"] = capo_bedrock_agent_runtime.types.metadata.serialize_json(
            value["metadata"]
        )
    return out


def deserialize_json(data: dict) -> FinalResponse:
    out: FinalResponse = {}  # type: ignore[typeddict-item]
    if data.get("text") is not None:
        out["text"] = data["text"]
    if data.get("metadata") is not None:
        import capo_bedrock_agent_runtime.types.metadata

        out["metadata"] = capo_bedrock_agent_runtime.types.metadata.deserialize_json(
            data["metadata"]
        )
    return out


def redact_sensitive(value: FinalResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "text" in value:
        out["text"] = "*** Sensitive Data Redacted ***"
    if "metadata" in value:
        out["metadata"] = "*** Sensitive Data Redacted ***"
    return out
