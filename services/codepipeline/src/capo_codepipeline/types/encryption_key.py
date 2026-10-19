"""Generated from Smithy shape ``com.amazonaws.codepipeline#EncryptionKey``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.encryption_key_id
    import capo_codepipeline.types.encryption_key_type


class EncryptionKey(TypedDict, closed=True):
    id: "capo_codepipeline.types.encryption_key_id.EncryptionKeyId"
    """<p>The ID used to identify the key. For an Amazon Web Services KMS key, you can use the key ID, the key ARN, or the alias ARN.</p> <note> <p>Aliases are recognized only in the account that created the KMS key. For cross-account actions, you can only use the key ID or key ARN to identify the key. Cross-account actions involve using the role from the other account (AccountB), so specifying the key ID will use the key from the other account (AccountB).</p> </note>"""
    type: "capo_codepipeline.types.encryption_key_type.EncryptionKeyType"
    """<p>The type of encryption key, such as an Amazon Web Services KMS key. When creating or updating a pipeline, the value must be set to 'KMS'.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EncryptionKey) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import capo_codepipeline.types.encryption_key_type

    out["type"] = capo_codepipeline.types.encryption_key_type.serialize_aws_json_1_1(
        value["type"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> EncryptionKey:
    out: EncryptionKey = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("type") is not None:
        import capo_codepipeline.types.encryption_key_type

        out["type"] = (
            capo_codepipeline.types.encryption_key_type.deserialize_aws_json_1_1(
                data["type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_codepipeline.types.encryption_key_type.EncryptionKeyType", ""
        )
    return out
