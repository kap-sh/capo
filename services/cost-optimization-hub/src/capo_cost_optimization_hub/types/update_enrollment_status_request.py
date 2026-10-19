"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#UpdateEnrollmentStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_optimization_hub.types.enrollment_status


class UpdateEnrollmentStatusRequest(TypedDict, closed=True):
    status: "capo_cost_optimization_hub.types.enrollment_status.EnrollmentStatus"
    """<p>Sets the account status.</p>"""
    include_member_accounts: NotRequired["bool"]
    """<p>Indicates whether to enroll member accounts of the organization if the account is the management account or delegated administrator.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateEnrollmentStatusRequest) -> dict:
    out: dict = {}
    import capo_cost_optimization_hub.types.enrollment_status

    out["status"] = (
        capo_cost_optimization_hub.types.enrollment_status.serialize_aws_json_1_0(
            value["status"]
        )
    )
    if "include_member_accounts" in value:
        out["includeMemberAccounts"] = value["include_member_accounts"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateEnrollmentStatusRequest:
    out: UpdateEnrollmentStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_cost_optimization_hub.types.enrollment_status

        out["status"] = (
            capo_cost_optimization_hub.types.enrollment_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_cost_optimization_hub.types.enrollment_status.EnrollmentStatus", ""
        )
    if data.get("includeMemberAccounts") is not None:
        out["include_member_accounts"] = data["includeMemberAccounts"]
    return out
