"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#Secret``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.secret_arn


class Secret(TypedDict, closed=True):
    secret_arn: "capo_bedrock_agentcore_control.types.secret_arn.SecretArn"
    """<p>The Amazon Resource Name (ARN) of the secret in Amazon Web Services Secrets Manager.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Secret) -> dict:
    out: dict = {}
    out["secretArn"] = value["secret_arn"]
    return out


def deserialize_json(data: dict) -> Secret:
    out: Secret = {}  # type: ignore[typeddict-item]
    if data.get("secretArn") is not None:
        out["secret_arn"] = data["secretArn"]
    else:
        out["secret_arn"] = ""
    return out
