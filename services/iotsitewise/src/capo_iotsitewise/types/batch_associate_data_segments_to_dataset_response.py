"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchAssociateDataSegmentsToDatasetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.failed_data_segment_associations
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.version


class BatchAssociateDataSegmentsToDatasetResponse(TypedDict, closed=True):
    dataset_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the dataset.</p>"""
    dataset_version: "capo_iotsitewise.types.version.Version"
    """<p>The version of the dataset after association.</p>"""
    failed_associations: "capo_iotsitewise.types.failed_data_segment_associations.FailedDataSegmentAssociations"
    """<p>A list of data segment associations that failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchAssociateDataSegmentsToDatasetResponse) -> dict:
    out: dict = {}
    out["datasetId"] = value["dataset_id"]
    out["datasetVersion"] = value["dataset_version"]
    import capo_iotsitewise.types.failed_data_segment_associations

    out["failedAssociations"] = (
        capo_iotsitewise.types.failed_data_segment_associations.serialize_json(
            value["failed_associations"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchAssociateDataSegmentsToDatasetResponse:
    out: BatchAssociateDataSegmentsToDatasetResponse = {}  # type: ignore[typeddict-item]
    if data.get("datasetId") is not None:
        out["dataset_id"] = data["datasetId"]
    else:
        out["dataset_id"] = ""
    if data.get("datasetVersion") is not None:
        out["dataset_version"] = data["datasetVersion"]
    else:
        out["dataset_version"] = ""
    if data.get("failedAssociations") is not None:
        import capo_iotsitewise.types.failed_data_segment_associations

        out["failed_associations"] = (
            capo_iotsitewise.types.failed_data_segment_associations.deserialize_json(
                data["failedAssociations"]
            )
        )
    else:
        out["failed_associations"] = []
    return out
