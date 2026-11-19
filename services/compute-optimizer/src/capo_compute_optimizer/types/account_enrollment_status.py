"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#AccountEnrollmentStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.account_id
    import capo_compute_optimizer.types.last_updated_timestamp
    import capo_compute_optimizer.types.status
    import capo_compute_optimizer.types.status_reason


class AccountEnrollmentStatus(TypedDict, closed=True):
    account_id: NotRequired["capo_compute_optimizer.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID.</p>"""
    status: NotRequired["capo_compute_optimizer.types.status.Status"]
    """<p>The account enrollment status.</p>"""
    status_reason: NotRequired[
        "capo_compute_optimizer.types.status_reason.StatusReason"
    ]
    """<p>The reason for the account enrollment status.</p> <p>For example, an account might show a status of <code>Pending</code> because member accounts of an organization require more time to be enrolled in the service.</p>"""
    last_updated_timestamp: NotRequired[
        "capo_compute_optimizer.types.last_updated_timestamp.LastUpdatedTimestamp"
    ]
    """<p>The Unix epoch timestamp, in seconds, of when the account enrollment status was last updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccountEnrollmentStatus) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "status" in value:
        import capo_compute_optimizer.types.status

        out["status"] = capo_compute_optimizer.types.status.serialize_aws_json_1_0(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "last_updated_timestamp" in value:
        import capo_compute_optimizer.types.last_updated_timestamp

        out["lastUpdatedTimestamp"] = (
            capo_compute_optimizer.types.last_updated_timestamp.serialize_aws_json_1_0(
                value["last_updated_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AccountEnrollmentStatus:
    out: AccountEnrollmentStatus = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("status") is not None:
        import capo_compute_optimizer.types.status

        out["status"] = capo_compute_optimizer.types.status.deserialize_aws_json_1_0(
            data["status"]
        )
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("lastUpdatedTimestamp") is not None:
        import capo_compute_optimizer.types.last_updated_timestamp

        out["last_updated_timestamp"] = (
            capo_compute_optimizer.types.last_updated_timestamp.deserialize_aws_json_1_0(
                data["lastUpdatedTimestamp"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AccountEnrollmentStatus) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "status" in value:
        import capo_compute_optimizer.types.status

        out["status"] = capo_compute_optimizer.types.status.serialize_cbor(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "last_updated_timestamp" in value:
        import capo_compute_optimizer.types.last_updated_timestamp

        out["lastUpdatedTimestamp"] = (
            capo_compute_optimizer.types.last_updated_timestamp.serialize_cbor(
                value["last_updated_timestamp"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> AccountEnrollmentStatus:
    out: AccountEnrollmentStatus = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("status") is not None:
        import capo_compute_optimizer.types.status

        out["status"] = capo_compute_optimizer.types.status.deserialize_cbor(
            data["status"]
        )
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("lastUpdatedTimestamp") is not None:
        import capo_compute_optimizer.types.last_updated_timestamp

        out["last_updated_timestamp"] = (
            capo_compute_optimizer.types.last_updated_timestamp.deserialize_cbor(
                data["lastUpdatedTimestamp"]
            )
        )
    return out
