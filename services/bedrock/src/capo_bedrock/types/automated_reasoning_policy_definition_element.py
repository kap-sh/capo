"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyDefinitionElement``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError, SerializationError
from capo_bedrock.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_definition_rule
    import capo_bedrock.types.automated_reasoning_policy_definition_type
    import capo_bedrock.types.automated_reasoning_policy_definition_variable


class _AutomatedReasoningPolicyDefinitionElement_policyDefinitionVariable(
    TypedDict, closed=True
):
    policyDefinitionVariable: "capo_bedrock.types.automated_reasoning_policy_definition_variable.AutomatedReasoningPolicyDefinitionVariable"


class _AutomatedReasoningPolicyDefinitionElement_policyDefinitionType(
    TypedDict, closed=True
):
    policyDefinitionType: "capo_bedrock.types.automated_reasoning_policy_definition_type.AutomatedReasoningPolicyDefinitionType"


class _AutomatedReasoningPolicyDefinitionElement_policyDefinitionRule(
    TypedDict, closed=True
):
    policyDefinitionRule: "capo_bedrock.types.automated_reasoning_policy_definition_rule.AutomatedReasoningPolicyDefinitionRule"


AutomatedReasoningPolicyDefinitionElement: TypeAlias = (
    _AutomatedReasoningPolicyDefinitionElement_policyDefinitionVariable
    | _AutomatedReasoningPolicyDefinitionElement_policyDefinitionType
    | _AutomatedReasoningPolicyDefinitionElement_policyDefinitionRule
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyDefinitionElement) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"AutomatedReasoningPolicyDefinitionElement: cannot serialize unknown variant {value.name!r}"
        )
    elif "policyDefinitionVariable" in value:
        import capo_bedrock.types.automated_reasoning_policy_definition_variable

        return {
            "policyDefinitionVariable": capo_bedrock.types.automated_reasoning_policy_definition_variable.serialize_json(
                value["policyDefinitionVariable"]
            )
        }
    elif "policyDefinitionType" in value:
        import capo_bedrock.types.automated_reasoning_policy_definition_type

        return {
            "policyDefinitionType": capo_bedrock.types.automated_reasoning_policy_definition_type.serialize_json(
                value["policyDefinitionType"]
            )
        }
    elif "policyDefinitionRule" in value:
        import capo_bedrock.types.automated_reasoning_policy_definition_rule

        return {
            "policyDefinitionRule": capo_bedrock.types.automated_reasoning_policy_definition_rule.serialize_json(
                value["policyDefinitionRule"]
            )
        }
    else:
        raise SerializationError(
            "AutomatedReasoningPolicyDefinitionElement: no variant present"
        )


def deserialize_json(data: dict) -> AutomatedReasoningPolicyDefinitionElement:
    if data.get("policyDefinitionVariable") is not None:
        import capo_bedrock.types.automated_reasoning_policy_definition_variable

        return {
            "policyDefinitionVariable": capo_bedrock.types.automated_reasoning_policy_definition_variable.deserialize_json(
                data["policyDefinitionVariable"]
            )
        }
    elif data.get("policyDefinitionType") is not None:
        import capo_bedrock.types.automated_reasoning_policy_definition_type

        return {
            "policyDefinitionType": capo_bedrock.types.automated_reasoning_policy_definition_type.deserialize_json(
                data["policyDefinitionType"]
            )
        }
    elif data.get("policyDefinitionRule") is not None:
        import capo_bedrock.types.automated_reasoning_policy_definition_rule

        return {
            "policyDefinitionRule": capo_bedrock.types.automated_reasoning_policy_definition_rule.deserialize_json(
                data["policyDefinitionRule"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "AutomatedReasoningPolicyDefinitionElement: no recognized variant key"
        )


def redact_sensitive(
    value: AutomatedReasoningPolicyDefinitionElement,
) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "policyDefinitionVariable" in value:
        import capo_bedrock.types.automated_reasoning_policy_definition_variable

        out["policyDefinitionVariable"] = (
            capo_bedrock.types.automated_reasoning_policy_definition_variable.redact_sensitive(
                value["policyDefinitionVariable"]
            )
        )
    if "policyDefinitionType" in value:
        import capo_bedrock.types.automated_reasoning_policy_definition_type

        out["policyDefinitionType"] = (
            capo_bedrock.types.automated_reasoning_policy_definition_type.redact_sensitive(
                value["policyDefinitionType"]
            )
        )
    if "policyDefinitionRule" in value:
        import capo_bedrock.types.automated_reasoning_policy_definition_rule

        out["policyDefinitionRule"] = (
            capo_bedrock.types.automated_reasoning_policy_definition_rule.redact_sensitive(
                value["policyDefinitionRule"]
            )
        )
    return out
