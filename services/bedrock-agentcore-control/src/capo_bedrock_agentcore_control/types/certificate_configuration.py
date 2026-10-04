"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CertificateConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.s3_certificate_configuration
    import capo_bedrock_agentcore_control.types.secrets_manager_certificate_configuration


class _CertificateConfiguration_s3(TypedDict, closed=True):
    s3: "capo_bedrock_agentcore_control.types.s3_certificate_configuration.S3CertificateConfiguration"


class _CertificateConfiguration_secretsManager(TypedDict, closed=True):
    secretsManager: "capo_bedrock_agentcore_control.types.secrets_manager_certificate_configuration.SecretsManagerCertificateConfiguration"


CertificateConfiguration: TypeAlias = (
    _CertificateConfiguration_s3 | _CertificateConfiguration_secretsManager
)


# --- restJson1 ser/de ---
def serialize_json(value: CertificateConfiguration) -> dict:
    if "s3" in value:
        import capo_bedrock_agentcore_control.types.s3_certificate_configuration

        return {
            "s3": capo_bedrock_agentcore_control.types.s3_certificate_configuration.serialize_json(
                value["s3"]
            )
        }
    elif "secretsManager" in value:
        import capo_bedrock_agentcore_control.types.secrets_manager_certificate_configuration

        return {
            "secretsManager": capo_bedrock_agentcore_control.types.secrets_manager_certificate_configuration.serialize_json(
                value["secretsManager"]
            )
        }
    else:
        raise SerializationError("CertificateConfiguration: no variant present")


def deserialize_json(data: dict) -> CertificateConfiguration:
    if data.get("s3") is not None:
        import capo_bedrock_agentcore_control.types.s3_certificate_configuration

        return {
            "s3": capo_bedrock_agentcore_control.types.s3_certificate_configuration.deserialize_json(
                data["s3"]
            )
        }
    elif data.get("secretsManager") is not None:
        import capo_bedrock_agentcore_control.types.secrets_manager_certificate_configuration

        return {
            "secretsManager": capo_bedrock_agentcore_control.types.secrets_manager_certificate_configuration.deserialize_json(
                data["secretsManager"]
            )
        }
    else:
        raise DeserializationError(
            "CertificateConfiguration: no recognized variant key"
        )
