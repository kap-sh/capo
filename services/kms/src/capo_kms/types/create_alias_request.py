"""Generated from Smithy shape ``com.amazonaws.kms#CreateAliasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kms.types.alias_name_type
    import capo_kms.types.key_id_type


class CreateAliasRequest(TypedDict, closed=True):
    alias_name: "capo_kms.types.alias_name_type.AliasNameType"
    """<p>Specifies the alias name. This value must begin with <code>alias/</code> followed by a name, such as <code>alias/ExampleAlias</code>. </p> <important> <p>Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.</p> </important> <p>The <code>AliasName</code> value must be string of 1-256 characters. It can contain only alphanumeric characters, forward slashes (/), underscores (_), and dashes (-). The alias name cannot begin with <code>alias/aws/</code>. The <code>alias/aws/</code> prefix is reserved for <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-key">Amazon Web Services managed keys</a>.</p>"""
    target_key_id: "capo_kms.types.key_id_type.KeyIdType"
    """<p>Associates the alias with the specified <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-mgn-key">customer managed key</a>. The KMS key must be in the same Amazon Web Services Region. </p> <p>A valid key ID is required. If you supply a null or empty string value, this operation returns an error.</p> <p>For help finding the key ID and ARN, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/find-cmk-id-arn.html">Find the key ID and key ARN</a> in the <i> <i>Key Management Service Developer Guide</i> </i>.</p> <p>Specify the key ID or key ARN of the KMS key.</p> <p>For example:</p> <ul> <li> <p>Key ID: <code>1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Key ARN: <code>arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> </ul> <p>To get the key ID and key ARN for a KMS key, use <a>ListKeys</a> or <a>DescribeKey</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAliasRequest) -> dict:
    out: dict = {}
    out["AliasName"] = value["alias_name"]
    out["TargetKeyId"] = value["target_key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAliasRequest:
    out: CreateAliasRequest = {}  # type: ignore[typeddict-item]
    if data.get("AliasName") is not None:
        out["alias_name"] = data["AliasName"]
    else:
        raise DeserializationError("CreateAliasRequest.alias_name required")
    if data.get("TargetKeyId") is not None:
        out["target_key_id"] = data["TargetKeyId"]
    else:
        raise DeserializationError("CreateAliasRequest.target_key_id required")
    return out
