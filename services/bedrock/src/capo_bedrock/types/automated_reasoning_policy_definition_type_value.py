"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyDefinitionTypeValue``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_definition_type_value_description
    import capo_bedrock.types.automated_reasoning_policy_definition_type_value_name


class AutomatedReasoningPolicyDefinitionTypeValue(TypedDict, closed=True):
    value: "capo_bedrock.types.automated_reasoning_policy_definition_type_value_name.AutomatedReasoningPolicyDefinitionTypeValueName"
    """<p>The actual value or identifier for this type value.</p>"""
    description: NotRequired[
        "capo_bedrock.types.automated_reasoning_policy_definition_type_value_description.AutomatedReasoningPolicyDefinitionTypeValueDescription"
    ]
    """<p>A human-readable description explaining what this type value represents and when it should be used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyDefinitionTypeValue) -> dict:
    out: dict = {}
    out["value"] = value["value"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyDefinitionTypeValue:
    out: AutomatedReasoningPolicyDefinitionTypeValue = {}  # type: ignore[typeddict-item]
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyDefinitionTypeValue.value required"
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out


def redact_sensitive(
    value: AutomatedReasoningPolicyDefinitionTypeValue,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
