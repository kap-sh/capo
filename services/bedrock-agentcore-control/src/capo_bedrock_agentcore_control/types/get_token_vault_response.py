"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetTokenVaultResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore_control.types.kms_configuration
    import capo_bedrock_agentcore_control.types.token_vault_id_type


class GetTokenVaultResponse(TypedDict, closed=True):
    token_vault_id: (
        "capo_bedrock_agentcore_control.types.token_vault_id_type.TokenVaultIdType"
    )
    """<p>The ID of the token vault.</p>"""
    kms_configuration: (
        "capo_bedrock_agentcore_control.types.kms_configuration.KmsConfiguration"
    )
    """<p>The KMS configuration for the token vault.</p>"""
    last_modified_date: "datetime.datetime"
    """<p>The timestamp when the token vault was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTokenVaultResponse) -> dict:
    out: dict = {}
    out["tokenVaultId"] = value["token_vault_id"]
    import capo_bedrock_agentcore_control.types.kms_configuration

    out["kmsConfiguration"] = (
        capo_bedrock_agentcore_control.types.kms_configuration.serialize_json(
            value["kms_configuration"]
        )
    )
    import capo_bedrock_agentcore_control.types._prelude.timestamp

    out["lastModifiedDate"] = (
        capo_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["last_modified_date"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetTokenVaultResponse:
    out: GetTokenVaultResponse = {}  # type: ignore[typeddict-item]
    if data.get("tokenVaultId") is not None:
        out["token_vault_id"] = data["tokenVaultId"]
    else:
        out["token_vault_id"] = ""
    if data.get("kmsConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.kms_configuration

        out["kms_configuration"] = (
            capo_bedrock_agentcore_control.types.kms_configuration.deserialize_json(
                data["kmsConfiguration"]
            )
        )
    else:
        raise DeserializationError("GetTokenVaultResponse.kms_configuration required")
    if data.get("lastModifiedDate") is not None:
        import capo_bedrock_agentcore_control.types._prelude.timestamp

        out["last_modified_date"] = (
            capo_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["lastModifiedDate"]
            )
        )
    else:
        import datetime

        out["last_modified_date"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
