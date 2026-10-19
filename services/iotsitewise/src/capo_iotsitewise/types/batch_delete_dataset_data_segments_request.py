"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchDeleteDatasetDataSegmentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.client_token
    import capo_iotsitewise.types.delete_data_segment_entries
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.workspace_name


class BatchDeleteDatasetDataSegmentsRequest(TypedDict, closed=True):
    dataset_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the session dataset from which to delete data segments.</p>"""
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the workspace that contains the dataset.</p>"""
    delete_data_segment_entries: (
        "capo_iotsitewise.types.delete_data_segment_entries.DeleteDataSegmentEntries"
    )
    """<p>The list of data segment entries to delete.</p>"""
    client_token: NotRequired["capo_iotsitewise.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure that the request is idempotent. If you retry a request that completed successfully using the same client token, the retry succeeds without performing any further actions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteDatasetDataSegmentsRequest) -> dict:
    out: dict = {}
    out["workspaceName"] = value["workspace_name"]
    import capo_iotsitewise.types.delete_data_segment_entries

    out["deleteDataSegmentEntries"] = (
        capo_iotsitewise.types.delete_data_segment_entries.serialize_json(
            value["delete_data_segment_entries"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> BatchDeleteDatasetDataSegmentsRequest:
    out: BatchDeleteDatasetDataSegmentsRequest = {}  # type: ignore[typeddict-item]
    if data.get("workspaceName") is not None:
        out["workspace_name"] = data["workspaceName"]
    else:
        out["workspace_name"] = ""
    if data.get("deleteDataSegmentEntries") is not None:
        import capo_iotsitewise.types.delete_data_segment_entries

        out["delete_data_segment_entries"] = (
            capo_iotsitewise.types.delete_data_segment_entries.deserialize_json(
                data["deleteDataSegmentEntries"]
            )
        )
    else:
        out["delete_data_segment_entries"] = []
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
