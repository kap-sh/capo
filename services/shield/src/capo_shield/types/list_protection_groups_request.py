"""Generated from Smithy shape ``com.amazonaws.shield#ListProtectionGroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_shield.types.inclusion_protection_group_filters
    import capo_shield.types.max_results
    import capo_shield.types.token


class ListProtectionGroupsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_shield.types.token.Token"]
    """<p>When you request a list of objects from Shield Advanced, if the response does not include all of the remaining available objects, Shield Advanced includes a <code>NextToken</code> value in the response. You can retrieve the next batch of objects by requesting the list again and providing the token that was returned by the prior call in your request. </p> <p>You can indicate the maximum number of objects that you want Shield Advanced to return for a single call with the <code>MaxResults</code> setting. Shield Advanced will not return more than <code>MaxResults</code> objects, but may return fewer, even if more objects are still available.</p> <p>Whenever more objects remain that Shield Advanced has not yet returned to you, the response will include a <code>NextToken</code> value.</p> <p>On your first call to a list operation, leave this setting empty.</p>"""
    max_results: NotRequired["capo_shield.types.max_results.MaxResults"]
    """<p>The greatest number of objects that you want Shield Advanced to return to the list request. Shield Advanced might return fewer objects than you indicate in this setting, even if more objects are available. If there are more objects remaining, Shield Advanced will always also return a <code>NextToken</code> value in the response.</p> <p>The default setting is 20.</p>"""
    inclusion_filters: NotRequired[
        "capo_shield.types.inclusion_protection_group_filters.InclusionProtectionGroupFilters"
    ]
    """<p>Narrows the set of protection groups that the call retrieves. You can retrieve a single protection group by its name and you can retrieve all protection groups that are configured with specific pattern or aggregation settings. You can provide up to one criteria per filter type. Shield Advanced returns the protection groups that exactly match all of the search criteria that you provide.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListProtectionGroupsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "inclusion_filters" in value:
        import capo_shield.types.inclusion_protection_group_filters

        out["InclusionFilters"] = (
            capo_shield.types.inclusion_protection_group_filters.serialize_aws_json_1_1(
                value["inclusion_filters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListProtectionGroupsRequest:
    out: ListProtectionGroupsRequest = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("InclusionFilters") is not None:
        import capo_shield.types.inclusion_protection_group_filters

        out["inclusion_filters"] = (
            capo_shield.types.inclusion_protection_group_filters.deserialize_aws_json_1_1(
                data["InclusionFilters"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListProtectionGroupsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "inclusion_filters" in value:
        import capo_shield.types.inclusion_protection_group_filters

        out["InclusionFilters"] = (
            capo_shield.types.inclusion_protection_group_filters.serialize_cbor(
                value["inclusion_filters"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ListProtectionGroupsRequest:
    out: ListProtectionGroupsRequest = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("InclusionFilters") is not None:
        import capo_shield.types.inclusion_protection_group_filters

        out["inclusion_filters"] = (
            capo_shield.types.inclusion_protection_group_filters.deserialize_cbor(
                data["InclusionFilters"]
            )
        )
    return out
