"""Generated from Smithy shape ``com.amazonaws.devicefarm#RunInsights``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.job_report
    import capo_device_farm.types.report_status


class RunInsights(TypedDict, closed=True):
    status: NotRequired["capo_device_farm.types.report_status.ReportStatus"]
    """<p>The status of the insights report for the run.</p>"""
    job_report: NotRequired["capo_device_farm.types.job_report.JobReport"]
    """<p>The job-level aggregated report for the run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RunInsights) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_device_farm.types.report_status

        out["status"] = capo_device_farm.types.report_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "job_report" in value:
        import capo_device_farm.types.job_report

        out["jobReport"] = capo_device_farm.types.job_report.serialize_aws_json_1_1(
            value["job_report"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RunInsights:
    out: RunInsights = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_device_farm.types.report_status

        out["status"] = capo_device_farm.types.report_status.deserialize_aws_json_1_1(
            data["status"]
        )
    if data.get("jobReport") is not None:
        import capo_device_farm.types.job_report

        out["job_report"] = capo_device_farm.types.job_report.deserialize_aws_json_1_1(
            data["jobReport"]
        )
    return out


def redact_sensitive(value: RunInsights) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "job_report" in value:
        import capo_device_farm.types.job_report

        out["job_report"] = capo_device_farm.types.job_report.redact_sensitive(
            value["job_report"]
        )
    return out
