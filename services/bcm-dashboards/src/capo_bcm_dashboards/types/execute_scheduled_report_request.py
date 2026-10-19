"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#ExecuteScheduledReportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bcm_dashboards.types.client_token
    import capo_bcm_dashboards.types.scheduled_report_arn


class ExecuteScheduledReportRequest(TypedDict, closed=True):
    arn: "capo_bcm_dashboards.types.scheduled_report_arn.ScheduledReportArn"
    """<p>The ARN of the scheduled report to execute.</p>"""
    client_token: NotRequired["capo_bcm_dashboards.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    dry_run: NotRequired["bool"]
    """<p>When set to <code>true</code>, validates the scheduled report configuration without triggering an actual execution.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExecuteScheduledReportRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "dry_run" in value:
        out["dryRun"] = value["dry_run"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ExecuteScheduledReportRequest:
    out: ExecuteScheduledReportRequest = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("dryRun") is not None:
        out["dry_run"] = data["dryRun"]
    return out
