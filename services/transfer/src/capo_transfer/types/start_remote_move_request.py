"""Generated from Smithy shape ``com.amazonaws.transfer#StartRemoteMoveRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.connector_id
    import capo_transfer.types.file_path


class StartRemoteMoveRequest(TypedDict, closed=True):
    connector_id: "capo_transfer.types.connector_id.ConnectorId"
    """<p>The unique identifier for the connector.</p>"""
    source_path: "capo_transfer.types.file_path.FilePath"
    """<p>The absolute path of the file or directory to move or rename. You can only specify one path per call to this operation.</p>"""
    target_path: "capo_transfer.types.file_path.FilePath"
    """<p>The absolute path for the target of the move/rename operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartRemoteMoveRequest) -> dict:
    out: dict = {}
    out["ConnectorId"] = value["connector_id"]
    out["SourcePath"] = value["source_path"]
    out["TargetPath"] = value["target_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartRemoteMoveRequest:
    out: StartRemoteMoveRequest = {}  # type: ignore[typeddict-item]
    if data.get("ConnectorId") is not None:
        out["connector_id"] = data["ConnectorId"]
    else:
        out["connector_id"] = ""
    if data.get("SourcePath") is not None:
        out["source_path"] = data["SourcePath"]
    else:
        out["source_path"] = ""
    if data.get("TargetPath") is not None:
        out["target_path"] = data["TargetPath"]
    else:
        out["target_path"] = ""
    return out
