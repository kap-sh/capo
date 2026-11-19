"""Generated from Smithy shape ``com.amazonaws.mgn#AssociationVmUUIDList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.vm_uuid

AssociationVmUUIDList: TypeAlias = list["capo_mgn.types.vm_uuid.VmUUID"]


# --- restJson1 ser/de ---
def serialize_json(value: AssociationVmUUIDList) -> list:
    return list(value)


def deserialize_json(data: list) -> AssociationVmUUIDList:
    return [item for item in data if item is not None]
