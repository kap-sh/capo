"""Generated from Smithy shape ``com.amazonaws.costandusagereportservice#DeleteReportDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cost_and_usage_report_service.types.report_name


class DeleteReportDefinitionRequest(TypedDict, closed=True):
    report_name: "capo_cost_and_usage_report_service.types.report_name.ReportName"
    """<p>The name of the report that you want to delete. The name must be unique, is case sensitive, and can't include spaces.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteReportDefinitionRequest) -> dict:
    out: dict = {}
    out["ReportName"] = value["report_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteReportDefinitionRequest:
    out: DeleteReportDefinitionRequest = {}  # type: ignore[typeddict-item]
    if data.get("ReportName") is not None:
        out["report_name"] = data["ReportName"]
    else:
        out["report_name"] = ""
    return out
