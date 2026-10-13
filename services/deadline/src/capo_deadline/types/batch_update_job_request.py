"""Generated from Smithy shape ``com.amazonaws.deadline#BatchUpdateJobRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.batch_update_job_items
    import capo_deadline.types.client_token


class BatchUpdateJobRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_deadline.types.client_token.ClientToken"]
    """<p>The unique token which the server uses to recognize retries of the same request.</p>"""
    jobs: "capo_deadline.types.batch_update_job_items.BatchUpdateJobItems"
    """<p>The list of jobs to update. You can specify up to 100 jobs per request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateJobRequest) -> dict:
    out: dict = {}
    import capo_deadline.types.batch_update_job_items

    out["jobs"] = capo_deadline.types.batch_update_job_items.serialize_json(
        value["jobs"]
    )
    return out


def deserialize_json(data: dict) -> BatchUpdateJobRequest:
    out: BatchUpdateJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("jobs") is not None:
        import capo_deadline.types.batch_update_job_items

        out["jobs"] = capo_deadline.types.batch_update_job_items.deserialize_json(
            data["jobs"]
        )
    else:
        raise DeserializationError("BatchUpdateJobRequest.jobs required")
    return out


def redact_sensitive(value: BatchUpdateJobRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "jobs" in value:
        import capo_deadline.types.batch_update_job_items

        out["jobs"] = capo_deadline.types.batch_update_job_items.redact_sensitive(
            value["jobs"]
        )
    return out
