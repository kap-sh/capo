"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ValidateFlowDefinitionResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_validations


class ValidateFlowDefinitionResponse(TypedDict, closed=True):
    validations: "capo_bedrock_agent.types.flow_validations.FlowValidations"
    """<p>Contains an array of objects, each of which contains an error identified by validation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidateFlowDefinitionResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.flow_validations

    out["validations"] = capo_bedrock_agent.types.flow_validations.serialize_json(
        value["validations"]
    )
    return out


def deserialize_json(data: dict) -> ValidateFlowDefinitionResponse:
    out: ValidateFlowDefinitionResponse = {}  # type: ignore[typeddict-item]
    if data.get("validations") is not None:
        import capo_bedrock_agent.types.flow_validations

        out["validations"] = capo_bedrock_agent.types.flow_validations.deserialize_json(
            data["validations"]
        )
    else:
        out["validations"] = []
    return out


def redact_sensitive(value: ValidateFlowDefinitionResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "validations" in value:
        import capo_bedrock_agent.types.flow_validations

        out["validations"] = capo_bedrock_agent.types.flow_validations.redact_sensitive(
            value["validations"]
        )
    return out
