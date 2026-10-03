"""Generated from Smithy shape ``com.amazonaws.networkfirewall#EncryptionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_firewall.types.encryption_type
    import capo_network_firewall.types.key_id


class EncryptionConfiguration(TypedDict, closed=True):
    key_id: NotRequired["capo_network_firewall.types.key_id.KeyId"]
    """<p>The ID of the Amazon Web Services Key Management Service (KMS) customer managed key. You can use any of the key identifiers that KMS supports, unless you're using a key that's managed by another account. If you're using a key managed by another account, then specify the key ARN. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id">Key ID</a> in the <i>Amazon Web Services KMS Developer Guide</i>.</p>"""
    type: "capo_network_firewall.types.encryption_type.EncryptionType"
    """<p>The type of Amazon Web Services KMS key to use for encryption of your Network Firewall resources.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EncryptionConfiguration) -> dict:
    out: dict = {}
    if "key_id" in value:
        out["KeyId"] = value["key_id"]
    import capo_network_firewall.types.encryption_type

    out["Type"] = capo_network_firewall.types.encryption_type.serialize_aws_json_1_0(
        value["type"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> EncryptionConfiguration:
    out: EncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("KeyId") is not None:
        out["key_id"] = data["KeyId"]
    if data.get("Type") is not None:
        import capo_network_firewall.types.encryption_type

        out["type"] = (
            capo_network_firewall.types.encryption_type.deserialize_aws_json_1_0(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("EncryptionConfiguration.type required")
    return out
