"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#UpdateEnrollmentStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_compute_optimizer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_compute_optimizer.types.include_member_accounts
    import capo_compute_optimizer.types.status


class UpdateEnrollmentStatusRequest(TypedDict, closed=True):
    status: "capo_compute_optimizer.types.status.Status"
    """<p>The new enrollment status of the account.</p> <p>The following status options are available:</p> <ul> <li> <p> <code>Active</code> - Opts in your account to the Compute Optimizer service. Compute Optimizer begins analyzing the configuration and utilization metrics of your Amazon Web Services resources after you opt in. For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/metrics.html">Metrics analyzed by Compute Optimizer</a> in the <i>Compute Optimizer User Guide</i>.</p> </li> <li> <p> <code>Inactive</code> - Opts out your account from the Compute Optimizer service. Your account's recommendations and related metrics data will be deleted from Compute Optimizer after you opt out.</p> </li> </ul> <note> <p>The <code>Pending</code> and <code>Failed</code> options cannot be used to update the enrollment status of an account. They are returned in the response of a request to update the enrollment status of an account.</p> </note>"""
    include_member_accounts: (
        "capo_compute_optimizer.types.include_member_accounts.IncludeMemberAccounts"
    )
    """<p>Indicates whether to enroll member accounts of the organization if the account is the management account of an organization.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateEnrollmentStatusRequest) -> dict:
    out: dict = {}
    import capo_compute_optimizer.types.status

    out["status"] = capo_compute_optimizer.types.status.serialize_aws_json_1_0(
        value["status"]
    )
    out["includeMemberAccounts"] = value.get("include_member_accounts", False)
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateEnrollmentStatusRequest:
    out: UpdateEnrollmentStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_compute_optimizer.types.status

        out["status"] = capo_compute_optimizer.types.status.deserialize_aws_json_1_0(
            data["status"]
        )
    else:
        raise DeserializationError("UpdateEnrollmentStatusRequest.status required")
    if data.get("includeMemberAccounts") is not None:
        out["include_member_accounts"] = data["includeMemberAccounts"]
    else:
        out["include_member_accounts"] = False
    return out
