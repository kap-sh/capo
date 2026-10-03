"""Generated from Smithy shape ``com.amazonaws.ecr#EncryptionConfigurationForRepositoryCreationTemplate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecr.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecr.types.encryption_type
    import capo_ecr.types.kms_key_for_repository_creation_template


class EncryptionConfigurationForRepositoryCreationTemplate(TypedDict, closed=True):
    encryption_type: "capo_ecr.types.encryption_type.EncryptionType"
    """<p>The encryption type to use.</p> <p>If you use the <code>KMS</code> encryption type, the contents of the repository will be encrypted using server-side encryption with Key Management Service key stored in KMS. When you use KMS to encrypt your data, you can either use the default Amazon Web Services managed KMS key for Amazon ECR, or specify your own KMS key, which you already created. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html">Protecting data using server-side encryption with an KMS key stored in Key Management Service (SSE-KMS)</a> in the <i>Amazon Simple Storage Service Console Developer Guide</i>.</p> <p>If you use the <code>AES256</code> encryption type, Amazon ECR uses server-side encryption with Amazon S3-managed encryption keys which encrypts the images in the repository using an AES256 encryption algorithm. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingServerSideEncryption.html">Protecting data using server-side encryption with Amazon S3-managed encryption keys (SSE-S3)</a> in the <i>Amazon Simple Storage Service Console Developer Guide</i>.</p>"""
    kms_key: NotRequired[
        "capo_ecr.types.kms_key_for_repository_creation_template.KmsKeyForRepositoryCreationTemplate"
    ]
    """<p>If you use the <code>KMS</code> encryption type, specify the KMS key to use for encryption. The full ARN of the KMS key must be specified. The key must exist in the same Region as the repository. If no key is specified, the default Amazon Web Services managed KMS key for Amazon ECR will be used.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: EncryptionConfigurationForRepositoryCreationTemplate,
) -> dict:
    out: dict = {}
    import capo_ecr.types.encryption_type

    out["encryptionType"] = capo_ecr.types.encryption_type.serialize_aws_json_1_1(
        value["encryption_type"]
    )
    if "kms_key" in value:
        out["kmsKey"] = value["kms_key"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> EncryptionConfigurationForRepositoryCreationTemplate:
    out: EncryptionConfigurationForRepositoryCreationTemplate = {}  # type: ignore[typeddict-item]
    if data.get("encryptionType") is not None:
        import capo_ecr.types.encryption_type

        out["encryption_type"] = (
            capo_ecr.types.encryption_type.deserialize_aws_json_1_1(
                data["encryptionType"]
            )
        )
    else:
        raise DeserializationError(
            "EncryptionConfigurationForRepositoryCreationTemplate.encryption_type required"
        )
    if data.get("kmsKey") is not None:
        out["kms_key"] = data["kmsKey"]
    return out
