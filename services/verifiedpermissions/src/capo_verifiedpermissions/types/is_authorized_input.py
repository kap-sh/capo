"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#IsAuthorizedInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.action_identifier
    import capo_verifiedpermissions.types.context_definition
    import capo_verifiedpermissions.types.entities_definition
    import capo_verifiedpermissions.types.entity_identifier
    import capo_verifiedpermissions.types.policy_store_id


class IsAuthorizedInput(TypedDict, closed=True):
    policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId"
    """<p>Specifies the ID of the policy store. Policies in this policy store will be used to make an authorization decision for the input.</p> <p>To specify a policy store, use its ID or alias name. When using an alias name, prefix it with <code>policy-store-alias/</code>. For example:</p> <ul> <li> <p>ID: <code>PSEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Alias name: <code>policy-store-alias/example-policy-store</code> </p> </li> </ul> <p>To view aliases, use <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html">ListPolicyStoreAliases</a>.</p>"""
    principal: NotRequired[
        "capo_verifiedpermissions.types.entity_identifier.EntityIdentifier"
    ]
    """<p>Specifies the principal for which the authorization decision is to be made.</p>"""
    action: NotRequired[
        "capo_verifiedpermissions.types.action_identifier.ActionIdentifier"
    ]
    """<p>Specifies the requested action to be authorized. For example, is the principal authorized to perform this action on the resource?</p>"""
    resource: NotRequired[
        "capo_verifiedpermissions.types.entity_identifier.EntityIdentifier"
    ]
    """<p>Specifies the resource for which the authorization decision is to be made.</p>"""
    context: NotRequired[
        "capo_verifiedpermissions.types.context_definition.ContextDefinition"
    ]
    """<p>Specifies additional context that can be used to make more granular authorization decisions.</p>"""
    entities: NotRequired[
        "capo_verifiedpermissions.types.entities_definition.EntitiesDefinition"
    ]
    """<p>(Optional) Specifies the list of resources and principals and their associated attributes that Verified Permissions can examine when evaluating the policies. These additional entities and their attributes can be referenced and checked by conditional elements in the policies in the specified policy store.</p> <note> <p>You can include only principal and resource entities in this parameter; you can't include actions. You must specify actions in the schema.</p> </note>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IsAuthorizedInput) -> dict:
    out: dict = {}
    out["policyStoreId"] = value["policy_store_id"]
    if "principal" in value:
        import capo_verifiedpermissions.types.entity_identifier

        out["principal"] = (
            capo_verifiedpermissions.types.entity_identifier.serialize_aws_json_1_0(
                value["principal"]
            )
        )
    if "action" in value:
        import capo_verifiedpermissions.types.action_identifier

        out["action"] = (
            capo_verifiedpermissions.types.action_identifier.serialize_aws_json_1_0(
                value["action"]
            )
        )
    if "resource" in value:
        import capo_verifiedpermissions.types.entity_identifier

        out["resource"] = (
            capo_verifiedpermissions.types.entity_identifier.serialize_aws_json_1_0(
                value["resource"]
            )
        )
    if "context" in value:
        import capo_verifiedpermissions.types.context_definition

        out["context"] = (
            capo_verifiedpermissions.types.context_definition.serialize_aws_json_1_0(
                value["context"]
            )
        )
    if "entities" in value:
        import capo_verifiedpermissions.types.entities_definition

        out["entities"] = (
            capo_verifiedpermissions.types.entities_definition.serialize_aws_json_1_0(
                value["entities"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> IsAuthorizedInput:
    out: IsAuthorizedInput = {}  # type: ignore[typeddict-item]
    if data.get("policyStoreId") is not None:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        raise DeserializationError("IsAuthorizedInput.policy_store_id required")
    if data.get("principal") is not None:
        import capo_verifiedpermissions.types.entity_identifier

        out["principal"] = (
            capo_verifiedpermissions.types.entity_identifier.deserialize_aws_json_1_0(
                data["principal"]
            )
        )
    if data.get("action") is not None:
        import capo_verifiedpermissions.types.action_identifier

        out["action"] = (
            capo_verifiedpermissions.types.action_identifier.deserialize_aws_json_1_0(
                data["action"]
            )
        )
    if data.get("resource") is not None:
        import capo_verifiedpermissions.types.entity_identifier

        out["resource"] = (
            capo_verifiedpermissions.types.entity_identifier.deserialize_aws_json_1_0(
                data["resource"]
            )
        )
    if data.get("context") is not None:
        import capo_verifiedpermissions.types.context_definition

        out["context"] = (
            capo_verifiedpermissions.types.context_definition.deserialize_aws_json_1_0(
                data["context"]
            )
        )
    if data.get("entities") is not None:
        import capo_verifiedpermissions.types.entities_definition

        out["entities"] = (
            capo_verifiedpermissions.types.entities_definition.deserialize_aws_json_1_0(
                data["entities"]
            )
        )
    return out
