"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#KmsKeySourceType``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.kms_key_arn


class KmsKeySourceType(TypedDict, closed=True):
    kms_key_arn: "capo_bedrock_agentcore_control.types.kms_key_arn.KmsKeyArn"
    """<p>The Amazon Resource Name (ARN) of the KMS key used to sign the JWT client assertion. The key must be an asymmetric key with key usage SIGN_VERIFY and a key spec compatible with the configured signing algorithm.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KmsKeySourceType) -> dict:
    out: dict = {}
    out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> KmsKeySourceType:
    out: KmsKeySourceType = {}  # type: ignore[typeddict-item]
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    else:
        out["kms_key_arn"] = ""
    return out
