"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.batch_get_task_identifiers


class BatchGetTaskRequest(TypedDict, closed=True):
    identifiers: (
        "capo_deadline.types.batch_get_task_identifiers.BatchGetTaskIdentifiers"
    )
    """<p>The list of task identifiers to retrieve. You can specify up to 100 identifiers per request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetTaskRequest) -> dict:
    out: dict = {}
    import capo_deadline.types.batch_get_task_identifiers

    out["identifiers"] = capo_deadline.types.batch_get_task_identifiers.serialize_json(
        value["identifiers"]
    )
    return out


def deserialize_json(data: dict) -> BatchGetTaskRequest:
    out: BatchGetTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("identifiers") is not None:
        import capo_deadline.types.batch_get_task_identifiers

        out["identifiers"] = (
            capo_deadline.types.batch_get_task_identifiers.deserialize_json(
                data["identifiers"]
            )
        )
    else:
        out["identifiers"] = []
    return out
