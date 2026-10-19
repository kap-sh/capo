"""Generated from Smithy shape ``com.amazonaws.deadline#BatchUpdateTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.batch_update_task_items
    import capo_deadline.types.client_token


class BatchUpdateTaskRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_deadline.types.client_token.ClientToken"]
    """<p>The unique token which the server uses to recognize retries of the same request.</p>"""
    tasks: "capo_deadline.types.batch_update_task_items.BatchUpdateTaskItems"
    """<p>The list of tasks to update. You can specify up to 100 tasks per request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateTaskRequest) -> dict:
    out: dict = {}
    import capo_deadline.types.batch_update_task_items

    out["tasks"] = capo_deadline.types.batch_update_task_items.serialize_json(
        value["tasks"]
    )
    return out


def deserialize_json(data: dict) -> BatchUpdateTaskRequest:
    out: BatchUpdateTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("tasks") is not None:
        import capo_deadline.types.batch_update_task_items

        out["tasks"] = capo_deadline.types.batch_update_task_items.deserialize_json(
            data["tasks"]
        )
    else:
        out["tasks"] = []
    return out
