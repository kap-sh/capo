"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#GetEnrollmentStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.last_updated_timestamp
    import capo_compute_optimizer.types.member_accounts_enrolled
    import capo_compute_optimizer.types.number_of_member_accounts_opted_in
    import capo_compute_optimizer.types.status
    import capo_compute_optimizer.types.status_reason


class GetEnrollmentStatusResponse(TypedDict, closed=True):
    status: NotRequired["capo_compute_optimizer.types.status.Status"]
    """<p>The enrollment status of the account.</p>"""
    status_reason: NotRequired[
        "capo_compute_optimizer.types.status_reason.StatusReason"
    ]
    """<p>The reason for the enrollment status of the account.</p> <p>For example, an account might show a status of <code>Pending</code> because member accounts of an organization require more time to be enrolled in the service.</p>"""
    member_accounts_enrolled: (
        "capo_compute_optimizer.types.member_accounts_enrolled.MemberAccountsEnrolled"
    )
    """<p>Confirms the enrollment status of member accounts of the organization, if the account is a management account of an organization.</p>"""
    last_updated_timestamp: NotRequired[
        "capo_compute_optimizer.types.last_updated_timestamp.LastUpdatedTimestamp"
    ]
    """<p>The Unix epoch timestamp, in seconds, of when the account enrollment status was last updated.</p>"""
    number_of_member_accounts_opted_in: NotRequired[
        "capo_compute_optimizer.types.number_of_member_accounts_opted_in.NumberOfMemberAccountsOptedIn"
    ]
    """<p>The count of organization member accounts that are opted in to the service, if your account is an organization management account.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetEnrollmentStatusResponse) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_compute_optimizer.types.status

        out["status"] = capo_compute_optimizer.types.status.serialize_aws_json_1_0(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    out["memberAccountsEnrolled"] = value.get("member_accounts_enrolled", False)
    if "last_updated_timestamp" in value:
        import capo_compute_optimizer.types.last_updated_timestamp

        out["lastUpdatedTimestamp"] = (
            capo_compute_optimizer.types.last_updated_timestamp.serialize_aws_json_1_0(
                value["last_updated_timestamp"]
            )
        )
    if "number_of_member_accounts_opted_in" in value:
        out["numberOfMemberAccountsOptedIn"] = value[
            "number_of_member_accounts_opted_in"
        ]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetEnrollmentStatusResponse:
    out: GetEnrollmentStatusResponse = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_compute_optimizer.types.status

        out["status"] = capo_compute_optimizer.types.status.deserialize_aws_json_1_0(
            data["status"]
        )
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("memberAccountsEnrolled") is not None:
        out["member_accounts_enrolled"] = data["memberAccountsEnrolled"]
    else:
        out["member_accounts_enrolled"] = False
    if data.get("lastUpdatedTimestamp") is not None:
        import capo_compute_optimizer.types.last_updated_timestamp

        out["last_updated_timestamp"] = (
            capo_compute_optimizer.types.last_updated_timestamp.deserialize_aws_json_1_0(
                data["lastUpdatedTimestamp"]
            )
        )
    if data.get("numberOfMemberAccountsOptedIn") is not None:
        out["number_of_member_accounts_opted_in"] = data[
            "numberOfMemberAccountsOptedIn"
        ]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetEnrollmentStatusResponse) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_compute_optimizer.types.status

        out["status"] = capo_compute_optimizer.types.status.serialize_cbor(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    out["memberAccountsEnrolled"] = value.get("member_accounts_enrolled", False)
    if "last_updated_timestamp" in value:
        import capo_compute_optimizer.types.last_updated_timestamp

        out["lastUpdatedTimestamp"] = (
            capo_compute_optimizer.types.last_updated_timestamp.serialize_cbor(
                value["last_updated_timestamp"]
            )
        )
    if "number_of_member_accounts_opted_in" in value:
        out["numberOfMemberAccountsOptedIn"] = value[
            "number_of_member_accounts_opted_in"
        ]
    return out


def deserialize_cbor(data: dict) -> GetEnrollmentStatusResponse:
    out: GetEnrollmentStatusResponse = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_compute_optimizer.types.status

        out["status"] = capo_compute_optimizer.types.status.deserialize_cbor(
            data["status"]
        )
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("memberAccountsEnrolled") is not None:
        out["member_accounts_enrolled"] = data["memberAccountsEnrolled"]
    else:
        out["member_accounts_enrolled"] = False
    if data.get("lastUpdatedTimestamp") is not None:
        import capo_compute_optimizer.types.last_updated_timestamp

        out["last_updated_timestamp"] = (
            capo_compute_optimizer.types.last_updated_timestamp.deserialize_cbor(
                data["lastUpdatedTimestamp"]
            )
        )
    if data.get("numberOfMemberAccountsOptedIn") is not None:
        out["number_of_member_accounts_opted_in"] = data[
            "numberOfMemberAccountsOptedIn"
        ]
    return out
