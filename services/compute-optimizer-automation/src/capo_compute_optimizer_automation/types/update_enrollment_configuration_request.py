"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#UpdateEnrollmentConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.client_token
    import capo_compute_optimizer_automation.types.enrollment_status


class UpdateEnrollmentConfigurationRequest(TypedDict, closed=True):
    status: "capo_compute_optimizer_automation.types.enrollment_status.EnrollmentStatus"
    """<p>The desired enrollment status. </p> <ul> <li> <p>Active - Enables the Automation feature for your account.</p> </li> <li> <p>Inactive - Disables the Automation feature for your account and stops all of your automation rules. If you opt in again later, all rules will be inactive, and you must enable the rules you want to run. You must wait at least 24 hours after opting out to opt in again.</p> </li> </ul> <note> <p>The <code>Pending</code> and <code>Failed</code> options cannot be used to update the enrollment status of an account. They are returned in the response of a request to update the enrollment status of an account.</p> <p>If you are a member account, your account must be disassociated from your organization’s management account before you can disable Automation. Contact your administrator to make this change.</p> </note>"""
    client_token: NotRequired[
        "capo_compute_optimizer_automation.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Must be 1-64 characters long and contain only alphanumeric characters, underscores, and hyphens.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateEnrollmentConfigurationRequest) -> dict:
    out: dict = {}
    import capo_compute_optimizer_automation.types.enrollment_status

    out["status"] = (
        capo_compute_optimizer_automation.types.enrollment_status.serialize_aws_json_1_0(
            value["status"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateEnrollmentConfigurationRequest:
    out: UpdateEnrollmentConfigurationRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
