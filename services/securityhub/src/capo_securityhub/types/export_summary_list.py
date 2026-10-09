"""Generated from Smithy shape ``com.amazonaws.securityhub#ExportSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.export_summary

ExportSummaryList: TypeAlias = list[
    "capo_securityhub.types.export_summary.ExportSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExportSummaryList) -> list:
    import capo_securityhub.types.export_summary

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.export_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ExportSummaryList:
    import capo_securityhub.types.export_summary

    out: ExportSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_securityhub.types.export_summary.deserialize_json(item))
    return out
