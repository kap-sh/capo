"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchAssociateDataSegmentsToDatasetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.associate_data_segment_entries
    import capo_iotsitewise.types.client_token
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.workspace_name


class BatchAssociateDataSegmentsToDatasetRequest(TypedDict, closed=True):
    dataset_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the curated dataset to associate data segments with.</p>"""
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the workspace that contains the dataset.</p>"""
    associate_data_segment_entries: "capo_iotsitewise.types.associate_data_segment_entries.AssociateDataSegmentEntries"
    """<p>The list of data segment entries to associate with the dataset.</p>"""
    client_token: NotRequired["capo_iotsitewise.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure that the request is idempotent. If you retry a request that completed successfully using the same client token, the retry succeeds without performing any further actions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchAssociateDataSegmentsToDatasetRequest) -> dict:
    out: dict = {}
    out["workspaceName"] = value["workspace_name"]
    import capo_iotsitewise.types.associate_data_segment_entries

    out["associateDataSegmentEntries"] = (
        capo_iotsitewise.types.associate_data_segment_entries.serialize_json(
            value["associate_data_segment_entries"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> BatchAssociateDataSegmentsToDatasetRequest:
    out: BatchAssociateDataSegmentsToDatasetRequest = {}  # type: ignore[typeddict-item]
    if data.get("workspaceName") is not None:
        out["workspace_name"] = data["workspaceName"]
    else:
        out["workspace_name"] = ""
    if data.get("associateDataSegmentEntries") is not None:
        import capo_iotsitewise.types.associate_data_segment_entries

        out["associate_data_segment_entries"] = (
            capo_iotsitewise.types.associate_data_segment_entries.deserialize_json(
                data["associateDataSegmentEntries"]
            )
        )
    else:
        out["associate_data_segment_entries"] = []
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
