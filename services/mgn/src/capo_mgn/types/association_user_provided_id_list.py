"""Generated from Smithy shape ``com.amazonaws.mgn#AssociationUserProvidedIDList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.association_user_provided_id

AssociationUserProvidedIDList: TypeAlias = list[
    "capo_mgn.types.association_user_provided_id.AssociationUserProvidedID"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssociationUserProvidedIDList) -> list:
    return list(value)


def deserialize_json(data: list) -> AssociationUserProvidedIDList:
    return [item for item in data if item is not None]
