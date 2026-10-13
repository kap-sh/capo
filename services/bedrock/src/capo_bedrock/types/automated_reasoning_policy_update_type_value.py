"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyUpdateTypeValue``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_definition_type_value_description
    import capo_bedrock.types.automated_reasoning_policy_definition_type_value_name


class AutomatedReasoningPolicyUpdateTypeValue(TypedDict, closed=True):
    value: "capo_bedrock.types.automated_reasoning_policy_definition_type_value_name.AutomatedReasoningPolicyDefinitionTypeValueName"
    """<p>The current identifier or name of the type value to update.</p>"""
    new_value: NotRequired[
        "capo_bedrock.types.automated_reasoning_policy_definition_type_value_name.AutomatedReasoningPolicyDefinitionTypeValueName"
    ]
    """<p>The new identifier or name for the type value, if you want to rename it.</p>"""
    description: NotRequired[
        "capo_bedrock.types.automated_reasoning_policy_definition_type_value_description.AutomatedReasoningPolicyDefinitionTypeValueDescription"
    ]
    """<p>The new description for the type value, replacing the previous description.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyUpdateTypeValue) -> dict:
    out: dict = {}
    out["value"] = value["value"]
    if "new_value" in value:
        out["newValue"] = value["new_value"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyUpdateTypeValue:
    out: AutomatedReasoningPolicyUpdateTypeValue = {}  # type: ignore[typeddict-item]
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyUpdateTypeValue.value required"
        )
    if data.get("newValue") is not None:
        out["new_value"] = data["newValue"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out


def redact_sensitive(value: AutomatedReasoningPolicyUpdateTypeValue) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
