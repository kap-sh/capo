"""Generated from Smithy shape ``com.amazonaws.bedrock#AdvancedPromptOptimizationInputConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.s3_uri


class AdvancedPromptOptimizationInputConfig(TypedDict, closed=True):
    s3_uri: "capo_bedrock.types.s3_uri.S3Uri"
    """<p>The S3 URI of the JSONL input file containing prompt templates and evaluation samples.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdvancedPromptOptimizationInputConfig) -> dict:
    out: dict = {}
    out["s3Uri"] = value["s3_uri"]
    return out


def deserialize_json(data: dict) -> AdvancedPromptOptimizationInputConfig:
    out: AdvancedPromptOptimizationInputConfig = {}  # type: ignore[typeddict-item]
    if data.get("s3Uri") is not None:
        out["s3_uri"] = data["s3Uri"]
    else:
        out["s3_uri"] = ""
    return out
