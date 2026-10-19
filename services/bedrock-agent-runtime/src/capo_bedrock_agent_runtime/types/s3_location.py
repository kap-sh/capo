"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#S3Location``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.s3_uri


class S3Location(TypedDict, closed=True):
    uri: "capo_bedrock_agent_runtime.types.s3_uri.S3Uri"
    """<p>The path to the Amazon S3 bucket where the image is stored.</p>"""


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
