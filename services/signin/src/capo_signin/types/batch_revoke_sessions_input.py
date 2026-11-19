"""Generated from Smithy shape ``com.amazonaws.signin#BatchRevokeSessionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_signin.types.principal_arn_filter
    import capo_signin.types.revocation_reason
    import capo_signin.types.session_arn_list


class BatchRevokeSessionsInput(TypedDict, closed=True):
    principal_arn: NotRequired[
        "capo_signin.types.principal_arn_filter.PrincipalArnFilter"
    ]
    """The identity that owns the sessions. Omit to use the caller. Specify arn:aws:iam::{account-id}:* to revoke any session in the account."""
    session_arns: "capo_signin.types.session_arn_list.SessionArnList"
    """The ARNs of the sessions to revoke"""
    reason: NotRequired["capo_signin.types.revocation_reason.RevocationReason"]
    """The reason for revoking the sessions"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchRevokeSessionsInput) -> dict:
    out: dict = {}
    if "principal_arn" in value:
        out["principalArn"] = value["principal_arn"]
    import capo_signin.types.session_arn_list

    out["sessionArns"] = capo_signin.types.session_arn_list.serialize_json(
        value["session_arns"]
    )
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> BatchRevokeSessionsInput:
    out: BatchRevokeSessionsInput = {}  # type: ignore[typeddict-item]
    if data.get("principalArn") is not None:
        out["principal_arn"] = data["principalArn"]
    if data.get("sessionArns") is not None:
        import capo_signin.types.session_arn_list

        out["session_arns"] = capo_signin.types.session_arn_list.deserialize_json(
            data["sessionArns"]
        )
    else:
        out["session_arns"] = []
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    return out
