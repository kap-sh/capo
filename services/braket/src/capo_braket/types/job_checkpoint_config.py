"""Generated from Smithy shape ``com.amazonaws.braket#JobCheckpointConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_braket.types.s3_path
    import capo_braket.types.string4096


class JobCheckpointConfig(TypedDict, closed=True):
    local_path: NotRequired["capo_braket.types.string4096.String4096"]
    """<p>(Optional) The local directory where checkpoint data is stored. The default directory is <code>/opt/braket/checkpoints/</code>.</p>"""
    s3_uri: "capo_braket.types.s3_path.S3Path"
    """<p>Identifies the S3 path where you want Amazon Braket to store checkpoint data. For example, <code>s3://bucket-name/key-name-prefix</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobCheckpointConfig) -> dict:
    out: dict = {}
    if "local_path" in value:
        out["localPath"] = value["local_path"]
    out["s3Uri"] = value["s3_uri"]
    return out


def deserialize_json(data: dict) -> JobCheckpointConfig:
    out: JobCheckpointConfig = {}  # type: ignore[typeddict-item]
    if data.get("localPath") is not None:
        out["local_path"] = data["localPath"]
    if data.get("s3Uri") is not None:
        out["s3_uri"] = data["s3Uri"]
    else:
        out["s3_uri"] = ""
    return out
