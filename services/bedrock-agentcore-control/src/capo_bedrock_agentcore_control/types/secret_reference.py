"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#SecretReference``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.secret_id_type
    import capo_bedrock_agentcore_control.types.secret_json_key_type


class SecretReference(TypedDict, closed=True):
    secret_id: "capo_bedrock_agentcore_control.types.secret_id_type.SecretIdType"
    """<p>The ID of the Amazon Web Services Secrets Manager secret that stores the secret value.</p>"""
    json_key: (
        "capo_bedrock_agentcore_control.types.secret_json_key_type.SecretJsonKeyType"
    )
    """<p>The JSON key used to extract the secret value from the Amazon Web Services Secrets Manager secret.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecretReference) -> dict:
    out: dict = {}
    out["secretId"] = value["secret_id"]
    out["jsonKey"] = value["json_key"]
    return out


def deserialize_json(data: dict) -> SecretReference:
    out: SecretReference = {}  # type: ignore[typeddict-item]
    if data.get("secretId") is not None:
        out["secret_id"] = data["secretId"]
    else:
        out["secret_id"] = ""
    if data.get("jsonKey") is not None:
        out["json_key"] = data["jsonKey"]
    else:
        out["json_key"] = ""
    return out
