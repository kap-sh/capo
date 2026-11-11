"""Generated from Smithy shape ``com.amazonaws.connectcases#BatchUpdateCaseIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectcases.types.batch_update_case_identifier

BatchUpdateCaseIdentifierList: TypeAlias = list[
    "capo_connectcases.types.batch_update_case_identifier.BatchUpdateCaseIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateCaseIdentifierList) -> list:
    import capo_connectcases.types.batch_update_case_identifier

    out: list = []
    for item in value:
        out.append(
            capo_connectcases.types.batch_update_case_identifier.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BatchUpdateCaseIdentifierList:
    import capo_connectcases.types.batch_update_case_identifier

    out: BatchUpdateCaseIdentifierList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_connectcases.types.batch_update_case_identifier.deserialize_json(item)
        )
    return out
