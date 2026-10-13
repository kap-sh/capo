"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyUpdateTypeMutation``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_definition_type


class AutomatedReasoningPolicyUpdateTypeMutation(TypedDict, closed=True):
    type: "capo_bedrock.types.automated_reasoning_policy_definition_type.AutomatedReasoningPolicyDefinitionType"
    """<p>The updated type definition containing the modified name, description, or values for the existing custom type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyUpdateTypeMutation) -> dict:
    out: dict = {}
    import capo_bedrock.types.automated_reasoning_policy_definition_type

    out["type"] = (
        capo_bedrock.types.automated_reasoning_policy_definition_type.serialize_json(
            value["type"]
        )
    )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyUpdateTypeMutation:
    out: AutomatedReasoningPolicyUpdateTypeMutation = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_bedrock.types.automated_reasoning_policy_definition_type

        out["type"] = (
            capo_bedrock.types.automated_reasoning_policy_definition_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyUpdateTypeMutation.type required"
        )
    return out


def redact_sensitive(
    value: AutomatedReasoningPolicyUpdateTypeMutation,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "type" in value:
        import capo_bedrock.types.automated_reasoning_policy_definition_type

        out["type"] = (
            capo_bedrock.types.automated_reasoning_policy_definition_type.redact_sensitive(
                value["type"]
            )
        )
    return out
