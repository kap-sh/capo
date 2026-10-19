"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#GetUploadStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.upload_id


class GetUploadStatusRequest(TypedDict, closed=True):
    upload_id: "capo_iotthingsgraph.types.upload_id.UploadId"
    """<p>The ID of the upload. This value is returned by the <code>UploadEntityDefinitions</code> action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetUploadStatusRequest) -> dict:
    out: dict = {}
    out["uploadId"] = value["upload_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetUploadStatusRequest:
    out: GetUploadStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("uploadId") is not None:
        out["upload_id"] = data["uploadId"]
    else:
        out["upload_id"] = ""
    return out
