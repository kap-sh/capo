"""Generated from Smithy shape ``com.amazonaws.mturk#DeleteWorkerBlockRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mturk.types.customer_id
    import capo_mturk.types.string


class DeleteWorkerBlockRequest(TypedDict, closed=True):
    worker_id: "capo_mturk.types.customer_id.CustomerId"
    """<p>The ID of the Worker to unblock.</p>"""
    reason: NotRequired["capo_mturk.types.string.String"]
    """<p>A message that explains the reason for unblocking the Worker. The Worker does not see this message.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteWorkerBlockRequest) -> dict:
    out: dict = {}
    out["WorkerId"] = value["worker_id"]
    if "reason" in value:
        out["Reason"] = value["reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteWorkerBlockRequest:
    out: DeleteWorkerBlockRequest = {}  # type: ignore[typeddict-item]
    if data.get("WorkerId") is not None:
        out["worker_id"] = data["WorkerId"]
    else:
        out["worker_id"] = ""
    if data.get("Reason") is not None:
        out["reason"] = data["Reason"]
    return out
