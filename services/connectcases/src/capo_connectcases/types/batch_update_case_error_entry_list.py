"""Generated from Smithy shape ``com.amazonaws.connectcases#BatchUpdateCaseErrorEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectcases.types.batch_update_case_error_entry

BatchUpdateCaseErrorEntryList: TypeAlias = list[
    "capo_connectcases.types.batch_update_case_error_entry.BatchUpdateCaseErrorEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateCaseErrorEntryList) -> list:
    import capo_connectcases.types.batch_update_case_error_entry

    out: list = []
    for item in value:
        out.append(
            capo_connectcases.types.batch_update_case_error_entry.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BatchUpdateCaseErrorEntryList:
    import capo_connectcases.types.batch_update_case_error_entry

    out: BatchUpdateCaseErrorEntryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_connectcases.types.batch_update_case_error_entry.deserialize_json(item)
        )
    return out
