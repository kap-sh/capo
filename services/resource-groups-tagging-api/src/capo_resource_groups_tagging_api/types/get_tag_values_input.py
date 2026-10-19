"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#GetTagValuesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_groups_tagging_api.types.pagination_token
    import capo_resource_groups_tagging_api.types.tag_key


class GetTagValuesInput(TypedDict, closed=True):
    pagination_token: NotRequired[
        "capo_resource_groups_tagging_api.types.pagination_token.PaginationToken"
    ]
    """<p>Specifies a <code>PaginationToken</code> response value from a previous request to indicate that you want the next page of results. Leave this parameter empty in your initial request.</p>"""
    key: "capo_resource_groups_tagging_api.types.tag_key.TagKey"
    """<p>Specifies the tag key for which you want to list all existing values that are currently used in the specified Amazon Web Services Region for the calling account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTagValuesInput) -> dict:
    out: dict = {}
    if "pagination_token" in value:
        out["PaginationToken"] = value["pagination_token"]
    out["Key"] = value["key"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTagValuesInput:
    out: GetTagValuesInput = {}  # type: ignore[typeddict-item]
    if data.get("PaginationToken") is not None:
        out["pagination_token"] = data["PaginationToken"]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    else:
        out["key"] = ""
    return out
