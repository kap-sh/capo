"""Generated from Smithy shape ``com.amazonaws.signin#BatchRevokeSessionError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_signin.types.session_arn


class BatchRevokeSessionError(TypedDict, closed=True):
    session_arn: "capo_signin.types.session_arn.SessionArn"
    """The session ARN"""
    code: "str"
    """The error code"""
    message: "str"
    """The error message"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchRevokeSessionError) -> dict:
    out: dict = {}
    out["sessionArn"] = value["session_arn"]
    out["code"] = value["code"]
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BatchRevokeSessionError:
    out: BatchRevokeSessionError = {}  # type: ignore[typeddict-item]
    if data.get("sessionArn") is not None:
        out["session_arn"] = data["sessionArn"]
    else:
        out["session_arn"] = ""
    if data.get("code") is not None:
        out["code"] = data["code"]
    else:
        out["code"] = ""
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out
