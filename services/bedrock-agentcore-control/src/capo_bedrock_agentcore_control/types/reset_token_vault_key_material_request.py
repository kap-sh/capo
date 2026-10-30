"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ResetTokenVaultKeyMaterialRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.token_vault_id_type


class ResetTokenVaultKeyMaterialRequest(TypedDict, closed=True):
    token_vault_id: (
        "capo_bedrock_agentcore_control.types.token_vault_id_type.TokenVaultIdType"
    )
    """<p>The unique identifier of the token vault to reset. To reset your account's default token vault, specify <code>default</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResetTokenVaultKeyMaterialRequest) -> dict:
    out: dict = {}
    out["tokenVaultId"] = value["token_vault_id"]
    return out


def deserialize_json(data: dict) -> ResetTokenVaultKeyMaterialRequest:
    out: ResetTokenVaultKeyMaterialRequest = {}  # type: ignore[typeddict-item]
    if data.get("tokenVaultId") is not None:
        out["token_vault_id"] = data["tokenVaultId"]
    else:
        out["token_vault_id"] = ""
    return out
