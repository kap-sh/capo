"""Generated from Smithy shape ``com.amazonaws.rbin#ListRulesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rbin.types.exclude_resource_tags
    import capo_rbin.types.lock_state
    import capo_rbin.types.max_results
    import capo_rbin.types.next_token
    import capo_rbin.types.resource_tags
    import capo_rbin.types.resource_type


class ListRulesRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_rbin.types.max_results.MaxResults"]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>NextToken</code> value.</p>"""
    next_token: NotRequired["capo_rbin.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""
    resource_type: "capo_rbin.types.resource_type.ResourceType"
    """<p>The resource type retained by the retention rule. Only retention rules that retain the specified resource type are listed. Currently, only EBS volumes, EBS snapshots, and EBS-backed AMIs are supported.</p> <ul> <li> <p>To list retention rules that retain EBS volumes, specify <code>EBS_VOLUME</code>.</p> </li> <li> <p>To list retention rules that retain EBS snapshots, specify <code>EBS_SNAPSHOT</code>.</p> </li> <li> <p>To list retention rules that retain EBS-backed AMIs, specify <code>EC2_IMAGE</code>.</p> </li> </ul>"""
    resource_tags: NotRequired["capo_rbin.types.resource_tags.ResourceTags"]
    """<p>[Tag-level retention rules only] Information about the resource tags used to identify resources that are retained by the retention rule.</p>"""
    lock_state: NotRequired["capo_rbin.types.lock_state.LockState"]
    """<p>The lock state of the retention rules to list. Only retention rules with the specified lock state are returned.</p>"""
    exclude_resource_tags: NotRequired[
        "capo_rbin.types.exclude_resource_tags.ExcludeResourceTags"
    ]
    """<p>[Region-level retention rules only] Information about the exclusion tags used to identify resources that are to be excluded, or ignored, by the retention rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRulesRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import capo_rbin.types.resource_type

    out["ResourceType"] = capo_rbin.types.resource_type.serialize_json(
        value["resource_type"]
    )
    if "resource_tags" in value:
        import capo_rbin.types.resource_tags

        out["ResourceTags"] = capo_rbin.types.resource_tags.serialize_json(
            value["resource_tags"]
        )
    if "lock_state" in value:
        import capo_rbin.types.lock_state

        out["LockState"] = capo_rbin.types.lock_state.serialize_json(
            value["lock_state"]
        )
    if "exclude_resource_tags" in value:
        import capo_rbin.types.exclude_resource_tags

        out["ExcludeResourceTags"] = (
            capo_rbin.types.exclude_resource_tags.serialize_json(
                value["exclude_resource_tags"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListRulesRequest:
    out: ListRulesRequest = {}  # type: ignore[typeddict-item]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("ResourceType") is not None:
        import capo_rbin.types.resource_type

        out["resource_type"] = capo_rbin.types.resource_type.deserialize_json(
            data["ResourceType"]
        )
    else:
        import typing

        out["resource_type"] = typing.cast(
            "capo_rbin.types.resource_type.ResourceType", ""
        )
    if data.get("ResourceTags") is not None:
        import capo_rbin.types.resource_tags

        out["resource_tags"] = capo_rbin.types.resource_tags.deserialize_json(
            data["ResourceTags"]
        )
    if data.get("LockState") is not None:
        import capo_rbin.types.lock_state

        out["lock_state"] = capo_rbin.types.lock_state.deserialize_json(
            data["LockState"]
        )
    if data.get("ExcludeResourceTags") is not None:
        import capo_rbin.types.exclude_resource_tags

        out["exclude_resource_tags"] = (
            capo_rbin.types.exclude_resource_tags.deserialize_json(
                data["ExcludeResourceTags"]
            )
        )
    return out
