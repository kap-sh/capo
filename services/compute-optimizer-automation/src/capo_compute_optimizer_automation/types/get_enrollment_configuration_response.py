"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#GetEnrollmentConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_compute_optimizer_automation.types.enrollment_status
    import capo_compute_optimizer_automation.types.organization_rule_mode


class GetEnrollmentConfigurationResponse(TypedDict, closed=True):
    status: "capo_compute_optimizer_automation.types.enrollment_status.EnrollmentStatus"
    """<p> The current enrollment status. </p>"""
    status_reason: NotRequired["str"]
    """<p> The reason for the current enrollment status. </p>"""
    organization_rule_mode: NotRequired[
        "capo_compute_optimizer_automation.types.organization_rule_mode.OrganizationRuleMode"
    ]
    """<p>Specifies whether the management account can create Automation rules that implement optimization actions for this account. </p>"""
    last_updated_timestamp: NotRequired["datetime.datetime"]
    """<p> The timestamp of the last update to the enrollment configuration. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetEnrollmentConfigurationResponse) -> dict:
    out: dict = {}
    import capo_compute_optimizer_automation.types.enrollment_status

    out["status"] = (
        capo_compute_optimizer_automation.types.enrollment_status.serialize_aws_json_1_0(
            value["status"]
        )
    )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "organization_rule_mode" in value:
        import capo_compute_optimizer_automation.types.organization_rule_mode

        out["organizationRuleMode"] = (
            capo_compute_optimizer_automation.types.organization_rule_mode.serialize_aws_json_1_0(
                value["organization_rule_mode"]
            )
        )
    if "last_updated_timestamp" in value:
        import capo_compute_optimizer_automation.types._prelude.timestamp

        out["lastUpdatedTimestamp"] = (
            capo_compute_optimizer_automation.types._prelude.timestamp.serialize_aws_json_1_0(
                value["last_updated_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetEnrollmentConfigurationResponse:
    out: GetEnrollmentConfigurationResponse = {}  # type: ignore[typeddict-item]
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
    if data.get("organizationRuleMode") is not None:
        import capo_compute_optimizer_automation.types.organization_rule_mode

        out["organization_rule_mode"] = (
            capo_compute_optimizer_automation.types.organization_rule_mode.deserialize_aws_json_1_0(
                data["organizationRuleMode"]
            )
        )
    if data.get("lastUpdatedTimestamp") is not None:
        import capo_compute_optimizer_automation.types._prelude.timestamp

        out["last_updated_timestamp"] = (
            capo_compute_optimizer_automation.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["lastUpdatedTimestamp"]
            )
        )
    return out
