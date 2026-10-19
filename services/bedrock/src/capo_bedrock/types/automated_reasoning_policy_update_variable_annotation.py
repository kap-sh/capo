"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyUpdateVariableAnnotation``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_definition_variable_description
    import capo_bedrock.types.automated_reasoning_policy_definition_variable_name


class AutomatedReasoningPolicyUpdateVariableAnnotation(TypedDict, closed=True):
    name: "capo_bedrock.types.automated_reasoning_policy_definition_variable_name.AutomatedReasoningPolicyDefinitionVariableName"
    """<p>The current name of the variable to update.</p>"""
    new_name: NotRequired[
        "capo_bedrock.types.automated_reasoning_policy_definition_variable_name.AutomatedReasoningPolicyDefinitionVariableName"
    ]
    """<p>The new name for the variable, if you want to rename it. If not provided, the name remains unchanged.</p>"""
    description: NotRequired[
        "capo_bedrock.types.automated_reasoning_policy_definition_variable_description.AutomatedReasoningPolicyDefinitionVariableDescription"
    ]
    """<p>The new description for the variable, replacing the previous description.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyUpdateVariableAnnotation) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "new_name" in value:
        out["newName"] = value["new_name"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyUpdateVariableAnnotation:
    out: AutomatedReasoningPolicyUpdateVariableAnnotation = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("newName") is not None:
        out["new_name"] = data["newName"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out


def redact_sensitive(
    value: AutomatedReasoningPolicyUpdateVariableAnnotation,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "new_name" in value:
        out["new_name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
