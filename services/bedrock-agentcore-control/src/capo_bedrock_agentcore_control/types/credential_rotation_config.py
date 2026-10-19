"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CredentialRotationConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.coinbase_cdp_rotation_targets


class _CredentialRotationConfig_coinbaseCDP(TypedDict, closed=True):
    coinbaseCDP: "capo_bedrock_agentcore_control.types.coinbase_cdp_rotation_targets.CoinbaseCdpRotationTargets"


CredentialRotationConfig: TypeAlias = (
    _CredentialRotationConfig_coinbaseCDP | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: CredentialRotationConfig) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"CredentialRotationConfig: cannot serialize unknown variant {value.name!r}"
        )
    elif "coinbaseCDP" in value:
        import capo_bedrock_agentcore_control.types.coinbase_cdp_rotation_targets

        return {
            "coinbaseCDP": capo_bedrock_agentcore_control.types.coinbase_cdp_rotation_targets.serialize_json(
                value["coinbaseCDP"]
            )
        }
    else:
        raise SerializationError("CredentialRotationConfig: no variant present")


def deserialize_json(data: dict) -> CredentialRotationConfig:
    if data.get("coinbaseCDP") is not None:
        import capo_bedrock_agentcore_control.types.coinbase_cdp_rotation_targets

        return {
            "coinbaseCDP": capo_bedrock_agentcore_control.types.coinbase_cdp_rotation_targets.deserialize_json(
                data["coinbaseCDP"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "CredentialRotationConfig: no recognized variant key"
        )
