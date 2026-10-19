"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#ListScheduledReportsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bcm_dashboards.types.next_page_token
    import capo_bcm_dashboards.types.scheduled_report_summary_list


class ListScheduledReportsResponse(TypedDict, closed=True):
    scheduled_reports: "capo_bcm_dashboards.types.scheduled_report_summary_list.ScheduledReportSummaryList"
    """<p>An array of scheduled report summaries, containing basic information about each scheduled report.</p>"""
    next_token: NotRequired["capo_bcm_dashboards.types.next_page_token.NextPageToken"]
    """<p>The token to use to retrieve the next page of results. Not returned if there are no more results to retrieve.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListScheduledReportsResponse) -> dict:
    out: dict = {}
    import capo_bcm_dashboards.types.scheduled_report_summary_list

    out["scheduledReports"] = (
        capo_bcm_dashboards.types.scheduled_report_summary_list.serialize_aws_json_1_0(
            value["scheduled_reports"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListScheduledReportsResponse:
    out: ListScheduledReportsResponse = {}  # type: ignore[typeddict-item]
    if data.get("scheduledReports") is not None:
        import capo_bcm_dashboards.types.scheduled_report_summary_list

        out["scheduled_reports"] = (
            capo_bcm_dashboards.types.scheduled_report_summary_list.deserialize_aws_json_1_0(
                data["scheduledReports"]
            )
        )
    else:
        out["scheduled_reports"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
