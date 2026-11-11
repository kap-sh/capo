"""Generated from Smithy shape ``com.amazonaws.batch#EksContainerLinuxCapabilityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.eks_container_linux_capability

EksContainerLinuxCapabilityList: TypeAlias = list[
    "capo_batch.types.eks_container_linux_capability.EksContainerLinuxCapability"
]


# --- restJson1 ser/de ---
def serialize_json(value: EksContainerLinuxCapabilityList) -> list:
    return list(value)


def deserialize_json(data: list) -> EksContainerLinuxCapabilityList:
    return [item for item in data if item is not None]
