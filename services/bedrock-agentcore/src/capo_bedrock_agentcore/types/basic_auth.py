"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#BasicAuth``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.secret_arn


class BasicAuth(TypedDict, closed=True):
    secret_arn: "capo_bedrock_agentcore.types.secret_arn.SecretArn"
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Secrets Manager secret containing proxy credentials. The secret must be a JSON object with <code>username</code> and <code>password</code> string fields that meet validation requirements. The caller must have <code>secretsmanager:GetSecretValue</code> permission for this ARN. Example secret format: <code>{"username": "proxy_user", "password": "secure_password"}</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BasicAuth) -> dict:
    out: dict = {}
    out["secretArn"] = value["secret_arn"]
    return out


def deserialize_json(data: dict) -> BasicAuth:
    out: BasicAuth = {}  # type: ignore[typeddict-item]
    if data.get("secretArn") is not None:
        out["secret_arn"] = data["secretArn"]
    else:
        raise DeserializationError("BasicAuth.secret_arn required")
    return out
