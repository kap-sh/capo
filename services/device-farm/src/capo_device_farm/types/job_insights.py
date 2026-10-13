"""Generated from Smithy shape ``com.amazonaws.devicefarm#JobInsights``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.report_status
    import capo_device_farm.types.test_report


class JobInsights(TypedDict, closed=True):
    status: NotRequired["capo_device_farm.types.report_status.ReportStatus"]
    """<p>The status of the insights report for the job.</p>"""
    test_report: NotRequired["capo_device_farm.types.test_report.TestReport"]
    """<p>The test-level aggregated report for the job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobInsights) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_device_farm.types.report_status

        out["status"] = capo_device_farm.types.report_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "test_report" in value:
        import capo_device_farm.types.test_report

        out["testReport"] = capo_device_farm.types.test_report.serialize_aws_json_1_1(
            value["test_report"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> JobInsights:
    out: JobInsights = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_device_farm.types.report_status

        out["status"] = capo_device_farm.types.report_status.deserialize_aws_json_1_1(
            data["status"]
        )
    if data.get("testReport") is not None:
        import capo_device_farm.types.test_report

        out["test_report"] = (
            capo_device_farm.types.test_report.deserialize_aws_json_1_1(
                data["testReport"]
            )
        )
    return out


def redact_sensitive(value: JobInsights) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "test_report" in value:
        import capo_device_farm.types.test_report

        out["test_report"] = capo_device_farm.types.test_report.redact_sensitive(
            value["test_report"]
        )
    return out
