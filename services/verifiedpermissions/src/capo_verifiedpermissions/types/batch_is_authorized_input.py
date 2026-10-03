"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#BatchIsAuthorizedInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.batch_is_authorized_input_list
    import capo_verifiedpermissions.types.entities_definition
    import capo_verifiedpermissions.types.policy_store_id


class BatchIsAuthorizedInput(TypedDict, closed=True):
    policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId"
    """<p>Specifies the ID of the policy store. Policies in this policy store will be used to make the authorization decisions for the input.</p> <p>To specify a policy store, use its ID or alias name. When using an alias name, prefix it with <code>policy-store-alias/</code>. For example:</p> <ul> <li> <p>ID: <code>PSEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Alias name: <code>policy-store-alias/example-policy-store</code> </p> </li> </ul> <p>To view aliases, use <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html">ListPolicyStoreAliases</a>.</p>"""
    entities: NotRequired[
        "capo_verifiedpermissions.types.entities_definition.EntitiesDefinition"
    ]
    """<p>(Optional) Specifies the list of resources and principals and their associated attributes that Verified Permissions can examine when evaluating the policies. These additional entities and their attributes can be referenced and checked by conditional elements in the policies in the specified policy store.</p> <note> <p>You can include only principal and resource entities in this parameter; you can't include actions. You must specify actions in the schema.</p> </note>"""
    requests: "capo_verifiedpermissions.types.batch_is_authorized_input_list.BatchIsAuthorizedInputList"
    """<p>An array of up to 30 requests that you want Verified Permissions to evaluate.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchIsAuthorizedInput) -> dict:
    out: dict = {}
    out["policyStoreId"] = value["policy_store_id"]
    if "entities" in value:
        import capo_verifiedpermissions.types.entities_definition

        out["entities"] = (
            capo_verifiedpermissions.types.entities_definition.serialize_aws_json_1_0(
                value["entities"]
            )
        )
    import capo_verifiedpermissions.types.batch_is_authorized_input_list

    out["requests"] = (
        capo_verifiedpermissions.types.batch_is_authorized_input_list.serialize_aws_json_1_0(
            value["requests"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchIsAuthorizedInput:
    out: BatchIsAuthorizedInput = {}  # type: ignore[typeddict-item]
    if data.get("policyStoreId") is not None:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        raise DeserializationError("BatchIsAuthorizedInput.policy_store_id required")
    if data.get("entities") is not None:
        import capo_verifiedpermissions.types.entities_definition

        out["entities"] = (
            capo_verifiedpermissions.types.entities_definition.deserialize_aws_json_1_0(
                data["entities"]
            )
        )
    if data.get("requests") is not None:
        import capo_verifiedpermissions.types.batch_is_authorized_input_list

        out["requests"] = (
            capo_verifiedpermissions.types.batch_is_authorized_input_list.deserialize_aws_json_1_0(
                data["requests"]
            )
        )
    else:
        raise DeserializationError("BatchIsAuthorizedInput.requests required")
    return out
