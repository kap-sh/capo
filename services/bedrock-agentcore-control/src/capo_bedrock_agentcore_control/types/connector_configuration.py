"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ConnectorConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.connector_parameter_overrides


class ConnectorConfiguration(TypedDict, closed=True):
    name: "str"
    """<p>The tool or operation name (for example, <code>retrieve</code> or <code>webSearch</code>).</p>"""
    description: NotRequired["str"]
    """<p>An agent-facing description override for this tool.</p>"""
    parameter_values: NotRequired["object"]
    """<p>Parameters to set as fixed or default values when provisioning this tool.</p>"""
    parameter_overrides: NotRequired[
        "capo_bedrock_agentcore_control.types.connector_parameter_overrides.ConnectorParameterOverrides"
    ]
    """<p>Parameters to expose to the agent at runtime, with optional description overrides.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorConfiguration) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "parameter_values" in value:
        out["parameterValues"] = value["parameter_values"]
    if "parameter_overrides" in value:
        import capo_bedrock_agentcore_control.types.connector_parameter_overrides

        out["parameterOverrides"] = (
            capo_bedrock_agentcore_control.types.connector_parameter_overrides.serialize_json(
                value["parameter_overrides"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConnectorConfiguration:
    out: ConnectorConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("parameterValues") is not None:
        out["parameter_values"] = data["parameterValues"]
    if data.get("parameterOverrides") is not None:
        import capo_bedrock_agentcore_control.types.connector_parameter_overrides

        out["parameter_overrides"] = (
            capo_bedrock_agentcore_control.types.connector_parameter_overrides.deserialize_json(
                data["parameterOverrides"]
            )
        )
    return out
