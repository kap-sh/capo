"""Generated from Smithy shape ``com.amazonaws.devicefarm#JobReport``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.job_report_metrics
    import capo_device_farm.types.report_message
    import capo_device_farm.types.sensitive_url


class JobReport(TypedDict, closed=True):
    message: NotRequired["capo_device_farm.types.report_message.ReportMessage"]
    """<p>A message associated with the job report.</p>"""
    metrics: NotRequired["capo_device_farm.types.job_report_metrics.JobReportMetrics"]
    """<p>The aggregated job-level metrics for the run.</p>"""
    job_details_url: NotRequired["capo_device_farm.types.sensitive_url.SensitiveURL"]
    """<p>A URL to the detailed job results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobReport) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "metrics" in value:
        import capo_device_farm.types.job_report_metrics

        out["metrics"] = (
            capo_device_farm.types.job_report_metrics.serialize_aws_json_1_1(
                value["metrics"]
            )
        )
    if "job_details_url" in value:
        out["jobDetailsUrl"] = value["job_details_url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> JobReport:
    out: JobReport = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("metrics") is not None:
        import capo_device_farm.types.job_report_metrics

        out["metrics"] = (
            capo_device_farm.types.job_report_metrics.deserialize_aws_json_1_1(
                data["metrics"]
            )
        )
    if data.get("jobDetailsUrl") is not None:
        out["job_details_url"] = data["jobDetailsUrl"]
    return out


def redact_sensitive(value: JobReport) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "job_details_url" in value:
        out["job_details_url"] = "*** Sensitive Data Redacted ***"
    return out
