"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#DefinitionS3Location``."""

from typing_extensions import NotRequired, TypedDict


class DefinitionS3Location(TypedDict, closed=True):
    bucket: "str"
    """<p>The name of the Amazon S3 bucket that contains the workflow definition file.</p>"""
    object_key: "str"
    """<p>The key (name) of the workflow definition file within the S3 bucket.</p>"""
    version_id: NotRequired["str"]
    """<p>Optional. The version ID of the workflow definition file in Amazon S3. If not specified, the latest version is used.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DefinitionS3Location) -> dict:
    out: dict = {}
    out["Bucket"] = value["bucket"]
    out["ObjectKey"] = value["object_key"]
    if "version_id" in value:
        out["VersionId"] = value["version_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DefinitionS3Location:
    out: DefinitionS3Location = {}  # type: ignore[typeddict-item]
    if data.get("Bucket") is not None:
        out["bucket"] = data["Bucket"]
    else:
        out["bucket"] = ""
    if data.get("ObjectKey") is not None:
        out["object_key"] = data["ObjectKey"]
    else:
        out["object_key"] = ""
    if data.get("VersionId") is not None:
        out["version_id"] = data["VersionId"]
    return out
