"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#EncryptionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_agent_registry_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_agent_registry_control.types.kms_key_arn


class EncryptionConfiguration(TypedDict, closed=True):
    kms_key_arn: "capo_agent_registry_control.types.kms_key_arn.KmsKeyArn"
    """<p>The Amazon Resource Name (ARN) of the customer-managed Amazon Web Services KMS key used to encrypt the registry's content. The key must be a symmetric encryption key in the same Amazon Web Services account and Region as the registry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionConfiguration) -> dict:
    out: dict = {}
    out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> EncryptionConfiguration:
    out: EncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    else:
        raise DeserializationError("EncryptionConfiguration.kms_key_arn required")
    return out
