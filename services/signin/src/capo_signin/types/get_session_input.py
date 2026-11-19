"""Generated from Smithy shape ``com.amazonaws.signin#GetSessionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_signin.types.principal_arn_filter
    import capo_signin.types.session_arn


class GetSessionInput(TypedDict, closed=True):
    session_arn: "capo_signin.types.session_arn.SessionArn"
    """The ARN of the session to retrieve"""
    principal_arn: NotRequired[
        "capo_signin.types.principal_arn_filter.PrincipalArnFilter"
    ]
    """The identity that owns the session. Omit to use the caller. Specify arn:aws:iam::{account-id}:* to retrieve any session in the account."""


# --- restJson1 ser/de ---
def serialize_json(value: GetSessionInput) -> dict:
    out: dict = {}
    out["sessionArn"] = value["session_arn"]
    if "principal_arn" in value:
        out["principalArn"] = value["principal_arn"]
    return out


def deserialize_json(data: dict) -> GetSessionInput:
    out: GetSessionInput = {}  # type: ignore[typeddict-item]
    if data.get("sessionArn") is not None:
        out["session_arn"] = data["sessionArn"]
    else:
        out["session_arn"] = ""
    if data.get("principalArn") is not None:
        out["principal_arn"] = data["principalArn"]
    return out
