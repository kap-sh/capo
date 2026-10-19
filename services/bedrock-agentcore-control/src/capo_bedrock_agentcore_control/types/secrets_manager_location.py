"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#SecretsManagerLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.tool_secret_arn


class SecretsManagerLocation(TypedDict, closed=True):
    secret_arn: "capo_bedrock_agentcore_control.types.tool_secret_arn.ToolSecretArn"
    """<p>The ARN of the Amazon Web Services Secrets Manager secret containing the certificate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecretsManagerLocation) -> dict:
    out: dict = {}
    out["secretArn"] = value["secret_arn"]
    return out


def deserialize_json(data: dict) -> SecretsManagerLocation:
    out: SecretsManagerLocation = {}  # type: ignore[typeddict-item]
    if data.get("secretArn") is not None:
        out["secret_arn"] = data["secretArn"]
    else:
        out["secret_arn"] = ""
    return out
