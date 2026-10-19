"""Generated from Smithy shape ``com.amazonaws.bedrock#S3ObjectDoc``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.k_bs3_uri


class S3ObjectDoc(TypedDict, closed=True):
    uri: "capo_bedrock.types.k_bs3_uri.kBS3Uri"
    """<p>The S3 URI location for the wrapper object of the document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3ObjectDoc) -> dict:
    out: dict = {}
    out["uri"] = value["uri"]
    return out


def deserialize_json(data: dict) -> S3ObjectDoc:
    out: S3ObjectDoc = {}  # type: ignore[typeddict-item]
    if data.get("uri") is not None:
        out["uri"] = data["uri"]
    else:
        out["uri"] = ""
    return out
