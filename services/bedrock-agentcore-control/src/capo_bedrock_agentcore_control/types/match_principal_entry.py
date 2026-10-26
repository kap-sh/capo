"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#MatchPrincipalEntry``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.iam_principal


class _MatchPrincipalEntry_iamPrincipal(TypedDict, closed=True):
    iamPrincipal: "capo_bedrock_agentcore_control.types.iam_principal.IamPrincipal"


MatchPrincipalEntry: TypeAlias = _MatchPrincipalEntry_iamPrincipal | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: MatchPrincipalEntry) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"MatchPrincipalEntry: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "iamPrincipal" in value:
        import capo_bedrock_agentcore_control.types.iam_principal

        return {
            "iamPrincipal": capo_bedrock_agentcore_control.types.iam_principal.serialize_json(
                value["iamPrincipal"]
            )
        }
    else:
        raise SerializationError("MatchPrincipalEntry: no variant present")


def deserialize_json(data: dict) -> MatchPrincipalEntry:
    if data.get("iamPrincipal") is not None:
        import capo_bedrock_agentcore_control.types.iam_principal

        return {
            "iamPrincipal": capo_bedrock_agentcore_control.types.iam_principal.deserialize_json(
                data["iamPrincipal"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("MatchPrincipalEntry: no recognized variant key")
