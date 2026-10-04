"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#SecretsManagerCertificateConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.certificate_secret_arn


class SecretsManagerCertificateConfiguration(TypedDict, closed=True):
    secret_arn: "capo_bedrock_agentcore_control.types.certificate_secret_arn.CertificateSecretArn"
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Secrets Manager secret that contains the PEM-encoded certificate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecretsManagerCertificateConfiguration) -> dict:
    out: dict = {}
    out["secretArn"] = value["secret_arn"]
    return out


def deserialize_json(data: dict) -> SecretsManagerCertificateConfiguration:
    out: SecretsManagerCertificateConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("secretArn") is not None:
        out["secret_arn"] = data["secretArn"]
    else:
        raise DeserializationError(
            "SecretsManagerCertificateConfiguration.secret_arn required"
        )
    return out
