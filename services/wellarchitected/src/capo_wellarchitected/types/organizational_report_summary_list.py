"""Generated from Smithy shape ``com.amazonaws.wellarchitected#OrganizationalReportSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.organizational_report_summary

OrganizationalReportSummaryList: TypeAlias = list[
    "capo_wellarchitected.types.organizational_report_summary.OrganizationalReportSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationalReportSummaryList) -> list:
    import capo_wellarchitected.types.organizational_report_summary

    out: list = []
    for item in value:
        out.append(
            capo_wellarchitected.types.organizational_report_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> OrganizationalReportSummaryList:
    import capo_wellarchitected.types.organizational_report_summary

    out: OrganizationalReportSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_wellarchitected.types.organizational_report_summary.deserialize_json(
                item
            )
        )
    return out
