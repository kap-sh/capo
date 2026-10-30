"""Generated from Smithy shape ``com.amazonaws.inspector2#ScanSourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.scan_source

ScanSourceList: TypeAlias = list["capo_inspector2.types.scan_source.ScanSource"]


# --- restJson1 ser/de ---
def serialize_json(value: ScanSourceList) -> list:
    return list(value)


def deserialize_json(data: list) -> ScanSourceList:
    return [item for item in data if item is not None]
