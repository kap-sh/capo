"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#UpdateEnrollmentStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.status
    import capo_compute_optimizer.types.status_reason


class UpdateEnrollmentStatusResponse(TypedDict, closed=True):
    status: NotRequired["capo_compute_optimizer.types.status.Status"]
    """<p>The enrollment status of the account.</p>"""
    status_reason: NotRequired[
        "capo_compute_optimizer.types.status_reason.StatusReason"
    ]
    """<p>The reason for the enrollment status of the account. For example, an account might show a status of <code>Pending</code> because member accounts of an organization require more time to be enrolled in the service.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateEnrollmentStatusResponse) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_compute_optimizer.types.status

        out["status"] = capo_compute_optimizer.types.status.serialize_aws_json_1_0(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateEnrollmentStatusResponse:
    out: UpdateEnrollmentStatusResponse = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_compute_optimizer.types.status

        out["status"] = capo_compute_optimizer.types.status.deserialize_aws_json_1_0(
            data["status"]
        )
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateEnrollmentStatusResponse) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_compute_optimizer.types.status

        out["status"] = capo_compute_optimizer.types.status.serialize_cbor(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    return out


def deserialize_cbor(data: dict) -> UpdateEnrollmentStatusResponse:
    out: UpdateEnrollmentStatusResponse = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_compute_optimizer.types.status

        out["status"] = capo_compute_optimizer.types.status.deserialize_cbor(
            data["status"]
        )
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    return out
