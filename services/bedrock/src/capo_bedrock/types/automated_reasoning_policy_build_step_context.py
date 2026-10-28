"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyBuildStepContext``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError, SerializationError
from capo_bedrock.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_mutation
    import capo_bedrock.types.automated_reasoning_policy_planning


class AutomatedReasoningPolicyBuildStepContextPlanningMember(TypedDict, closed=True):
    planning: "capo_bedrock.types.automated_reasoning_policy_planning.AutomatedReasoningPolicyPlanning"


class AutomatedReasoningPolicyBuildStepContextMutationMember(TypedDict, closed=True):
    mutation: "capo_bedrock.types.automated_reasoning_policy_mutation.AutomatedReasoningPolicyMutation"


AutomatedReasoningPolicyBuildStepContext: TypeAlias = (
    AutomatedReasoningPolicyBuildStepContextPlanningMember
    | AutomatedReasoningPolicyBuildStepContextMutationMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyBuildStepContext) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AutomatedReasoningPolicyBuildStepContext: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "planning" in value:
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
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
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
