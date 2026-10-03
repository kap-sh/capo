"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#IsAuthorizedWithTokenInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.action_identifier
    import capo_verifiedpermissions.types.context_definition
    import capo_verifiedpermissions.types.entities_definition
    import capo_verifiedpermissions.types.entity_identifier
    import capo_verifiedpermissions.types.policy_store_id
    import capo_verifiedpermissions.types.token


class IsAuthorizedWithTokenInput(TypedDict, closed=True):
    policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId"
    """<p>Specifies the ID of the policy store. Policies in this policy store will be used to make an authorization decision for the input.</p> <p>To specify a policy store, use its ID or alias name. When using an alias name, prefix it with <code>policy-store-alias/</code>. For example:</p> <ul> <li> <p>ID: <code>PSEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Alias name: <code>policy-store-alias/example-policy-store</code> </p> </li> </ul> <p>To view aliases, use <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html">ListPolicyStoreAliases</a>.</p>"""
    identity_token: NotRequired["capo_verifiedpermissions.types.token.Token"]
    """<p>Specifies an identity token for the principal to be authorized. This token is provided to you by the identity provider (IdP) associated with the specified identity source. You must specify either an <code>accessToken</code>, an <code>identityToken</code>, or both.</p> <p>Must be an ID token. Verified Permissions returns an error if the <code>token_use</code> claim in the submitted token isn't <code>id</code>.</p>"""
    access_token: NotRequired["capo_verifiedpermissions.types.token.Token"]
    """<p>Specifies an access token for the principal to be authorized. This token is provided to you by the identity provider (IdP) associated with the specified identity source. You must specify either an <code>accessToken</code>, an <code>identityToken</code>, or both.</p> <p>Must be an access token. Verified Permissions returns an error if the <code>token_use</code> claim in the submitted token isn't <code>access</code>.</p>"""
    action: NotRequired[
        "capo_verifiedpermissions.types.action_identifier.ActionIdentifier"
    ]
    """<p>Specifies the requested action to be authorized. Is the specified principal authorized to perform this action on the specified resource.</p>"""
    resource: NotRequired[
        "capo_verifiedpermissions.types.entity_identifier.EntityIdentifier"
    ]
    """<p>Specifies the resource for which the authorization decision is made. For example, is the principal allowed to perform the action on the resource?</p>"""
    context: NotRequired[
        "capo_verifiedpermissions.types.context_definition.ContextDefinition"
    ]
    """<p>Specifies additional context that can be used to make more granular authorization decisions.</p>"""
    entities: NotRequired[
        "capo_verifiedpermissions.types.entities_definition.EntitiesDefinition"
    ]
    """<p>(Optional) Specifies the list of resources and their associated attributes that Verified Permissions can examine when evaluating the policies. These additional entities and their attributes can be referenced and checked by conditional elements in the policies in the specified policy store.</p> <important> <p>You can't include principals in this parameter, only resource and action entities. This parameter can't include any entities of a type that matches the user or group entity types that you defined in your identity source.</p> <ul> <li> <p>The <code>IsAuthorizedWithToken</code> operation takes principal attributes from <b> <i>only</i> </b> the <code>identityToken</code> or <code>accessToken</code> passed to the operation.</p> </li> <li> <p>For action entities, you can include only their <code>Identifier</code> and <code>EntityType</code>. </p> </li> </ul> </important>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IsAuthorizedWithTokenInput) -> dict:
    out: dict = {}
    out["policyStoreId"] = value["policy_store_id"]
    if "identity_token" in value:
        out["identityToken"] = value["identity_token"]
    if "access_token" in value:
        out["accessToken"] = value["access_token"]
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


def deserialize_aws_json_1_0(data: dict) -> IsAuthorizedWithTokenInput:
    out: IsAuthorizedWithTokenInput = {}  # type: ignore[typeddict-item]
    if data.get("policyStoreId") is not None:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        raise DeserializationError(
            "IsAuthorizedWithTokenInput.policy_store_id required"
        )
    if data.get("identityToken") is not None:
        out["identity_token"] = data["identityToken"]
    if data.get("accessToken") is not None:
        out["access_token"] = data["accessToken"]
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
