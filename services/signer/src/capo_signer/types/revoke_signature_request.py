"""Generated from Smithy shape ``com.amazonaws.signer#RevokeSignatureRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_signer.types.account_id
    import capo_signer.types.job_id
    import capo_signer.types.revocation_reason_string


class RevokeSignatureRequest(TypedDict, closed=True):
    job_id: "capo_signer.types.job_id.JobId"
    """<p>ID of the signing job to be revoked.</p>"""
    job_owner: NotRequired["capo_signer.types.account_id.AccountId"]
    """<p>AWS account ID of the job owner.</p>"""
    reason: "capo_signer.types.revocation_reason_string.RevocationReasonString"
    """<p>The reason for revoking the signing job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RevokeSignatureRequest) -> dict:
    out: dict = {}
    if "job_owner" in value:
        out["jobOwner"] = value["job_owner"]
    out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> RevokeSignatureRequest:
    out: RevokeSignatureRequest = {}  # type: ignore[typeddict-item]
    if data.get("jobOwner") is not None:
        out["job_owner"] = data["jobOwner"]
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    else:
        out["reason"] = ""
    return out
