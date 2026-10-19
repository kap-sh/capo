"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#CancelMetadataTransferJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iottwinmaker.types.id
    import capo_iottwinmaker.types.metadata_transfer_job_progress
    import capo_iottwinmaker.types.metadata_transfer_job_status
    import capo_iottwinmaker.types.timestamp
    import capo_iottwinmaker.types.twin_maker_arn


class CancelMetadataTransferJobResponse(TypedDict, closed=True):
    metadata_transfer_job_id: "capo_iottwinmaker.types.id.Id"
    """<p>The metadata transfer job Id.</p>"""
    arn: "capo_iottwinmaker.types.twin_maker_arn.TwinMakerArn"
    """<p>The metadata transfer job ARN.</p>"""
    update_date_time: "capo_iottwinmaker.types.timestamp.Timestamp"
    """<p>Used to update the DateTime property.</p>"""
    status: (
        "capo_iottwinmaker.types.metadata_transfer_job_status.MetadataTransferJobStatus"
    )
    """<p>The metadata transfer job's status.</p>"""
    progress: NotRequired[
        "capo_iottwinmaker.types.metadata_transfer_job_progress.MetadataTransferJobProgress"
    ]
    """<p>The metadata transfer job's progress.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelMetadataTransferJobResponse) -> dict:
    out: dict = {}
    out["metadataTransferJobId"] = value["metadata_transfer_job_id"]
    out["arn"] = value["arn"]
    import capo_iottwinmaker.types.timestamp

    out["updateDateTime"] = capo_iottwinmaker.types.timestamp.serialize_json(
        value["update_date_time"]
    )
    import capo_iottwinmaker.types.metadata_transfer_job_status

    out["status"] = capo_iottwinmaker.types.metadata_transfer_job_status.serialize_json(
        value["status"]
    )
    if "progress" in value:
        import capo_iottwinmaker.types.metadata_transfer_job_progress

        out["progress"] = (
            capo_iottwinmaker.types.metadata_transfer_job_progress.serialize_json(
                value["progress"]
            )
        )
    return out


def deserialize_json(data: dict) -> CancelMetadataTransferJobResponse:
    out: CancelMetadataTransferJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("metadataTransferJobId") is not None:
        out["metadata_transfer_job_id"] = data["metadataTransferJobId"]
    else:
        out["metadata_transfer_job_id"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("updateDateTime") is not None:
        import capo_iottwinmaker.types.timestamp

        out["update_date_time"] = capo_iottwinmaker.types.timestamp.deserialize_json(
            data["updateDateTime"]
        )
    else:
        import datetime

        out["update_date_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("status") is not None:
        import capo_iottwinmaker.types.metadata_transfer_job_status

        out["status"] = (
            capo_iottwinmaker.types.metadata_transfer_job_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("CancelMetadataTransferJobResponse.status required")
    if data.get("progress") is not None:
        import capo_iottwinmaker.types.metadata_transfer_job_progress

        out["progress"] = (
            capo_iottwinmaker.types.metadata_transfer_job_progress.deserialize_json(
                data["progress"]
            )
        )
    return out
