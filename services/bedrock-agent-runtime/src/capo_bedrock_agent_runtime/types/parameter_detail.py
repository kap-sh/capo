"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ParameterDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.parameter_description
    import capo_bedrock_agent_runtime.types.parameter_type


class ParameterDetail(TypedDict, closed=True):
    description: NotRequired[
        "capo_bedrock_agent_runtime.types.parameter_description.ParameterDescription"
    ]
    """<p> A description of the parameter. Helps the foundation model determine how to elicit the parameters from the user. </p>"""
    type: "capo_bedrock_agent_runtime.types.parameter_type.ParameterType"
    """<p> The data type of the parameter. </p>"""
    required: NotRequired["bool"]
    """<p> Whether the parameter is required for the agent to complete the function for action group invocation. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParameterDetail) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    import capo_bedrock_agent_runtime.types.parameter_type

    out["type"] = capo_bedrock_agent_runtime.types.parameter_type.serialize_json(
        value["type"]
    )
    if "required" in value:
        out["required"] = value["required"]
    return out


def deserialize_json(data: dict) -> ParameterDetail:
    out: ParameterDetail = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("type") is not None:
        import capo_bedrock_agent_runtime.types.parameter_type

        out["type"] = capo_bedrock_agent_runtime.types.parameter_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_bedrock_agent_runtime.types.parameter_type.ParameterType", ""
        )
    if data.get("required") is not None:
        out["required"] = data["required"]
    return out
