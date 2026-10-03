"""Generated from Smithy shape ``com.amazonaws.kms#GrantConstraints``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kms.types.encryption_context_type
    import capo_kms.types.grant_constraint_source_arn_type


class GrantConstraints(TypedDict, closed=True):
    encryption_context_subset: NotRequired[
        "capo_kms.types.encryption_context_type.EncryptionContextType"
    ]
    """<p>A list of key-value pairs that must be included in the encryption context of the <a href="https://docs.aws.amazon.com/kms/latest/developerguide/kms-cryptography.html#cryptographic-operations">cryptographic operation</a> request. The grant allows the cryptographic operation only when the encryption context in the request includes the key-value pairs specified in this constraint, although it can include additional key-value pairs.</p>"""
    encryption_context_equals: NotRequired[
        "capo_kms.types.encryption_context_type.EncryptionContextType"
    ]
    """<p>A list of key-value pairs that must match the encryption context in the <a href="https://docs.aws.amazon.com/kms/latest/developerguide/kms-cryptography.html#cryptographic-operations">cryptographic operation</a> request. The grant allows the operation only when the encryption context in the request is the same as the encryption context specified in this constraint.</p>"""
    source_arn: NotRequired[
        "capo_kms.types.grant_constraint_source_arn_type.GrantConstraintSourceArnType"
    ]
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Name (ARN)</a> of an Amazon Web Services resource on behalf of which the request is made. This is effectively the same as having the <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourcearn">aws:SourceArn</a> global condition key in the grant. The SourceArn constraint ensures that the principal can use the KMS key only when the request is made on behalf of the specified resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GrantConstraints) -> dict:
    out: dict = {}
    if "encryption_context_subset" in value:
        import capo_kms.types.encryption_context_type

        out["EncryptionContextSubset"] = (
            capo_kms.types.encryption_context_type.serialize_aws_json_1_1(
                value["encryption_context_subset"]
            )
        )
    if "encryption_context_equals" in value:
        import capo_kms.types.encryption_context_type

        out["EncryptionContextEquals"] = (
            capo_kms.types.encryption_context_type.serialize_aws_json_1_1(
                value["encryption_context_equals"]
            )
        )
    if "source_arn" in value:
        out["SourceArn"] = value["source_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GrantConstraints:
    out: GrantConstraints = {}  # type: ignore[typeddict-item]
    if data.get("EncryptionContextSubset") is not None:
        import capo_kms.types.encryption_context_type

        out["encryption_context_subset"] = (
            capo_kms.types.encryption_context_type.deserialize_aws_json_1_1(
                data["EncryptionContextSubset"]
            )
        )
    if data.get("EncryptionContextEquals") is not None:
        import capo_kms.types.encryption_context_type

        out["encryption_context_equals"] = (
            capo_kms.types.encryption_context_type.deserialize_aws_json_1_1(
                data["EncryptionContextEquals"]
            )
        )
    if data.get("SourceArn") is not None:
        out["source_arn"] = data["SourceArn"]
    return out
