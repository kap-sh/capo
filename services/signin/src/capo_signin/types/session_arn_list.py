"""Generated from Smithy shape ``com.amazonaws.signin#SessionArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_signin.types.session_arn

SessionArnList: TypeAlias = list["capo_signin.types.session_arn.SessionArn"]


# --- restJson1 ser/de ---
def serialize_json(value: SessionArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> SessionArnList:
    return [item for item in data if item is not None]
