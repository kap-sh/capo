"""Generated from Smithy shape ``com.amazonaws.bedrockagent#CustomTransformationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.intermediate_storage
    import capo_bedrock_agent.types.transformations


class CustomTransformationConfiguration(TypedDict, closed=True):
    intermediate_storage: (
        "capo_bedrock_agent.types.intermediate_storage.IntermediateStorage"
    )
    """<p>An S3 bucket path for input and output objects.</p>"""
    transformations: "capo_bedrock_agent.types.transformations.Transformations"
    """<p>A Lambda function that processes documents.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomTransformationConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.intermediate_storage

    out["intermediateStorage"] = (
        capo_bedrock_agent.types.intermediate_storage.serialize_json(
            value["intermediate_storage"]
        )
    )
    import capo_bedrock_agent.types.transformations

    out["transformations"] = capo_bedrock_agent.types.transformations.serialize_json(
        value["transformations"]
    )
    return out


def deserialize_json(data: dict) -> CustomTransformationConfiguration:
    out: CustomTransformationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("intermediateStorage") is not None:
        import capo_bedrock_agent.types.intermediate_storage

        out["intermediate_storage"] = (
            capo_bedrock_agent.types.intermediate_storage.deserialize_json(
                data["intermediateStorage"]
            )
        )
    else:
        raise DeserializationError(
            "CustomTransformationConfiguration.intermediate_storage required"
        )
    if data.get("transformations") is not None:
        import capo_bedrock_agent.types.transformations

        out["transformations"] = (
            capo_bedrock_agent.types.transformations.deserialize_json(
                data["transformations"]
            )
        )
    else:
        out["transformations"] = []
    return out
