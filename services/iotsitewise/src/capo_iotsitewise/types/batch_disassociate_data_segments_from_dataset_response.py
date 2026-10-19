"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchDisassociateDataSegmentsFromDatasetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.failed_data_segment_disassociations
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.version


class BatchDisassociateDataSegmentsFromDatasetResponse(TypedDict, closed=True):
    dataset_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the dataset.</p>"""
    dataset_version: "capo_iotsitewise.types.version.Version"
    """<p>The version of the dataset after disassociation.</p>"""
    failed_disassociations: "capo_iotsitewise.types.failed_data_segment_disassociations.FailedDataSegmentDisassociations"
    """<p>A list of data segment disassociations that failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDisassociateDataSegmentsFromDatasetResponse) -> dict:
    out: dict = {}
    out["datasetId"] = value["dataset_id"]
    out["datasetVersion"] = value["dataset_version"]
    import capo_iotsitewise.types.failed_data_segment_disassociations

    out["failedDisassociations"] = (
        capo_iotsitewise.types.failed_data_segment_disassociations.serialize_json(
            value["failed_disassociations"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchDisassociateDataSegmentsFromDatasetResponse:
    out: BatchDisassociateDataSegmentsFromDatasetResponse = {}  # type: ignore[typeddict-item]
    if data.get("datasetId") is not None:
        out["dataset_id"] = data["datasetId"]
    else:
        out["dataset_id"] = ""
    if data.get("datasetVersion") is not None:
        out["dataset_version"] = data["datasetVersion"]
    else:
        out["dataset_version"] = ""
    if data.get("failedDisassociations") is not None:
        import capo_iotsitewise.types.failed_data_segment_disassociations

        out["failed_disassociations"] = (
            capo_iotsitewise.types.failed_data_segment_disassociations.deserialize_json(
                data["failedDisassociations"]
            )
        )
    else:
        out["failed_disassociations"] = []
    return out
