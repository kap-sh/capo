"""Generated from Smithy shape ``com.amazonaws.qconnect#DataSummaryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.data_summary

DataSummaryList: TypeAlias = list["capo_qconnect.types.data_summary.DataSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: DataSummaryList) -> list:
    import capo_qconnect.types.data_summary

    out: list = []
    for item in value:
        out.append(capo_qconnect.types.data_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataSummaryList:
    import capo_qconnect.types.data_summary

    out: DataSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_qconnect.types.data_summary.deserialize_json(item))
    return out


def redact_sensitive(value: DataSummaryList) -> list[Any]:
    import capo_qconnect.types.data_summary

    return [capo_qconnect.types.data_summary.redact_sensitive(item) for item in value]
