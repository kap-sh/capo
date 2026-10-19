"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#BedrockFoundationModelModelConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.bedrock_model_arn


class BedrockFoundationModelModelConfiguration(TypedDict, closed=True):
    model_arn: "capo_bedrock_agent_runtime.types.bedrock_model_arn.BedrockModelArn"
    """<p>The ARN of the Bedrock foundation model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BedrockFoundationModelModelConfiguration) -> dict:
    out: dict = {}
    out["modelArn"] = value["model_arn"]
    return out


def deserialize_json(data: dict) -> BedrockFoundationModelModelConfiguration:
    out: BedrockFoundationModelModelConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("modelArn") is not None:
        out["model_arn"] = data["modelArn"]
    else:
        out["model_arn"] = ""
    return out
