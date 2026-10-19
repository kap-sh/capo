"""Generated from Smithy shape ``com.amazonaws.deadline#UpdateSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.client_token
    import capo_deadline.types.farm_id
    import capo_deadline.types.job_id
    import capo_deadline.types.queue_id
    import capo_deadline.types.session_id
    import capo_deadline.types.session_lifecycle_target_status


class UpdateSessionRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """<p>The farm ID to update in the session.</p>"""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """<p>The queue ID to update in the session.</p>"""
    job_id: "capo_deadline.types.job_id.JobId"
    """<p>The job ID to update in the session.</p>"""
    session_id: "capo_deadline.types.session_id.SessionId"
    """<p>The session ID to update.</p>"""
    client_token: NotRequired["capo_deadline.types.client_token.ClientToken"]
    """<p>The unique token which the server uses to recognize retries of the same request.</p>"""
    target_lifecycle_status: "capo_deadline.types.session_lifecycle_target_status.SessionLifecycleTargetStatus"
    """<p>The life cycle status to update in the session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSessionRequest) -> dict:
    out: dict = {}
    import capo_deadline.types.session_lifecycle_target_status

    out["targetLifecycleStatus"] = (
        capo_deadline.types.session_lifecycle_target_status.serialize_json(
            value["target_lifecycle_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateSessionRequest:
    out: UpdateSessionRequest = {}  # type: ignore[typeddict-item]
    if data.get("targetLifecycleStatus") is not None:
        import capo_deadline.types.session_lifecycle_target_status

        out["target_lifecycle_status"] = (
            capo_deadline.types.session_lifecycle_target_status.deserialize_json(
                data["targetLifecycleStatus"]
            )
        )
    else:
        import typing

        out["target_lifecycle_status"] = typing.cast(
            "capo_deadline.types.session_lifecycle_target_status.SessionLifecycleTargetStatus",
            "",
        )
    return out
