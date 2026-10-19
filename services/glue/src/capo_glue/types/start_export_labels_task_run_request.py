"""Generated from Smithy shape ``com.amazonaws.glue#StartExportLabelsTaskRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.hash_string
    import capo_glue.types.uri_string


class StartExportLabelsTaskRunRequest(TypedDict, closed=True):
    transform_id: "capo_glue.types.hash_string.HashString"
    """<p>The unique identifier of the machine learning transform.</p>"""
    output_s3_path: "capo_glue.types.uri_string.UriString"
    """<p>The Amazon S3 path where you export the labels.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartExportLabelsTaskRunRequest) -> dict:
    out: dict = {}
    out["TransformId"] = value["transform_id"]
    out["OutputS3Path"] = value["output_s3_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartExportLabelsTaskRunRequest:
    out: StartExportLabelsTaskRunRequest = {}  # type: ignore[typeddict-item]
    if data.get("TransformId") is not None:
        out["transform_id"] = data["TransformId"]
    else:
        out["transform_id"] = ""
    if data.get("OutputS3Path") is not None:
        out["output_s3_path"] = data["OutputS3Path"]
    else:
        out["output_s3_path"] = ""
    return out
