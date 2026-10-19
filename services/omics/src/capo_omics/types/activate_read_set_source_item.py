"""Generated from Smithy shape ``com.amazonaws.omics#ActivateReadSetSourceItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.job_status_message
    import capo_omics.types.read_set_activation_job_item_status
    import capo_omics.types.read_set_id


class ActivateReadSetSourceItem(TypedDict, closed=True):
    read_set_id: "capo_omics.types.read_set_id.ReadSetId"
    """<p>The source's read set ID.</p>"""
    status: "capo_omics.types.read_set_activation_job_item_status.ReadSetActivationJobItemStatus"
    """<p>The source's status.</p>"""
    status_message: NotRequired["capo_omics.types.job_status_message.JobStatusMessage"]
    """<p>The source's status message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActivateReadSetSourceItem) -> dict:
    out: dict = {}
    out["readSetId"] = value["read_set_id"]
    out["status"] = value["status"]
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    return out


def deserialize_json(data: dict) -> ActivateReadSetSourceItem:
    out: ActivateReadSetSourceItem = {}  # type: ignore[typeddict-item]
    if data.get("readSetId") is not None:
        out["read_set_id"] = data["readSetId"]
    else:
        out["read_set_id"] = ""
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("statusMessage") is not None:
        out["status_message"] = data["statusMessage"]
    return out
