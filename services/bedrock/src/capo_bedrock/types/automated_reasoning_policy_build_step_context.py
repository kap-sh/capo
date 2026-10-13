"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyBuildStepContext``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_mutation
    import capo_bedrock.types.automated_reasoning_policy_planning


class _AutomatedReasoningPolicyBuildStepContext_planning(TypedDict, closed=True):
    planning: "capo_bedrock.types.automated_reasoning_policy_planning.AutomatedReasoningPolicyPlanning"


class _AutomatedReasoningPolicyBuildStepContext_mutation(TypedDict, closed=True):
    mutation: "capo_bedrock.types.automated_reasoning_policy_mutation.AutomatedReasoningPolicyMutation"


AutomatedReasoningPolicyBuildStepContext: TypeAlias = (
    _AutomatedReasoningPolicyBuildStepContext_planning
    | _AutomatedReasoningPolicyBuildStepContext_mutation
)


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyBuildStepContext) -> dict:
    if "planning" in value:
        import capo_bedrock.types.automated_reasoning_policy_planning

        return {
            "planning": capo_bedrock.types.automated_reasoning_policy_planning.serialize_json(
                value["planning"]
            )
        }
    elif "mutation" in value:
        import capo_bedrock.types.automated_reasoning_policy_mutation

        return {
            "mutation": capo_bedrock.types.automated_reasoning_policy_mutation.serialize_json(
                value["mutation"]
            )
        }
    else:
        raise SerializationError(
            "AutomatedReasoningPolicyBuildStepContext: no variant present"
        )


def deserialize_json(data: dict) -> AutomatedReasoningPolicyBuildStepContext:
    if data.get("planning") is not None:
        import capo_bedrock.types.automated_reasoning_policy_planning

        return {
            "planning": capo_bedrock.types.automated_reasoning_policy_planning.deserialize_json(
                data["planning"]
            )
        }
    elif data.get("mutation") is not None:
        import capo_bedrock.types.automated_reasoning_policy_mutation

        return {
            "mutation": capo_bedrock.types.automated_reasoning_policy_mutation.deserialize_json(
                data["mutation"]
            )
        }
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyBuildStepContext: no recognized variant key"
        )


def redact_sensitive(value: AutomatedReasoningPolicyBuildStepContext) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "mutation" in value:
        import capo_bedrock.types.automated_reasoning_policy_mutation

        out["mutation"] = (
            capo_bedrock.types.automated_reasoning_policy_mutation.redact_sensitive(
                value["mutation"]
            )
        )
    return out
