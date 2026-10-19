"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#UploadEntityDefinitionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.upload_id


class UploadEntityDefinitionsResponse(TypedDict, closed=True):
    upload_id: "capo_iotthingsgraph.types.upload_id.UploadId"
    """<p>The ID that specifies the upload action. You can use this to track the status of the upload.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UploadEntityDefinitionsResponse) -> dict:
    out: dict = {}
    out["uploadId"] = value["upload_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UploadEntityDefinitionsResponse:
    out: UploadEntityDefinitionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("uploadId") is not None:
        out["upload_id"] = data["uploadId"]
    else:
        out["upload_id"] = ""
    return out
