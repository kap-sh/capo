"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#ListRequiredTagsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_groups_tagging_api.types.pagination_token
    import capo_resource_groups_tagging_api.types.required_tags_for_list_required_tags


class ListRequiredTagsOutput(TypedDict, closed=True):
    required_tags: NotRequired[
        "capo_resource_groups_tagging_api.types.required_tags_for_list_required_tags.RequiredTagsForListRequiredTags"
    ]
    """<p>The required tags.</p>"""
    next_token: NotRequired[
        "capo_resource_groups_tagging_api.types.pagination_token.PaginationToken"
    ]
    """<p>A token for requesting another page of required tags if the <code>NextToken</code> response element indicates that more required tags are available. Use the value of the returned <code>NextToken</code> element in your request until the token comes back as null. Pass null if this is the first call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRequiredTagsOutput) -> dict:
    out: dict = {}
    if "required_tags" in value:
        import capo_resource_groups_tagging_api.types.required_tags_for_list_required_tags

        out["RequiredTags"] = (
            capo_resource_groups_tagging_api.types.required_tags_for_list_required_tags.serialize_aws_json_1_1(
                value["required_tags"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListRequiredTagsOutput:
    out: ListRequiredTagsOutput = {}  # type: ignore[typeddict-item]
    if data.get("RequiredTags") is not None:
        import capo_resource_groups_tagging_api.types.required_tags_for_list_required_tags

        out["required_tags"] = (
            capo_resource_groups_tagging_api.types.required_tags_for_list_required_tags.deserialize_aws_json_1_1(
                data["RequiredTags"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListRequiredTagsOutput) -> dict:
    out: dict = {}
    if "required_tags" in value:
        import capo_resource_groups_tagging_api.types.required_tags_for_list_required_tags

        out["RequiredTags"] = (
            capo_resource_groups_tagging_api.types.required_tags_for_list_required_tags.serialize_cbor(
                value["required_tags"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListRequiredTagsOutput:
    out: ListRequiredTagsOutput = {}  # type: ignore[typeddict-item]
    if data.get("RequiredTags") is not None:
        import capo_resource_groups_tagging_api.types.required_tags_for_list_required_tags

        out["required_tags"] = (
            capo_resource_groups_tagging_api.types.required_tags_for_list_required_tags.deserialize_cbor(
                data["RequiredTags"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
