"""Generated from Smithy shape ``com.amazonaws.devicefarm#TestReport``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.report_message
    import capo_device_farm.types.sensitive_url
    import capo_device_farm.types.test_report_metrics


class TestReport(TypedDict, closed=True):
    message: NotRequired["capo_device_farm.types.report_message.ReportMessage"]
    """<p>A message associated with the test report.</p>"""
    metrics: NotRequired["capo_device_farm.types.test_report_metrics.TestReportMetrics"]
    """<p>The aggregated test-level metrics for the job.</p>"""
    test_details_url: NotRequired["capo_device_farm.types.sensitive_url.SensitiveURL"]
    """<p>A URL to the detailed test results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestReport) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "metrics" in value:
        import capo_device_farm.types.test_report_metrics

        out["metrics"] = (
            capo_device_farm.types.test_report_metrics.serialize_aws_json_1_1(
                value["metrics"]
            )
        )
    if "test_details_url" in value:
        out["testDetailsUrl"] = value["test_details_url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TestReport:
    out: TestReport = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("metrics") is not None:
        import capo_device_farm.types.test_report_metrics

        out["metrics"] = (
            capo_device_farm.types.test_report_metrics.deserialize_aws_json_1_1(
                data["metrics"]
            )
        )
    if data.get("testDetailsUrl") is not None:
        out["test_details_url"] = data["testDetailsUrl"]
    return out


def redact_sensitive(value: TestReport) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "test_details_url" in value:
        out["test_details_url"] = "*** Sensitive Data Redacted ***"
    return out
