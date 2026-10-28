"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ResourceShareDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError, SerializationError
from capo_mediaconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mediaconnect.types.consumed_resource_share_details
    import capo_mediaconnect.types.owned_resource_share_details


class ResourceShareDetailsOwnedMember(TypedDict, closed=True):
    Owned: (
        "capo_mediaconnect.types.owned_resource_share_details.OwnedResourceShareDetails"
    )


class ResourceShareDetailsConsumedMember(TypedDict, closed=True):
    Consumed: "capo_mediaconnect.types.consumed_resource_share_details.ConsumedResourceShareDetails"


ResourceShareDetails: TypeAlias = (
    ResourceShareDetailsOwnedMember
    | ResourceShareDetailsConsumedMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ResourceShareDetails) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ResourceShareDetails: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Owned" in value:
        import capo_mediaconnect.types.owned_resource_share_details

        return {
            "owned": capo_mediaconnect.types.owned_resource_share_details.serialize_json(
                value["Owned"]
            )
        }
    elif "Consumed" in value:
        import capo_mediaconnect.types.consumed_resource_share_details

        return {
            "consumed": capo_mediaconnect.types.consumed_resource_share_details.serialize_json(
                value["Consumed"]
            )
        }
    else:
        raise SerializationError("ResourceShareDetails: no variant present")


def deserialize_json(data: dict) -> ResourceShareDetails:
    if data.get("owned") is not None:
        import capo_mediaconnect.types.owned_resource_share_details

        return {
            "Owned": capo_mediaconnect.types.owned_resource_share_details.deserialize_json(
                data["owned"]
            )
        }
    elif data.get("consumed") is not None:
        import capo_mediaconnect.types.consumed_resource_share_details

        return {
            "Consumed": capo_mediaconnect.types.consumed_resource_share_details.deserialize_json(
                data["consumed"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ResourceShareDetails: no recognized variant key")
