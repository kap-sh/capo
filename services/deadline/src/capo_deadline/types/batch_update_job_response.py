"""Generated from Smithy shape ``com.amazonaws.deadline#BatchUpdateJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.batch_update_job_errors


class BatchUpdateJobResponse(TypedDict, closed=True):
    errors: "capo_deadline.types.batch_update_job_errors.BatchUpdateJobErrors"
    """<p>A list of errors for jobs that could not be updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateJobResponse) -> dict:
    out: dict = {}
    import capo_deadline.types.batch_update_job_errors

    out["errors"] = capo_deadline.types.batch_update_job_errors.serialize_json(
        value["errors"]
    )
    return out


def deserialize_json(data: dict) -> BatchUpdateJobResponse:
    out: BatchUpdateJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("errors") is not None:
        import capo_deadline.types.batch_update_job_errors

        out["errors"] = capo_deadline.types.batch_update_job_errors.deserialize_json(
            data["errors"]
        )
    else:
        out["errors"] = []
    return out
