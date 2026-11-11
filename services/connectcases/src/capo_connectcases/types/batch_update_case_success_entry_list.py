"""Generated from Smithy shape ``com.amazonaws.connectcases#BatchUpdateCaseSuccessEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectcases.types.batch_update_case_success_entry

BatchUpdateCaseSuccessEntryList: TypeAlias = list[
    "capo_connectcases.types.batch_update_case_success_entry.BatchUpdateCaseSuccessEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateCaseSuccessEntryList) -> list:
    import capo_connectcases.types.batch_update_case_success_entry

    out: list = []
    for item in value:
        out.append(
            capo_connectcases.types.batch_update_case_success_entry.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BatchUpdateCaseSuccessEntryList:
    import capo_connectcases.types.batch_update_case_success_entry

    out: BatchUpdateCaseSuccessEntryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_connectcases.types.batch_update_case_success_entry.deserialize_json(
                item
            )
        )
    return out
