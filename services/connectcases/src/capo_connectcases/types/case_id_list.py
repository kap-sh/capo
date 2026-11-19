"""Generated from Smithy shape ``com.amazonaws.connectcases#CaseIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectcases.types.case_id

CaseIdList: TypeAlias = list["capo_connectcases.types.case_id.CaseId"]


# --- restJson1 ser/de ---
def serialize_json(value: CaseIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> CaseIdList:
    return [item for item in data if item is not None]
