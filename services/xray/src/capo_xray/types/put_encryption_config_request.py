"""Generated from Smithy shape ``com.amazonaws.xray#PutEncryptionConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.encryption_key_id
    import capo_xray.types.encryption_type


class PutEncryptionConfigRequest(TypedDict, closed=True):
    key_id: NotRequired["capo_xray.types.encryption_key_id.EncryptionKeyId"]
    """<p>An Amazon Web Services KMS key in one of the following formats:</p> <ul> <li> <p> <b>Alias</b> - The name of the key. For example, <code>alias/MyKey</code>.</p> </li> <li> <p> <b>Key ID</b> - The KMS key ID of the key. For example, <code>ae4aa6d49-a4d8-9df9-a475-4ff6d7898456</code>. Amazon Web Services X-Ray does not support asymmetric KMS keys.</p> </li> <li> <p> <b>ARN</b> - The full Amazon Resource Name of the key ID or alias. For example, <code>arn:aws:kms:us-east-2:123456789012:key/ae4aa6d49-a4d8-9df9-a475-4ff6d7898456</code>. Use this format to specify a key in a different account.</p> </li> </ul> <p>Omit this key if you set <code>Type</code> to <code>NONE</code>.</p>"""
    type: "capo_xray.types.encryption_type.EncryptionType"
    """<p>The type of encryption. Set to <code>KMS</code> to use your own key for encryption. Set to <code>NONE</code> for default encryption.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutEncryptionConfigRequest) -> dict:
    out: dict = {}
    if "key_id" in value:
        out["KeyId"] = value["key_id"]
    import capo_xray.types.encryption_type

    out["Type"] = capo_xray.types.encryption_type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> PutEncryptionConfigRequest:
    out: PutEncryptionConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("KeyId") is not None:
        out["key_id"] = data["KeyId"]
    if data.get("Type") is not None:
        import capo_xray.types.encryption_type

        out["type"] = capo_xray.types.encryption_type.deserialize_json(data["Type"])
    else:
        import typing

        out["type"] = typing.cast("capo_xray.types.encryption_type.EncryptionType", "")
    return out
