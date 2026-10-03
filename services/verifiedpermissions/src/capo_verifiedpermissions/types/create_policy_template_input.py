"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#CreatePolicyTemplateInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.idempotency_token
    import capo_verifiedpermissions.types.policy_statement
    import capo_verifiedpermissions.types.policy_store_id
    import capo_verifiedpermissions.types.policy_template_description
    import capo_verifiedpermissions.types.policy_template_name


class CreatePolicyTemplateInput(TypedDict, closed=True):
    client_token: NotRequired[
        "capo_verifiedpermissions.types.idempotency_token.IdempotencyToken"
    ]
    """<p>Specifies a unique, case-sensitive ID that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value.</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>ConflictException</code> error.</p> <p>Verified Permissions recognizes a <code>ClientToken</code> for eight hours. After eight hours, the next request with the same parameters performs the operation again regardless of the value of <code>ClientToken</code>.</p>"""
    policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId"
    """<p>The ID of the policy store in which to create the policy template.</p> <p>To specify a policy store, use its ID or alias name. When using an alias name, prefix it with <code>policy-store-alias/</code>. For example:</p> <ul> <li> <p>ID: <code>PSEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Alias name: <code>policy-store-alias/example-policy-store</code> </p> </li> </ul> <p>To view aliases, use <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html">ListPolicyStoreAliases</a>.</p>"""
    description: NotRequired[
        "capo_verifiedpermissions.types.policy_template_description.PolicyTemplateDescription"
    ]
    """<p>Specifies a description for the policy template.</p>"""
    statement: "capo_verifiedpermissions.types.policy_statement.PolicyStatement"
    """<p>Specifies the content that you want to use for the new policy template, written in the Cedar policy language.</p>"""
    name: NotRequired[
        "capo_verifiedpermissions.types.policy_template_name.PolicyTemplateName"
    ]
    """<p>Specifies a name for the policy template that is unique among all policy templates within the policy store. You can use the name in place of the policy template ID in API operations that reference the policy template. The name must be prefixed with <code>name/</code>.</p> <p>If you specify a name that is already associated with another policy template in the policy store, you receive a <code>ConflictException</code> error.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreatePolicyTemplateInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["policyStoreId"] = value["policy_store_id"]
    if "description" in value:
        out["description"] = value["description"]
    out["statement"] = value["statement"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreatePolicyTemplateInput:
    out: CreatePolicyTemplateInput = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("policyStoreId") is not None:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        raise DeserializationError("CreatePolicyTemplateInput.policy_store_id required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("statement") is not None:
        out["statement"] = data["statement"]
    else:
        raise DeserializationError("CreatePolicyTemplateInput.statement required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    return out
