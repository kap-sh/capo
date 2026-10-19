"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#S3Source``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.s3_uri


class S3Source(TypedDict, closed=True):
    s3_uri: "capo_bedrock_agentcore_control.types.s3_uri.S3Uri"
    """<p> Amazon S3 URI of the JSONL file (for example, <code>s3://my-bucket/path/to/examples.jsonl</code>). </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Source) -> dict:
    out: dict = {}
    out["s3Uri"] = value["s3_uri"]
    return out


def deserialize_json(data: dict) -> S3Source:
    out: S3Source = {}  # type: ignore[typeddict-item]
    if data.get("s3Uri") is not None:
        out["s3_uri"] = data["s3Uri"]
    else:
        out["s3_uri"] = ""
    return out
