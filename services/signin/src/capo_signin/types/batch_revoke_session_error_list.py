"""Generated from Smithy shape ``com.amazonaws.signin#BatchRevokeSessionErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_signin.types.batch_revoke_session_error

BatchRevokeSessionErrorList: TypeAlias = list[
    "capo_signin.types.batch_revoke_session_error.BatchRevokeSessionError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchRevokeSessionErrorList) -> list:
    import capo_signin.types.batch_revoke_session_error

    out: list = []
    for item in value:
        out.append(capo_signin.types.batch_revoke_session_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchRevokeSessionErrorList:
    import capo_signin.types.batch_revoke_session_error

    out: BatchRevokeSessionErrorList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_signin.types.batch_revoke_session_error.deserialize_json(item))
    return out
