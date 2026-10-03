"""Generated from Smithy shape ``com.amazonaws.kms#ReEncryptRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kms.types.ciphertext_type
    import capo_kms.types.dry_run_modifier_list
    import capo_kms.types.encryption_algorithm_spec
    import capo_kms.types.encryption_context_type
    import capo_kms.types.grant_token_list
    import capo_kms.types.key_id_type
    import capo_kms.types.nullable_boolean_type


class ReEncryptRequest(TypedDict, closed=True):
    ciphertext_blob: NotRequired["capo_kms.types.ciphertext_type.CiphertextType"]
    """<p>Ciphertext of the data to reencrypt.</p> <p>This parameter is required in all cases except when <code>DryRun</code> is <code>true</code> and <code>DryRunModifiers</code> is set to <code>IGNORE_CIPHERTEXT</code>.</p>"""
    source_encryption_context: NotRequired[
        "capo_kms.types.encryption_context_type.EncryptionContextType"
    ]
    """<p>Specifies the encryption context to use to decrypt the ciphertext. Enter the same encryption context that was used to encrypt the ciphertext.</p> <p>An <i>encryption context</i> is a collection of non-secret key-value pairs that represent additional authenticated data. When you use an encryption context to encrypt data, you must specify the same (an exact case-sensitive match) encryption context to decrypt the data. An encryption context is supported only on operations with symmetric encryption KMS keys. On operations with symmetric encryption KMS keys, an encryption context is optional, but it is strongly recommended.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/encrypt_context.html">Encryption context</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
    source_key_id: NotRequired["capo_kms.types.key_id_type.KeyIdType"]
    """<p>Specifies the KMS key that KMS will use to decrypt the ciphertext before it is re-encrypted.</p> <p>Enter a key ID of the KMS key that was used to encrypt the ciphertext. If you identify a different KMS key, the <code>ReEncrypt</code> operation throws an <code>IncorrectKeyException</code>.</p> <p>This parameter is required only when the ciphertext was encrypted under an asymmetric KMS key or when <code>DryRun</code> is <code>true</code> and <code>DryRunModifiers</code> is set to <code>IGNORE_CIPHERTEXT</code>. If you used a symmetric encryption KMS key, KMS can get the KMS key from metadata that it adds to the symmetric ciphertext blob. However, it is always recommended as a best practice. This practice ensures that you use the KMS key that you intend.</p> <p>To specify a KMS key, use its key ID, key ARN, alias name, or alias ARN. When using an alias name, prefix it with <code>"alias/"</code>. To specify a KMS key in a different Amazon Web Services account, you should use the key ARN or alias ARN.</p> <p>For example:</p> <ul> <li> <p>Key ID: <code>1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Key ARN: <code>arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Alias name: <code>alias/ExampleAlias</code> </p> </li> <li> <p>Alias ARN: <code>arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias</code> </p> </li> </ul> <p>To get the key ID and key ARN for a KMS key, use <a>ListKeys</a> or <a>DescribeKey</a>. To get the alias name and alias ARN, use <a>ListAliases</a>.</p>"""
    destination_key_id: "capo_kms.types.key_id_type.KeyIdType"
    """<p>A unique identifier for the KMS key that is used to reencrypt the data. Specify a symmetric encryption KMS key or an asymmetric KMS key with a <code>KeyUsage</code> value of <code>ENCRYPT_DECRYPT</code>. To find the <code>KeyUsage</code> value of a KMS key, use the <a>DescribeKey</a> operation.</p> <p>To specify a KMS key, use its key ID, key ARN, alias name, or alias ARN. When using an alias name, prefix it with <code>"alias/"</code>. To specify a KMS key in a different Amazon Web Services account, you must use the key ARN or alias ARN.</p> <p>For example:</p> <ul> <li> <p>Key ID: <code>1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Key ARN: <code>arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Alias name: <code>alias/ExampleAlias</code> </p> </li> <li> <p>Alias ARN: <code>arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias</code> </p> </li> </ul> <p>To get the key ID and key ARN for a KMS key, use <a>ListKeys</a> or <a>DescribeKey</a>. To get the alias name and alias ARN, use <a>ListAliases</a>.</p>"""
    destination_encryption_context: NotRequired[
        "capo_kms.types.encryption_context_type.EncryptionContextType"
    ]
    """<p>Specifies that encryption context to use when the reencrypting the data.</p> <important> <p>Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.</p> </important> <p>A destination encryption context is valid only when the destination KMS key is a symmetric encryption KMS key. The standard ciphertext format for asymmetric KMS keys does not include fields for metadata.</p> <p>An <i>encryption context</i> is a collection of non-secret key-value pairs that represent additional authenticated data. When you use an encryption context to encrypt data, you must specify the same (an exact case-sensitive match) encryption context to decrypt the data. An encryption context is supported only on operations with symmetric encryption KMS keys. On operations with symmetric encryption KMS keys, an encryption context is optional, but it is strongly recommended.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/encrypt_context.html">Encryption context</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
    source_encryption_algorithm: NotRequired[
        "capo_kms.types.encryption_algorithm_spec.EncryptionAlgorithmSpec"
    ]
    """<p>Specifies the encryption algorithm that KMS will use to decrypt the ciphertext before it is reencrypted. The default value, <code>SYMMETRIC_DEFAULT</code>, represents the algorithm used for symmetric encryption KMS keys.</p> <p>Specify the same algorithm that was used to encrypt the ciphertext. If you specify a different algorithm, the decrypt attempt fails.</p> <p>This parameter is required only when the ciphertext was encrypted under an asymmetric KMS key.</p>"""
    destination_encryption_algorithm: NotRequired[
        "capo_kms.types.encryption_algorithm_spec.EncryptionAlgorithmSpec"
    ]
    """<p>Specifies the encryption algorithm that KMS will use to reecrypt the data after it has decrypted it. The default value, <code>SYMMETRIC_DEFAULT</code>, represents the encryption algorithm used for symmetric encryption KMS keys.</p> <p>This parameter is required only when the destination KMS key is an asymmetric KMS key.</p>"""
    grant_tokens: NotRequired["capo_kms.types.grant_token_list.GrantTokenList"]
    """<p>A list of grant tokens.</p> <p>Use a grant token when your permission to call this operation comes from a new grant that has not yet achieved <i>eventual consistency</i>. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/grants.html#grant_token">Grant token</a> and <a href="https://docs.aws.amazon.com/kms/latest/developerguide/using-grant-token.html">Using a grant token</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
    dry_run: NotRequired["capo_kms.types.nullable_boolean_type.NullableBooleanType"]
    """<p>Checks if your request will succeed. <code>DryRun</code> is an optional parameter. </p> <p>To learn more about how to use this parameter, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/testing-permissions.html">Testing your permissions</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
    dry_run_modifiers: NotRequired[
        "capo_kms.types.dry_run_modifier_list.DryRunModifierList"
    ]
    """<p>Specifies the modifiers to apply to the dry run operation. <code>DryRunModifiers</code> is an optional parameter that only applies when <code>DryRun</code> is set to <code>true</code>.</p> <p>When set to <code>IGNORE_CIPHERTEXT</code>, KMS performs only authorization validation without ciphertext validation. This allows you to test permissions without requiring a valid ciphertext blob.</p> <p>To learn more about how to use this parameter, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/testing-permissions.html">Testing your permissions</a> in the <i>Key Management Service Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReEncryptRequest) -> dict:
    out: dict = {}
    if "ciphertext_blob" in value:
        import capo_kms.types.ciphertext_type

        out["CiphertextBlob"] = capo_kms.types.ciphertext_type.serialize_aws_json_1_1(
            value["ciphertext_blob"]
        )
    if "source_encryption_context" in value:
        import capo_kms.types.encryption_context_type

        out["SourceEncryptionContext"] = (
            capo_kms.types.encryption_context_type.serialize_aws_json_1_1(
                value["source_encryption_context"]
            )
        )
    if "source_key_id" in value:
        out["SourceKeyId"] = value["source_key_id"]
    out["DestinationKeyId"] = value["destination_key_id"]
    if "destination_encryption_context" in value:
        import capo_kms.types.encryption_context_type

        out["DestinationEncryptionContext"] = (
            capo_kms.types.encryption_context_type.serialize_aws_json_1_1(
                value["destination_encryption_context"]
            )
        )
    if "source_encryption_algorithm" in value:
        import capo_kms.types.encryption_algorithm_spec

        out["SourceEncryptionAlgorithm"] = (
            capo_kms.types.encryption_algorithm_spec.serialize_aws_json_1_1(
                value["source_encryption_algorithm"]
            )
        )
    if "destination_encryption_algorithm" in value:
        import capo_kms.types.encryption_algorithm_spec

        out["DestinationEncryptionAlgorithm"] = (
            capo_kms.types.encryption_algorithm_spec.serialize_aws_json_1_1(
                value["destination_encryption_algorithm"]
            )
        )
    if "grant_tokens" in value:
        import capo_kms.types.grant_token_list

        out["GrantTokens"] = capo_kms.types.grant_token_list.serialize_aws_json_1_1(
            value["grant_tokens"]
        )
    if "dry_run" in value:
        out["DryRun"] = value["dry_run"]
    if "dry_run_modifiers" in value:
        import capo_kms.types.dry_run_modifier_list

        out["DryRunModifiers"] = (
            capo_kms.types.dry_run_modifier_list.serialize_aws_json_1_1(
                value["dry_run_modifiers"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReEncryptRequest:
    out: ReEncryptRequest = {}  # type: ignore[typeddict-item]
    if data.get("CiphertextBlob") is not None:
        import capo_kms.types.ciphertext_type

        out["ciphertext_blob"] = (
            capo_kms.types.ciphertext_type.deserialize_aws_json_1_1(
                data["CiphertextBlob"]
            )
        )
    if data.get("SourceEncryptionContext") is not None:
        import capo_kms.types.encryption_context_type

        out["source_encryption_context"] = (
            capo_kms.types.encryption_context_type.deserialize_aws_json_1_1(
                data["SourceEncryptionContext"]
            )
        )
    if data.get("SourceKeyId") is not None:
        out["source_key_id"] = data["SourceKeyId"]
    if data.get("DestinationKeyId") is not None:
        out["destination_key_id"] = data["DestinationKeyId"]
    else:
        raise DeserializationError("ReEncryptRequest.destination_key_id required")
    if data.get("DestinationEncryptionContext") is not None:
        import capo_kms.types.encryption_context_type

        out["destination_encryption_context"] = (
            capo_kms.types.encryption_context_type.deserialize_aws_json_1_1(
                data["DestinationEncryptionContext"]
            )
        )
    if data.get("SourceEncryptionAlgorithm") is not None:
        import capo_kms.types.encryption_algorithm_spec

        out["source_encryption_algorithm"] = (
            capo_kms.types.encryption_algorithm_spec.deserialize_aws_json_1_1(
                data["SourceEncryptionAlgorithm"]
            )
        )
    if data.get("DestinationEncryptionAlgorithm") is not None:
        import capo_kms.types.encryption_algorithm_spec

        out["destination_encryption_algorithm"] = (
            capo_kms.types.encryption_algorithm_spec.deserialize_aws_json_1_1(
                data["DestinationEncryptionAlgorithm"]
            )
        )
    if data.get("GrantTokens") is not None:
        import capo_kms.types.grant_token_list

        out["grant_tokens"] = capo_kms.types.grant_token_list.deserialize_aws_json_1_1(
            data["GrantTokens"]
        )
    if data.get("DryRun") is not None:
        out["dry_run"] = data["DryRun"]
    if data.get("DryRunModifiers") is not None:
        import capo_kms.types.dry_run_modifier_list

        out["dry_run_modifiers"] = (
            capo_kms.types.dry_run_modifier_list.deserialize_aws_json_1_1(
                data["DryRunModifiers"]
            )
        )
    return out
