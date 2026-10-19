"""Generated from Smithy shape ``com.amazonaws.braket#ScriptModeConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_braket.types.compression_type
    import capo_braket.types.s3_path


class ScriptModeConfig(TypedDict, closed=True):
    entry_point: "str"
    """<p>The entry point in the algorithm scripts from where the execution begins in the hybrid job.</p>"""
    s3_uri: "capo_braket.types.s3_path.S3Path"
    """<p>The URI that specifies the S3 path to the algorithm scripts used by an Amazon Braket hybrid job.</p>"""
    compression_type: NotRequired["capo_braket.types.compression_type.CompressionType"]
    """<p>The type of compression used to store the algorithm scripts in Amazon S3 storage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScriptModeConfig) -> dict:
    out: dict = {}
    out["entryPoint"] = value["entry_point"]
    out["s3Uri"] = value["s3_uri"]
    if "compression_type" in value:
        out["compressionType"] = value["compression_type"]
    return out


def deserialize_json(data: dict) -> ScriptModeConfig:
    out: ScriptModeConfig = {}  # type: ignore[typeddict-item]
    if data.get("entryPoint") is not None:
        out["entry_point"] = data["entryPoint"]
    else:
        out["entry_point"] = ""
    if data.get("s3Uri") is not None:
        out["s3_uri"] = data["s3Uri"]
    else:
        out["s3_uri"] = ""
    if data.get("compressionType") is not None:
        out["compression_type"] = data["compressionType"]
    return out
