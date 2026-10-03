"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#DeletePolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.policy_id
    import capo_verifiedpermissions.types.policy_store_id


class DeletePolicyInput(TypedDict, closed=True):
    policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId"
    """<p>Specifies the ID of the policy store that contains the policy that you want to delete.</p> <p>To specify a policy store, use its ID or alias name. When using an alias name, prefix it with <code>policy-store-alias/</code>. For example:</p> <ul> <li> <p>ID: <code>PSEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Alias name: <code>policy-store-alias/example-policy-store</code> </p> </li> </ul> <p>To view aliases, use <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html">ListPolicyStoreAliases</a>.</p>"""
    policy_id: "capo_verifiedpermissions.types.policy_id.PolicyId"
    """<p>Specifies the ID of the policy that you want to delete.</p> <p>You can use the policy name in place of the policy ID. When using a name, prefix it with <code>name/</code>. For example:</p> <ul> <li> <p>ID: <code>SPEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Name: <code>name/example-policy</code> </p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeletePolicyInput) -> dict:
    out: dict = {}
    out["policyStoreId"] = value["policy_store_id"]
    out["policyId"] = value["policy_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeletePolicyInput:
    out: DeletePolicyInput = {}  # type: ignore[typeddict-item]
    if data.get("policyStoreId") is not None:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        raise DeserializationError("DeletePolicyInput.policy_store_id required")
    if data.get("policyId") is not None:
        out["policy_id"] = data["policyId"]
    else:
        raise DeserializationError("DeletePolicyInput.policy_id required")
    return out
