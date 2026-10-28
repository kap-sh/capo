"""Generated from Smithy shape ``com.amazonaws.datazone#GrantedEntity``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError
from capo_datazone.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_datazone.types.listing_revision


class GrantedEntityListingMember(TypedDict, closed=True):
    listing: "capo_datazone.types.listing_revision.ListingRevision"


GrantedEntity: TypeAlias = GrantedEntityListingMember | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: GrantedEntity) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"GrantedEntity: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "listing" in value:
        import capo_datazone.types.listing_revision

        return {
            "listing": capo_datazone.types.listing_revision.serialize_json(
                value["listing"]
            )
        }
    else:
        raise SerializationError("GrantedEntity: no variant present")


def deserialize_json(data: dict) -> GrantedEntity:
    if data.get("listing") is not None:
        import capo_datazone.types.listing_revision

        return {
            "listing": capo_datazone.types.listing_revision.deserialize_json(
                data["listing"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("GrantedEntity: no recognized variant key")
