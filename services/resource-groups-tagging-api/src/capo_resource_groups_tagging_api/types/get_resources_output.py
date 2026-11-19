"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#GetResourcesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_groups_tagging_api.types.pagination_token
    import capo_resource_groups_tagging_api.types.resource_tag_mapping_list


class GetResourcesOutput(TypedDict, closed=True):
    pagination_token: NotRequired[
        "capo_resource_groups_tagging_api.types.pagination_token.PaginationToken"
    ]
    """<p>A string that indicates that there is more data available than this response contains. To receive the next part of the response, specify this response value as the <code>PaginationToken</code> value in the request for the next page.</p>"""
    resource_tag_mapping_list: NotRequired[
        "capo_resource_groups_tagging_api.types.resource_tag_mapping_list.ResourceTagMappingList"
    ]
    """<p>A list of resource ARNs and the tags (keys and values) associated with each.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResourcesOutput) -> dict:
    out: dict = {}
    if "pagination_token" in value:
        out["PaginationToken"] = value["pagination_token"]
    if "resource_tag_mapping_list" in value:
        import capo_resource_groups_tagging_api.types.resource_tag_mapping_list

        out["ResourceTagMappingList"] = (
            capo_resource_groups_tagging_api.types.resource_tag_mapping_list.serialize_aws_json_1_1(
                value["resource_tag_mapping_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResourcesOutput:
    out: GetResourcesOutput = {}  # type: ignore[typeddict-item]
    if data.get("PaginationToken") is not None:
        out["pagination_token"] = data["PaginationToken"]
    if data.get("ResourceTagMappingList") is not None:
        import capo_resource_groups_tagging_api.types.resource_tag_mapping_list

        out["resource_tag_mapping_list"] = (
            capo_resource_groups_tagging_api.types.resource_tag_mapping_list.deserialize_aws_json_1_1(
                data["ResourceTagMappingList"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetResourcesOutput) -> dict:
    out: dict = {}
    if "pagination_token" in value:
        out["PaginationToken"] = value["pagination_token"]
    if "resource_tag_mapping_list" in value:
        import capo_resource_groups_tagging_api.types.resource_tag_mapping_list

        out["ResourceTagMappingList"] = (
            capo_resource_groups_tagging_api.types.resource_tag_mapping_list.serialize_cbor(
                value["resource_tag_mapping_list"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> GetResourcesOutput:
    out: GetResourcesOutput = {}  # type: ignore[typeddict-item]
    if data.get("PaginationToken") is not None:
        out["pagination_token"] = data["PaginationToken"]
    if data.get("ResourceTagMappingList") is not None:
        import capo_resource_groups_tagging_api.types.resource_tag_mapping_list

        out["resource_tag_mapping_list"] = (
            capo_resource_groups_tagging_api.types.resource_tag_mapping_list.deserialize_cbor(
                data["ResourceTagMappingList"]
            )
        )
    return out
