"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyAddTypeMutation``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_definition_type


class AutomatedReasoningPolicyAddTypeMutation(TypedDict, closed=True):
    type: "capo_bedrock.types.automated_reasoning_policy_definition_type.AutomatedReasoningPolicyDefinitionType"
    """<p>The type definition that specifies the name, description, and possible values for the new custom type being added to the policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyAddTypeMutation) -> dict:
    out: dict = {}
    import capo_bedrock.types.automated_reasoning_policy_definition_type

    out["type"] = (
        capo_bedrock.types.automated_reasoning_policy_definition_type.serialize_json(
            value["type"]
        )
    )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyAddTypeMutation:
    out: AutomatedReasoningPolicyAddTypeMutation = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_bedrock.types.automated_reasoning_policy_definition_type

        out["type"] = (
            capo_bedrock.types.automated_reasoning_policy_definition_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyAddTypeMutation.type required"
        )
    return out


def redact_sensitive(value: AutomatedReasoningPolicyAddTypeMutation) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "type" in value:
        import capo_bedrock.types.automated_reasoning_policy_definition_type

        out["type"] = (
            capo_bedrock.types.automated_reasoning_policy_definition_type.redact_sensitive(
                value["type"]
            )
        )
    return out
