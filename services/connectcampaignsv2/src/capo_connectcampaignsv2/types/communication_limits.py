"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#CommunicationLimits``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connectcampaignsv2.errors import DeserializationError, SerializationError
from capo_connectcampaignsv2.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.communication_limit_list


class _CommunicationLimits_communicationLimitsList(TypedDict, closed=True):
    communicationLimitsList: (
        "capo_connectcampaignsv2.types.communication_limit_list.CommunicationLimitList"
    )


CommunicationLimits: TypeAlias = (
    _CommunicationLimits_communicationLimitsList | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: CommunicationLimits) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"CommunicationLimits: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "communicationLimitsList" in value:
        import capo_connectcampaignsv2.types.communication_limit_list

        return {
            "communicationLimitsList": capo_connectcampaignsv2.types.communication_limit_list.serialize_json(
                value["communicationLimitsList"]
            )
        }
    else:
        raise SerializationError("CommunicationLimits: no variant present")


def deserialize_json(data: dict) -> CommunicationLimits:
    if data.get("communicationLimitsList") is not None:
        import capo_connectcampaignsv2.types.communication_limit_list

        return {
            "communicationLimitsList": capo_connectcampaignsv2.types.communication_limit_list.deserialize_json(
                data["communicationLimitsList"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("CommunicationLimits: no recognized variant key")
