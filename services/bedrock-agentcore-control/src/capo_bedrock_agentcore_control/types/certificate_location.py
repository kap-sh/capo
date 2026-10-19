"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CertificateLocation``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.secrets_manager_location


class _CertificateLocation_secretsManager(TypedDict, closed=True):
    secretsManager: "capo_bedrock_agentcore_control.types.secrets_manager_location.SecretsManagerLocation"


CertificateLocation: TypeAlias = (
    _CertificateLocation_secretsManager | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: CertificateLocation) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"CertificateLocation: cannot serialize unknown variant {value.name!r}"
        )
    elif "secretsManager" in value:
        import capo_bedrock_agentcore_control.types.secrets_manager_location

        return {
            "secretsManager": capo_bedrock_agentcore_control.types.secrets_manager_location.serialize_json(
                value["secretsManager"]
            )
        }
    else:
        raise SerializationError("CertificateLocation: no variant present")


def deserialize_json(data: dict) -> CertificateLocation:
    if data.get("secretsManager") is not None:
        import capo_bedrock_agentcore_control.types.secrets_manager_location

        return {
            "secretsManager": capo_bedrock_agentcore_control.types.secrets_manager_location.deserialize_json(
                data["secretsManager"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("CertificateLocation: no recognized variant key")
