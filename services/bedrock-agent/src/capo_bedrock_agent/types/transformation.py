"""Generated from Smithy shape ``com.amazonaws.bedrockagent#Transformation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.step_type
    import capo_bedrock_agent.types.transformation_function


class Transformation(TypedDict, closed=True):
    transformation_function: (
        "capo_bedrock_agent.types.transformation_function.TransformationFunction"
    )
    """<p>A Lambda function that processes documents.</p>"""
    step_to_apply: "capo_bedrock_agent.types.step_type.StepType"
    """<p>When the service applies the transformation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Transformation) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.transformation_function

    out["transformationFunction"] = (
        capo_bedrock_agent.types.transformation_function.serialize_json(
            value["transformation_function"]
        )
    )
    import capo_bedrock_agent.types.step_type

    out["stepToApply"] = capo_bedrock_agent.types.step_type.serialize_json(
        value["step_to_apply"]
    )
    return out


def deserialize_json(data: dict) -> Transformation:
    out: Transformation = {}  # type: ignore[typeddict-item]
    if data.get("transformationFunction") is not None:
        import capo_bedrock_agent.types.transformation_function

        out["transformation_function"] = (
            capo_bedrock_agent.types.transformation_function.deserialize_json(
                data["transformationFunction"]
            )
        )
    else:
        raise DeserializationError("Transformation.transformation_function required")
    if data.get("stepToApply") is not None:
        import capo_bedrock_agent.types.step_type

        out["step_to_apply"] = capo_bedrock_agent.types.step_type.deserialize_json(
            data["stepToApply"]
        )
    else:
        import typing

        out["step_to_apply"] = typing.cast(
            "capo_bedrock_agent.types.step_type.StepType", ""
        )
    return out
