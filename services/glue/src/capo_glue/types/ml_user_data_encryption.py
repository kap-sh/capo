"""Generated from Smithy shape ``com.amazonaws.glue#MLUserDataEncryption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.ml_user_data_encryption_mode_string
    import capo_glue.types.name_string


class MLUserDataEncryption(TypedDict, closed=True):
    ml_user_data_encryption_mode: "capo_glue.types.ml_user_data_encryption_mode_string.MLUserDataEncryptionModeString"
    """<p>The encryption mode applied to user data. Valid values are:</p> <ul> <li> <p>DISABLED: encryption is disabled</p> </li> <li> <p>SSEKMS: use of server-side encryption with Key Management Service (SSE-KMS) for user data stored in Amazon S3.</p> </li> </ul>"""
    kms_key_id: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The ID for the customer-provided KMS key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MLUserDataEncryption) -> dict:
    out: dict = {}
    import capo_glue.types.ml_user_data_encryption_mode_string

    out["MlUserDataEncryptionMode"] = (
        capo_glue.types.ml_user_data_encryption_mode_string.serialize_aws_json_1_1(
            value["ml_user_data_encryption_mode"]
        )
    )
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MLUserDataEncryption:
    out: MLUserDataEncryption = {}  # type: ignore[typeddict-item]
    if data.get("MlUserDataEncryptionMode") is not None:
        import capo_glue.types.ml_user_data_encryption_mode_string

        out["ml_user_data_encryption_mode"] = (
            capo_glue.types.ml_user_data_encryption_mode_string.deserialize_aws_json_1_1(
                data["MlUserDataEncryptionMode"]
            )
        )
    else:
        import typing

        out["ml_user_data_encryption_mode"] = typing.cast(
            "capo_glue.types.ml_user_data_encryption_mode_string.MLUserDataEncryptionModeString",
            "",
        )
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    return out
