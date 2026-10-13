"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#Citation``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.generated_response_part
    import capo_bedrock_agent_runtime.types.retrieved_references


class Citation(TypedDict, closed=True):
    generated_response_part: NotRequired[
        "capo_bedrock_agent_runtime.types.generated_response_part.GeneratedResponsePart"
    ]
    """<p>Contains the generated response and metadata </p>"""
    retrieved_references: NotRequired[
        "capo_bedrock_agent_runtime.types.retrieved_references.RetrievedReferences"
    ]
    """<p>Contains metadata about the sources cited for the generated response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Citation) -> dict:
    out: dict = {}
    if "generated_response_part" in value:
        import capo_bedrock_agent_runtime.types.generated_response_part

        out["generatedResponsePart"] = (
            capo_bedrock_agent_runtime.types.generated_response_part.serialize_json(
                value["generated_response_part"]
            )
        )
    if "retrieved_references" in value:
        import capo_bedrock_agent_runtime.types.retrieved_references

        out["retrievedReferences"] = (
            capo_bedrock_agent_runtime.types.retrieved_references.serialize_json(
                value["retrieved_references"]
            )
        )
    return out


def deserialize_json(data: dict) -> Citation:
    out: Citation = {}  # type: ignore[typeddict-item]
    if data.get("generatedResponsePart") is not None:
        import capo_bedrock_agent_runtime.types.generated_response_part

        out["generated_response_part"] = (
            capo_bedrock_agent_runtime.types.generated_response_part.deserialize_json(
                data["generatedResponsePart"]
            )
        )
    if data.get("retrievedReferences") is not None:
        import capo_bedrock_agent_runtime.types.retrieved_references

        out["retrieved_references"] = (
            capo_bedrock_agent_runtime.types.retrieved_references.deserialize_json(
                data["retrievedReferences"]
            )
        )
    return out


def redact_sensitive(value: Citation) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "generated_response_part" in value:
        import capo_bedrock_agent_runtime.types.generated_response_part

        out["generated_response_part"] = (
            capo_bedrock_agent_runtime.types.generated_response_part.redact_sensitive(
                value["generated_response_part"]
            )
        )
    if "retrieved_references" in value:
        import capo_bedrock_agent_runtime.types.retrieved_references

        out["retrieved_references"] = (
            capo_bedrock_agent_runtime.types.retrieved_references.redact_sensitive(
                value["retrieved_references"]
            )
        )
    return out
