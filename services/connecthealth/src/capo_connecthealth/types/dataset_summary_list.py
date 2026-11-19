"""Generated from Smithy shape ``com.amazonaws.connecthealth#DatasetSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connecthealth.types.dataset_summary

DatasetSummaryList: TypeAlias = list[
    "capo_connecthealth.types.dataset_summary.DatasetSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DatasetSummaryList) -> list:
    import capo_connecthealth.types.dataset_summary

    out: list = []
    for item in value:
        out.append(capo_connecthealth.types.dataset_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> DatasetSummaryList:
    import capo_connecthealth.types.dataset_summary

    out: DatasetSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_connecthealth.types.dataset_summary.deserialize_json(item))
    return out
