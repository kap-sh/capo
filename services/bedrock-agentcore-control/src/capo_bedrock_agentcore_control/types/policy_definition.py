"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PolicyDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.cedar_policy
    import capo_bedrock_agentcore_control.types.policy_generation_details
    import capo_bedrock_agentcore_control.types.policy_statement


class _PolicyDefinition_cedar(TypedDict, closed=True):
    cedar: "capo_bedrock_agentcore_control.types.cedar_policy.CedarPolicy"


class _PolicyDefinition_policyGeneration(TypedDict, closed=True):
    policyGeneration: "capo_bedrock_agentcore_control.types.policy_generation_details.PolicyGenerationDetails"


class _PolicyDefinition_policy(TypedDict, closed=True):
    policy: "capo_bedrock_agentcore_control.types.policy_statement.PolicyStatement"


PolicyDefinition: TypeAlias = (
    _PolicyDefinition_cedar
    | _PolicyDefinition_policyGeneration
    | _PolicyDefinition_policy
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: PolicyDefinition) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"PolicyDefinition: cannot serialize unknown variant {value.name!r}"
        )
    elif "cedar" in value:
        import capo_bedrock_agentcore_control.types.cedar_policy

        return {
            "cedar": capo_bedrock_agentcore_control.types.cedar_policy.serialize_json(
                value["cedar"]
            )
        }
    elif "policyGeneration" in value:
        import capo_bedrock_agentcore_control.types.policy_generation_details

        return {
            "policyGeneration": capo_bedrock_agentcore_control.types.policy_generation_details.serialize_json(
                value["policyGeneration"]
            )
        }
    elif "policy" in value:
        import capo_bedrock_agentcore_control.types.policy_statement

        return {
            "policy": capo_bedrock_agentcore_control.types.policy_statement.serialize_json(
                value["policy"]
            )
        }
    else:
        raise SerializationError("PolicyDefinition: no variant present")


def deserialize_json(data: dict) -> PolicyDefinition:
    if data.get("cedar") is not None:
        import capo_bedrock_agentcore_control.types.cedar_policy

        return {
            "cedar": capo_bedrock_agentcore_control.types.cedar_policy.deserialize_json(
                data["cedar"]
            )
        }
    elif data.get("policyGeneration") is not None:
        import capo_bedrock_agentcore_control.types.policy_generation_details

        return {
            "policyGeneration": capo_bedrock_agentcore_control.types.policy_generation_details.deserialize_json(
                data["policyGeneration"]
            )
        }
    elif data.get("policy") is not None:
        import capo_bedrock_agentcore_control.types.policy_statement

        return {
            "policy": capo_bedrock_agentcore_control.types.policy_statement.deserialize_json(
                data["policy"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("PolicyDefinition: no recognized variant key")
