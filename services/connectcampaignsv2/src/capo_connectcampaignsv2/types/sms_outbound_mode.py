"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#SmsOutboundMode``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connectcampaignsv2.errors import DeserializationError, SerializationError
from capo_connectcampaignsv2.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.agentless_config


class _SmsOutboundMode_agentless(TypedDict, closed=True):
    agentless: "capo_connectcampaignsv2.types.agentless_config.AgentlessConfig"


SmsOutboundMode: TypeAlias = _SmsOutboundMode_agentless | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: SmsOutboundMode) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"SmsOutboundMode: cannot serialize unknown variant {value.name!r}"
        )
    elif "agentless" in value:
        import capo_connectcampaignsv2.types.agentless_config

        return {
            "agentless": capo_connectcampaignsv2.types.agentless_config.serialize_json(
                value["agentless"]
            )
        }
    else:
        raise SerializationError("SmsOutboundMode: no variant present")


def deserialize_json(data: dict) -> SmsOutboundMode:
    if data.get("agentless") is not None:
        import capo_connectcampaignsv2.types.agentless_config

        return {
            "agentless": capo_connectcampaignsv2.types.agentless_config.deserialize_json(
                data["agentless"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("SmsOutboundMode: no recognized variant key")
