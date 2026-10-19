"""Generated from Smithy shape ``com.amazonaws.shield#ListProtectionGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_shield.types.protection_groups
    import capo_shield.types.token


class ListProtectionGroupsResponse(TypedDict, closed=True):
    protection_groups: "capo_shield.types.protection_groups.ProtectionGroups"
    """<p></p>"""
    next_token: NotRequired["capo_shield.types.token.Token"]
    """<p>When you request a list of objects from Shield Advanced, if the response does not include all of the remaining available objects, Shield Advanced includes a <code>NextToken</code> value in the response. You can retrieve the next batch of objects by requesting the list again and providing the token that was returned by the prior call in your request. </p> <p>You can indicate the maximum number of objects that you want Shield Advanced to return for a single call with the <code>MaxResults</code> setting. Shield Advanced will not return more than <code>MaxResults</code> objects, but may return fewer, even if more objects are still available.</p> <p>Whenever more objects remain that Shield Advanced has not yet returned to you, the response will include a <code>NextToken</code> value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListProtectionGroupsResponse) -> dict:
    out: dict = {}
    import capo_shield.types.protection_groups

    out["ProtectionGroups"] = (
        capo_shield.types.protection_groups.serialize_aws_json_1_1(
            value["protection_groups"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListProtectionGroupsResponse:
    out: ListProtectionGroupsResponse = {}  # type: ignore[typeddict-item]
    if data.get("ProtectionGroups") is not None:
        import capo_shield.types.protection_groups

        out["protection_groups"] = (
            capo_shield.types.protection_groups.deserialize_aws_json_1_1(
                data["ProtectionGroups"]
            )
        )
    else:
        out["protection_groups"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
