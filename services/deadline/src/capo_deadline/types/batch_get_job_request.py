"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.batch_get_job_identifiers


class BatchGetJobRequest(TypedDict, closed=True):
    identifiers: "capo_deadline.types.batch_get_job_identifiers.BatchGetJobIdentifiers"
    """The list of job identifiers to retrieve. You can specify up to 100 identifiers per request."""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetJobRequest) -> dict:
    out: dict = {}
    import capo_deadline.types.batch_get_job_identifiers

    out["identifiers"] = capo_deadline.types.batch_get_job_identifiers.serialize_json(
        value["identifiers"]
    )
    return out


def deserialize_json(data: dict) -> BatchGetJobRequest:
    out: BatchGetJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("identifiers") is not None:
        import capo_deadline.types.batch_get_job_identifiers

        out["identifiers"] = (
            capo_deadline.types.batch_get_job_identifiers.deserialize_json(
                data["identifiers"]
            )
        )
    else:
        out["identifiers"] = []
    return out
