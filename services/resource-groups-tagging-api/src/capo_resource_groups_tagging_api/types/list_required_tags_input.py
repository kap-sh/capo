"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#ListRequiredTagsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_groups_tagging_api.types.max_results_for_list_required_tags
    import capo_resource_groups_tagging_api.types.pagination_token


class ListRequiredTagsInput(TypedDict, closed=True):
    next_token: NotRequired[
        "capo_resource_groups_tagging_api.types.pagination_token.PaginationToken"
    ]
    """<p>A token for requesting another page of required tags if the <code>NextToken</code> response element indicates that more required tags are available. Use the value of the returned <code>NextToken</code> element in your request until the token comes back as null. Pass null if this is the first call.</p>"""
    max_results: NotRequired[
        "capo_resource_groups_tagging_api.types.max_results_for_list_required_tags.MaxResultsForListRequiredTags"
    ]
    """<p>The maximum number of required tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRequiredTagsInput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListRequiredTagsInput:
    out: ListRequiredTagsInput = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListRequiredTagsInput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_cbor(data: dict) -> ListRequiredTagsInput:
    out: ListRequiredTagsInput = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
