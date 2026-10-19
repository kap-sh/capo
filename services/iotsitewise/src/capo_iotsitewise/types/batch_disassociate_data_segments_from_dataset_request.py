"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchDisassociateDataSegmentsFromDatasetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.client_token
    import capo_iotsitewise.types.disassociate_data_segment_entries
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.workspace_name


class BatchDisassociateDataSegmentsFromDatasetRequest(TypedDict, closed=True):
    dataset_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the curated dataset to disassociate data segments from.</p>"""
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the workspace that contains the dataset.</p>"""
    disassociate_data_segment_entries: "capo_iotsitewise.types.disassociate_data_segment_entries.DisassociateDataSegmentEntries"
    """<p>The list of data segment entries to disassociate from the dataset.</p>"""
    client_token: NotRequired["capo_iotsitewise.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure that the request is idempotent. If you retry a request that completed successfully using the same client token, the retry succeeds without performing any further actions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDisassociateDataSegmentsFromDatasetRequest) -> dict:
    out: dict = {}
    out["workspaceName"] = value["workspace_name"]
    import capo_iotsitewise.types.disassociate_data_segment_entries

    out["disassociateDataSegmentEntries"] = (
        capo_iotsitewise.types.disassociate_data_segment_entries.serialize_json(
            value["disassociate_data_segment_entries"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> BatchDisassociateDataSegmentsFromDatasetRequest:
    out: BatchDisassociateDataSegmentsFromDatasetRequest = {}  # type: ignore[typeddict-item]
    if data.get("workspaceName") is not None:
        out["workspace_name"] = data["workspaceName"]
    else:
        out["workspace_name"] = ""
    if data.get("disassociateDataSegmentEntries") is not None:
        import capo_iotsitewise.types.disassociate_data_segment_entries

        out["disassociate_data_segment_entries"] = (
            capo_iotsitewise.types.disassociate_data_segment_entries.deserialize_json(
                data["disassociateDataSegmentEntries"]
            )
        )
    else:
        out["disassociate_data_segment_entries"] = []
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
