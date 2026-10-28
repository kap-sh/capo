"""Generated from Smithy shape ``com.amazonaws.datazone#GrantedEntityInput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError
from capo_datazone.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_datazone.types.listing_revision_input


class GrantedEntityInputListingMember(TypedDict, closed=True):
    listing: "capo_datazone.types.listing_revision_input.ListingRevisionInput"


GrantedEntityInput: TypeAlias = GrantedEntityInputListingMember | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: GrantedEntityInput) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"GrantedEntityInput: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "listing" in value:
        import capo_datazone.types.listing_revision_input

        return {
            "listing": capo_datazone.types.listing_revision_input.serialize_json(
                value["listing"]
            )
        }
    else:
        raise SerializationError("GrantedEntityInput: no variant present")


def deserialize_json(data: dict) -> GrantedEntityInput:
    if data.get("listing") is not None:
        import capo_datazone.types.listing_revision_input

        return {
            "listing": capo_datazone.types.listing_revision_input.deserialize_json(
                data["listing"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("GrantedEntityInput: no recognized variant key")
