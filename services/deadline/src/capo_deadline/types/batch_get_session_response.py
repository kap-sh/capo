"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetSessionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.batch_get_session_errors
    import capo_deadline.types.batch_get_session_items


class BatchGetSessionResponse(TypedDict, closed=True):
    sessions: "capo_deadline.types.batch_get_session_items.BatchGetSessionItems"
    """A list of sessions that were successfully retrieved."""
    errors: "capo_deadline.types.batch_get_session_errors.BatchGetSessionErrors"
    """A list of errors for sessions that could not be retrieved."""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetSessionResponse) -> dict:
    out: dict = {}
    import capo_deadline.types.batch_get_session_items

    out["sessions"] = capo_deadline.types.batch_get_session_items.serialize_json(
        value["sessions"]
    )
    import capo_deadline.types.batch_get_session_errors

    out["errors"] = capo_deadline.types.batch_get_session_errors.serialize_json(
        value["errors"]
    )
    return out


def deserialize_json(data: dict) -> BatchGetSessionResponse:
    out: BatchGetSessionResponse = {}  # type: ignore[typeddict-item]
    if data.get("sessions") is not None:
        import capo_deadline.types.batch_get_session_items

        out["sessions"] = capo_deadline.types.batch_get_session_items.deserialize_json(
            data["sessions"]
        )
    else:
        out["sessions"] = []
    if data.get("errors") is not None:
        import capo_deadline.types.batch_get_session_errors

        out["errors"] = capo_deadline.types.batch_get_session_errors.deserialize_json(
            data["errors"]
        )
    else:
        out["errors"] = []
    return out
