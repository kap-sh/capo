"""Generated from Smithy shape ``com.amazonaws.bedrockagent#S3Location``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.s3_bucket_uri


class S3Location(TypedDict, closed=True):
    uri: "capo_bedrock_agent.types.s3_bucket_uri.S3BucketUri"
    """<p>The location's URI. For example, <code>s3://my-bucket/chunk-processor/</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Location) -> dict:
    out: dict = {}
    out["uri"] = value["uri"]
    return out


def deserialize_json(data: dict) -> S3Location:
    out: S3Location = {}  # type: ignore[typeddict-item]
    if data.get("uri") is not None:
        out["uri"] = data["uri"]
    else:
        out["uri"] = ""
    return out
