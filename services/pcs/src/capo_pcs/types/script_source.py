"""Generated from Smithy shape ``com.amazonaws.pcs#ScriptSource``."""

from typing_extensions import NotRequired, TypedDict


class ScriptSource(TypedDict, closed=True):
    script_location: "str"
    """<p>The location of the script. Specify either an Amazon S3 URI in the format <code>s3://bucket-name/key</code> or an HTTPS URL.</p>"""
    s3_version_id: NotRequired["str"]
    """<p>The Amazon S3 version ID of the script. Use this value to pin the script to a specific version in a versioned Amazon S3 bucket. This value is only valid when <code>scriptLocation</code> is an Amazon S3 URI.</p>"""
    checksum: NotRequired["str"]
    """<p>The SHA-256 checksum of the script content, as a 64-character hexadecimal string. This value is optional. When specified, PCS uses this value to verify the integrity of the downloaded script.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ScriptSource) -> dict:
    out: dict = {}
    out["scriptLocation"] = value["script_location"]
    if "s3_version_id" in value:
        out["s3VersionId"] = value["s3_version_id"]
    if "checksum" in value:
        out["checksum"] = value["checksum"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ScriptSource:
    out: ScriptSource = {}  # type: ignore[typeddict-item]
    if data.get("scriptLocation") is not None:
        out["script_location"] = data["scriptLocation"]
    else:
        out["script_location"] = ""
    if data.get("s3VersionId") is not None:
        out["s3_version_id"] = data["s3VersionId"]
    if data.get("checksum") is not None:
        out["checksum"] = data["checksum"]
    return out
