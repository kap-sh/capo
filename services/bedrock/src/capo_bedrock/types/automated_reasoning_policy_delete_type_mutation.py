"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyDeleteTypeMutation``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_definition_type_name


class AutomatedReasoningPolicyDeleteTypeMutation(TypedDict, closed=True):
    name: "capo_bedrock.types.automated_reasoning_policy_definition_type_name.AutomatedReasoningPolicyDefinitionTypeName"
    """<p>The name of the custom type to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyDeleteTypeMutation) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyDeleteTypeMutation:
    out: AutomatedReasoningPolicyDeleteTypeMutation = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyDeleteTypeMutation.name required"
        )
    return out


def redact_sensitive(
    value: AutomatedReasoningPolicyDeleteTypeMutation,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out
