"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#GetPolicyTemplateInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.policy_store_id
    import capo_verifiedpermissions.types.policy_template_id


class GetPolicyTemplateInput(TypedDict, closed=True):
    policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId"
    """<p>Specifies the ID of the policy store that contains the policy template that you want information about.</p> <p>To specify a policy store, use its ID or alias name. When using an alias name, prefix it with <code>policy-store-alias/</code>. For example:</p> <ul> <li> <p>ID: <code>PSEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Alias name: <code>policy-store-alias/example-policy-store</code> </p> </li> </ul> <p>To view aliases, use <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html">ListPolicyStoreAliases</a>.</p>"""
    policy_template_id: (
        "capo_verifiedpermissions.types.policy_template_id.PolicyTemplateId"
    )
    """<p>Specifies the ID of the policy template that you want information about.</p> <p>You can use the policy template name in place of the policy template ID. When using a name, prefix it with <code>name/</code>. For example:</p> <ul> <li> <p>ID: <code>PTEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Name: <code>name/example-policy-template</code> </p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetPolicyTemplateInput) -> dict:
    out: dict = {}
    out["policyStoreId"] = value["policy_store_id"]
    out["policyTemplateId"] = value["policy_template_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetPolicyTemplateInput:
    out: GetPolicyTemplateInput = {}  # type: ignore[typeddict-item]
    if data.get("policyStoreId") is not None:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        raise DeserializationError("GetPolicyTemplateInput.policy_store_id required")
    if data.get("policyTemplateId") is not None:
        out["policy_template_id"] = data["policyTemplateId"]
    else:
        raise DeserializationError("GetPolicyTemplateInput.policy_template_id required")
    return out
