"""Generated from Smithy shape ``com.amazonaws.mediaconnect#MergeRouterInputProtocolConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError, SerializationError
from capo_mediaconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mediaconnect.types.rist_router_input_configuration
    import capo_mediaconnect.types.rtp_router_input_configuration


class _MergeRouterInputProtocolConfiguration_Rtp(TypedDict, closed=True):
    Rtp: "capo_mediaconnect.types.rtp_router_input_configuration.RtpRouterInputConfiguration"


class _MergeRouterInputProtocolConfiguration_Rist(TypedDict, closed=True):
    Rist: "capo_mediaconnect.types.rist_router_input_configuration.RistRouterInputConfiguration"


MergeRouterInputProtocolConfiguration: TypeAlias = (
    _MergeRouterInputProtocolConfiguration_Rtp
    | _MergeRouterInputProtocolConfiguration_Rist
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: MergeRouterInputProtocolConfiguration) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"MergeRouterInputProtocolConfiguration: cannot serialize unknown variant {value.name!r}"
        )
    elif "Rtp" in value:
        import capo_mediaconnect.types.rtp_router_input_configuration

        return {
            "rtp": capo_mediaconnect.types.rtp_router_input_configuration.serialize_json(
                value["Rtp"]
            )
        }
    elif "Rist" in value:
        import capo_mediaconnect.types.rist_router_input_configuration

        return {
            "rist": capo_mediaconnect.types.rist_router_input_configuration.serialize_json(
                value["Rist"]
            )
        }
    else:
        raise SerializationError(
            "MergeRouterInputProtocolConfiguration: no variant present"
        )


def deserialize_json(data: dict) -> MergeRouterInputProtocolConfiguration:
    if data.get("rtp") is not None:
        import capo_mediaconnect.types.rtp_router_input_configuration

        return {
            "Rtp": capo_mediaconnect.types.rtp_router_input_configuration.deserialize_json(
                data["rtp"]
            )
        }
    elif data.get("rist") is not None:
        import capo_mediaconnect.types.rist_router_input_configuration

        return {
            "Rist": capo_mediaconnect.types.rist_router_input_configuration.deserialize_json(
                data["rist"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "MergeRouterInputProtocolConfiguration: no recognized variant key"
        )
