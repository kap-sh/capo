"""Generated from Smithy shape ``com.amazonaws.glue#IcebergEncryptedKey``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.encrypted_key_metadata_string
    import capo_glue.types.encryption_key_id_string
    import capo_glue.types.string_to_string_map


class IcebergEncryptedKey(TypedDict, closed=True):
    key_id: "capo_glue.types.encryption_key_id_string.EncryptionKeyIdString"
    """<p>Unique identifier of the encryption key used for Iceberg table encryption. This ID is used to reference the key in table metadata and track which key was used to encrypt specific data.</p>"""
    encrypted_key_metadata: (
        "capo_glue.types.encrypted_key_metadata_string.EncryptedKeyMetadataString"
    )
    """<p>Encrypted key and metadata, base64 encoded. The format of encrypted key metadata is determined by the table's encryption scheme and can be a wrapped format specific to the table's KMS provider.</p>"""
    encrypted_by_id: NotRequired[
        "capo_glue.types.encryption_key_id_string.EncryptionKeyIdString"
    ]
    """<p>Optional ID of the key used to encrypt or wrap the key metadata in Iceberg table encryption. This field references another encryption key that was used to encrypt the current key's metadata.</p>"""
    properties: NotRequired["capo_glue.types.string_to_string_map.StringToStringMap"]
    """<p>A string to string map of additional metadata used by the table's encryption scheme. These properties provide additional context and configuration for the encryption key implementation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IcebergEncryptedKey) -> dict:
    out: dict = {}
    out["KeyId"] = value["key_id"]
    out["EncryptedKeyMetadata"] = value["encrypted_key_metadata"]
    if "encrypted_by_id" in value:
        out["EncryptedById"] = value["encrypted_by_id"]
    if "properties" in value:
        import capo_glue.types.string_to_string_map

        out["Properties"] = capo_glue.types.string_to_string_map.serialize_aws_json_1_1(
            value["properties"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> IcebergEncryptedKey:
    out: IcebergEncryptedKey = {}  # type: ignore[typeddict-item]
    if data.get("KeyId") is not None:
        out["key_id"] = data["KeyId"]
    else:
        out["key_id"] = ""
    if data.get("EncryptedKeyMetadata") is not None:
        out["encrypted_key_metadata"] = data["EncryptedKeyMetadata"]
    else:
        out["encrypted_key_metadata"] = ""
    if data.get("EncryptedById") is not None:
        out["encrypted_by_id"] = data["EncryptedById"]
    if data.get("Properties") is not None:
        import capo_glue.types.string_to_string_map

        out["properties"] = (
            capo_glue.types.string_to_string_map.deserialize_aws_json_1_1(
                data["Properties"]
            )
        )
    return out
