"""Generated from Smithy shape ``com.amazonaws.kms#GenerateDataKeyWithoutPlaintextRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kms.types.data_key_spec
    import capo_kms.types.encryption_context_type
    import capo_kms.types.grant_token_list
    import capo_kms.types.key_id_type
    import capo_kms.types.nullable_boolean_type
    import capo_kms.types.number_of_bytes_type


class GenerateDataKeyWithoutPlaintextRequest(TypedDict, closed=True):
    key_id: "capo_kms.types.key_id_type.KeyIdType"
    """<p>Specifies the symmetric encryption KMS key that encrypts the data key. You cannot specify an asymmetric KMS key or a KMS key in a custom key store. To get the type and origin of your KMS key, use the <a>DescribeKey</a> operation.</p> <p>To specify a KMS key, use its key ID, key ARN, alias name, or alias ARN. When using an alias name, prefix it with <code>"alias/"</code>. To specify a KMS key in a different Amazon Web Services account, you must use the key ARN or alias ARN.</p> <p>For example:</p> <ul> <li> <p>Key ID: <code>1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Key ARN: <code>arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Alias name: <code>alias/ExampleAlias</code> </p> </li> <li> <p>Alias ARN: <code>arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias</code> </p> </li> </ul> <p>To get the key ID and key ARN for a KMS key, use <a>ListKeys</a> or <a>DescribeKey</a>. To get the alias name and alias ARN, use <a>ListAliases</a>.</p>"""
    encryption_context: NotRequired[
        "capo_kms.types.encryption_context_type.EncryptionContextType"
    ]
    """<p>Specifies the encryption context that will be used when encrypting the data key.</p> <important> <p>Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.</p> </important> <p>An <i>encryption context</i> is a collection of non-secret key-value pairs that represent additional authenticated data. When you use an encryption context to encrypt data, you must specify the same (an exact case-sensitive match) encryption context to decrypt the data. An encryption context is supported only on operations with symmetric encryption KMS keys. On operations with symmetric encryption KMS keys, an encryption context is optional, but it is strongly recommended.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/encrypt_context.html">Encryption context</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
    key_spec: NotRequired["capo_kms.types.data_key_spec.DataKeySpec"]
    """<p>The length of the data key. Use <code>AES_128</code> to generate a 128-bit symmetric key, or <code>AES_256</code> to generate a 256-bit symmetric key.</p>"""
    number_of_bytes: NotRequired[
        "capo_kms.types.number_of_bytes_type.NumberOfBytesType"
    ]
    """<p>The length of the data key in bytes. For example, use the value 64 to generate a 512-bit data key (64 bytes is 512 bits). For common key lengths (128-bit and 256-bit symmetric keys), we recommend that you use the <code>KeySpec</code> field instead of this one.</p>"""
    grant_tokens: NotRequired["capo_kms.types.grant_token_list.GrantTokenList"]
    """<p>A list of grant tokens.</p> <p>Use a grant token when your permission to call this operation comes from a new grant that has not yet achieved <i>eventual consistency</i>. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/grants.html#grant_token">Grant token</a> and <a href="https://docs.aws.amazon.com/kms/latest/developerguide/using-grant-token.html">Using a grant token</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
    dry_run: NotRequired["capo_kms.types.nullable_boolean_type.NullableBooleanType"]
    """<p>Checks if your request will succeed. <code>DryRun</code> is an optional parameter. </p> <p>To learn more about how to use this parameter, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/testing-permissions.html">Testing your permissions</a> in the <i>Key Management Service Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GenerateDataKeyWithoutPlaintextRequest) -> dict:
    out: dict = {}
    out["KeyId"] = value["key_id"]
    if "encryption_context" in value:
        import capo_kms.types.encryption_context_type

        out["EncryptionContext"] = (
            capo_kms.types.encryption_context_type.serialize_aws_json_1_1(
                value["encryption_context"]
            )
        )
    if "key_spec" in value:
        import capo_kms.types.data_key_spec

        out["KeySpec"] = capo_kms.types.data_key_spec.serialize_aws_json_1_1(
            value["key_spec"]
        )
    if "number_of_bytes" in value:
        out["NumberOfBytes"] = value["number_of_bytes"]
    if "grant_tokens" in value:
        import capo_kms.types.grant_token_list

        out["GrantTokens"] = capo_kms.types.grant_token_list.serialize_aws_json_1_1(
            value["grant_tokens"]
        )
    if "dry_run" in value:
        out["DryRun"] = value["dry_run"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GenerateDataKeyWithoutPlaintextRequest:
    out: GenerateDataKeyWithoutPlaintextRequest = {}  # type: ignore[typeddict-item]
    if data.get("KeyId") is not None:
        out["key_id"] = data["KeyId"]
    else:
        raise DeserializationError(
            "GenerateDataKeyWithoutPlaintextRequest.key_id required"
        )
    if data.get("EncryptionContext") is not None:
        import capo_kms.types.encryption_context_type

        out["encryption_context"] = (
            capo_kms.types.encryption_context_type.deserialize_aws_json_1_1(
                data["EncryptionContext"]
            )
        )
    if data.get("KeySpec") is not None:
        import capo_kms.types.data_key_spec

        out["key_spec"] = capo_kms.types.data_key_spec.deserialize_aws_json_1_1(
            data["KeySpec"]
        )
    if data.get("NumberOfBytes") is not None:
        out["number_of_bytes"] = data["NumberOfBytes"]
    if data.get("GrantTokens") is not None:
        import capo_kms.types.grant_token_list

        out["grant_tokens"] = capo_kms.types.grant_token_list.deserialize_aws_json_1_1(
            data["GrantTokens"]
        )
    if data.get("DryRun") is not None:
        out["dry_run"] = data["DryRun"]
    return out
