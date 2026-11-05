"""Generated from Smithy shape ``com.amazonaws.connect#CaseEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.case_entry

CaseEntries: TypeAlias = list["capo_connect.types.case_entry.CaseEntry"]


# --- restJson1 ser/de ---
def serialize_json(value: CaseEntries) -> list:
    import capo_connect.types.case_entry

    out: list = []
    for item in value:
        out.append(capo_connect.types.case_entry.serialize_json(item))
    return out


def deserialize_json(data: list) -> CaseEntries:
    import capo_connect.types.case_entry

    out: CaseEntries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_connect.types.case_entry.deserialize_json(item))
    return out
