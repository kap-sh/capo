"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#GetEnrollmentStatusesForOrganizationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.account_enrollment_statuses
    import capo_compute_optimizer.types.next_token


class GetEnrollmentStatusesForOrganizationResponse(TypedDict, closed=True):
    account_enrollment_statuses: NotRequired[
        "capo_compute_optimizer.types.account_enrollment_statuses.AccountEnrollmentStatuses"
    ]
    """<p>An array of objects that describe the enrollment statuses of organization member accounts.</p>"""
    next_token: NotRequired["capo_compute_optimizer.types.next_token.NextToken"]
    """<p>The token to use to advance to the next page of account enrollment statuses.</p> <p>This value is null when there are no more pages of account enrollment statuses to return.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetEnrollmentStatusesForOrganizationResponse) -> dict:
    out: dict = {}
    if "account_enrollment_statuses" in value:
        import capo_compute_optimizer.types.account_enrollment_statuses

        out["accountEnrollmentStatuses"] = (
            capo_compute_optimizer.types.account_enrollment_statuses.serialize_aws_json_1_0(
                value["account_enrollment_statuses"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> GetEnrollmentStatusesForOrganizationResponse:
    out: GetEnrollmentStatusesForOrganizationResponse = {}  # type: ignore[typeddict-item]
    if data.get("accountEnrollmentStatuses") is not None:
        import capo_compute_optimizer.types.account_enrollment_statuses

        out["account_enrollment_statuses"] = (
            capo_compute_optimizer.types.account_enrollment_statuses.deserialize_aws_json_1_0(
                data["accountEnrollmentStatuses"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetEnrollmentStatusesForOrganizationResponse) -> dict:
    out: dict = {}
    if "account_enrollment_statuses" in value:
        import capo_compute_optimizer.types.account_enrollment_statuses

        out["accountEnrollmentStatuses"] = (
            capo_compute_optimizer.types.account_enrollment_statuses.serialize_cbor(
                value["account_enrollment_statuses"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> GetEnrollmentStatusesForOrganizationResponse:
    out: GetEnrollmentStatusesForOrganizationResponse = {}  # type: ignore[typeddict-item]
    if data.get("accountEnrollmentStatuses") is not None:
        import capo_compute_optimizer.types.account_enrollment_statuses

        out["account_enrollment_statuses"] = (
            capo_compute_optimizer.types.account_enrollment_statuses.deserialize_cbor(
                data["accountEnrollmentStatuses"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
