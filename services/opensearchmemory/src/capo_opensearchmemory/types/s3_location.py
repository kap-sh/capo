"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#S3Location``."""

from typing_extensions import TypedDict


class S3Location(TypedDict, closed=True):
    uri: "str"
    """<p>The object's S3 URI, for example <code>s3://bucket/key</code>. The bucket must be in the space's Region. You need <code>s3:GetObject</code> on the object, and <code>kms:Decrypt</code> on its key if the object uses SSE-KMS. The event doesn't store the object itself.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: S3Location) -> dict:
    out: dict = {}
    out["uri"] = value["uri"]
    return out


def deserialize_aws_json_1_0(data: dict) -> S3Location:
    out: S3Location = {}  # type: ignore[typeddict-item]
    if data.get("uri") is not None:
        out["uri"] = data["uri"]
    else:
        out["uri"] = ""
    return out
