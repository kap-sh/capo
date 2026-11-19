"""Generated from Smithy shape ``com.amazonaws.mgn#AssociationCidrList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.cidr_block

AssociationCidrList: TypeAlias = list["capo_mgn.types.cidr_block.CidrBlock"]


# --- restJson1 ser/de ---
def serialize_json(value: AssociationCidrList) -> list:
    return list(value)


def deserialize_json(data: list) -> AssociationCidrList:
    return [item for item in data if item is not None]
