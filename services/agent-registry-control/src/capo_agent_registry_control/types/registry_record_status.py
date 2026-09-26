"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#RegistryRecordStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>Registry record status</p>"""
RegistryRecordStatus: TypeAlias = Literal[
    "DRAFT",
    "PENDING_APPROVAL",
    "APPROVED",
    "REJECTED",
    "DEPRECATED",
    "CREATING",
    "UPDATING",
    "CREATE_FAILED",
    "UPDATE_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: RegistryRecordStatus) -> str:
    return value


def deserialize_json(data: str) -> RegistryRecordStatus:
    return cast(RegistryRecordStatus, data)
