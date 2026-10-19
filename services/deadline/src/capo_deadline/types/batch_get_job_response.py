"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetJobResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.batch_get_job_errors
    import capo_deadline.types.batch_get_job_items


class BatchGetJobResponse(TypedDict, closed=True):
    jobs: "capo_deadline.types.batch_get_job_items.BatchGetJobItems"
    """<p>A list of jobs that were successfully retrieved.</p>"""
    errors: "capo_deadline.types.batch_get_job_errors.BatchGetJobErrors"
    """<p>A list of errors for jobs that could not be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetJobResponse) -> dict:
    out: dict = {}
    import capo_deadline.types.batch_get_job_items

    out["jobs"] = capo_deadline.types.batch_get_job_items.serialize_json(value["jobs"])
    import capo_deadline.types.batch_get_job_errors

    out["errors"] = capo_deadline.types.batch_get_job_errors.serialize_json(
        value["errors"]
    )
    return out


def deserialize_json(data: dict) -> BatchGetJobResponse:
    out: BatchGetJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("jobs") is not None:
        import capo_deadline.types.batch_get_job_items

        out["jobs"] = capo_deadline.types.batch_get_job_items.deserialize_json(
            data["jobs"]
        )
    else:
        out["jobs"] = []
    if data.get("errors") is not None:
        import capo_deadline.types.batch_get_job_errors

        out["errors"] = capo_deadline.types.batch_get_job_errors.deserialize_json(
            data["errors"]
        )
    else:
        out["errors"] = []
    return out


def redact_sensitive(value: BatchGetJobResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "jobs" in value:
        import capo_deadline.types.batch_get_job_items

        out["jobs"] = capo_deadline.types.batch_get_job_items.redact_sensitive(
            value["jobs"]
        )
    return out
