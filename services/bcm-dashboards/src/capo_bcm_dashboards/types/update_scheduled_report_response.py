"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#UpdateScheduledReportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bcm_dashboards.types.scheduled_report_arn


class UpdateScheduledReportResponse(TypedDict, closed=True):
    arn: "capo_bcm_dashboards.types.scheduled_report_arn.ScheduledReportArn"
    """<p>The ARN of the updated scheduled report.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateScheduledReportResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateScheduledReportResponse:
    out: UpdateScheduledReportResponse = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    return out
