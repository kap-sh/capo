"""Generated from Smithy shape ``com.amazonaws.ebs#ChangedBlocks``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_ebs.types.changed_block

ChangedBlocks: TypeAlias = list["capo_ebs.types.changed_block.ChangedBlock"]


# --- restJson1 ser/de ---
def serialize_json(value: ChangedBlocks) -> list:
    import capo_ebs.types.changed_block

    out: list = []
    for item in value:
        out.append(capo_ebs.types.changed_block.serialize_json(item))
    return out


def deserialize_json(data: list) -> ChangedBlocks:
    import capo_ebs.types.changed_block

    out: ChangedBlocks = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ebs.types.changed_block.deserialize_json(item))
    return out


def redact_sensitive(value: ChangedBlocks) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
