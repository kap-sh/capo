"""Generated from Smithy shape ``com.amazonaws.shield#ListResourcesInProtectionGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_shield.types.max_results
    import capo_shield.types.protection_group_id
    import capo_shield.types.token


class ListResourcesInProtectionGroupRequest(TypedDict, closed=True):
    protection_group_id: "capo_shield.types.protection_group_id.ProtectionGroupId"
    """<p>The name of the protection group. You use this to identify the protection group in lists and to manage the protection group, for example to update, delete, or describe it. </p>"""
    next_token: NotRequired["capo_shield.types.token.Token"]
    """<p>When you request a list of objects from Shield Advanced, if the response does not include all of the remaining available objects, Shield Advanced includes a <code>NextToken</code> value in the response. You can retrieve the next batch of objects by requesting the list again and providing the token that was returned by the prior call in your request. </p> <p>You can indicate the maximum number of objects that you want Shield Advanced to return for a single call with the <code>MaxResults</code> setting. Shield Advanced will not return more than <code>MaxResults</code> objects, but may return fewer, even if more objects are still available.</p> <p>Whenever more objects remain that Shield Advanced has not yet returned to you, the response will include a <code>NextToken</code> value.</p> <p>On your first call to a list operation, leave this setting empty.</p>"""
    max_results: NotRequired["capo_shield.types.max_results.MaxResults"]
    """<p>The greatest number of objects that you want Shield Advanced to return to the list request. Shield Advanced might return fewer objects than you indicate in this setting, even if more objects are available. If there are more objects remaining, Shield Advanced will always also return a <code>NextToken</code> value in the response.</p> <p>The default setting is 20.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResourcesInProtectionGroupRequest) -> dict:
    out: dict = {}
    out["ProtectionGroupId"] = value["protection_group_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListResourcesInProtectionGroupRequest:
    out: ListResourcesInProtectionGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProtectionGroupId") is not None:
        out["protection_group_id"] = data["ProtectionGroupId"]
    else:
        out["protection_group_id"] = ""
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
