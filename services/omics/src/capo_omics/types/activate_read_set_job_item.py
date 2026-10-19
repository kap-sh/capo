"""Generated from Smithy shape ``com.amazonaws.omics#ActivateReadSetJobItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_omics.types.activation_job_id
    import capo_omics.types.read_set_activation_job_status
    import capo_omics.types.sequence_store_id


class ActivateReadSetJobItem(TypedDict, closed=True):
    id: "capo_omics.types.activation_job_id.ActivationJobId"
    """<p>The job's ID.</p>"""
    sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId"
    """<p>The job's sequence store ID.</p>"""
    status: "capo_omics.types.read_set_activation_job_status.ReadSetActivationJobStatus"
    """<p>The job's status.</p>"""
    creation_time: "datetime.datetime"
    """<p>When the job was created.</p>"""
    completion_time: NotRequired["datetime.datetime"]
    """<p>When the job completed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActivateReadSetJobItem) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["sequenceStoreId"] = value["sequence_store_id"]
    out["status"] = value["status"]
    import capo_omics._protocol.serialize

    out["creationTime"] = capo_omics._protocol.serialize.fmt_date_time(
        value["creation_time"]
    )
    if "completion_time" in value:
        import capo_omics._protocol.serialize

        out["completionTime"] = capo_omics._protocol.serialize.fmt_date_time(
            value["completion_time"]
        )
    return out


def deserialize_json(data: dict) -> ActivateReadSetJobItem:
    out: ActivateReadSetJobItem = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("sequenceStoreId") is not None:
        out["sequence_store_id"] = data["sequenceStoreId"]
    else:
        out["sequence_store_id"] = ""
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("creationTime") is not None:
        import datetime

        out["creation_time"] = datetime.datetime.fromisoformat(
            data["creationTime"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["creation_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("completionTime") is not None:
        import datetime

        out["completion_time"] = datetime.datetime.fromisoformat(
            data["completionTime"].replace("Z", "+00:00")
        )
    return out
