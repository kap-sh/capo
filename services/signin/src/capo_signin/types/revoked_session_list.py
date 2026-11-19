"""Generated from Smithy shape ``com.amazonaws.signin#RevokedSessionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_signin.types.revoked_session

RevokedSessionList: TypeAlias = list["capo_signin.types.revoked_session.RevokedSession"]


# --- restJson1 ser/de ---
def serialize_json(value: RevokedSessionList) -> list:
    import capo_signin.types.revoked_session

    out: list = []
    for item in value:
        out.append(capo_signin.types.revoked_session.serialize_json(item))
    return out


def deserialize_json(data: list) -> RevokedSessionList:
    import capo_signin.types.revoked_session

    out: RevokedSessionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_signin.types.revoked_session.deserialize_json(item))
    return out
