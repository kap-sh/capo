"""Generated from Smithy shape ``com.amazonaws.signin#BatchRevokeSessionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_signin.types.batch_revoke_session_error_list
    import capo_signin.types.revoked_session_list


class BatchRevokeSessionsOutput(TypedDict, closed=True):
    revoked_sessions: "capo_signin.types.revoked_session_list.RevokedSessionList"
    """Sessions that were revoked"""
    errors: (
        "capo_signin.types.batch_revoke_session_error_list.BatchRevokeSessionErrorList"
    )
    """Sessions that could not be revoked"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchRevokeSessionsOutput) -> dict:
    out: dict = {}
    import capo_signin.types.revoked_session_list

    out["revokedSessions"] = capo_signin.types.revoked_session_list.serialize_json(
        value["revoked_sessions"]
    )
    import capo_signin.types.batch_revoke_session_error_list

    out["errors"] = capo_signin.types.batch_revoke_session_error_list.serialize_json(
        value["errors"]
    )
    return out


def deserialize_json(data: dict) -> BatchRevokeSessionsOutput:
    out: BatchRevokeSessionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("revokedSessions") is not None:
        import capo_signin.types.revoked_session_list

        out["revoked_sessions"] = (
            capo_signin.types.revoked_session_list.deserialize_json(
                data["revokedSessions"]
            )
        )
    else:
        out["revoked_sessions"] = []
    if data.get("errors") is not None:
        import capo_signin.types.batch_revoke_session_error_list

        out["errors"] = (
            capo_signin.types.batch_revoke_session_error_list.deserialize_json(
                data["errors"]
            )
        )
    else:
        out["errors"] = []
    return out
