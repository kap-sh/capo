"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FunctionDefinition``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.function_description
    import capo_bedrock_agent_runtime.types.parameter_map
    import capo_bedrock_agent_runtime.types.require_confirmation
    import capo_bedrock_agent_runtime.types.resource_name


class FunctionDefinition(TypedDict, closed=True):
    name: "capo_bedrock_agent_runtime.types.resource_name.ResourceName"
    """<p> A name for the function. </p>"""
    description: NotRequired[
        "capo_bedrock_agent_runtime.types.function_description.FunctionDescription"
    ]
    """<p> A description of the function and its purpose. </p>"""
    parameters: NotRequired[
        "capo_bedrock_agent_runtime.types.parameter_map.ParameterMap"
    ]
    """<p> The parameters that the agent elicits from the user to fulfill the function. </p>"""
    require_confirmation: NotRequired[
        "capo_bedrock_agent_runtime.types.require_confirmation.RequireConfirmation"
    ]
    """<p> Contains information if user confirmation is required to invoke the function. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FunctionDefinition) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "parameters" in value:
        import capo_bedrock_agent_runtime.types.parameter_map

        out["parameters"] = (
            capo_bedrock_agent_runtime.types.parameter_map.serialize_json(
                value["parameters"]
            )
        )
    if "require_confirmation" in value:
        import capo_bedrock_agent_runtime.types.require_confirmation

        out["requireConfirmation"] = (
            capo_bedrock_agent_runtime.types.require_confirmation.serialize_json(
                value["require_confirmation"]
            )
        )
    return out


def deserialize_json(data: dict) -> FunctionDefinition:
    out: FunctionDefinition = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("FunctionDefinition.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("parameters") is not None:
        import capo_bedrock_agent_runtime.types.parameter_map

        out["parameters"] = (
            capo_bedrock_agent_runtime.types.parameter_map.deserialize_json(
                data["parameters"]
            )
        )
    if data.get("requireConfirmation") is not None:
        import capo_bedrock_agent_runtime.types.require_confirmation

        out["require_confirmation"] = (
            capo_bedrock_agent_runtime.types.require_confirmation.deserialize_json(
                data["requireConfirmation"]
            )
        )
    return out


def redact_sensitive(value: FunctionDefinition) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out
