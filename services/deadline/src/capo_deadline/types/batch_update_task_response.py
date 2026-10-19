"""Generated from Smithy shape ``com.amazonaws.deadline#BatchUpdateTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.batch_update_task_errors


class BatchUpdateTaskResponse(TypedDict, closed=True):
    errors: "capo_deadline.types.batch_update_task_errors.BatchUpdateTaskErrors"
    """<p>A list of errors for tasks that could not be updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateTaskResponse) -> dict:
    out: dict = {}
    import capo_deadline.types.batch_update_task_errors

    out["errors"] = capo_deadline.types.batch_update_task_errors.serialize_json(
        value["errors"]
    )
    return out


def deserialize_json(data: dict) -> BatchUpdateTaskResponse:
    out: BatchUpdateTaskResponse = {}  # type: ignore[typeddict-item]
    if data.get("errors") is not None:
        import capo_deadline.types.batch_update_task_errors

        out["errors"] = capo_deadline.types.batch_update_task_errors.deserialize_json(
            data["errors"]
        )
    else:
        out["errors"] = []
    return out
