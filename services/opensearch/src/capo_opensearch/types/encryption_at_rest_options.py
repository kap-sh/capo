"""Generated from Smithy shape ``com.amazonaws.opensearch#EncryptionAtRestOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.boolean
    import capo_opensearch.types.encryption_mode
    import capo_opensearch.types.kms_key_id


class EncryptionAtRestOptions(TypedDict, closed=True):
    enabled: NotRequired["capo_opensearch.types.boolean.Boolean"]
    """<p>True to enable encryption at rest.</p>"""
    kms_key_id: NotRequired["capo_opensearch.types.kms_key_id.KmsKeyId"]
    """<p>The KMS key ID. Takes the form <code>1a2a3a4-1a2a-3a4a-5a6a-1a2a3a4a5a6a</code>.</p>"""
    encryption_mode: NotRequired["capo_opensearch.types.encryption_mode.EncryptionMode"]
    """<p>The type of encryption at rest applied to the domain's data. Valid values are <code>DISK</code> and <code>NATIVE</code>. <code>DISK</code> is the default and uses volume-level encryption. <code>NATIVE</code> uses engine-native, index-level encryption and requires encryption at rest to be enabled and OpenSearch version 3.3 or later. After the mode is set to <code>NATIVE</code>, it can't be changed back to <code>DISK</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionAtRestOptions) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "encryption_mode" in value:
        import capo_opensearch.types.encryption_mode

        out["EncryptionMode"] = capo_opensearch.types.encryption_mode.serialize_json(
            value["encryption_mode"]
        )
    return out


def deserialize_json(data: dict) -> EncryptionAtRestOptions:
    out: EncryptionAtRestOptions = {}  # type: ignore[typeddict-item]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("EncryptionMode") is not None:
        import capo_opensearch.types.encryption_mode

        out["encryption_mode"] = capo_opensearch.types.encryption_mode.deserialize_json(
            data["EncryptionMode"]
        )
    return out
