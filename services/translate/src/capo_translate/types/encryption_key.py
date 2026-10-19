"""Generated from Smithy shape ``com.amazonaws.translate#EncryptionKey``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_translate.types.encryption_key_id
    import capo_translate.types.encryption_key_type


class EncryptionKey(TypedDict, closed=True):
    type: "capo_translate.types.encryption_key_type.EncryptionKeyType"
    """<p>The type of encryption key used by Amazon Translate to encrypt this object.</p>"""
    id: "capo_translate.types.encryption_key_id.EncryptionKeyID"
    """<p>The Amazon Resource Name (ARN) of the encryption key being used to encrypt this object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EncryptionKey) -> dict:
    out: dict = {}
    import capo_translate.types.encryption_key_type

    out["Type"] = capo_translate.types.encryption_key_type.serialize_aws_json_1_1(
        value["type"]
    )
    out["Id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EncryptionKey:
    out: EncryptionKey = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_translate.types.encryption_key_type

        out["type"] = capo_translate.types.encryption_key_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_translate.types.encryption_key_type.EncryptionKeyType", ""
        )
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    return out
