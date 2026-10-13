"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#Attribution``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.citations


class Attribution(TypedDict, closed=True):
    citations: NotRequired["capo_bedrock_agent_runtime.types.citations.Citations"]
    """<p>A list of citations and related information for a part of an agent response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Attribution) -> dict:
    out: dict = {}
    if "citations" in value:
        import capo_bedrock_agent_runtime.types.citations

        out["citations"] = capo_bedrock_agent_runtime.types.citations.serialize_json(
            value["citations"]
        )
    return out


def deserialize_json(data: dict) -> Attribution:
    out: Attribution = {}  # type: ignore[typeddict-item]
    if data.get("citations") is not None:
        import capo_bedrock_agent_runtime.types.citations

        out["citations"] = capo_bedrock_agent_runtime.types.citations.deserialize_json(
            data["citations"]
        )
    return out


def redact_sensitive(value: Attribution) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "citations" in value:
        import capo_bedrock_agent_runtime.types.citations

        out["citations"] = capo_bedrock_agent_runtime.types.citations.redact_sensitive(
            value["citations"]
        )
    return out
