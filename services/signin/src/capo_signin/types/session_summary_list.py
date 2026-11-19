"""Generated from Smithy shape ``com.amazonaws.signin#SessionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_signin.types.session

SessionSummaryList: TypeAlias = list["capo_signin.types.session.Session"]


# --- restJson1 ser/de ---
def serialize_json(value: SessionSummaryList) -> list:
    import capo_signin.types.session

    out: list = []
    for item in value:
        out.append(capo_signin.types.session.serialize_json(item))
    return out


def deserialize_json(data: list) -> SessionSummaryList:
    import capo_signin.types.session

    out: SessionSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_signin.types.session.deserialize_json(item))
    return out
