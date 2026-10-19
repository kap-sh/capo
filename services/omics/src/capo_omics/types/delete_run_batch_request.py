"""Generated from Smithy shape ``com.amazonaws.omics#DeleteRunBatchRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_omics.types.batch_id


class DeleteRunBatchRequest(TypedDict, closed=True):
    batch_id: "capo_omics.types.batch_id.BatchId"
    """<p>The identifier portion of the run batch ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRunBatchRequest) -> dict:
    out: dict = {}
    out["batchId"] = value["batch_id"]
    return out


def deserialize_json(data: dict) -> DeleteRunBatchRequest:
    out: DeleteRunBatchRequest = {}  # type: ignore[typeddict-item]
    if data.get("batchId") is not None:
        out["batch_id"] = data["batchId"]
    else:
        out["batch_id"] = ""
    return out
