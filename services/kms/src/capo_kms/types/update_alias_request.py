"""Generated from Smithy shape ``com.amazonaws.kms#UpdateAliasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kms.types.alias_name_type
    import capo_kms.types.key_id_type


class UpdateAliasRequest(TypedDict, closed=True):
    alias_name: "capo_kms.types.alias_name_type.AliasNameType"
    """<p>Identifies the alias that is changing its KMS key. This value must begin with <code>alias/</code> followed by the alias name, such as <code>alias/ExampleAlias</code>. You cannot use <code>UpdateAlias</code> to change the alias name.</p> <important> <p>Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.</p> </important>"""
    target_key_id: "capo_kms.types.key_id_type.KeyIdType"
    """<p>Identifies the <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-mgn-key">customer managed key</a> to associate with the alias. You don't have permission to associate an alias with an <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-key">Amazon Web Services managed key</a>.</p> <p>The KMS key must be in the same Amazon Web Services account and Region as the alias. Also, the new target KMS key must be the same type as the current target KMS key (both symmetric or both asymmetric or both HMAC) and they must have the same key usage. </p> <p>Specify the key ID or key ARN of the KMS key.</p> <p>For example:</p> <ul> <li> <p>Key ID: <code>1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Key ARN: <code>arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> </ul> <p>To get the key ID and key ARN for a KMS key, use <a>ListKeys</a> or <a>DescribeKey</a>.</p> <p>To verify that the alias is mapped to the correct KMS key, use <a>ListAliases</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateAliasRequest) -> dict:
    out: dict = {}
    out["AliasName"] = value["alias_name"]
    out["TargetKeyId"] = value["target_key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateAliasRequest:
    out: UpdateAliasRequest = {}  # type: ignore[typeddict-item]
    if data.get("AliasName") is not None:
        out["alias_name"] = data["AliasName"]
    else:
        raise DeserializationError("UpdateAliasRequest.alias_name required")
    if data.get("TargetKeyId") is not None:
        out["target_key_id"] = data["TargetKeyId"]
    else:
        raise DeserializationError("UpdateAliasRequest.target_key_id required")
    return out
