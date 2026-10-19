"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#GetTableRestoreStatusRequest``."""

from typing_extensions import TypedDict


class GetTableRestoreStatusRequest(TypedDict, closed=True):
    table_restore_request_id: "str"
    """<p>The ID of the <code>RestoreTableFromSnapshot</code> request to return status for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTableRestoreStatusRequest) -> dict:
    out: dict = {}
    out["tableRestoreRequestId"] = value["table_restore_request_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTableRestoreStatusRequest:
    out: GetTableRestoreStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("tableRestoreRequestId") is not None:
        out["table_restore_request_id"] = data["tableRestoreRequestId"]
    else:
        out["table_restore_request_id"] = ""
    return out
