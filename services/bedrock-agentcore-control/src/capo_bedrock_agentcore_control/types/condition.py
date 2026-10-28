"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#Condition``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.match_models
    import capo_bedrock_agentcore_control.types.match_paths
    import capo_bedrock_agentcore_control.types.match_principals


class ConditionMatchPrincipalsMember(TypedDict, closed=True):
    matchPrincipals: (
        "capo_bedrock_agentcore_control.types.match_principals.MatchPrincipals"
    )


class ConditionMatchPathsMember(TypedDict, closed=True):
    matchPaths: "capo_bedrock_agentcore_control.types.match_paths.MatchPaths"


class ConditionMatchModelsMember(TypedDict, closed=True):
    matchModels: "capo_bedrock_agentcore_control.types.match_models.MatchModels"


Condition: TypeAlias = (
    ConditionMatchPrincipalsMember
    | ConditionMatchPathsMember
    | ConditionMatchModelsMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: Condition) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"Condition: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "matchPrincipals" in value:
        import capo_bedrock_agentcore_control.types.match_principals

        return {
            "matchPrincipals": capo_bedrock_agentcore_control.types.match_principals.serialize_json(
                value["matchPrincipals"]
            )
        }
    elif "matchPaths" in value:
        import capo_bedrock_agentcore_control.types.match_paths

        return {
            "matchPaths": capo_bedrock_agentcore_control.types.match_paths.serialize_json(
                value["matchPaths"]
            )
        }
    elif "matchModels" in value:
        import capo_bedrock_agentcore_control.types.match_models

        return {
            "matchModels": capo_bedrock_agentcore_control.types.match_models.serialize_json(
                value["matchModels"]
            )
        }
    else:
        raise SerializationError("Condition: no variant present")


def deserialize_json(data: dict) -> Condition:
    if data.get("matchPrincipals") is not None:
        import capo_bedrock_agentcore_control.types.match_principals

        return {
            "matchPrincipals": capo_bedrock_agentcore_control.types.match_principals.deserialize_json(
                data["matchPrincipals"]
            )
        }
    elif data.get("matchPaths") is not None:
        import capo_bedrock_agentcore_control.types.match_paths

        return {
            "matchPaths": capo_bedrock_agentcore_control.types.match_paths.deserialize_json(
                data["matchPaths"]
            )
        }
    elif data.get("matchModels") is not None:
        import capo_bedrock_agentcore_control.types.match_models

        return {
            "matchModels": capo_bedrock_agentcore_control.types.match_models.deserialize_json(
                data["matchModels"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("Condition: no recognized variant key")
