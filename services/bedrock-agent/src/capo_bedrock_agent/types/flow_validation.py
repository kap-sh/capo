"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowValidation``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_validation_details
    import capo_bedrock_agent.types.flow_validation_severity
    import capo_bedrock_agent.types.flow_validation_type
    import capo_bedrock_agent.types.non_blank_string


class FlowValidation(TypedDict, closed=True):
    message: "capo_bedrock_agent.types.non_blank_string.NonBlankString"
    """<p>A message describing the validation error.</p>"""
    severity: "capo_bedrock_agent.types.flow_validation_severity.FlowValidationSeverity"
    """<p>The severity of the issue described in the message.</p>"""
    details: NotRequired[
        "capo_bedrock_agent.types.flow_validation_details.FlowValidationDetails"
    ]
    """<p>Specific details about the validation issue encountered in the flow.</p>"""
    type: NotRequired[
        "capo_bedrock_agent.types.flow_validation_type.FlowValidationType"
    ]
    """<p>The type of validation issue encountered in the flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowValidation) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    import capo_bedrock_agent.types.flow_validation_severity

    out["severity"] = capo_bedrock_agent.types.flow_validation_severity.serialize_json(
        value["severity"]
    )
    if "details" in value:
        import capo_bedrock_agent.types.flow_validation_details

        out["details"] = (
            capo_bedrock_agent.types.flow_validation_details.serialize_json(
                value["details"]
            )
        )
    if "type" in value:
        import capo_bedrock_agent.types.flow_validation_type

        out["type"] = capo_bedrock_agent.types.flow_validation_type.serialize_json(
            value["type"]
        )
    return out


def deserialize_json(data: dict) -> FlowValidation:
    out: FlowValidation = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("FlowValidation.message required")
    if data.get("severity") is not None:
        import capo_bedrock_agent.types.flow_validation_severity

        out["severity"] = (
            capo_bedrock_agent.types.flow_validation_severity.deserialize_json(
                data["severity"]
            )
        )
    else:
        raise DeserializationError("FlowValidation.severity required")
    if data.get("details") is not None:
        import capo_bedrock_agent.types.flow_validation_details

        out["details"] = (
            capo_bedrock_agent.types.flow_validation_details.deserialize_json(
                data["details"]
            )
        )
    if data.get("type") is not None:
        import capo_bedrock_agent.types.flow_validation_type

        out["type"] = capo_bedrock_agent.types.flow_validation_type.deserialize_json(
            data["type"]
        )
    return out


def redact_sensitive(value: FlowValidation) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "details" in value:
        import capo_bedrock_agent.types.flow_validation_details

        out["details"] = (
            capo_bedrock_agent.types.flow_validation_details.redact_sensitive(
                value["details"]
            )
        )
    return out
