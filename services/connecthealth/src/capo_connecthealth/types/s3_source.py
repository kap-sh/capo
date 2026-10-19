"""Generated from Smithy shape ``com.amazonaws.connecthealth#S3Source``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connecthealth.types.s3_uri


class S3Source(TypedDict, closed=True):
    uri: "capo_connecthealth.types.s3_uri.S3Uri"
    """<p>The S3 URI.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Source) -> dict:
    out: dict = {}
    out["uri"] = value["uri"]
    return out


def deserialize_json(data: dict) -> S3Source:
    out: S3Source = {}  # type: ignore[typeddict-item]
    if data.get("uri") is not None:
        out["uri"] = data["uri"]
    else:
        out["uri"] = ""
    return out
