"""Generated from Smithy shape ``com.amazonaws.connecthealth#OutputDataConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connecthealth.types.s3_uri


class OutputDataConfig(TypedDict, closed=True):
    s3_output_path: "capo_connecthealth.types.s3_uri.S3Uri"
    """<p>S3 URI where the insights output will be stored.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutputDataConfig) -> dict:
    out: dict = {}
    out["s3OutputPath"] = value["s3_output_path"]
    return out


def deserialize_json(data: dict) -> OutputDataConfig:
    out: OutputDataConfig = {}  # type: ignore[typeddict-item]
    if data.get("s3OutputPath") is not None:
        out["s3_output_path"] = data["s3OutputPath"]
    else:
        out["s3_output_path"] = ""
    return out
