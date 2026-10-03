"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#GetPolicyStoreInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.policy_store_id


class GetPolicyStoreInput(TypedDict, closed=True):
    policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId"
    """<p>Specifies the policy store that you want information about.</p> <p>To specify a policy store, use its ID or alias name. When using an alias name, prefix it with <code>policy-store-alias/</code>. For example:</p> <ul> <li> <p>ID: <code>PSEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Alias name: <code>policy-store-alias/example-policy-store</code> </p> </li> </ul> <p>To view aliases, use <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html">ListPolicyStoreAliases</a>.</p>"""
    tags: "bool"
    """<p>Specifies whether to return the tags that are attached to the policy store. If this parameter is included in the API call, the tags are returned, otherwise they are not returned.</p> <note> <p>If this parameter is included in the API call but there are no tags attached to the policy store, the <code>tags</code> response parameter is omitted from the response.</p> </note>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetPolicyStoreInput) -> dict:
    out: dict = {}
    out["policyStoreId"] = value["policy_store_id"]
    out["tags"] = value.get("tags", False)
    return out


def deserialize_aws_json_1_0(data: dict) -> GetPolicyStoreInput:
    out: GetPolicyStoreInput = {}  # type: ignore[typeddict-item]
    if data.get("policyStoreId") is not None:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        raise DeserializationError("GetPolicyStoreInput.policy_store_id required")
    if data.get("tags") is not None:
        out["tags"] = data["tags"]
    else:
        out["tags"] = False
    return out
