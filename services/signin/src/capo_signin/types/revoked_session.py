"""Generated from Smithy shape ``com.amazonaws.signin#RevokedSession``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_signin.types.session_arn


class RevokedSession(TypedDict, closed=True):
    session_arn: "capo_signin.types.session_arn.SessionArn"
    """The revoked session ARN"""


# --- restJson1 ser/de ---
def serialize_json(value: RevokedSession) -> dict:
    out: dict = {}
    out["sessionArn"] = value["session_arn"]
    return out


def deserialize_json(data: dict) -> RevokedSession:
    out: RevokedSession = {}  # type: ignore[typeddict-item]
    if data.get("sessionArn") is not None:
        out["session_arn"] = data["sessionArn"]
    else:
        out["session_arn"] = ""
    return out
