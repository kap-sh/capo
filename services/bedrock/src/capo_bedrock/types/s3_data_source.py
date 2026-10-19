"""Generated from Smithy shape ``com.amazonaws.bedrock#S3DataSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.s3_uri


class S3DataSource(TypedDict, closed=True):
    s3_uri: "capo_bedrock.types.s3_uri.S3Uri"
    """<p>The URI of the Amazon S3 data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3DataSource) -> dict:
    out: dict = {}
    out["s3Uri"] = value["s3_uri"]
    return out


def deserialize_json(data: dict) -> S3DataSource:
    out: S3DataSource = {}  # type: ignore[typeddict-item]
    if data.get("s3Uri") is not None:
        out["s3_uri"] = data["s3Uri"]
    else:
        out["s3_uri"] = ""
    return out
