"""Generated from Smithy shape ``com.amazonaws.kms#EncapsulateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kms.types.encapsulation_algorithm_spec
    import capo_kms.types.grant_token_list
    import capo_kms.types.key_id_type
    import capo_kms.types.nullable_boolean_type


class EncapsulateRequest(TypedDict, closed=True):
    key_id: "capo_kms.types.key_id_type.KeyIdType"
    """<p>Identifies an asymmetric ML-KEM KMS key. KMS uses the public key in the specified key pair to encapsulate the shared secret. ML-KEM KMS keys have a <code>KeySpec</code> value of <code>ML_KEM_512</code>, <code>ML_KEM_768</code>, or <code>ML_KEM_1024</code> and a <code>KeyUsage</code> value of <code>ENCAPSULATE_DECAPSULATE</code>. To find the <code>KeySpec</code> and <code>KeyUsage</code> of a KMS key, use the <a>DescribeKey</a> operation.</p> <p>To specify a KMS key, use its key ID, key ARN, alias name, or alias ARN. When using an alias name, prefix it with <code>"alias/"</code>. To specify a KMS key in a different Amazon Web Services account, you must use the key ARN or alias ARN.</p> <p>For example:</p> <ul> <li> <p>Key ID: <code>1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Key ARN: <code>arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Alias name: <code>alias/ExampleAlias</code> </p> </li> <li> <p>Alias ARN: <code>arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias</code> </p> </li> </ul> <p>To get the key ID and key ARN for a KMS key, use <a>ListKeys</a> or <a>DescribeKey</a>. To get the alias name and alias ARN, use <a>ListAliases</a>.</p>"""
    encapsulation_algorithm: (
        "capo_kms.types.encapsulation_algorithm_spec.EncapsulationAlgorithmSpec"
    )
    """<p>Specifies the key encapsulation algorithm used to generate the shared secret and its encapsulated form. The only valid value is <code>ML_KEM</code>.</p>"""
    grant_tokens: NotRequired["capo_kms.types.grant_token_list.GrantTokenList"]
    """<p>A list of grant tokens.</p> <p>Use a grant token when your permission to call this operation comes from a new grant that has not yet achieved <i>eventual consistency</i>. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/grants.html#grant_token">Grant token</a> and <a href="https://docs.aws.amazon.com/kms/latest/developerguide/using-grant-token.html">Using a grant token</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
    dry_run: NotRequired["capo_kms.types.nullable_boolean_type.NullableBooleanType"]
    """<p>Checks if your request will succeed. <code>DryRun</code> is an optional parameter. </p> <p>To learn more about how to use this parameter, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/testing-permissions.html">Testing your permissions</a> in the <i>Key Management Service Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EncapsulateRequest) -> dict:
    out: dict = {}
    out["KeyId"] = value["key_id"]
    import capo_kms.types.encapsulation_algorithm_spec

    out["EncapsulationAlgorithm"] = (
        capo_kms.types.encapsulation_algorithm_spec.serialize_aws_json_1_1(
            value["encapsulation_algorithm"]
        )
    )
    if "grant_tokens" in value:
        import capo_kms.types.grant_token_list

        out["GrantTokens"] = capo_kms.types.grant_token_list.serialize_aws_json_1_1(
            value["grant_tokens"]
        )
    if "dry_run" in value:
        out["DryRun"] = value["dry_run"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EncapsulateRequest:
    out: EncapsulateRequest = {}  # type: ignore[typeddict-item]
    if data.get("KeyId") is not None:
        out["key_id"] = data["KeyId"]
    else:
        out["key_id"] = ""
    if data.get("EncapsulationAlgorithm") is not None:
        import capo_kms.types.encapsulation_algorithm_spec

        out["encapsulation_algorithm"] = (
            capo_kms.types.encapsulation_algorithm_spec.deserialize_aws_json_1_1(
                data["EncapsulationAlgorithm"]
            )
        )
    else:
        import typing

        out["encapsulation_algorithm"] = typing.cast(
            "capo_kms.types.encapsulation_algorithm_spec.EncapsulationAlgorithmSpec", ""
        )
    if data.get("GrantTokens") is not None:
        import capo_kms.types.grant_token_list

        out["grant_tokens"] = capo_kms.types.grant_token_list.deserialize_aws_json_1_1(
            data["GrantTokens"]
        )
    if data.get("DryRun") is not None:
        out["dry_run"] = data["DryRun"]
    return out
