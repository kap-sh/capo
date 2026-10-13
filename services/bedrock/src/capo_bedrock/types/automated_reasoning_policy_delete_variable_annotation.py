"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyDeleteVariableAnnotation``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_definition_variable_name


class AutomatedReasoningPolicyDeleteVariableAnnotation(TypedDict, closed=True):
    name: "capo_bedrock.types.automated_reasoning_policy_definition_variable_name.AutomatedReasoningPolicyDefinitionVariableName"
    """<p>The name of the variable to delete from the policy. The variable must not be referenced by any rules.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyDeleteVariableAnnotation) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyDeleteVariableAnnotation:
    out: AutomatedReasoningPolicyDeleteVariableAnnotation = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyDeleteVariableAnnotation.name required"
        )
    return out


def redact_sensitive(
    value: AutomatedReasoningPolicyDeleteVariableAnnotation,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out
