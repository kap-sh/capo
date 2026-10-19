"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#CreateMetadataTransferJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iottwinmaker.types.id
    import capo_iottwinmaker.types.metadata_transfer_job_status
    import capo_iottwinmaker.types.timestamp
    import capo_iottwinmaker.types.twin_maker_arn


class CreateMetadataTransferJobResponse(TypedDict, closed=True):
    metadata_transfer_job_id: "capo_iottwinmaker.types.id.Id"
    """<p>The metadata transfer job Id.</p>"""
    arn: "capo_iottwinmaker.types.twin_maker_arn.TwinMakerArn"
    """<p>The metadata transfer job ARN.</p>"""
    creation_date_time: "capo_iottwinmaker.types.timestamp.Timestamp"
    """<p>The The metadata transfer job creation DateTime property.</p>"""
    status: (
        "capo_iottwinmaker.types.metadata_transfer_job_status.MetadataTransferJobStatus"
    )
    """<p>The metadata transfer job response status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMetadataTransferJobResponse) -> dict:
    out: dict = {}
    out["metadataTransferJobId"] = value["metadata_transfer_job_id"]
    out["arn"] = value["arn"]
    import capo_iottwinmaker.types.timestamp

    out["creationDateTime"] = capo_iottwinmaker.types.timestamp.serialize_json(
        value["creation_date_time"]
    )
    import capo_iottwinmaker.types.metadata_transfer_job_status

    out["status"] = capo_iottwinmaker.types.metadata_transfer_job_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> CreateMetadataTransferJobResponse:
    out: CreateMetadataTransferJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("metadataTransferJobId") is not None:
        out["metadata_transfer_job_id"] = data["metadataTransferJobId"]
    else:
        out["metadata_transfer_job_id"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("creationDateTime") is not None:
        import capo_iottwinmaker.types.timestamp

        out["creation_date_time"] = capo_iottwinmaker.types.timestamp.deserialize_json(
            data["creationDateTime"]
        )
    else:
        import datetime

        out["creation_date_time"] = datetime.datetime.fromtimestamp(
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
        raise DeserializationError("CreateMetadataTransferJobResponse.status required")
    return out
