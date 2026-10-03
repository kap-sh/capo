"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#PolicyItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.action_identifier_list
    import capo_verifiedpermissions.types.entity_identifier
    import capo_verifiedpermissions.types.policy_definition_item
    import capo_verifiedpermissions.types.policy_effect
    import capo_verifiedpermissions.types.policy_id
    import capo_verifiedpermissions.types.policy_name
    import capo_verifiedpermissions.types.policy_store_id
    import capo_verifiedpermissions.types.policy_type
    import capo_verifiedpermissions.types.timestamp_format


class PolicyItem(TypedDict, closed=True):
    policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId"
    """<p>The identifier of the policy store where the policy you want information about is stored.</p>"""
    policy_id: "capo_verifiedpermissions.types.policy_id.PolicyId"
    """<p>The identifier of the policy you want information about.</p>"""
    policy_type: "capo_verifiedpermissions.types.policy_type.PolicyType"
    """<p>The type of the policy. This is one of the following values:</p> <ul> <li> <p> <code>STATIC</code> </p> </li> <li> <p> <code>TEMPLATE_LINKED</code> </p> </li> </ul>"""
    principal: NotRequired[
        "capo_verifiedpermissions.types.entity_identifier.EntityIdentifier"
    ]
    """<p>The principal associated with the policy.</p>"""
    resource: NotRequired[
        "capo_verifiedpermissions.types.entity_identifier.EntityIdentifier"
    ]
    """<p>The resource associated with the policy.</p>"""
    actions: NotRequired[
        "capo_verifiedpermissions.types.action_identifier_list.ActionIdentifierList"
    ]
    """<p>The action that a policy permits or forbids. For example, <code>{"actions": [{"actionId": "ViewPhoto", "actionType": "PhotoFlash::Action"}, {"entityID": "SharePhoto", "entityType": "PhotoFlash::Action"}]}</code>.</p>"""
    definition: (
        "capo_verifiedpermissions.types.policy_definition_item.PolicyDefinitionItem"
    )
    """<p>The policy definition of an item in the list of policies returned.</p>"""
    created_date: "capo_verifiedpermissions.types.timestamp_format.TimestampFormat"
    """<p>The date and time the policy was created.</p>"""
    last_updated_date: "capo_verifiedpermissions.types.timestamp_format.TimestampFormat"
    """<p>The date and time the policy was most recently updated.</p>"""
    effect: NotRequired["capo_verifiedpermissions.types.policy_effect.PolicyEffect"]
    """<p>The effect of the decision that a policy returns to an authorization request. For example, <code>"effect": "Permit"</code>.</p>"""
    name: NotRequired["capo_verifiedpermissions.types.policy_name.PolicyName"]
    """<p>The name of the policy, if one was assigned when the policy was created or last updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PolicyItem) -> dict:
    out: dict = {}
    out["policyStoreId"] = value["policy_store_id"]
    out["policyId"] = value["policy_id"]
    import capo_verifiedpermissions.types.policy_type

    out["policyType"] = (
        capo_verifiedpermissions.types.policy_type.serialize_aws_json_1_0(
            value["policy_type"]
        )
    )
    if "principal" in value:
        import capo_verifiedpermissions.types.entity_identifier

        out["principal"] = (
            capo_verifiedpermissions.types.entity_identifier.serialize_aws_json_1_0(
                value["principal"]
            )
        )
    if "resource" in value:
        import capo_verifiedpermissions.types.entity_identifier

        out["resource"] = (
            capo_verifiedpermissions.types.entity_identifier.serialize_aws_json_1_0(
                value["resource"]
            )
        )
    if "actions" in value:
        import capo_verifiedpermissions.types.action_identifier_list

        out["actions"] = (
            capo_verifiedpermissions.types.action_identifier_list.serialize_aws_json_1_0(
                value["actions"]
            )
        )
    import capo_verifiedpermissions.types.policy_definition_item

    out["definition"] = (
        capo_verifiedpermissions.types.policy_definition_item.serialize_aws_json_1_0(
            value["definition"]
        )
    )
    import capo_verifiedpermissions.types.timestamp_format

    out["createdDate"] = (
        capo_verifiedpermissions.types.timestamp_format.serialize_aws_json_1_0(
            value["created_date"]
        )
    )
    import capo_verifiedpermissions.types.timestamp_format

    out["lastUpdatedDate"] = (
        capo_verifiedpermissions.types.timestamp_format.serialize_aws_json_1_0(
            value["last_updated_date"]
        )
    )
    if "effect" in value:
        import capo_verifiedpermissions.types.policy_effect

        out["effect"] = (
            capo_verifiedpermissions.types.policy_effect.serialize_aws_json_1_0(
                value["effect"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PolicyItem:
    out: PolicyItem = {}  # type: ignore[typeddict-item]
    if data.get("policyStoreId") is not None:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        raise DeserializationError("PolicyItem.policy_store_id required")
    if data.get("policyId") is not None:
        out["policy_id"] = data["policyId"]
    else:
        raise DeserializationError("PolicyItem.policy_id required")
    if data.get("policyType") is not None:
        import capo_verifiedpermissions.types.policy_type

        out["policy_type"] = (
            capo_verifiedpermissions.types.policy_type.deserialize_aws_json_1_0(
                data["policyType"]
            )
        )
    else:
        raise DeserializationError("PolicyItem.policy_type required")
    if data.get("principal") is not None:
        import capo_verifiedpermissions.types.entity_identifier

        out["principal"] = (
            capo_verifiedpermissions.types.entity_identifier.deserialize_aws_json_1_0(
                data["principal"]
            )
        )
    if data.get("resource") is not None:
        import capo_verifiedpermissions.types.entity_identifier

        out["resource"] = (
            capo_verifiedpermissions.types.entity_identifier.deserialize_aws_json_1_0(
                data["resource"]
            )
        )
    if data.get("actions") is not None:
        import capo_verifiedpermissions.types.action_identifier_list

        out["actions"] = (
            capo_verifiedpermissions.types.action_identifier_list.deserialize_aws_json_1_0(
                data["actions"]
            )
        )
    if data.get("definition") is not None:
        import capo_verifiedpermissions.types.policy_definition_item

        out["definition"] = (
            capo_verifiedpermissions.types.policy_definition_item.deserialize_aws_json_1_0(
                data["definition"]
            )
        )
    else:
        raise DeserializationError("PolicyItem.definition required")
    if data.get("createdDate") is not None:
        import capo_verifiedpermissions.types.timestamp_format

        out["created_date"] = (
            capo_verifiedpermissions.types.timestamp_format.deserialize_aws_json_1_0(
                data["createdDate"]
            )
        )
    else:
        raise DeserializationError("PolicyItem.created_date required")
    if data.get("lastUpdatedDate") is not None:
        import capo_verifiedpermissions.types.timestamp_format

        out["last_updated_date"] = (
            capo_verifiedpermissions.types.timestamp_format.deserialize_aws_json_1_0(
                data["lastUpdatedDate"]
            )
        )
    else:
        raise DeserializationError("PolicyItem.last_updated_date required")
    if data.get("effect") is not None:
        import capo_verifiedpermissions.types.policy_effect

        out["effect"] = (
            capo_verifiedpermissions.types.policy_effect.deserialize_aws_json_1_0(
                data["effect"]
            )
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    return out
