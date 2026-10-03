"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#UpdatePolicyOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.action_identifier_list
    import capo_verifiedpermissions.types.entity_identifier
    import capo_verifiedpermissions.types.policy_effect
    import capo_verifiedpermissions.types.policy_id
    import capo_verifiedpermissions.types.policy_store_id
    import capo_verifiedpermissions.types.policy_type
    import capo_verifiedpermissions.types.timestamp_format


class UpdatePolicyOutput(TypedDict, closed=True):
    policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId"
    """<p>The ID of the policy store that contains the policy that was updated.</p>"""
    policy_id: "capo_verifiedpermissions.types.policy_id.PolicyId"
    """<p>The ID of the policy that was updated.</p>"""
    policy_type: "capo_verifiedpermissions.types.policy_type.PolicyType"
    """<p>The type of the policy that was updated.</p>"""
    principal: NotRequired[
        "capo_verifiedpermissions.types.entity_identifier.EntityIdentifier"
    ]
    """<p>The principal specified in the policy's scope. This element isn't included in the response when <code>Principal</code> isn't present in the policy content.</p>"""
    resource: NotRequired[
        "capo_verifiedpermissions.types.entity_identifier.EntityIdentifier"
    ]
    """<p>The resource specified in the policy's scope. This element isn't included in the response when <code>Resource</code> isn't present in the policy content.</p>"""
    actions: NotRequired[
        "capo_verifiedpermissions.types.action_identifier_list.ActionIdentifierList"
    ]
    """<p>The action that a policy permits or forbids. For example, <code>{"actions": [{"actionId": "ViewPhoto", "actionType": "PhotoFlash::Action"}, {"entityID": "SharePhoto", "entityType": "PhotoFlash::Action"}]}</code>.</p>"""
    created_date: "capo_verifiedpermissions.types.timestamp_format.TimestampFormat"
    """<p>The date and time that the policy was originally created.</p>"""
    last_updated_date: "capo_verifiedpermissions.types.timestamp_format.TimestampFormat"
    """<p>The date and time that the policy was most recently updated.</p>"""
    effect: NotRequired["capo_verifiedpermissions.types.policy_effect.PolicyEffect"]
    """<p>The effect of the decision that a policy returns to an authorization request. For example, <code>"effect": "Permit"</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdatePolicyOutput) -> dict:
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
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdatePolicyOutput:
    out: UpdatePolicyOutput = {}  # type: ignore[typeddict-item]
    if data.get("policyStoreId") is not None:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        raise DeserializationError("UpdatePolicyOutput.policy_store_id required")
    if data.get("policyId") is not None:
        out["policy_id"] = data["policyId"]
    else:
        raise DeserializationError("UpdatePolicyOutput.policy_id required")
    if data.get("policyType") is not None:
        import capo_verifiedpermissions.types.policy_type

        out["policy_type"] = (
            capo_verifiedpermissions.types.policy_type.deserialize_aws_json_1_0(
                data["policyType"]
            )
        )
    else:
        raise DeserializationError("UpdatePolicyOutput.policy_type required")
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
    if data.get("createdDate") is not None:
        import capo_verifiedpermissions.types.timestamp_format

        out["created_date"] = (
            capo_verifiedpermissions.types.timestamp_format.deserialize_aws_json_1_0(
                data["createdDate"]
            )
        )
    else:
        raise DeserializationError("UpdatePolicyOutput.created_date required")
    if data.get("lastUpdatedDate") is not None:
        import capo_verifiedpermissions.types.timestamp_format

        out["last_updated_date"] = (
            capo_verifiedpermissions.types.timestamp_format.deserialize_aws_json_1_0(
                data["lastUpdatedDate"]
            )
        )
    else:
        raise DeserializationError("UpdatePolicyOutput.last_updated_date required")
    if data.get("effect") is not None:
        import capo_verifiedpermissions.types.policy_effect

        out["effect"] = (
            capo_verifiedpermissions.types.policy_effect.deserialize_aws_json_1_0(
                data["effect"]
            )
        )
    return out
