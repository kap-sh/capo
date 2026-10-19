"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetWorkerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.batch_get_worker_identifiers


class BatchGetWorkerRequest(TypedDict, closed=True):
    identifiers: (
        "capo_deadline.types.batch_get_worker_identifiers.BatchGetWorkerIdentifiers"
    )
    """<p>The list of worker identifiers to retrieve. You can specify up to 100 identifiers per request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetWorkerRequest) -> dict:
    out: dict = {}
    import capo_deadline.types.batch_get_worker_identifiers

    out["identifiers"] = (
        capo_deadline.types.batch_get_worker_identifiers.serialize_json(
            value["identifiers"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetWorkerRequest:
    out: BatchGetWorkerRequest = {}  # type: ignore[typeddict-item]
    if data.get("identifiers") is not None:
        import capo_deadline.types.batch_get_worker_identifiers

        out["identifiers"] = (
            capo_deadline.types.batch_get_worker_identifiers.deserialize_json(
                data["identifiers"]
            )
        )
    else:
        out["identifiers"] = []
    return out
