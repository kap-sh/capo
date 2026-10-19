"""Generated from Smithy shape ``com.amazonaws.glue#EncryptionAtRest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.catalog_encryption_mode
    import capo_glue.types.iam_role_arn
    import capo_glue.types.name_string


class EncryptionAtRest(TypedDict, closed=True):
    catalog_encryption_mode: (
        "capo_glue.types.catalog_encryption_mode.CatalogEncryptionMode"
    )
    """<p>The encryption-at-rest mode for encrypting Data Catalog data.</p>"""
    sse_aws_kms_key_id: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The ID of the KMS key to use for encryption at rest.</p>"""
    catalog_encryption_service_role: NotRequired[
        "capo_glue.types.iam_role_arn.IAMRoleArn"
    ]
    """<p>The role that Glue assumes to encrypt and decrypt the Data Catalog objects on the caller's behalf.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EncryptionAtRest) -> dict:
    out: dict = {}
    import capo_glue.types.catalog_encryption_mode

    out["CatalogEncryptionMode"] = (
        capo_glue.types.catalog_encryption_mode.serialize_aws_json_1_1(
            value["catalog_encryption_mode"]
        )
    )
    if "sse_aws_kms_key_id" in value:
        out["SseAwsKmsKeyId"] = value["sse_aws_kms_key_id"]
    if "catalog_encryption_service_role" in value:
        out["CatalogEncryptionServiceRole"] = value["catalog_encryption_service_role"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EncryptionAtRest:
    out: EncryptionAtRest = {}  # type: ignore[typeddict-item]
    if data.get("CatalogEncryptionMode") is not None:
        import capo_glue.types.catalog_encryption_mode

        out["catalog_encryption_mode"] = (
            capo_glue.types.catalog_encryption_mode.deserialize_aws_json_1_1(
                data["CatalogEncryptionMode"]
            )
        )
    else:
        import typing

        out["catalog_encryption_mode"] = typing.cast(
            "capo_glue.types.catalog_encryption_mode.CatalogEncryptionMode", ""
        )
    if data.get("SseAwsKmsKeyId") is not None:
        out["sse_aws_kms_key_id"] = data["SseAwsKmsKeyId"]
    if data.get("CatalogEncryptionServiceRole") is not None:
        out["catalog_encryption_service_role"] = data["CatalogEncryptionServiceRole"]
    return out
