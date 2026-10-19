"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrieveAndGenerateSessionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.kms_key_arn


class RetrieveAndGenerateSessionConfiguration(TypedDict, closed=True):
    kms_key_arn: "capo_bedrock_agent_runtime.types.kms_key_arn.KmsKeyArn"
    """<p>The ARN of the KMS key encrypting the session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrieveAndGenerateSessionConfiguration) -> dict:
    out: dict = {}
    out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> RetrieveAndGenerateSessionConfiguration:
    out: RetrieveAndGenerateSessionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    else:
        out["kms_key_arn"] = ""
    return out
