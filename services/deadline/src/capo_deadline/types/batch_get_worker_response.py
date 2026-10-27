"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetWorkerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.batch_get_worker_errors
    import capo_deadline.types.batch_get_worker_items


class BatchGetWorkerResponse(TypedDict, closed=True):
    workers: "capo_deadline.types.batch_get_worker_items.BatchGetWorkerItems"
    """A list of workers that were successfully retrieved."""
    errors: "capo_deadline.types.batch_get_worker_errors.BatchGetWorkerErrors"
    """A list of errors for workers that could not be retrieved."""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetWorkerResponse) -> dict:
    out: dict = {}
    import capo_deadline.types.batch_get_worker_items

    out["workers"] = capo_deadline.types.batch_get_worker_items.serialize_json(
        value["workers"]
    )
    import capo_deadline.types.batch_get_worker_errors

    out["errors"] = capo_deadline.types.batch_get_worker_errors.serialize_json(
        value["errors"]
    )
    return out


def deserialize_json(data: dict) -> BatchGetWorkerResponse:
    out: BatchGetWorkerResponse = {}  # type: ignore[typeddict-item]
    if data.get("workers") is not None:
        import capo_deadline.types.batch_get_worker_items

        out["workers"] = capo_deadline.types.batch_get_worker_items.deserialize_json(
            data["workers"]
        )
    else:
        out["workers"] = []
    if data.get("errors") is not None:
        import capo_deadline.types.batch_get_worker_errors

        out["errors"] = capo_deadline.types.batch_get_worker_errors.deserialize_json(
            data["errors"]
        )
    else:
        out["errors"] = []
    return out
