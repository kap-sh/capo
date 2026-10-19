"""Generated from Smithy shape ``com.amazonaws.athena#EncryptionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.encryption_option
    import capo_athena.types.string


class EncryptionConfiguration(TypedDict, closed=True):
    encryption_option: "capo_athena.types.encryption_option.EncryptionOption"
    """<p>Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys (<code>SSE_S3</code>), server-side encryption with KMS-managed keys (<code>SSE_KMS</code>), or client-side encryption with KMS-managed keys (<code>CSE_KMS</code>) is used.</p> <p>If a query runs in a workgroup and the workgroup overrides client-side settings, then the workgroup's setting for encryption is used. It specifies whether query results must be encrypted, for all queries that run in this workgroup. </p>"""
    kms_key: NotRequired["capo_athena.types.string.String"]
    """<p>For <code>SSE_KMS</code> and <code>CSE_KMS</code>, this is the KMS key ARN or ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EncryptionConfiguration) -> dict:
    out: dict = {}
    import capo_athena.types.encryption_option

    out["EncryptionOption"] = (
        capo_athena.types.encryption_option.serialize_aws_json_1_1(
            value["encryption_option"]
        )
    )
    if "kms_key" in value:
        out["KmsKey"] = value["kms_key"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EncryptionConfiguration:
    out: EncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("EncryptionOption") is not None:
        import capo_athena.types.encryption_option

        out["encryption_option"] = (
            capo_athena.types.encryption_option.deserialize_aws_json_1_1(
                data["EncryptionOption"]
            )
        )
    else:
        import typing

        out["encryption_option"] = typing.cast(
            "capo_athena.types.encryption_option.EncryptionOption", ""
        )
    if data.get("KmsKey") is not None:
        out["kms_key"] = data["KmsKey"]
    return out
