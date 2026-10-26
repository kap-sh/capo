"""Generated from Smithy shape ``com.amazonaws.groundstation#UplinkDataflowDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_groundstation.errors import DeserializationError, SerializationError
from capo_groundstation.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_groundstation.types.uplink_connection_details


class _UplinkDataflowDetails_agentConnectionDetails(TypedDict, closed=True):
    agentConnectionDetails: (
        "capo_groundstation.types.uplink_connection_details.UplinkConnectionDetails"
    )


UplinkDataflowDetails: TypeAlias = (
    _UplinkDataflowDetails_agentConnectionDetails | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: UplinkDataflowDetails) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"UplinkDataflowDetails: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "agentConnectionDetails" in value:
        import capo_groundstation.types.uplink_connection_details

        return {
            "agentConnectionDetails": capo_groundstation.types.uplink_connection_details.serialize_json(
                value["agentConnectionDetails"]
            )
        }
    else:
        raise SerializationError("UplinkDataflowDetails: no variant present")


def deserialize_json(data: dict) -> UplinkDataflowDetails:
    if data.get("agentConnectionDetails") is not None:
        import capo_groundstation.types.uplink_connection_details

        return {
            "agentConnectionDetails": capo_groundstation.types.uplink_connection_details.deserialize_json(
                data["agentConnectionDetails"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("UplinkDataflowDetails: no recognized variant key")
