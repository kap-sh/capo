"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GenerateQueryRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.query_generation_input
    import capo_bedrock_agent_runtime.types.transformation_configuration


class GenerateQueryRequest(TypedDict, closed=True):
    query_generation_input: (
        "capo_bedrock_agent_runtime.types.query_generation_input.QueryGenerationInput"
    )
    """<p>Specifies information about a natural language query to transform into SQL.</p>"""
    transformation_configuration: "capo_bedrock_agent_runtime.types.transformation_configuration.TransformationConfiguration"
    """<p>Specifies configurations for transforming the natural language query into SQL.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerateQueryRequest) -> dict:
    out: dict = {}
    import capo_bedrock_agent_runtime.types.query_generation_input

    out["queryGenerationInput"] = (
        capo_bedrock_agent_runtime.types.query_generation_input.serialize_json(
            value["query_generation_input"]
        )
    )
    import capo_bedrock_agent_runtime.types.transformation_configuration

    out["transformationConfiguration"] = (
        capo_bedrock_agent_runtime.types.transformation_configuration.serialize_json(
            value["transformation_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> GenerateQueryRequest:
    out: GenerateQueryRequest = {}  # type: ignore[typeddict-item]
    if data.get("queryGenerationInput") is not None:
        import capo_bedrock_agent_runtime.types.query_generation_input

        out["query_generation_input"] = (
            capo_bedrock_agent_runtime.types.query_generation_input.deserialize_json(
                data["queryGenerationInput"]
            )
        )
    else:
        raise DeserializationError(
            "GenerateQueryRequest.query_generation_input required"
        )
    if data.get("transformationConfiguration") is not None:
        import capo_bedrock_agent_runtime.types.transformation_configuration

        out["transformation_configuration"] = (
            capo_bedrock_agent_runtime.types.transformation_configuration.deserialize_json(
                data["transformationConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "GenerateQueryRequest.transformation_configuration required"
        )
    return out


def redact_sensitive(value: GenerateQueryRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "query_generation_input" in value:
        out["query_generation_input"] = "*** Sensitive Data Redacted ***"
    return out
