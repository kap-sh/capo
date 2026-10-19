"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#WhatsAppOutboundMode``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connectcampaignsv2.errors import DeserializationError, SerializationError
from capo_connectcampaignsv2.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.agentless_config


class _WhatsAppOutboundMode_agentless(TypedDict, closed=True):
    agentless: "capo_connectcampaignsv2.types.agentless_config.AgentlessConfig"


WhatsAppOutboundMode: TypeAlias = _WhatsAppOutboundMode_agentless | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: WhatsAppOutboundMode) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"WhatsAppOutboundMode: cannot serialize unknown variant {value.name!r}"
        )
    elif "agentless" in value:
        import capo_connectcampaignsv2.types.agentless_config

        return {
            "agentless": capo_connectcampaignsv2.types.agentless_config.serialize_json(
                value["agentless"]
            )
        }
    else:
        raise SerializationError("WhatsAppOutboundMode: no variant present")


def deserialize_json(data: dict) -> WhatsAppOutboundMode:
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
        raise DeserializationError("WhatsAppOutboundMode: no recognized variant key")
