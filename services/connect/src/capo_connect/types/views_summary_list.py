"""Generated from Smithy shape ``com.amazonaws.connect#ViewsSummaryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.view_summary

ViewsSummaryList: TypeAlias = list["capo_connect.types.view_summary.ViewSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: ViewsSummaryList) -> list:
    import capo_connect.types.view_summary

    out: list = []
    for item in value:
        out.append(capo_connect.types.view_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ViewsSummaryList:
    import capo_connect.types.view_summary

    out: ViewsSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_connect.types.view_summary.deserialize_json(item))
    return out


def redact_sensitive(value: ViewsSummaryList) -> list[Any]:
    import capo_connect.types.view_summary

    return [capo_connect.types.view_summary.redact_sensitive(item) for item in value]
