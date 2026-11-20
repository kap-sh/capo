"""Generated from Smithy shape ``com.amazonaws.abusesignal#ListAbuseReportStatusesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_abuse_signal.types.next_token
    import capo_abuse_signal.types.report_status_list


class ListAbuseReportStatusesResponse(TypedDict, closed=True):
    reports: "capo_abuse_signal.types.report_status_list.ReportStatusList"
    """<p>A list of abuse report status items. This list is empty when no reports are found for the calling account, or when no reports match the specified <code>correlationId</code> filter.</p>"""
    next_token: NotRequired["capo_abuse_signal.types.next_token.NextToken"]
    """<p>The pagination token for the next page of results. This value is <code>null</code> when there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAbuseReportStatusesResponse) -> dict:
    out: dict = {}
    import capo_abuse_signal.types.report_status_list

    out["reports"] = capo_abuse_signal.types.report_status_list.serialize_json(
        value["reports"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAbuseReportStatusesResponse:
    out: ListAbuseReportStatusesResponse = {}  # type: ignore[typeddict-item]
    if data.get("reports") is not None:
        import capo_abuse_signal.types.report_status_list

        out["reports"] = capo_abuse_signal.types.report_status_list.deserialize_json(
            data["reports"]
        )
    else:
        out["reports"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
