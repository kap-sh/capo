"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#BatchGetPolicyInputItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.policy_id
    import capo_verifiedpermissions.types.policy_store_id


class BatchGetPolicyInputItem(TypedDict, closed=True):
    policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId"
    """<p>The identifier of the policy store where the policy you want information about is stored.</p>"""
    policy_id: "capo_verifiedpermissions.types.policy_id.PolicyId"
    """<p>The identifier of the policy you want information about.</p> <p>You can use the policy name in place of the policy ID. When using a name, prefix it with <code>name/</code>. For example:</p> <ul> <li> <p>ID: <code>SPEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Name: <code>name/example-policy</code> </p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchGetPolicyInputItem) -> dict:
    out: dict = {}
    out["policyStoreId"] = value["policy_store_id"]
    out["policyId"] = value["policy_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchGetPolicyInputItem:
    out: BatchGetPolicyInputItem = {}  # type: ignore[typeddict-item]
    if data.get("policyStoreId") is not None:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        out["policy_store_id"] = ""
    if data.get("policyId") is not None:
        out["policy_id"] = data["policyId"]
    else:
        out["policy_id"] = ""
    return out
