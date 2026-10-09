"""Generated from Smithy shape ``com.amazonaws.eks#AckDisabledServicesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eks.types.ack_service_name

AckDisabledServicesList: TypeAlias = list[
    "capo_eks.types.ack_service_name.AckServiceName"
]


# --- restJson1 ser/de ---
def serialize_json(value: AckDisabledServicesList) -> list:
    return list(value)


def deserialize_json(data: list) -> AckDisabledServicesList:
    return [item for item in data if item is not None]
