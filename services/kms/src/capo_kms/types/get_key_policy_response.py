"""Generated from Smithy shape ``com.amazonaws.kms#GetKeyPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kms.types.policy_name_type
    import capo_kms.types.policy_type


class GetKeyPolicyResponse(TypedDict, closed=True):
    policy: NotRequired["capo_kms.types.policy_type.PolicyType"]
    """<p>A key policy document in JSON format.</p>"""
    policy_name: NotRequired["capo_kms.types.policy_name_type.PolicyNameType"]
    """<p>The name of the key policy. Valid values are:</p> <dl> <dt>default</dt> <dd> <p>The key policy that you manage.</p> </dd> <dt>AWS_RAM</dt> <dd> <p>The key policy that RAM manages for KMS keys that you share through RAM.</p> </dd> </dl>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetKeyPolicyResponse) -> dict:
    out: dict = {}
    if "policy" in value:
        out["Policy"] = value["policy"]
    if "policy_name" in value:
        out["PolicyName"] = value["policy_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetKeyPolicyResponse:
    out: GetKeyPolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("Policy") is not None:
        out["policy"] = data["Policy"]
    if data.get("PolicyName") is not None:
        out["policy_name"] = data["PolicyName"]
    return out
