"""Generated from Smithy shape ``com.amazonaws.abusesignal#ReportStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_abuse_signal.types.report_status_list_item

ReportStatusList: TypeAlias = list[
    "capo_abuse_signal.types.report_status_list_item.ReportStatusListItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReportStatusList) -> list:
    import capo_abuse_signal.types.report_status_list_item

    out: list = []
    for item in value:
        out.append(capo_abuse_signal.types.report_status_list_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> ReportStatusList:
    import capo_abuse_signal.types.report_status_list_item

    out: ReportStatusList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_abuse_signal.types.report_status_list_item.deserialize_json(item)
        )
    return out
