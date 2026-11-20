"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#UnifiedConversational``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearchmemory.types.unified_conversational_source


class UnifiedConversational(TypedDict, closed=True):
    source: "capo_opensearchmemory.types.unified_conversational_source.UnifiedConversationalSource"
    """<p>The conversation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UnifiedConversational) -> dict:
    out: dict = {}
    import capo_opensearchmemory.types.unified_conversational_source

    out["source"] = (
        capo_opensearchmemory.types.unified_conversational_source.serialize_aws_json_1_0(
            value["source"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UnifiedConversational:
    out: UnifiedConversational = {}  # type: ignore[typeddict-item]
    if data.get("source") is not None:
        import capo_opensearchmemory.types.unified_conversational_source

        out["source"] = (
            capo_opensearchmemory.types.unified_conversational_source.deserialize_aws_json_1_0(
                data["source"]
            )
        )
    else:
        out["source"] = {"$unknown": {"name": ""}}
    return out


def redact_sensitive(value: UnifiedConversational) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "source" in value:
        import capo_opensearchmemory.types.unified_conversational_source

        out["source"] = (
            capo_opensearchmemory.types.unified_conversational_source.redact_sensitive(
                value["source"]
            )
        )
    return out
