"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchDeleteDatasetDataSegmentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.failed_data_segment_deletions
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.version


class BatchDeleteDatasetDataSegmentsResponse(TypedDict, closed=True):
    dataset_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the dataset.</p>"""
    dataset_version: "capo_iotsitewise.types.version.Version"
    """<p>The version of the dataset after deletion.</p>"""
    errors: "capo_iotsitewise.types.failed_data_segment_deletions.FailedDataSegmentDeletions"
    """<p>A list of data segment deletions that failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteDatasetDataSegmentsResponse) -> dict:
    out: dict = {}
    out["datasetId"] = value["dataset_id"]
    out["datasetVersion"] = value["dataset_version"]
    import capo_iotsitewise.types.failed_data_segment_deletions

    out["errors"] = capo_iotsitewise.types.failed_data_segment_deletions.serialize_json(
        value["errors"]
    )
    return out


def deserialize_json(data: dict) -> BatchDeleteDatasetDataSegmentsResponse:
    out: BatchDeleteDatasetDataSegmentsResponse = {}  # type: ignore[typeddict-item]
    if data.get("datasetId") is not None:
        out["dataset_id"] = data["datasetId"]
    else:
        out["dataset_id"] = ""
    if data.get("datasetVersion") is not None:
        out["dataset_version"] = data["datasetVersion"]
    else:
        out["dataset_version"] = ""
    if data.get("errors") is not None:
        import capo_iotsitewise.types.failed_data_segment_deletions

        out["errors"] = (
            capo_iotsitewise.types.failed_data_segment_deletions.deserialize_json(
                data["errors"]
            )
        )
    else:
        out["errors"] = []
    return out
