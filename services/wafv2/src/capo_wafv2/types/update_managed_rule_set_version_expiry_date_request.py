"""Generated from Smithy shape ``com.amazonaws.wafv2#UpdateManagedRuleSetVersionExpiryDateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wafv2.types.entity_id
    import capo_wafv2.types.entity_name
    import capo_wafv2.types.lock_token
    import capo_wafv2.types.scope
    import capo_wafv2.types.timestamp
    import capo_wafv2.types.version_key_string


class UpdateManagedRuleSetVersionExpiryDateRequest(TypedDict, closed=True):
    name: "capo_wafv2.types.entity_name.EntityName"
    """<p>The name of the managed rule set. You use this, along with the rule set ID, to identify the rule set.</p> <p>This name is assigned to the corresponding managed rule group, which your customers can access and use. </p>"""
    scope: "capo_wafv2.types.scope.Scope"
    """<p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>"""
    id: "capo_wafv2.types.entity_id.EntityId"
    """<p>A unique identifier for the managed rule set. The ID is returned in the responses to commands like <code>list</code>. You provide it to operations like <code>get</code> and <code>update</code>.</p>"""
    lock_token: "capo_wafv2.types.lock_token.LockToken"
    """<p>A token used for optimistic locking. WAF returns a token to your <code>get</code> and <code>list</code> requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like <code>update</code> and <code>delete</code>. WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a <code>WAFOptimisticLockException</code>. If this happens, perform another <code>get</code>, and use the new token returned by that operation. </p>"""
    version_to_expire: "capo_wafv2.types.version_key_string.VersionKeyString"
    """<p>The version that you want to remove from your list of offerings for the named managed rule group. </p>"""
    expiry_timestamp: "capo_wafv2.types.timestamp.Timestamp"
    """<p>The time that you want the version to expire.</p> <p>Times are in Coordinated Universal Time (UTC) format. UTC format includes the special designator, Z. For example, "2016-09-27T14:50Z". </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateManagedRuleSetVersionExpiryDateRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_wafv2.types.scope

    out["Scope"] = capo_wafv2.types.scope.serialize_aws_json_1_1(value["scope"])
    out["Id"] = value["id"]
    out["LockToken"] = value["lock_token"]
    out["VersionToExpire"] = value["version_to_expire"]
    import capo_wafv2.types.timestamp

    out["ExpiryTimestamp"] = capo_wafv2.types.timestamp.serialize_aws_json_1_1(
        value["expiry_timestamp"]
    )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> UpdateManagedRuleSetVersionExpiryDateRequest:
    out: UpdateManagedRuleSetVersionExpiryDateRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError(
            "UpdateManagedRuleSetVersionExpiryDateRequest.name required"
        )
    if data.get("Scope") is not None:
        import capo_wafv2.types.scope

        out["scope"] = capo_wafv2.types.scope.deserialize_aws_json_1_1(data["Scope"])
    else:
        raise DeserializationError(
            "UpdateManagedRuleSetVersionExpiryDateRequest.scope required"
        )
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        raise DeserializationError(
            "UpdateManagedRuleSetVersionExpiryDateRequest.id required"
        )
    if data.get("LockToken") is not None:
        out["lock_token"] = data["LockToken"]
    else:
        raise DeserializationError(
            "UpdateManagedRuleSetVersionExpiryDateRequest.lock_token required"
        )
    if data.get("VersionToExpire") is not None:
        out["version_to_expire"] = data["VersionToExpire"]
    else:
        raise DeserializationError(
            "UpdateManagedRuleSetVersionExpiryDateRequest.version_to_expire required"
        )
    if data.get("ExpiryTimestamp") is not None:
        import capo_wafv2.types.timestamp

        out["expiry_timestamp"] = capo_wafv2.types.timestamp.deserialize_aws_json_1_1(
            data["ExpiryTimestamp"]
        )
    else:
        raise DeserializationError(
            "UpdateManagedRuleSetVersionExpiryDateRequest.expiry_timestamp required"
        )
    return out
