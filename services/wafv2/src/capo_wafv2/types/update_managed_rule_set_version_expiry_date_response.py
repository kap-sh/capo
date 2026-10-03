"""Generated from Smithy shape ``com.amazonaws.wafv2#UpdateManagedRuleSetVersionExpiryDateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.lock_token
    import capo_wafv2.types.timestamp
    import capo_wafv2.types.version_key_string


class UpdateManagedRuleSetVersionExpiryDateResponse(TypedDict, closed=True):
    expiring_version: NotRequired[
        "capo_wafv2.types.version_key_string.VersionKeyString"
    ]
    """<p>The version that is set to expire. </p>"""
    expiry_timestamp: NotRequired["capo_wafv2.types.timestamp.Timestamp"]
    """<p>The time that the version will expire. </p> <p>Times are in Coordinated Universal Time (UTC) format. UTC format includes the special designator, Z. For example, "2016-09-27T14:50Z". </p>"""
    next_lock_token: NotRequired["capo_wafv2.types.lock_token.LockToken"]
    """<p>A token used for optimistic locking. WAF returns a token to your <code>get</code> and <code>list</code> requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like <code>update</code> and <code>delete</code>. WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a <code>WAFOptimisticLockException</code>. If this happens, perform another <code>get</code>, and use the new token returned by that operation. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: UpdateManagedRuleSetVersionExpiryDateResponse,
) -> dict:
    out: dict = {}
    if "expiring_version" in value:
        out["ExpiringVersion"] = value["expiring_version"]
    if "expiry_timestamp" in value:
        import capo_wafv2.types.timestamp

        out["ExpiryTimestamp"] = capo_wafv2.types.timestamp.serialize_aws_json_1_1(
            value["expiry_timestamp"]
        )
    if "next_lock_token" in value:
        out["NextLockToken"] = value["next_lock_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> UpdateManagedRuleSetVersionExpiryDateResponse:
    out: UpdateManagedRuleSetVersionExpiryDateResponse = {}  # type: ignore[typeddict-item]
    if data.get("ExpiringVersion") is not None:
        out["expiring_version"] = data["ExpiringVersion"]
    if data.get("ExpiryTimestamp") is not None:
        import capo_wafv2.types.timestamp

        out["expiry_timestamp"] = capo_wafv2.types.timestamp.deserialize_aws_json_1_1(
            data["ExpiryTimestamp"]
        )
    if data.get("NextLockToken") is not None:
        out["next_lock_token"] = data["NextLockToken"]
    return out
