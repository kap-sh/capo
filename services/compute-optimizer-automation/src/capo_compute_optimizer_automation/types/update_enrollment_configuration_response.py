"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#UpdateEnrollmentConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_compute_optimizer_automation.types.enrollment_status


class UpdateEnrollmentConfigurationResponse(TypedDict, closed=True):
    status: "capo_compute_optimizer_automation.types.enrollment_status.EnrollmentStatus"
    """<p> The updated enrollment status. </p>"""
    status_reason: NotRequired["str"]
    """<p> The reason for the updated enrollment status. </p>"""
    last_updated_timestamp: "datetime.datetime"
    """<p> The timestamp when the enrollment configuration was last updated. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateEnrollmentConfigurationResponse) -> dict:
    out: dict = {}
    import capo_compute_optimizer_automation.types.enrollment_status

    out["status"] = (
        capo_compute_optimizer_automation.types.enrollment_status.serialize_aws_json_1_0(
            value["status"]
        )
    )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    import capo_compute_optimizer_automation.types._prelude.timestamp

    out["lastUpdatedTimestamp"] = (
        capo_compute_optimizer_automation.types._prelude.timestamp.serialize_aws_json_1_0(
            value["last_updated_timestamp"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateEnrollmentConfigurationResponse:
    out: UpdateEnrollmentConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_compute_optimizer_automation.types.enrollment_status

        out["status"] = (
            capo_compute_optimizer_automation.types.enrollment_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_compute_optimizer_automation.types.enrollment_status.EnrollmentStatus",
            "",
        )
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("lastUpdatedTimestamp") is not None:
        import capo_compute_optimizer_automation.types._prelude.timestamp

        out["last_updated_timestamp"] = (
            capo_compute_optimizer_automation.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["lastUpdatedTimestamp"]
            )
        )
    else:
        import datetime

        out["last_updated_timestamp"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
